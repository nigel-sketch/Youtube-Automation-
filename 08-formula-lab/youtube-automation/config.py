"""
Booked Wild YouTube Automation — Central Configuration

SOURCE OF TRUTH: Brand_Context.md, Brand_Voice_Guide.md,
Content_Standards.md, Product_Offerings.md (uploaded 2026-05-17)

SETUP NOTES:
- Add logo files to assets/:
    logo-dark.png   (BOOKEDWILD wordmark on dark background — for dark video slides)
    logo-light.png  (BOOKEDWILD wordmark on light background — for light thumbnails)
    logo-icon.png   (wolf icon only — for video watermark, bottom-right corner)
- Flip UPLOAD_PRIVACY to "public" only when Colin approves.
"""

# ── Channel Identity ──────────────────────────────────────────────────────────

CHANNEL_NAME = "Booked Wild"
CHANNEL_HANDLE = "@BookedWild"
CHANNEL_DESCRIPTION = (
    "Booked Wild gets independent travel and hospitality operators recommended by AI "
    "search engines like ChatGPT, Claude, and Perplexity — then rebuilds their booking "
    "flow so visibility turns into direct bookings, not commission paid to OTAs. "
    "Lodges, tour operators, retreat hosts, self-catering rentals, experience providers "
    "across Europe. New video every day."
)
CHANNEL_KEYWORDS = [
    "direct bookings", "AI visibility", "independent travel business",
    "OTA dependency", "tour operator marketing", "lodge marketing",
    "Booked Wild", "Deep Insight Audit", "AI search travel",
    "reduce OTA commission", "GetYourGuide commission", "Booking.com alternatives"
]

# ── Upload Settings ───────────────────────────────────────────────────────────

UPLOAD_PRIVACY = "private"          # → "public" when Colin approves
VIDEO_CATEGORY_ID = "27"            # Education
VIDEO_LANGUAGE = "en"
BASE_TAGS = [
    "direct bookings", "AI visibility", "OTA dependency", "independent travel",
    "tour operator", "lodge marketing", "Booked Wild", "Deep Insight Audit",
    "travel marketing", "direct booking strategy", "AI search"
]

# ── Brand Colours (from Booked Wild logo) ─────────────────────────────────────

BACKGROUND_COLOR = (15, 15, 15)         # #0F0F0F — near-black (logo background)
ACCENT_COLOR = (200, 113, 55)           # #C87137 — Booked Wild orange-brown
TEXT_COLOR = (255, 255, 255)            # white
SECONDARY_TEXT_COLOR = (200, 200, 200)  # light grey for body text

# ── Video Format ──────────────────────────────────────────────────────────────

VIDEO_RESOLUTION = (1920, 1080)
VIDEO_FPS = 24
THUMBNAIL_RESOLUTION = (1280, 720)

IMAGES_PER_VIDEO = 4    # Pexels image calls per video; set to 0 for Pillow-only

# Font: try assets first, then common system fonts (Ubuntu/Debian on GitHub Actions)
import os as _os
def _find_font() -> str:
    candidates = [
        "assets/font.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
    ]
    for p in candidates:
        if _os.path.exists(p):
            return p
    return candidates[0]

FONT_PATH = _find_font()
FONT_SIZE_TITLE = 80
FONT_SIZE_HEADING = 64
FONT_SIZE_BODY = 46
FONT_SIZE_CITATION = 26
TEXT_PADDING = 100

# ── Logo Paths (add these files manually to assets/) ───────

LOGO_DARK_PATH = "assets/logo-dark.png"    # for dark video slides
LOGO_LIGHT_PATH = "assets/logo-light.png"  # for light thumbnails
LOGO_ICON_PATH = "assets/logo-icon.png"    # for video watermark

# ── AI Models ─────────────────────────────────────────────────────────────────

CLAUDE_TOPIC_MODEL = "claude-haiku-4-5"
CLAUDE_SCRIPT_MODEL = "claude-sonnet-4-6"
GEMINI_RESEARCH_MODEL = "gemini-2.0-flash"
GEMINI_IMAGE_MODEL = "imagen-3.0-generate-002"
ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel — warm, professional

# ── CTAs ──────────────────────────────────────────────────────────────────────

AUDIT_CTA_URL = "https://www.bookedwild.com/audit/deep-insight"
FREE_AUDIT_URL = "https://www.bookedwild.com/audit"

# CTA Verb Library (Brand_Voice_Guide.md §8) — use these, never "Learn more" / "Get started"
CTA_EXAMPLES = [
    f"Run the free AI visibility audit at {FREE_AUDIT_URL}",
    f"Buy the £97 Deep Insight Audit at {AUDIT_CTA_URL}",
    "Book the 30-minute call at bookedwild.com",
    "See where you're invisible to AI search — run my audit",
    "Own your bookings — start at bookedwild.com",
]

# ── Topic Seeds ───────────────────────────────────────────────────────────────
# Three pillars: OTA dependency pain | AI visibility | Direct booking conversion

TOPIC_SEEDS = [
    # OTA dependency and margin pain
    "why GetYourGuide's 20–30% commission is eating your margin every single month",
    "the real cost of Booking.com dependency for independent lodge owners",
    "how independent travel operators are being taxed twice: invisibility then commission",
    "what you lose every time a guest books through Viator instead of direct",
    "why building your business on OTA rented land is the most expensive mistake in travel",
    "how to calculate exactly how much OTA commission is costing your business each year",
    "the rate parity trap: what OTA contracts actually mean for your direct booking price",

    # AI visibility
    "why ChatGPT and Perplexity aren't recommending your lodge, retreat, or tour",
    "how AI search is replacing OTA browsing for travel planning in 2026",
    "what schema markup actually does for independent travel business visibility",
    "why your competitor shows up in ChatGPT recommendations and you don't",
    "how to get your kayaking tour cited by AI search engines before your competitors do",
    "the five surfaces AI engines use to decide which travel businesses to recommend",
    "what llms.txt and AGENTS.md files do for your AI search visibility",
    "why entity density in your website copy matters for AI citation",

    # Direct booking conversion
    "why most independent travel websites lose bookings before the guest even enquires",
    "how to move bookings from GetYourGuide to direct without losing occupancy",
    "what a direct booking flow looks like for a 6-room lake district lodge",
    "how a Cornwall retreat recovered 38% of its bookings from OTAs to direct",
    "the Deep Insight Audit: what it checks and what operators find out",
    "how Direct Booking OS runs four AI agents for independent operators at £65 a month",
    "why fixing your booking funnel beats spending more on social media ads",
    "how independent operators build AI citation share before competitors lock it in",
    "what the Booked Wild Method's five surfaces cover for tour operators",
    "how to get your food and drink venue recommended by AI travel searches",
]

# ── Booked Wild SOP ───────────────────────────────────────────────────────────
# Source: Brand_Context.md, Brand_Voice_Guide.md, Content_Standards.md,
#         Product_Offerings.md — uploaded 2026-05-17

BOOKED_WILD_SOP = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOOKED WILD — SOURCE-OF-TRUTH CONTENT STANDARDS
For use by the YouTube automation article agent
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

═══════════════════════════════════════════════════
BRAND POSITIONING
═══════════════════════════════════════════════════

Primary:
Booked Wild gets independent travel and hospitality operators recommended by AI search
engines like ChatGPT, Claude, and Perplexity — then rebuilds the booking flow so
visibility turns into direct bookings, not commission paid to OTAs.

Short version (use across video CTAs and closings):
Get recommended. Own your bookings. Own your future.

Structural argument (use in Anti-OTA sections):
AI-mediated discovery is replacing OTA-mediated discovery for travel planning.
Operators visible in AI search can move bookings from Booking.com, GetYourGuide, Viator,
Airbnb, and Tripadvisor Experiences — where 15–30% commission disappears every month —
to direct channels they control. Operators invisible in AI search stay locked in the OTA
dependency cycle: pay platform commission for visibility, lose the guest relationship at
checkout, repeat next season.

Sharpest version:
Independent travel businesses are being taxed twice: first by invisibility, then by
commission. Booked Wild fixes both.

═══════════════════════════════════════════════════
IDEAL CUSTOMER PROFILES (ICPs)
Source: Brand_Context.md
═══════════════════════════════════════════════════

PRIMARY ICP: Independent travel and hospitality experience providers in Europe.
Annual revenue: £200k–£3m.

Specific operator types:
- Lodges and resorts with on-site hospitality (3–30 rooms)
- Tour operators running guided experiences (1–10 staff)
- Retreat hosts (yoga, wellness, adventure, creative)
- Self-catering rental owners (cabins, cottages, chalets, glamping, holiday homes — 2–10 props)
- Experience providers (kayaking, foraging, husky, photography, food tours)
- Destination food and drink venues (gastropubs, boutique restaurants, travel-draw cafés)

Operator profile:
- Already run some direct booking but pay 15–30% commission to OTAs on the rest
- Website built 3–8 years ago that's "fine but not winning"
- Spend £1,000–£8,000/month on an inconsistent mix of social, ads, and agency retainers
- Most bookings from OTA dependency, repeat guests, word of mouth, inconsistent SEO
- Actively worried about AI search visibility but don't know what to do
- Have read the OTA contract rate parity clauses and felt the squeeze
- Buy productised services with fixed prices when deliverable is concrete, sub-£2k for one-offs
- Buy retainers when there's a clear monthly outcome

SECONDARY ICP: Tourism boards and DMOs looking for B2B research/benchmark data.

THE SIX PAIN POINTS (use these verbatim in scripts):
1. "AI search is recommending competitors when travellers ask for accommodation, experiences,
   or restaurants in my region — and I don't show up at all."
2. "I'm paying GetYourGuide / Viator / Booking.com 20–30% commission on bookings I should
   be getting directly, and the commission costs are eating my margin."
3. "I've spent £5,000+ on websites and SEO that don't generate enquiries or bookings."
4. "I don't know who to trust on AI visibility — every agency claims to do it, nobody can
   prove it works, and the buzzwords are exhausting."
5. "Generic AI tools and ChatGPT prompts produce content that sounds like every other lodge
   / tour operator / restaurant in my area."
6. "I'm building my business on rented land. If Booking.com or Airbnb changes their
   algorithm or raises commission again, I'm exposed."

THREE DECISION TRIGGERS (when operators buy):
a. They see a competitor mentioned by ChatGPT or Perplexity when they test a relevant query
b. They receive a quarterly OTA commission statement that crystallises the cost
c. They're planning a website rebuild and realise traditional SEO doesn't address AI search

═══════════════════════════════════════════════════
VOICE MODE FOR VIDEO SCRIPTS
Source: Brand_Voice_Guide.md §3 and §9 (channel table)
═══════════════════════════════════════════════════

YouTube video scripts use: STORYTELLING HOST + ANTI-OTA ADVOCATE fire

Storytelling Host energy: Warm | Inviting | Sensory
Sounds like a travel writer who actually went to the place. Real details. Real people.
Real moments. Specific over generic. Sensory language with restraint.

Anti-OTA Advocate edges for argument sections: Confident | Unapologetic | Strategic
Sounds like someone who's read the OTA contracts, run the commission maths, and decided
to stop being polite about it.

Example Storytelling Host paragraph:
"Cottage in the Woods sleeps eight in a converted Forestry Commission lodge near Grizedale
Forest, with direct booking from £180 a night in November. Last winter Sarah, who runs it,
started messaging guests on the morning of arrival when the weather turned — the kind of
attention an OTA confirmation email never replicates. By March her direct booking share
had moved from 22% to 64%."

Example Anti-OTA Advocate line:
"OTAs are not partners. They are platforms designed to own your customer and your margins.
Every commission paid is a piece of your freedom handed away."

Wild/Tamed contrast (use deliberately, not on every slide):
Tamed world (OTA): algorithms, commissions, platform control, dependence, rented land
Wild world (direct): recommendations, margin, ownership, resilience, owned ground

═══════════════════════════════════════════════════
CONTENT STRUCTURE RULES
Source: Content_Standards.md + Brand_Voice_Guide.md §6
═══════════════════════════════════════════════════

RULE 1 — CITATION BLOCK
Every article opens with a 50–80 word direct answer within the first 100 words.
- Sentence 1: answers the implicit question of the article
- Following sentences: named entities, numbers, places — no "we help"
- Plain text, no rhetorical flourishes
- Entity-dense: named people, places, businesses, dates, statistics

RULE 2 — FRONT-LOADED ANSWER
Every H2 section opens with a 30–50 word direct answer before any prose or context.
44%+ of AI citations come from the first 30% of a piece.

RULE 3 — ENTITY DENSITY
Every paragraph contains 2+ named entities:
- Specific places (Lake District, Levi, Cornwall — not "the region")
- Specific businesses (Coastal Living Devon, GetYourGuide — not "a platform")
- Specific people (Colin Harrison — not "our founder")
- Specific numbers (£495, 27% commission, 200 operators)
- Specific dates (March 2026 — not "recently")
- Specific platforms (GoHighLevel, Tripadvisor, Viator)

RULE 4 — QUESTION-BASED H2s
Format H2s as questions — the operator's own question.

ARTICLE STRUCTURE:
1. meta title (50–60 chars, search-optimised)
2. meta description (140–155 chars, search phrase included)
3. slug (lowercase, hyphenated)
4. H1 (matches or closely echoes meta title)
5. Citation block (50–80 word direct answer, first 100 words)
6. Question-based H2s (4–6 sections, 80–120 words each)
7. Direct-answer opening sentence per section
8. Inline citations beside each stat or claim
9. CTA section using CTA Verb Library phrases
10. Sources list
11. Note for Colin — not for publication (QC + score)

═══════════════════════════════════════════════════
BANNED WORDS — ABSOLUTE
Source: Brand_Voice_Guide.md §5 and Content_Standards.md
═══════════════════════════════════════════════════

THE "NO HELP" RULE (single most important):
"help", "helping", "helps" — BANNED in all client-facing copy, no exceptions.
When you reach for "help", stop. Identify what physically happens. Write that instead.
  ❌ "We help operators get more bookings"
  ✅ "We rebuild the booking flow" / "We move bookings from OTA to direct"

VAGUE-MARKETING LIST (banned):
solutions, services (as generic noun), bespoke, tailored, custom (as vague qualifier),
world-class, cutting-edge, next-level, game-changing, innovative,
leverage (as verb), unlock, empower, elevate, transform,
synergy, holistic, robust (for software), seamless

CTA PLACEHOLDER LIST (banned):
get started, learn more, find out more, click here, submit

AGENCY SELF-AGGRANDISING (banned):
"we're passionate about", "we pride ourselves on", "industry-leading", "award-winning",
"helping ambitious brands", "unlock your potential", "digital transformation"

OVERPROMISE LANGUAGE (banned):
"guaranteed results", "proven to increase", "significantly increase",
"dramatically boost", "top-ranked", any revenue/ranking/booking guarantee

AI-FILLER LANGUAGE (banned):
"In today's competitive landscape...", "It's no secret that...",
"In the ever-evolving world of...", "Now more than ever..."

UK ENGLISH:
favour (not favor), optimisation (not optimization), recognise (not recognize),
travelling (not traveling), cancelled (not canceled)

═══════════════════════════════════════════════════
SIGNATURE VOCABULARY (use across scripts)
Source: Brand_Voice_Guide.md §5
═══════════════════════════════════════════════════

Core themes: wild, freedom, direct bookings, independence, local-first, sustainable,
purpose, simplicity, reconnection, control, profitability, resilience, regeneration,
legacy, presence, get recommended, AI search visibility, productised services

Anti-OTA anchors: "commission creep", "visibility theft", "dependence trap",
"race to the bottom pricing", "platform ownership vs provider ownership",
"building on rented land", "renting demand", "the illusion of OTA visibility"

Signature phrases (use across videos, not all on one):
- "Own your bookings. Own your brand. Own your future."
- "Don't build your business on rented land."
- "Every commission paid is a piece of your freedom handed away."
- "OTAs are not partners."
- "Direct bookings aren't just revenue — they're resilience."
- "Get recommended. Own your bookings. Own your future."

═══════════════════════════════════════════════════
CTA VERB LIBRARY
Source: Brand_Voice_Guide.md §8
═══════════════════════════════════════════════════

Use these for all video CTAs. Never "learn more" / "get started".

Audit / diagnostic:
  "Run the free AI visibility audit at bookedwild.com/audit"
  "See where you're invisible to AI search"
  "Check your AI visibility score"
  "Test your business — bookedwild.com/audit"

Buy / book:
  "Buy the £97 Deep Insight Audit at bookedwild.com/audit/deep-insight"
  "Book the 30-minute call at bookedwild.com"

Movement:
  "Own my bookings"
  "Take back my margin"
  "Leave the rented land"
  "Build the direct booking engine"

═══════════════════════════════════════════════════
PRODUCT KNOWLEDGE (for CTAs and references in scripts)
Source: Product_Offerings.md
═══════════════════════════════════════════════════

AUDIT FUNNEL:
- Free SEOptimer Audit: instant 100+ check, captures email — bookedwild.com/audit
- £97 Deep Insight Audit: 30-min video walkthrough + written 3-month roadmap.
  Manual review: Tripadvisor + GBP, AI prompt tests against 5 engines for operator's
  specific queries, named competitor analysis (3 competitors), prioritised action list.
  Delivered in 5 working days. — bookedwild.com/audit/deep-insight

ONE-OFF SERVICES:
- £395 Tripadvisor & GBP Optimisation (7 working days)
- £495 AI Visibility Fix: schema markup, llms.txt, AGENTS.md, citation blocks,
  plain-text pricing, FAQPage structure (14 working days)
- £1,200 Embedded Itinerary (+ optional £99/mo quarterly refresh)

PLATFORM:
- £65/mo Direct Booking OS (DBOS): GoHighLevel sub-account, booking calendar,
  automated confirmations, review requests, WhatsApp integration, 4 AI agents bundled:
  AI Inquiry Responder, AI Review Responder, AI Itinerary Builder, AI Booking Recovery
  Setup: £0 DIY or £495 DFY

WEBSITES:
- £850 + £65/mo AI-Optimised Property Website (solo accommodation hosts only)
  Full Astro build, schema, DBOS bundled, 4 SEO blog articles
- From £2,250 + VAT AI-Ready Website Rebuild (multi-property, tour operators)

FLAGSHIP RECURRING:
- AI Visibility Service — built on The Booked Wild Method (five surfaces):
  Pitch | Publish | Product | Profile | Partnership
  Standard: £1,500/mo — 2 articles/mo, 4 LinkedIn posts, quarterly press + partnership push
  Plus:     £2,500/mo — 4 articles/mo, 8 LinkedIn posts, monthly press + partnership push
  Premium:  £4,000/mo — 6 articles/mo + newsletter, monthly press, DMO-level partnerships
  All tiers: DBOS bundled, AI Visibility Fix bundled as month-one foundation
  Minimum: 9 months (one pause permitted)

FREE TOOLS (mention for credibility):
- AI Visibility Score — bookedwild.com/tools/ai-visibility-score
- Citation Checker — bookedwild.com/tools/citation-checker
- Booking Loss Calculator — bookedwild.com/tools/booking-loss-calculator

THE BOOKED WILD METHOD (name it, don't just say "our approach"):
Five surfaces: Pitch, Publish, Product, Profile, Partnership

OUTCOMES TRACKED (use in scripts to show specificity, no guarantees):
- AI citation share across 5 engines on agreed query targets
- Direct booking volume vs OTA mix
- OTA dependency percentage shift
(No ranking or revenue guarantees — "increase the likelihood", "build the citation surfaces",
"improve the structural signals")

═══════════════════════════════════════════════════
QC STANDARDS (self-check before outputting any script)
Source: Content_Standards.md
═══════════════════════════════════════════════════

✓ No invented or uncited statistics
✓ No "help" anywhere in the copy
✓ No words from the banned list
✓ Citation block: 50–80 word direct answer in first 100 words
✓ Every H2 opens with 30–50 word direct answer
✓ 2+ named entities per paragraph
✓ H2s are questions
✓ CTA uses CTA Verb Library phrases, links to correct URL
✓ UK English throughout
✓ No ranking / revenue / booking guarantees
✓ Sources are credible (STR, Phocuswire, Skift, Siteminder, AirDNA, CBRE, named trade press)
✓ Markdown is clean
✓ Article supports at least one Booked Wild commercial priority
"""

# ── File Paths ────────────────────────────────────────────────────────────────

UPLOAD_LOG_PATH = "logs/upload_log.json"
ASSETS_DIR = "youtube_automation/assets"
