"""Parse a Booked Wild markdown article into structured VideoScript objects."""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class VideoSlide:
    heading: str
    body_text: str
    citation: str | None = None


@dataclass
class VideoScript:
    title: str
    slides: list[VideoSlide] = field(default_factory=list)
    cta: str = ""
    youtube_title: str = ""
    youtube_description: str = ""
    tags: list[str] = field(default_factory=list)


def parse_article(md_text: str) -> VideoScript:
    """
    Parse a Booked Wild markdown article into a VideoScript.

    Expected markdown structure:
      # H1 Title
      ## Question H2
      Body text...
      ## Another H2
      Body text...
      ## Sources
      - source list (excluded from video)
    """
    lines = md_text.strip().splitlines()
    script = VideoScript(title="")

    current_heading = ""
    current_body: list[str] = []

    # Headings that are excluded entirely from the video
    _EXCLUDED_HEADINGS = {
        "sources", "references", "source map",
        "note for colin", "note for colin — not for publication",
        "qc notes", "qc report",
    }

    # Headings that map to the CTA slide
    _CTA_HEADINGS = {
        "ready to find your direct booking gaps?",
        "what should you do next?",
        "next steps", "what next?", "cta",
        "want to find your direct booking gaps?",
    }

    def flush(heading: str, body_lines: list[str]):
        body = "\n".join(body_lines).strip()
        if not body:
            return
        if heading.lower() in _EXCLUDED_HEADINGS:
            return
        # Strip the "---" horizontal rule that precedes Note for Colin
        if body.startswith("---"):
            return

        # Extract inline citation — e.g. (Source: STR, 2023)
        citation_match = re.search(r"\(Source:\s*([^)]+)\)", body)
        citation = citation_match.group(1).strip() if citation_match else None
        # Remove citations from spoken text (keep in slide footer instead)
        clean_body = re.sub(r"\s*\(Source:[^)]+\)", "", body).strip()
        # Remove markdown link syntax
        clean_body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", clean_body)
        # Remove bold/italic markers
        clean_body = re.sub(r"\*\*(.+?)\*\*", r"\1", clean_body)
        clean_body = re.sub(r"\*(.+?)\*", r"\1", clean_body)
        # Remove horizontal rules
        clean_body = re.sub(r"---+", "", clean_body).strip()

        if heading.lower() in _CTA_HEADINGS:
            script.cta = clean_body
        else:
            script.slides.append(VideoSlide(heading=heading, body_text=clean_body, citation=citation))

    for line in lines:
        if line.startswith("# ") and not script.title:
            script.title = line[2:].strip()
        elif line.startswith("## "):
            flush(current_heading, current_body)
            current_heading = line[3:].strip()
            current_body = []
        elif current_heading:
            current_body.append(line)

    flush(current_heading, current_body)

    if not script.youtube_title:
        script.youtube_title = script.title

    return script


def from_script_dict(script_dict: dict) -> VideoScript:
    """Build a VideoScript from the dict returned by script_writer.write_script()."""
    md = script_dict.get("article_markdown", "")
    video_script = parse_article(md)
    video_script.youtube_title = script_dict.get("youtube_title", video_script.title)
    video_script.youtube_description = script_dict.get("youtube_description", "")
    video_script.tags = script_dict.get("tags", [])
    return video_script
