---
name: social-research
description: Run multi-platform social media research across YouTube, Reddit, Google News, Instagram, and Quora for any product or topic. Use when the user asks for "social media research", "what's the buzz on", "community sentiment", "Reddit/YouTube/Instagram analysis", or "social listening".
allowed-tools: Bash Read
argument-hint: <product or topic to research>
---

## Social Media Research Skill

Multi-platform social research across YouTube, Reddit, Google News, Instagram, and Quora. Designed for BabyOrgano product research across Indian platforms.

### CRITICAL: If no topic is provided in `$ARGUMENTS`, you MUST ask the user what product or topic they want to research. Do NOT guess.

### Usage

Activate the virtual environment and run the social research script:

```bash
cd /home/user/Sneha && source .venv/bin/activate && python scripts/dpap_social_research.py --product "$ARGUMENTS" --platforms youtube,reddit,google,instagram,quora --output report
```

### Parameters

- `--product` (REQUIRED): Product or topic to research
- `--platforms`: Comma-separated platforms to search (default: all)
  - `youtube` — Searches 5 query variations via yt-dlp, deduplicates, flags complaints
  - `reddit` — Public JSON API, searches r/india, r/IndianParents, r/Ayurveda, r/supplements
  - `google` — Google News RSS feed, flags regulatory/safety articles
  - `instagram` — Generates hashtag URLs for manual browser review
  - `quora` — Generates search URLs for manual browser review
- `--yt-count`: YouTube results per query (default: 15)
- `--output`: `report` (human-readable) or `json` (machine-readable)

### Examples

```bash
# All platforms
python scripts/dpap_social_research.py --product "baby hair oil" --output report

# YouTube + Reddit only
python scripts/dpap_social_research.py --product "kids immunity" --platforms youtube,reddit --output report

# JSON output for piping
python scripts/dpap_social_research.py --product "ashwagandha for kids" --output json
```

### How to Present Results

1. **YouTube** — Show top 10 videos with title, channel, views, URL. Flag complaint videos separately.
2. **Reddit** — Show sentiment (positive/negative/neutral) and top posts with scores.
3. **Google News** — Show recent articles. Highlight any flagged articles (recalls, bans, safety warnings).
4. **Instagram** — Show hashtag URLs for manual review in browser.
5. **Quora** — Show search URLs for manual review in browser.

After results, offer: "Want me to send the YouTube URLs to NotebookLM for deeper analysis?"
