# Content Standards

The build-side execution rules for every piece of writing on bookedwild.com. This file works alongside `brand_context/Brand_Voice_Guide.md` — that file owns voice, tone, modes, and signature language. This file owns the structural editorial rules that make AI engines extract Booked Wild content cleanly.

If the two ever conflict, the Brand_Voice_Guide is the canonical source.

---

## Quick map of what lives where

- **Brand_Voice_Guide.md** (in `/brand_context/`) — Voice modes, signature phrases, wild/tamed contrast, banned words list, signature vocabulary, anti-OTA anchors, when to use which voice mode per channel.
- **Content_Standards.md** (this file) — Structural rules every page follows: citation block format, front-loaded answer rule, entity density rule, Specificity Audit checklist, FAQ structure, list/table rules, freshness rules.

Both files apply to every page. Read both before generating content.

---

## The four non-negotiable structural rules

These apply to every page on the site, regardless of voice mode.

### 1. The citation block

Every page opens with a 50–80 word direct answer in the first paragraph. Sits within the first 100 words of the page. Voice mode varies by page (Rewilding Evangelist for homepage, Commercial Guide for service pages, etc.) — structure is constant.

**Format:**

- Sentence one answers the implicit question of the page
- Following sentences add concrete specificity (named entities, numbers, places)
- No "we help" / "we offer" / "we provide" — describe what physically happens
- Plain text, no rhetorical flourishes
- Entity-dense (named people, places, businesses, dates, statistics)

**Example (service page):**

> "The £495 AI Visibility Fix audits your website, Tripadvisor profile, Google Business Profile, and AI search citations against 20 specific signals. We then implement the technical fixes — schema markup, llms.txt, citation blocks, plain-text pricing, FAQPage structure — that AI engines like ChatGPT and Perplexity use to decide which businesses to recommend. Delivered in 14 days."

### 2. Front-loaded answer rule

Every H2 section opens with a 30–50 word direct answer to the H2's implicit question, before any prose, build-up, or context.

44%+ of AI citations come from the first 30% of a piece. Travel publications traditionally bury the answer; AI engines skip past the lede and cite later. Lead with the answer. Add the supporting prose afterward.

**Bad:**
> ## Why does AI search matter for travel businesses?
>
> Travel has always been a deeply personal, emotional decision. People dream about places. They imagine themselves there. They ask friends, read reviews, plan and re-plan. The way that planning happens has shifted gradually...

**Good:**
> ## Why does AI search matter for travel businesses?
>
> AI search engines like ChatGPT, Claude, and Perplexity now answer travel-planning questions directly without sending users to operator websites. Travellers ask "best lodges in Cornwall" and get three named recommendations — if your business isn't one of them, you don't appear in the buying decision at all.
>
> This shift accelerated through 2025 and 2026...

### 3. Entity density

Every paragraph contains at least 2 named entities. Cited content has 3-4x higher entity density than normal English. Match it.

Named entities:

- Specific places (Lake District, Levi, Cornwall, not "the region")
- Specific businesses (Coastal Living Devon, not "a holiday let")
- Specific people (Colin Harrison, not "our founder")
- Specific dates (March 2026, not "recently")
- Specific numbers (£495, 27% commission, 200 operators)
- Specific tools or platforms (GoHighLevel, GetYourGuide, Tripadvisor)
- Specific schema types (FAQPage, Service, Person)

**Heuristic:** if you're reaching for "many," "various," "leading," "robust," "premium" — stop. Replace with a named example or a number.

**Bad (entity density 0):**
> Many independent operators struggle with platform commissions, which can take a significant chunk of their revenue and limit their ability to invest in marketing.

**Good (entity density 4):**
> GetYourGuide takes 20–30% commission per booking. Viator's basic rate is 27%. Booking.com sits at 15–18% for accommodation. For an independent Cornish lodge turning over £400,000 a year, that's £60,000–£120,000 leaving the business annually.

### 4. Question-based H2s

Format H2s as questions wherever possible. AI engines extract better from question-shaped headings, and they match how prospects phrase queries.

| Bad H2 | Good H2 |
|--------|---------|
| Our Approach | How does the Booked Wild Method work? |
| The Process | What happens during a £97 Deep Insight Audit? |
| About Direct Booking | Why do independent lodges lose bookings to OTAs? |
| Pricing | How much does the AI Visibility Fix cost? |
| Services | What services does Booked Wild offer? |

---

## The Specificity Audit (pre-publish checklist)

Before any page goes live, it passes the Specificity Audit (Crestodina framework). Run this as the final pre-publish check.

### 1. Descriptive H1

The H1 must tell a stranger exactly what this page is about. If you removed the rest of the page, would the H1 alone explain its purpose?

- ❌ "Welcome to Booked Wild"
- ❌ "Get Recommended"
- ✅ "Marketing for independent travel and hospitality businesses across Europe"
- ✅ "The £495 AI Visibility Fix"

### 2. Specific hero image

Specific to this page's exact topic. No stock photography. No generic AI imagery (robots, brains, circuits). No agency-trope imagery (laptops, handshakes, lightbulbs).

- ✅ Screenshot of an AI engine citing Booked Wild content
- ✅ Real photograph of a Booked Wild client's lodge
- ✅ Structured diagram specific to this page's argument

### 3. Descriptive subheads

Every H2 must add information. Generic subheads ("Solutions," "Services," "Learn More") get rewritten or removed.

### 4. Descriptive navigation labels

Top nav and footer labels must be descriptive.

- ❌ "Tools" → ✅ "Free audit"
- ❌ "About" → ✅ "How we work" or "Our team"
- ❌ "Resources" → ✅ "Journal" or "Research"
- ❌ "Contact" → ✅ "Book a call"

### 5. Compelling CTA verbs

Every CTA describes what physically happens. See the CTA Verb Library in Brand_Voice_Guide.md for the full list.

- ❌ "Submit" → ✅ "Run my audit"
- ❌ "Get started" → ✅ "Book the 30-minute call"
- ❌ "Click here" → ✅ "See what's included for £495"
- ❌ "Learn more" → ✅ "Read the September 2026 research"

---

## Source attribution and references

Statistics and external claims need verifiable sourcing. Every page on the site uses the same pattern: inline hyperlinks in body copy, with `/research/sources` acting as the single canonical bibliography that catalogues everything cited. There is no on-page References section anywhere on the site — not on pillars, not on research reports, not in footers.

Note: "citation block" (the 50–80 word answer block at the top of every page) is a separate concept from "citations" (sourcing for statistics). They share a word but mean different things on this site.

### The pattern: inline hyperlinks site-wide

The "one hyperlinked statistic per ~200 words" rule from the four non-negotiables is the floor, not the ceiling. The same rule applies on every page type — pillars, satellites, services, ICPs, destinations, case studies, research reports, tools, the homepage. No special pillar-only or research-only escalation.

- Anchor text describes the source ("Princeton/Georgia Tech GEO research"), not "click here," "this study," or the bare statistic.
- Open in same tab; `rel="noopener"` only where the destination is a domain we can't fully vouch for.
- Dead or moved links break pre-publish review. Fix or remove before merge.

### Where the link points

Three routing rules:

- **Open external source available** → link directly to the original (Princeton arxiv, Schema.org docs, Eurostat dataset, individual OTA published rates). Most links go here.
- **Paywalled or hard-to-access source** → link to `/research/sources#[source-slug]` instead of the paywall. Reader gets context and Booked Wild's interpretation; the original is still attributed visibly on the sources page.
- **Booked Wild's own proprietary data** → link to the relevant report on `/research/[slug]` (e.g. the European Travel AI Visibility Index Q1 2026 page).

### Schema citations (machine-readable layer)

Even though there's no visible bibliography, the JSON-LD on every Article and ScholarlyArticle still emits a `citation` array with the structured source records. AI engines parsing structured data see all the citations regardless of page presentation. This is the AEO-relevant signal — the visual treatment is for human readers.

- Article schema includes a `citation` array generated from the inline links at build time
- Each `citation` references a `ScholarlyArticle`, `Report`, or `CreativeWork` with `author`, `datePublished`, `publisher`, `url`
- `/research/sources` itself emits `ItemList` schema with each source as an item

### The references hub: `/research/sources`

The single canonical catalogue for every external source cited across the site, plus Booked Wild's own primary research as a visibly distinct section.

- Listed by topic cluster (AI citation, OTA economics, travel buyer behaviour, schema, performance, direct booking, European market)
- Each entry: source title (linked to original), author(s), year, publication, source type, paywall flag if applicable, last-verified date, "Cited on N pages" auto-generated count
- Booked Wild's own data sits in a visually distinct amber-tinted section at the top of the page
- The "Cited on N pages" count is auto-generated at build time by scanning rendered HTML for outbound URLs matching each source's `source_url`

This page is genuinely useful as a standalone reading surface, which is what makes it a citation target rather than just a backstop. AI engines and human researchers searching for a specific study can land on `/research/sources`, see Booked Wild's curation, and discover the brand. See `Reference_Page_Spec.md` for the full page spec.

### Distinguishing proprietary vs external statistics

Booked Wild's own data — from the European Travel AI Visibility Index, internal client tracking, our citation monitoring — needs to be **visibly distinct** from third-party data, both inline in body copy and on the references hub.

- **Inline:** prefix proprietary stats with "Booked Wild research:" before the figure, then link to the relevant report on `/research/[slug]`.
- **On `/research/sources`:** proprietary entries appear at the top of the page in a separate amber-tinted section ("Booked Wild research and primary data"), each carrying a "Booked Wild" tag.
- **External stats:** standard inline link to the original source, no prefix.

The proprietary data is the moat. Mixing it indistinguishably with external research undersells it.

### What does not need a hyperlink-cited source

- Direct quotes from named clients (the named attribution is the source)
- Claims about Booked Wild's own services, prices, or process (we are the source)
- Common knowledge in the travel industry stated without a specific number (e.g. "OTAs charge commission on every booking" — uncontroversial, no source needed)
- Hypothetical or illustrative numbers explicitly framed as such ("imagine a £400,000-turnover lodge...")

### What does need a hyperlink-cited source

- Any specific percentage, rate, or quantified claim about AI citation behaviour, OTA economics, or travel buyer patterns
- Any statistic attributed to a named external organisation
- Any technical claim about how AI engines, schema, or search algorithms work that isn't documented on Booked Wild's own pages
- Any market-sizing figure (TAM, sector revenue, traveller volumes)

If a pillar or research report includes 5+ unsourced quantified claims at pre-publish review, it goes back to the author. The whole point of long-form authority content is that it stands up to scrutiny.

### Build-time validation

A simple build script enforces the pattern without writers needing to touch the sources collection directly:

- All outbound links in MDX files are scanned at build time
- Any URL that matches a `source_url` in `src/content/sources/` increments that source's `cited_on` count automatically
- New external sources cited in body copy that don't yet exist in the sources collection trigger a build warning (not failure) — the writer or editor adds the MDX entry as part of the editorial flow
- Dead-link checking runs as a separate quarterly script, not on every build

---

## Voice mode per page type

The voice mode flexes by page. The structural rules above apply across all modes.

| Page type | Voice mode | Notes |
|-----------|------------|-------|
| Homepage hero / opening | Rewilding Evangelist + Commercial Guide blend | Movement language allowed; signature phrases allowed |
| Homepage body sections | Commercial Guide | Specific, structured, productised |
| `/audit` and `/audit/deep-insight` | Commercial Guide | Outcome-led, posted price, specific deliverables |
| Service pages (`/services/[slug]`) | Commercial Guide | The workhorse mode |
| ICP pages (`/marketing-for/[slug]`) | Commercial Guide with brief Anti-OTA edges | Lead with the ICP's pain |
| Destination pages (`/destinations/[slug]`) | Commercial Guide | Operator-facing, regional pain |
| Case studies | Storytelling Host | Real names, real numbers, real outcomes |
| Journal pillars | Commercial Guide with Anti-OTA fire on argument sections | Pillar quality, front-loaded |
| Journal satellites | Commercial Guide | Tactical, FAQ-heavy |
| Research reports | Commercial Guide with citation density | Methodologically defensible |
| Tools | Commercial Guide | Functional, outcome-led |
| Pricing | Commercial Guide | Plain numbers, posted, no apology |
| Method | Commercial Guide with Rewilding Evangelist on intro | Named framework |
| About | Rewilding Evangelist for opening, Commercial Guide for team/structure | Manifesto allowed in opening section |
| About / Founder (Colin) | Rewilding Evangelist + Storytelling Host | Real bio, embedded specifics |
| Journalist / team pages | Storytelling Host | Warm, specific, real |
| Contact | Commercial Guide | Functional, no flourish |
| Cold email | Anti-OTA Advocate | Sharp, specific observation, single CTA |
| LinkedIn (Colin) | Storytelling Host with Anti-OTA fire | Personal, opinionated |
| Onboarding / member emails | Ally & Mentor | Supportive, practical |

---

## Banned words (canonical list)

The full list lives in Brand_Voice_Guide.md. Headline summary:

- **The "help" rule:** banned in client-facing copy, no exceptions.
- **The vague-marketing list:** solutions, services (as generic noun), bespoke, tailored, custom, world-class, cutting-edge, innovative, leverage, unlock, empower, transform, synergy, holistic, robust, seamless.
- **The CTA placeholder list:** get started, learn more, find out more, click here, submit.
- **The agency self-aggrandising list:** "we're passionate about," "we pride ourselves on," "industry-leading," "award-winning."

If a banned word appears in client-facing copy, the page hasn't passed pre-publish review.

---

## Structural elements

### FAQs

Every primary page (homepage, services, ICPs, destinations, pricing, audit pages) ends with a FAQ section.

- 6–12 questions per page
- Each question is something a real prospect actually asks
- Each answer is 40–100 words, front-loaded
- FAQPage schema is mandatory
- Questions should match the language prospects use, not internal language

### Lists

Use bulleted lists for:

- Deliverables ("what's included")
- Specific examples (4+ items)
- Steps in a process (numbered, not bulleted)

Don't use lists for:

- Anything that should flow as prose
- 1–2 items (rewrite as a sentence)

### Tables

Use tables for:

- Comparison ("this vs. that")
- Pricing tiers
- Per-platform data (commission rates, citation counts)

Plain HTML tables. AI engines extract them cleanly.

### Quotes

Pull-quotes from clients are powerful but only if:

- Full attribution (name, business, link to their site)
- Quantified outcome where possible
- No anonymised "happy client" quotes

---

## Pricing language

Always:

- Real numbers in plain text ("£495" not "from £495" not "starting at £495")
- Both currencies displayed where relevant ("£495 / €570")
- What's recurring vs. one-off explicitly stated
- Payment timing explicit ("paid before kick-off" / "monthly in advance")

Never:

- "Contact us for pricing"
- "Custom quote"
- "Investment levels start at..."
- "Get in touch to discuss pricing"

Posted pricing is part of the brand stance. Hiding prices behind discovery calls is what generic agencies do.

---

## Authorship and attribution

Every journal article, research report, and case study has a named author with a byline.

- No "Booked Wild Team" or "Editorial Team" attributions
- Named author's profile linked from byline
- Person schema on every author page
- Author bios appear on every article they wrote

---

## Freshness

- Last-updated timestamp visible on every content page
- Content reviewed quarterly
- Pillar articles refreshed quarterly with new statistics
- Research reports update on a fixed quarterly schedule
- Case studies updated when client situations change

---

## When to break a rule

The rules above are defaults that fit 95% of cases. The 5% exception:

- Direct quotes from clients can use "help" if that's the natural word they used
- Citation blocks may exceed 80 words for genuinely complex products
- A satellite article may be shorter than 2,000 words if the topic genuinely doesn't need more
- Sensory language may appear in Commercial Guide territory if it lifts a specific moment (a hero line, a closing paragraph) — sparingly

Document why a rule was broken in the page's frontmatter under `editorial_notes`. If three pages break the same rule, the rule is wrong — update this file or the Brand_Voice_Guide rather than continuing to break it.
