# Research Environment — Operating Instructions

This repository is a standalone research environment. Its purpose is to research companies, markets, and marketing/business practices, and to build a durable, well-organized knowledge base rather than one-off answers. These instructions are permanent — follow them for every research task in this repo.

## Folder Structure

```
research/
  india/                  Market, company, and industry research specific to India
  global/                 Market, company, and industry research outside India (or cross-market/global-scale)
  profitability/          Research on what makes companies/business models profitable — margins, unit economics, monetization
  failed-and-struggling/  Post-mortems and case studies on companies that failed, declined, or are struggling — what went wrong
  campaigns/              Deep dives on specific marketing/ad campaigns (any company, any market)

companies/                Per-company profiles and dossiers (one subfolder per company)
sources/                  Raw source material — links, transcripts, PDFs, scraped pages, citations — backing any research file
financials/               Financial data, statements, models, and analysis pulled during research
marketing/                Marketing strategy, positioning, and campaign analysis not tied to a single company folder
branding/                 Brand identity, voice, visual identity, and brand strategy research
channels/                 Channel-specific research (paid, organic, social, retail, D2C, marketplace, etc.)
strategy/                 Synthesized strategic insights, frameworks, and recommendations drawn from research
outputs/                  Finished deliverables meant to be shared or presented (reports, decks, briefs, artifacts)
```

## Core Principles

1. **Sources over assertions.** Every non-trivial claim in a research file should be traceable to something in `sources/`. Save raw material (links, snapshots, transcripts) to `sources/` as you go — don't rely on memory of a fetch that happened mid-conversation.
2. **Company research lives in one place.** If research is about a specific company, it belongs under `companies/<company-name>/`, even if it also touches profitability, campaigns, or a specific market. Use `research/india/`, `research/global/`, `research/profitability/`, `research/failed-and-struggling/`, and `research/campaigns/` for cross-company or thematic research, and link back to the relevant `companies/<company-name>/` folder rather than duplicating content.
3. **Raw vs. synthesized.** Raw notes, data pulls, and source material go in `sources/` or the relevant topical folder (`financials/`, `marketing/`, `branding/`, `channels/`). Distilled conclusions, comparisons, and recommendations go in `strategy/`. Keep these distinct — don't mix raw dumps and analysis in the same file.
4. **Outputs are deliverables, not drafts.** Only place a file in `outputs/` when it's a finished, presentable artifact (report, deck, brief, infographic, etc.). Working drafts stay in the topical folder until they're ready to graduate.
5. **File naming.** Use lowercase, hyphenated, descriptive filenames with dates where relevant, e.g. `companies/acme-co/financials-2026-08.md`, `research/failed-and-struggling/quibi-postmortem.md`. Avoid vague names like `notes.md` or `research.md`.
6. **Scope before research.** Before starting a new research task, confirm the topic, geography (India/global), and depth expected. Don't assume — ask if the request is ambiguous.
7. **No research without a request.** Don't proactively start researching a topic; wait for explicit direction on what to investigate.

## Available Skills

This environment has skills installed under `.claude/skills/` that are useful for research work, including:

- `/yt-research` — search YouTube for videos on a topic
- `/notebooklm` — send sources to NotebookLM for analysis and artifact generation (infographics, decks, flashcards, reports)
- `customer-research`, `competitor-alternatives`, `content-strategy`, `seo-audit`, and other marketing skills — useful for company/market/competitive research
- `product-marketing-context` — useful when research needs to be framed against a specific product/audience

Use these where they fit naturally into a research task rather than doing manual equivalents from scratch.

## Workflow for a Research Request

1. Confirm scope: topic, company/companies, geography, and what folder(s) the output belongs in.
2. Gather sources; save raw material to `sources/` (and `companies/<name>/` if company-specific).
3. Do the analysis; place it in the appropriate topical folder (`financials/`, `marketing/`, `branding/`, `channels/`, or the relevant `research/` subfolder).
4. If the task calls for a synthesized recommendation or takeaway, write it to `strategy/`.
5. If a polished deliverable is requested, produce it in `outputs/`.
6. Always cite back to `sources/` so findings can be verified later.
