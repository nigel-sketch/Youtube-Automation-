"""
Automated daily pipeline — entry point for GitHub Actions.

Run: python pipeline_auto.py
"""

import os
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import config
from article_to_video import from_script_dict
from researcher import research_topic
from script_writer import write_script
from thumbnail_creator import generate_thumbnail
from topic_generator import generate_topic
from uploader import log_upload, upload_video
from video_creator import build_video


def run():
    anthropic_key = os.environ["ANTHROPIC_API_KEY"]
    gemini_key = os.environ.get("GEMINI_API_KEY")
    pexels_key = os.environ.get("PEXELS_API_KEY")

    run_dir = Path(tempfile.mkdtemp(prefix="yw_run_"))
    print(f"[pipeline] Run directory: {run_dir}")

    try:
        # 1 — Topic
        print("[pipeline] Generating topic...")
        topic = generate_topic(config.UPLOAD_LOG_PATH, anthropic_key)
        print(f"[pipeline] Topic: {topic}")

        # 2 — Research
        print("[pipeline] Researching topic...")
        research_pack = research_topic(topic, gemini_key) if gemini_key else ""

        # 3 — Script / article
        print("[pipeline] Writing script...")
        script_dict = write_script(topic, research_pack, anthropic_key)

        # 4 — Parse into VideoScript
        video_script = from_script_dict(script_dict)
        print(f"[pipeline] Script ready: {len(video_script.slides)} slides")

        # 5 — Build video
        video_path = run_dir / "video.mp4"
        print("[pipeline] Building video...")
        build_video(video_script, video_path, pexels_key=pexels_key)
        print(f"[pipeline] Video: {video_path} ({video_path.stat().st_size // 1024 // 1024} MB)")

        # 6 — Thumbnail
        thumbnail_path = run_dir / "thumbnail.jpg"
        print("[pipeline] Creating thumbnail...")
        generate_thumbnail(video_script.youtube_title, thumbnail_path, pexels_key=pexels_key)

        # 7 — Upload
        print("[pipeline] Uploading to YouTube...")
        video_id = upload_video(video_path, thumbnail_path, video_script)

        # 8 — Log
        log_upload(topic, video_id)
        print(f"[pipeline] Done! https://youtu.be/{video_id}")

    except Exception as e:
        print(f"[pipeline] FAILED: {e}", file=sys.stderr)
        raise
    finally:
        shutil.rmtree(run_dir, ignore_errors=True)


if __name__ == "__main__":
    run()
