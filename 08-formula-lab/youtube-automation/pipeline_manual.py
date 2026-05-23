"""
Manual pipeline — convert an existing Booked Wild .md article to a YouTube video.

Usage:
  python pipeline_manual.py /path/to/booked-wild-article.md
  python pipeline_manual.py /path/to/article.md --no-upload
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
from pathlib import Path

import config
from article_to_video import parse_article
from thumbnail_creator import generate_thumbnail
from uploader import log_upload, upload_video
from video_creator import build_video


def run(article_path: Path, skip_upload: bool = False):
    gemini_key = os.environ.get("GEMINI_API_KEY")

    print(f"[manual] Reading article: {article_path}")
    md_text = article_path.read_text(encoding="utf-8")
    video_script = parse_article(md_text)
    video_script.youtube_title = video_script.title
    print(f"[manual] Parsed: '{video_script.title}' ({len(video_script.slides)} slides)")

    run_dir = Path(tempfile.mkdtemp(prefix="yw_manual_"))

    try:
        video_path = run_dir / "video.mp4"
        print("[manual] Building video...")
        build_video(video_script, video_path, gemini_key=gemini_key)
        print(f"[manual] Video: {video_path}")

        thumbnail_path = run_dir / "thumbnail.jpg"
        print("[manual] Creating thumbnail...")
        generate_thumbnail(video_script.youtube_title, thumbnail_path, gemini_key=gemini_key)

        if skip_upload:
            out_video = Path.cwd() / f"{article_path.stem}.mp4"
            out_thumb = Path.cwd() / f"{article_path.stem}_thumbnail.jpg"
            shutil.copy(video_path, out_video)
            shutil.copy(thumbnail_path, out_thumb)
            print(f"[manual] Saved (no upload):\n  {out_video}\n  {out_thumb}")
            return

        answer = input("[manual] Upload to YouTube? (y/N): ").strip().lower()
        if answer != "y":
            print("[manual] Upload skipped.")
            return

        print("[manual] Uploading...")
        video_id = upload_video(video_path, thumbnail_path, video_script)
        log_upload(video_script.title, video_id)
        print(f"[manual] Done! https://youtu.be/{video_id}")

    finally:
        shutil.rmtree(run_dir, ignore_errors=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a Booked Wild .md article to YouTube")
    parser.add_argument("article", type=Path, help="Path to the .md article file")
    parser.add_argument("--no-upload", action="store_true", help="Build video locally, skip upload")
    args = parser.parse_args()

    if not args.article.exists():
        print(f"Error: file not found: {args.article}", file=sys.stderr)
        sys.exit(1)

    run(args.article, skip_upload=args.no_upload)
