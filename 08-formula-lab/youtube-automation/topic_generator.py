"""Generate a fresh daily topic for the Booked Wild channel using Claude, avoiding recently used ones."""

import json
import os
import random
import time
from pathlib import Path

import anthropic

import config


def _load_recent_topics(history_path: str, limit: int = 10) -> list[str]:
    path = Path(history_path)
    if not path.exists():
        return []
    with open(path) as f:
        data = json.load(f)
    return [entry["topic"] for entry in data.get("topics", [])[-limit:]]


def generate_topic(history_path: str, api_key: str) -> str:
    """Return a topic title string, avoiding the last 10 uploaded topics."""
    recent = _load_recent_topics(history_path)
    seeds_sample = random.sample(config.TOPIC_SEEDS, min(5, len(config.TOPIC_SEEDS)))

    avoid_block = ""
    if recent:
        avoid_block = "Do NOT use any of these recently covered topics:\n" + "\n".join(
            f"- {t}" for t in recent
        )

    prompt = (
        f"You are a content strategist for '{config.CHANNEL_NAME}', a YouTube channel "
        "helping independent travel business owners — hotels, guesthouses, B&Bs, tour "
        "operators, boutique venues, and activity providers — get found by AI, grow direct "
        "bookings, and stop losing margin and customer data to OTAs.\n\n"
        f"{avoid_block}\n\n"
        "Generate ONE new video topic title. Requirements:\n"
        "- 8–12 words\n"
        "- Specific and actionable, not generic\n"
        "- Written from the operator's perspective (their question or problem)\n"
        "- UK English\n"
        "- Relevant to: OTA dependency, AI/search visibility, direct booking conversion, "
        "margin loss, customer data ownership, or the Deep Insight Audit\n"
        "- Must NOT make booking/revenue/ranking guarantees\n\n"
        "Inspiration themes (don't copy verbatim):\n"
        + "\n".join(f"- {s}" for s in seeds_sample)
        + "\n\nReturn ONLY the topic title, nothing else."
    )

    client = anthropic.Anthropic(api_key=api_key)
    for attempt in range(3):
        try:
            response = client.messages.create(
                model=config.CLAUDE_TOPIC_MODEL,
                max_tokens=60,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content[0].text.strip().strip('"')
        except anthropic.APIConnectionError:
            if attempt == 2:
                raise
            time.sleep(5 * (2 ** attempt))
        except anthropic.RateLimitError:
            time.sleep(60)
    raise RuntimeError("Failed to generate topic after 3 attempts")
