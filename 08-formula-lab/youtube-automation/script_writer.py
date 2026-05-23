"""Write a Booked Wild video script using Claude, following all source-of-truth standards."""

import json
import time

import anthropic

import config

_SYSTEM = f"""You are the Booked Wild article agent. You write video scripts for independent
travel and hospitality experience providers in Europe — lodges (3–30 rooms), tour operators
(1–10 staff), retreat hosts (yoga, wellness, adventure), self-catering rental owners
(cabins, chalets, glamping — 2–10 properties), experience providers (kayaking, foraging,
husky, photography, food tours), and destination food and drink venues.

These operators have annual revenue of £200k–£3m, pay 15–30% commission to OTAs
(Booking.com, GetYourGuide, Viator, Airbnb, Tripadvisor Experiences), and are actively
worried about AI search visibility — not knowing whether ChatGPT and Perplexity recommend
them or their competitors.

VOICE MODE: Storytelling Host + Anti-OTA Advocate fire (per Brand_Voice_Guide.md §9
channel table for video scripts). Warm, inviting, real details, specific people and places
and numbers — with commercially fierce Anti-OTA edges in argument sections.

FULL BRAND SOP:
{config.BOOKED_WILD_SOP}

CONTENT STRUCTURE RULES (non-negotiable):
1. Citation block: 50–80 word direct answer within the first 100 words. Entity-dense.
2. Every H2 opens with a 30–50 word front-loaded direct answer before any prose.
3. Every paragraph has 2+ named entities (places, businesses, people, dates, numbers).
4. H2s are questions — the operator's own question.
5. Inline citations beside every stat or claim. Never invent a statistic.

THE "NO HELP" RULE (absolute, no exceptions):
The word "help" and its variants are banned from all copy. When you reach for "help",
stop — identify what physically happens and write that instead.
  Wrong: "We help operators get more bookings"
  Right: "We move bookings from OTA to direct" / "We rebuild the booking flow"

CTAs must use CTA Verb Library phrases (see SOP). Never "learn more", "get started",
"find out more". Always link to {config.AUDIT_CTA_URL} or {config.FREE_AUDIT_URL}.
"""

_RESPONSE_SCHEMA = """{
  "meta_title": "string (50-60 chars, search-optimised)",
  "meta_description": "string (140-155 chars, search phrase included)",
  "slug": "string (lowercase, hyphenated)",
  "youtube_title": "string (max 70 chars, curiosity-driven, operator's own words)",
  "youtube_description": "string (150-200 words — topic bullets, CTA URL, hashtags)",
  "tags": ["tag1", "tag2", "...up to 10 tags"],
  "article_markdown": "string — full article following this exact structure:

# H1 Title

[Citation block — 50-80 word direct answer, 2+ named entities, no 'help']

## Question H2 — the operator's real question?
[30-50 word front-loaded direct answer. Then 60-80 word body. 2+ named entities.
Cite every stat inline: e.g. GetYourGuide charges 20–30% commission per booking (GetYourGuide, 2025).]

## Question H2 — second question?
[Same structure: front-loaded answer, body, inline citations, 2+ named entities]

## Question H2 — third question?
[Same structure]

## Question H2 — fourth question (practical action)?
[Same structure]

## Ready to see where you're invisible to AI search?
[CTA — 40-60 words. Use CTA Verb Library phrases. Include the audit URL.
Never 'learn more' or 'get started'.]

## Sources
- [Source 1 — named publication/organisation, year]
- [Source 2]

---
*Note for Colin — not for publication*
[QC summary: which claims are cited, any areas to double-check, QC score rationale]",

  "qc_score": "integer 1-10",
  "qc_notes": "string (plain text note for Colin — citations checked, any soft claims flagged)"
}"""


def write_script(topic: str, research_pack: str, api_key: str) -> dict:
    """
    Return a dict matching _RESPONSE_SCHEMA.
    article_markdown follows full Booked Wild SOP structure.
    qc_score and qc_notes are the agent's self-assessment for Colin's review.
    """
    user_prompt = (
        f"Write a Booked Wild YouTube video script on this topic:\n\n"
        f"**{topic}**\n\n"
        f"Research pack — incorporate these facts naturally with inline citations:\n"
        f"{research_pack}\n\n"
        f"Hard requirements:\n"
        f"- Voice: Storytelling Host + Anti-OTA fire (real operator names, real places, "
        f"real numbers — warm but commercially fierce)\n"
        f"- Citation block: 50–80 word direct answer in first 100 words\n"
        f"- Every H2 opens with a 30–50 word front-loaded direct answer\n"
        f"- 2+ named entities per paragraph\n"
        f"- No invented statistics — cite every quantified claim inline\n"
        f"- No 'help' anywhere — describe what physically happens instead\n"
        f"- No banned words (see SOP)\n"
        f"- CTA uses CTA Verb Library phrases, links to {config.AUDIT_CTA_URL}\n"
        f"- UK English throughout\n"
        f"- Self-QC: score the article out of 10 and leave a note for Colin\n\n"
        f"Respond with valid JSON matching this schema:\n{_RESPONSE_SCHEMA}"
    )

    client = anthropic.Anthropic(api_key=api_key)

    for attempt in range(3):
        try:
            response = client.messages.create(
                model=config.CLAUDE_SCRIPT_MODEL,
                max_tokens=8000,
                system=_SYSTEM,
                messages=[{"role": "user", "content": user_prompt}],
            )
            raw = response.content[0].text.strip()

            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]

            result = json.loads(raw.strip())

            qc_score = result.get("qc_score", "?")
            qc_notes = result.get("qc_notes", "")
            print(f"[script_writer] QC score: {qc_score}/10")
            if qc_score and int(str(qc_score)) < 7:
                print(f"[script_writer] WARNING — low QC score. Notes: {qc_notes}")

            return result

        except json.JSONDecodeError as e:
            if attempt < 2:
                user_prompt += (
                    "\n\nYour previous response was not valid JSON. "
                    "Return ONLY the JSON object, no surrounding text or markdown fences."
                )
                time.sleep(3)
                continue
            raise ValueError(f"Claude returned invalid JSON after 3 attempts: {e}") from e

        except anthropic.APIConnectionError:
            if attempt == 2:
                raise
            time.sleep(5 * (2 ** attempt))

        except anthropic.RateLimitError:
            time.sleep(60)

    raise RuntimeError("Failed to generate script after 3 attempts")
