"""
One-time local OAuth setup — generates the YouTube refresh token.

Run this ONCE on your Mac (not in GitHub Actions):
  pip install google-auth-oauthlib
  python youtube_automation/setup_oauth.py --credentials /path/to/client_secret.json

The script opens your browser, you sign in with your Booked Wild Gmail,
and grant the requested YouTube permissions.
Copy the printed refresh token into GitHub Secrets as YOUTUBE_REFRESH_TOKEN.
"""

import argparse
import json
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
]


def main():
    parser = argparse.ArgumentParser(description="Generate YouTube OAuth refresh token")
    parser.add_argument(
        "--credentials",
        required=True,
        type=Path,
        help="Path to client_secret.json downloaded from Google Cloud Console",
    )
    args = parser.parse_args()

    if not args.credentials.exists():
        print(f"Error: credentials file not found: {args.credentials}")
        return

    flow = InstalledAppFlow.from_client_secrets_file(str(args.credentials), scopes=SCOPES)
    credentials = flow.run_local_server(port=0)

    print("\n" + "=" * 60)
    print("SUCCESS — add these to GitHub Secrets:")
    print("=" * 60)

    client_info = json.loads(args.credentials.read_text())
    client = client_info.get("installed") or client_info.get("web", {})

    print(f"YOUTUBE_CLIENT_ID     = {client.get('client_id')}")
    print(f"YOUTUBE_CLIENT_SECRET = {client.get('client_secret')}")
    print(f"YOUTUBE_REFRESH_TOKEN = {credentials.refresh_token}")
    print("=" * 60)


if __name__ == "__main__":
    main()
