"""Build a branded MP4 video from a VideoScript using MoviePy and ElevenLabs/gTTS."""

from __future__ import annotations

import io
import os
import time
from pathlib import Path

import google.generativeai as genai
from moviepy import (
    AudioFileClip,
    CompositeVideoClip,
    ImageClip,
    concatenate_audioclips,
    concatenate_videoclips,
    vfx,
)
from PIL import Image, ImageDraw, ImageFont

import config
from article_to_video import VideoScript, VideoSlide


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        return ImageFont.truetype(config.FONT_PATH, size)
    except (IOError, OSError):
        return ImageFont.load_default()


def _wrap_text(text: str, font, max_width: int, draw: ImageDraw.ImageDraw) -> str:
    words = text.split()
    lines = []
    current = []
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


def _fetch_pexels_image(query: str, api_key: str, size: tuple[int, int]) -> Image.Image | None:
    """Fetch a relevant stock photo from Pexels as a slide background."""
    import requests
    try:
        resp = requests.get(
            "https://api.pexels.com/v1/search",
            headers={"Authorization": api_key},
            params={"query": query, "per_page": 1, "orientation": "landscape"},
            timeout=10,
        )
        resp.raise_for_status()
        photos = resp.json().get("photos", [])
        if not photos:
            return None
        img_url = photos[0]["src"]["original"]
        img_resp = requests.get(img_url, timeout=20)
        img_resp.raise_for_status()
        return Image.open(io.BytesIO(img_resp.content)).resize(size)
    except Exception as e:
        print(f"[video_creator] Pexels fetch failed: {e}. Using solid background.")
    return None


def _local_background(size: tuple[int, int]) -> Image.Image | None:
    """Pick a random image from assets/images/ or assets/ as slide background."""
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


def _make_slide_image(
    heading: str,
    body_text: str,
    citation: str | None,
    pexels_key: str | None,
    use_pexels: bool,
) -> Image.Image:
    w, h = config.VIDEO_RESOLUTION
    pad = config.TEXT_PADDING

    # Try local images first (from assets/images/), then Pexels, then solid colour
    bg = _local_background((w, h))
    if bg is None and use_pexels and pexels_key:
        search_query = f"travel nature {heading[:40]}"
        bg = _fetch_pexels_image(search_query, pexels_key, (w, h))
    else:
        bg = None

    if bg is None:
        bg = Image.new("RGB", (w, h), color=config.BACKGROUND_COLOR)
        # Subtle accent stripe on left edge
        draw = ImageDraw.Draw(bg)
        draw.rectangle([(0, 0), (8, h)], fill=config.ACCENT_COLOR)

    draw = ImageDraw.Draw(bg, "RGBA")

    # Dark overlay so text is always readable on any background
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 160))
    bg = Image.alpha_composite(bg.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(bg)

    heading_font = _load_font(config.FONT_SIZE_HEADING)
    body_font = _load_font(config.FONT_SIZE_BODY)
    citation_font = _load_font(config.FONT_SIZE_CITATION)

    max_text_width = w - 2 * pad

    # Draw heading
    wrapped_heading = _wrap_text(heading, heading_font, max_text_width, draw)
    heading_bbox = draw.multiline_textbbox((0, 0), wrapped_heading, font=heading_font, spacing=8)
    heading_h = heading_bbox[3] - heading_bbox[1]

    # Draw body
    wrapped_body = _wrap_text(body_text, body_font, max_text_width, draw)
    body_bbox = draw.multiline_textbbox((0, 0), wrapped_body, font=body_font, spacing=12)
    body_h = body_bbox[3] - body_bbox[1]

    gap = 40
    total_h = heading_h + gap + body_h
    start_y = (h - total_h) // 2

    draw.multiline_text(
        (pad, start_y),
        wrapped_heading,
        font=heading_font,
        fill=config.TEXT_COLOR,
        spacing=8,
    )
    draw.multiline_text(
        (pad, start_y + heading_h + gap),
        wrapped_body,
        font=body_font,
        fill=(220, 220, 220),
        spacing=12,
    )

    # Citation
    if citation:
        draw.text(
            (pad, h - pad - 30),
            f"Source: {citation}",
            font=citation_font,
            fill=(160, 160, 160),
        )

    # Logo watermark
    logo_path = Path(config.LOGO_ICON_PATH)
    if logo_path.exists():
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo.thumbnail((220, 80))
            logo_x = w - logo.width - pad // 2
            logo_y = h - logo.height - pad // 2
            bg.paste(logo, (logo_x, logo_y), logo)
        except Exception:
            pass

    return bg


def _make_intro_slide(title: str) -> Image.Image:
    w, h = config.VIDEO_RESOLUTION
    img = Image.new("RGB", (w, h), color=config.BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (8, h)], fill=config.ACCENT_COLOR)

    title_font = _load_font(config.FONT_SIZE_TITLE)
    sub_font = _load_font(config.FONT_SIZE_BODY)

    max_w = w - 2 * config.TEXT_PADDING
    wrapped = _wrap_text(title, title_font, max_w, draw)
    bbox = draw.multiline_textbbox((0, 0), wrapped, font=title_font, spacing=10)
    th = bbox[3] - bbox[1]
    draw.multiline_text(
        (config.TEXT_PADDING, (h - th) // 2 - 40),
        wrapped,
        font=title_font,
        fill=config.TEXT_COLOR,
        spacing=10,
    )
    draw.text(
        (config.TEXT_PADDING, (h + th) // 2 + 20),
        config.CHANNEL_NAME,
        font=sub_font,
        fill=config.ACCENT_COLOR,
    )
    return img


def _make_outro_slide(cta: str) -> Image.Image:
    w, h = config.VIDEO_RESOLUTION
    img = Image.new("RGB", (w, h), color=config.BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (w, 8)], fill=config.ACCENT_COLOR)

    body_font = _load_font(config.FONT_SIZE_BODY)
    sub_font = _load_font(config.FONT_SIZE_CITATION)

    max_w = w - 2 * config.TEXT_PADDING
    wrapped_cta = _wrap_text(cta or "Subscribe for daily travel marketing strategy.", body_font, max_w, draw)
    bbox = draw.multiline_textbbox((0, 0), wrapped_cta, font=body_font, spacing=12)
    th = bbox[3] - bbox[1]
    draw.multiline_text(
        (config.TEXT_PADDING, (h - th) // 2),
        wrapped_cta,
        font=body_font,
        fill=config.TEXT_COLOR,
        spacing=12,
    )
    draw.text(
        (config.TEXT_PADDING, h - config.TEXT_PADDING - 30),
        config.CHANNEL_HANDLE,
        font=sub_font,
        fill=config.ACCENT_COLOR,
    )
    return img


def _clean_for_tts(text: str) -> str:
    """Strip markdown symbols that TTS would read aloud."""
    import re
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)   # **bold** → bold
    text = re.sub(r'\*(.+?)\*', r'\1', text)         # *italic* → italic
    text = re.sub(r'---+', '', text)                  # horizontal rules
    text = re.sub(r'#+\s*', '', text)                 # headings
    text = re.sub(r'^\s*[-•]\s*', '', text, flags=re.MULTILINE)  # bullets
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)        # links
    text = re.sub(r'\n{2,}', ' ', text)              # multiple newlines → space
    return text.strip()


def _synth_audio(text: str, output_path: Path) -> float:
    """Synthesise text to MP3 using Edge TTS (primary), ElevenLabs, or gTTS fallback."""
    text = _clean_for_tts(text)

    # Try Edge TTS first — free, high quality, no account needed
    try:
        import asyncio
        import edge_tts
        async def _edge_synth():
            communicate = edge_tts.Communicate(text, voice="en-GB-SoniaNeural")
            await communicate.save(str(output_path))
        asyncio.run(_edge_synth())
    except Exception as e:
        print(f"[video_creator] Edge TTS failed: {e}. Falling back to gTTS.")
        from gtts import gTTS
        tts = gTTS(text=text, lang="en", tld="co.uk")
        tts.save(str(output_path))

    clip = AudioFileClip(str(output_path))
    duration = clip.duration
    clip.close()
    return duration


def build_video(
    script: VideoScript,
    output_path: Path,
    pexels_key: str | None = None,
) -> Path:
    """
    Assemble a full MP4 video from the VideoScript.
    Returns the path to the finished video file.
    """
    tmp_dir = output_path.parent / "tmp_audio"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    clips = []
    audio_clips = []
    pexels_calls_used = 0

    # ── Intro slide ───────────────────────────────────────────────────────────
    intro_audio_path = tmp_dir / "intro.mp3"
    intro_duration = _synth_audio(script.title, intro_audio_path)
    intro_duration = max(intro_duration, 3.0)

    intro_img = _make_intro_slide(script.title)
    intro_arr = __import__("numpy").array(intro_img)
    intro_clip = ImageClip(intro_arr).with_duration(intro_duration).with_effects([vfx.FadeIn(0.4)])
    clips.append(intro_clip)
    audio_clips.append(AudioFileClip(str(intro_audio_path)))

    # ── Content slides ────────────────────────────────────────────────────────
    for i, slide in enumerate(script.slides):
        use_pexels = (
            pexels_key is not None
            and config.IMAGES_PER_VIDEO > 0
            and pexels_calls_used < config.IMAGES_PER_VIDEO
        )

        slide_audio_path = tmp_dir / f"slide_{i}.mp3"
        slide_duration = _synth_audio(slide.body_text, slide_audio_path)
        slide_duration = max(slide_duration, 4.0)

        slide_img = _make_slide_image(
            heading=slide.heading,
            body_text=slide.body_text,
            citation=slide.citation,
            pexels_key=pexels_key,
            use_pexels=use_pexels,
        )
        if use_pexels:
            pexels_calls_used += 1

        import numpy as np
        slide_arr = np.array(slide_img)
        slide_clip = (
            ImageClip(slide_arr)
            .with_duration(slide_duration)
            .with_effects([vfx.FadeIn(0.3), vfx.FadeOut(0.2)])
        )
        clips.append(slide_clip)
        audio_clips.append(AudioFileClip(str(slide_audio_path)))

    # ── Outro slide ───────────────────────────────────────────────────────────
    outro_text = script.cta or f"Subscribe to {config.CHANNEL_NAME} for daily travel marketing strategy."
    outro_audio_path = tmp_dir / "outro.mp3"
    outro_duration = _synth_audio(outro_text, outro_audio_path)
    outro_duration = max(outro_duration, 4.0)

    import numpy as np
    outro_img = _make_outro_slide(script.cta)
    outro_arr = np.array(outro_img)
    outro_clip = ImageClip(outro_arr).with_duration(outro_duration).with_effects([vfx.FadeIn(0.4)])
    clips.append(outro_clip)
    audio_clips.append(AudioFileClip(str(outro_audio_path)))

    # ── Assemble ──────────────────────────────────────────────────────────────
    final_video = concatenate_videoclips(clips, method="compose")
    final_audio = concatenate_audioclips(audio_clips)
    final_video = final_video.with_audio(final_audio)

    final_video.write_videofile(
        str(output_path),
        fps=config.VIDEO_FPS,
        codec="libx264",
        audio_codec="aac",
        temp_audiofile="temp_audio.m4a",
        temp_audiofile_path=str(tmp_dir),
        remove_temp=True,
        logger=None,
    )

    # Clean up tmp audio
    import shutil
    shutil.rmtree(tmp_dir, ignore_errors=True)

    return output_path
