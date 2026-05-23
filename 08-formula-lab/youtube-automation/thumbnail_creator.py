"""Generate a branded 1280x720 YouTube thumbnail."""

from __future__ import annotations

import io
from pathlib import Path

import requests
from PIL import Image, ImageDraw, ImageFont

import config


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        return ImageFont.truetype(config.FONT_PATH, size)
    except (IOError, OSError):
        return ImageFont.load_default()


def _wrap_text(text: str, font, max_width: int, draw: ImageDraw.ImageDraw) -> str:
    words = text.split()
    lines, current = [], []
    for word in words:
        test = " ".join(current + [word])
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] > max_width and current:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return "\n".join(lines)


def _pexels_background(title: str, api_key: str) -> Image.Image | None:
    try:
        resp = requests.get(
            "https://api.pexels.com/v1/search",
            headers={"Authorization": api_key},
            params={"query": f"travel nature landscape {title[:40]}", "per_page": 1, "orientation": "landscape"},
            timeout=10,
        )
        resp.raise_for_status()
        photos = resp.json().get("photos", [])
        if not photos:
            return None
        img_url = photos[0]["src"]["original"]
        img_resp = requests.get(img_url, timeout=20)
        img_resp.raise_for_status()
        return Image.open(io.BytesIO(img_resp.content)).resize(config.THUMBNAIL_RESOLUTION)
    except Exception as e:
        print(f"[thumbnail] Pexels fetch failed: {e}. Using solid background.")
    return None


def _local_background(size: tuple[int, int]) -> Image.Image | None:
    """Pick a random image from assets/images/ or assets/ as background."""
    import random
    candidates = []
    for folder in [Path("assets/images"), Path("assets")]:
        if folder.exists():
            candidates += list(folder.glob("*.jpg")) + list(folder.glob("*.png"))
    candidates = [f for f in candidates if f.is_file()]
    if not candidates:
        return None
    try:
        return Image.open(random.choice(candidates)).resize(size)
    except Exception:
        return None


def generate_thumbnail(
    title: str,
    output_path: Path,
    pexels_key: str | None = None,
) -> Path:
    """
    Create a 1280x720 JPEG thumbnail.
    Uses Pexels for background if a key is provided, otherwise Pillow-only.
    """
    w, h = config.THUMBNAIL_RESOLUTION

    # Try local images first, then Pexels, then solid colour
    bg = _local_background((w, h))
    if bg is None and pexels_key and config.IMAGES_PER_VIDEO > 0:
        bg = _pexels_background(title, pexels_key)

    if bg is None:
        bg = Image.new("RGB", (w, h), color=config.BACKGROUND_COLOR)
        draw = ImageDraw.Draw(bg)
        # Left accent stripe
        draw.rectangle([(0, 0), (12, h)], fill=config.ACCENT_COLOR)
        # Top accent stripe
        draw.rectangle([(0, 0), (w, 8)], fill=config.ACCENT_COLOR)

    # Dark overlay for text legibility
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 140))
    bg = Image.alpha_composite(bg.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(bg)

    title_font = _load_font(90)
    brand_font = _load_font(40)

    pad = 60
    max_text_width = w - 2 * pad

    wrapped = _wrap_text(title, title_font, max_text_width, draw)
    bbox = draw.multiline_textbbox((0, 0), wrapped, font=title_font, spacing=12)
    text_h = bbox[3] - bbox[1]

    # Centre title vertically, shifted slightly up
    start_y = max(pad, (h - text_h) // 2 - 30)
    draw.multiline_text(
        (pad, start_y),
        wrapped,
        font=title_font,
        fill=config.TEXT_COLOR,
        spacing=12,
    )

    # Channel name bottom-left
    draw.text(
        (pad, h - pad - 40),
        config.CHANNEL_NAME,
        font=brand_font,
        fill=config.ACCENT_COLOR,
    )

    # Logo bottom-right
    logo_path = Path(config.LOGO_ICON_PATH)
    if logo_path.exists():
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo.thumbnail((180, 60))
            bg.paste(logo, (w - logo.width - pad, h - logo.height - pad // 2), logo)
        except Exception:
            pass

    output_path.parent.mkdir(parents=True, exist_ok=True)
    bg.save(str(output_path), "JPEG", quality=92)

    # Verify size < 2 MB (YouTube limit)
    size_mb = output_path.stat().st_size / (1024 * 1024)
    if size_mb > 2:
        bg.save(str(output_path), "JPEG", quality=75)

    return output_path
