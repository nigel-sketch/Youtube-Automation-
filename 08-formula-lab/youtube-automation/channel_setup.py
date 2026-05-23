"""
One-time channel branding setup — run locally after OAuth is configured.

Sets:
  - Channel description
  - Channel keywords
  - Channel banner image

Cannot set via API (do manually in studio.youtube.com):
  - Profile picture
  - Channel name

Usage:
  python channel_setup.py
  python channel_setup.py --banner /path/to/banner.png
"""

import argparse
import os
from pathlib import Path

from googleapiclient.http import MediaFileUpload

import config
from auth import get_youtube_service


def set_channel_metadata(youtube):
    print("[channel_setup] Setting description and keywords...")
    youtube.channels().update(
        part="brandingSettings",
        body={
            "id": "",  # empty = authenticated channel
            "brandingSettings": {
                "channel": {
                    "description": config.CHANNEL_DESCRIPTION,
                    "keywords": " ".join(f'"{k}"' for k in config.CHANNEL_KEYWORDS),
                    "country": "GB",
                }
            },
        },
    ).execute()
    print("[channel_setup] Channel metadata updated.")


def set_channel_banner(youtube, banner_path: Path):
    print(f"[channel_setup] Uploading banner: {banner_path}")
    response = youtube.channelBanners().insert(
        media_body=MediaFileUpload(str(banner_path), mimetype="image/png"),
    ).execute()

    banner_url = response.get("url")
    youtube.channels().update(
        part="brandingSettings",
        body={
            "brandingSettings": {
                "image": {"bannerExternalUrl": banner_url}
            }
        },
    ).execute()
    print(f"[channel_setup] Banner set: {banner_url}")


def main():
    parser = argparse.ArgumentParser(description="Set Booked Wild channel branding via YouTube API")
    parser.add_argument("--banner", type=Path, help="Path to banner image (PNG, min 2560x1440)")
    args = parser.parse_args()

    youtube = get_youtube_service()
    set_channel_metadata(youtube)

    if args.banner:
        if not args.banner.exists():
            print(f"Error: banner file not found: {args.banner}")
        else:
            set_channel_banner(youtube, args.banner)

    print("\n[channel_setup] Done.")
    print("Remember to set your profile picture and channel name manually at studio.youtube.com")


if __name__ == "__main__":
    main()
