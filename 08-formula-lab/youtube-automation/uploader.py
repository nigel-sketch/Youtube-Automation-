"""Upload a video to YouTube and set its thumbnail and metadata."""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

from googleapiclient.http import MediaFileUpload

import config
from article_to_video import VideoScript
from auth import get_youtube_service


def _build_description(script: VideoScript) -> str:
    if script.youtube_description:
        return script.youtube_description
    # Fallback: auto-generate from slides
    lines = [script.title, ""]
    lines.append("In this video:")
    for slide in script.slides:
        lines.append(f"  • {slide.heading}")
    lines.append("")
    lines.append(f"🔍 Find your direct booking gaps — Deep Insight Audit: {config.AUDIT_CTA_URL}")
    lines.append(f"🔔 Subscribe for daily hospitality strategy: {config.CHANNEL_HANDLE}")
    lines.append(f"\n#DirectBookings #AIVisibility #IndependentTravel #BookedWild #OTACommission")
    return "\n".join(lines)


def upload_video(
    video_path: Path,
    thumbnail_path: Path,
    script: VideoScript,
) -> str:
    """
    Upload the video to YouTube, set thumbnail, and return the video_id.
    Reads credentials from environment variables.
    """
    youtube = get_youtube_service()

    all_tags = list(dict.fromkeys(config.BASE_TAGS + script.tags))  # deduplicated

    body = {
        "snippet": {
            "title": script.youtube_title or script.title,
            "description": _build_description(script),
            "tags": all_tags[:30],  # YouTube max 30 tags
            "categoryId": config.VIDEO_CATEGORY_ID,
            "defaultLanguage": config.VIDEO_LANGUAGE,
            "defaultAudioLanguage": config.VIDEO_LANGUAGE,
        },
        "status": {
            "privacyStatus": config.UPLOAD_PRIVACY,
            "selfDeclaredMadeForKids": False,
        },
    }

    media = MediaFileUpload(
        str(video_path),
        mimetype="video/mp4",
        resumable=True,
        chunksize=10 * 1024 * 1024,  # 10 MB chunks
    )

    print(f"[uploader] Uploading '{script.youtube_title}' as {config.UPLOAD_PRIVACY}...")
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            pct = int(status.progress() * 100)
            print(f"[uploader] Upload progress: {pct}%")

    video_id = response["id"]
    print(f"[uploader] Video uploaded: https://youtu.be/{video_id}")

    # Set thumbnail
    if thumbnail_path.exists():
        try:
            youtube.thumbnails().set(
                videoId=video_id,
                media_body=MediaFileUpload(str(thumbnail_path), mimetype="image/jpeg"),
            ).execute()
            print("[uploader] Thumbnail set.")
        except Exception as e:
            print(f"[uploader] Thumbnail upload failed (non-fatal): {e}")

    return video_id


def log_upload(topic: str, video_id: str, log_path: str = config.UPLOAD_LOG_PATH):
    """Append the upload record to the JSON log file."""
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = {"topics": []}
    if path.exists():
        with open(path) as f:
            data = json.load(f)

    data["topics"].append(
        {
            "date": datetime.utcnow().strftime("%Y-%m-%d"),
            "topic": topic,
            "video_id": video_id,
            "url": f"https://youtu.be/{video_id}",
        }
    )

    with open(path, "w") as f:
        json.dump(data, f, indent=2)
