# Booked Wild Social Media Workflow Rules

## Core rule

This workflow is manual-first.

Colin specifically asked us to start manually so we understand the process, learn what good content looks like, and keep the human trust element strong.

AI can support research, structure, hooks, drafting options, and QA, but the final judgement, tone, and approval must stay human-led.

Do not over-automate this workflow yet.

## Content priorities

- Use UK English.
- Focus on UK/EU travel and hospitality businesses.
- Prioritise ICP pain points.
- Create useful, trustworthy, data-backed content.
- Every draft must be relevant to a real audience problem.
- Avoid generic agency language.
- Avoid over-polished AI tone.
- Do not make unsupported claims.
- Do not publish anything without Nigel/Colin review.

## Every content draft must identify

- Target ICP
- Pain point
- Hook
- Key claim or insight
- Supporting source
- Suggested channel
- CTA or next step
- Asset direction
- Review status

## Source hierarchy

Use this source priority order:

1. Colin meeting transcript and direct Colin instructions
2. Booked Wild source-of-truth MD files
3. Direct creator links, videos, posts and manually reviewed examples
4. Credible external research sources
5. Gemini, Manus, Claude and ChatGPT outputs as research inputs only

Do not treat LLM-generated claims as facts unless verified against a direct source.

## Evidence rule

Anything used in a draft must trace back to a source.

Use the evidence-library folder to store:

- direct source links
- manual video/post observations
- transcript notes
- verified claims
- unverified claims
- social examples
- Booked Wild source notes

Separate verified claims from unverified claims.

## Matt Diamante / HeyTony analysis — status as of 2026-05-22

**Automated analysis complete.** Top 50 Shorts by view count (from a full catalog of 1,076) have been analyzed from captions and titles. Three deliverables are saved in `02-reference-creators/`:

| File | What it is |
| ---- | ---------- |
| `TRANSCRIPT-SUMMARY.md` | Deduped content from all 50 Shorts, grouped by 7 themes, most repeated tools and phrases |
| `PLAYBOOK.md` | Full replication guide for Colin — 5 hook archetypes with Booked Wild equivalents, script template, what not to copy |
| `TOP-20-IDEAS.md` | 20 filmable Short ideas for Booked Wild ICP with title, hook, script bullets, visual direction, and CTA for each |

**Remaining gap — manual visual review required (approx. 5 minutes):**

The automated analysis cannot capture Matt's visual hooks, absurd opening scenes, bridge phrases, or editing rhythm. Colin must watch these 5 URLs before filming anything:

| Views | Title | URL |
| ----- | ----- | --- |
| 519k | Why is no one talking about this? | [gvYHDjUScUE](https://www.youtube.com/shorts/gvYHDjUScUE) |
| 255k | And he's fully booked | [2JrcV2E7L1Y](https://www.youtube.com/shorts/2JrcV2E7L1Y) |
| 119k | He knows NOTHING about SEO | [TzjELQQVIPQ](https://www.youtube.com/shorts/TzjELQQVIPQ) |
| 121k | The best ChatGPT prompt ever? | [b1fzXxZql-k](https://www.youtube.com/shorts/b1fzXxZql-k) |
| 74k | Do you remember this ad? | [Z2M2wTvSACc](https://www.youtube.com/shorts/Z2M2wTvSACc) |

After watching, fill in the visual layer section of `02-reference-creators/matt-diamante-youtube-shorts-analysis.md`.

**Original research focus (for reference):**

Colin likes the natural, human, short-form educational style. The analysis confirms the formula: first 3-second hook built on proof/contradiction/forbidden knowledge → one actionable tip → proof screenshot → single CTA. All details are in `PLAYBOOK.md`.

## AI agents / sub-agent rule

AI agents and Claude Code sub-agents are allowed for research-stage and preparation work.

Allowed uses:

- source research
- evidence organisation
- claim verification
- creator and style analysis
- ICP and pain-point mapping
- hook generation
- draft options
- QA checks

Not allowed yet:

- publishing
- scheduling
- social account posting
- scraping systems
- API automation
- unsupervised content creation
- final approval

Manual-first means human judgement remains in control.

Nigel and Colin must review content before anything is published.

All agent outputs are draft or research material until reviewed by Nigel and, where needed, Colin.

### Recommended agent setup

Start with three simple agents only.

#### 1. Research Agent

Purpose: gather sources, update research-log.md, update creator-sources.md, flag missing evidence.
Output: source notes only — no final copy.

#### 2. Claim QA Agent

Purpose: check every stat and claim, separate verified from unverified, suggest safe wording.
Output: updates to claim-bank.md, verified-claims.md, unverified-claims.md.

#### 3. Content QA Agent

Purpose: review draft scripts and posts against ICP, pain point, hook, source, Booked Wild tone, Colin filmability, and the human trust rule.
Output: score, risks, suggested edits — no approval authority.

## ChatGPT agent/mode usage

ChatGPT may be used in three approved modes:

1. Research QA Agent
2. Claim Verifier Agent
3. Content QA Agent

These modes support research, claim checking, draft review, and quality control.

They must not:

- publish content
- schedule content
- connect social accounts
- scrape social media
- approve final posts
- replace Nigel or Colin judgement

All outputs from these modes are draft or research material until reviewed by Nigel and, where needed, Colin.

## First priority

Create one short video script for Colin and one supporting social post/caption for review by Wednesday or Thursday at the latest.

## Do not do yet

- Do not create automation.
- Do not create API integrations.
- Do not create agents that publish, schedule, post, or operate without human review.
- Do not create publishing scripts.
- Do not connect to GitHub until asked.
- Do not publish anything.
- Do not treat AI research outputs as verified sources.
- Do not use unsupported statistics.
- Do not build a 30-post backlog until the first manual review cycle is complete.

## Formula Lab — 08-formula-lab/

A separate sandbox folder for cloning the HeyTony short-form system for Booked Wild. Working on this in parallel with Cursor. Not part of the main content workflow yet — nothing from here gets published without full Nigel/Colin review.

Purpose: clone Matt Diamante's *formula* (structure, hooks, CTAs, visual style) — not his words, his brand, or his face. Colin is the on-camera avatar. No AI presenter.

See `08-formula-lab/README.md` for the full brief, clone rules, and next-session plan.

---

## Current stage definition of done

This stage is complete when:

- the local folder structure is created
- the evidence-library exists
- Matt Diamante / HeyTony source links are saved
- at least 10 YouTube Shorts are manually reviewed
- the first swipe-file table is filled in
- one video script and one supporting post are drafted for Nigel/Colin review

Do not move into publishing, automation, or backlog creation before this is complete.
