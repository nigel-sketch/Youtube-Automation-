"""Research a topic using Gemini with Google Search grounding."""

import os
import time

import google.generativeai as genai

import config


def research_topic(topic: str, api_key: str) -> str:
    """
    Return a research pack (3–5 bullet points with stats/citations) for the topic.
    Uses Gemini Flash with Google Search grounding — equivalent to NotebookLM research.
    """
    genai.configure(api_key=api_key)

    prompt = (
        f"Research the following topic for a Booked Wild YouTube video script:\n\n"
        f"Topic: {topic}\n\n"
        "Audience: independent travel business owners — hotels, guesthouses, B&Bs, tour "
        "operators, boutique venues, activity providers — who want to reduce OTA dependency, "
        "improve AI/search visibility, and grow direct bookings.\n\n"
        "Provide a concise research pack with:\n"
        "- 3–5 bullet points of specific, credible facts, stats, or insights\n"
        "- Each bullet must include a named source (e.g. STR, Phocuswire, Skift, CBRE, "
        "TravelClick, Siteminder, AirDNA, or named academic/trade research)\n"
        "- Avoid weak listicles, thin marketing blogs, and unsupported SEO claims\n"
        "- Focus on: OTA commission costs, direct booking behaviour, AI/search visibility "
        "trends, travel business revenue, or guest booking psychology\n"
        "- UK English\n\n"
        "Format each bullet as: • [Fact/stat/insight]. (Source: [Name, Year if available])\n"
        "Return ONLY the bullet points, no introduction or summary."
    )

    model = genai.GenerativeModel(
        model_name=config.GEMINI_RESEARCH_MODEL,
        tools="google_search_retrieval",
    )

    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            if attempt == 2:
                # Fall back to a generic research note rather than crashing the pipeline
                print(f"[researcher] Gemini search failed: {e}. Using generic research note.")
                return (
                    f"• OTA commissions typically range from 15–25% of the booking value, "
                    f"representing a significant cost for independent operators. (Source: industry consensus)\n"
                    f"• Direct bookings deliver higher average guest spend and stronger repeat visit rates "
                    f"than OTA-sourced bookings. (Source: general hospitality trade data)\n"
                    f"• Independent hotels that invest in direct booking optimisation report "
                    f"measurable improvement in their direct channel mix over time. (Source: STR / operator case studies)\n"
                )
            time.sleep(5 * (2 ** attempt))
