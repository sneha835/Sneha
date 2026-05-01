---
name: keyword-research
description: Get Google Trends search volume and interest data for top keywords related to a product or topic in India. Use when the user asks for "top keywords", "search volume", "keyword research", "trending keywords", or "Google Trends data".
allowed-tools: Bash Read
argument-hint: <product or topic to find keywords for>
---

## Keyword Research Skill — Google Trends India

Find top keywords and their search volume / interest data for any product or topic using Google Trends (India).

### CRITICAL: If no topic is provided in `$ARGUMENTS`, you MUST ask the user what product or topic they want keyword data for. Do NOT guess.

### Usage

Activate the virtual environment and run the keyword research script:

```bash
cd /home/user/Sneha && source .venv/bin/activate && python scripts/keyword_research.py --topic "$ARGUMENTS" --count 10
```

### Parameters

- `--topic` (REQUIRED): The product or topic to find keywords for
- `--count`: Number of top keywords to return (default: 10)
- `--timeframe`: Time range — `today 12-m` (default), `today 3-m`, `today 5-y`
- `--output`: Output format — `report` (default) or `json`

### Examples

```bash
# Top 10 keywords for baby hair oil
python scripts/keyword_research.py --topic "baby hair oil" --count 10

# Top 15 keywords, last 3 months
python scripts/keyword_research.py --topic "kids immunity" --count 15 --timeframe "today 3-m"

# JSON output
python scripts/keyword_research.py --topic "ayurvedic drops for kids" --count 10 --output json
```

### Output Fields

For each keyword the script returns:
- **Keyword** — The search term
- **Avg Interest** — Average Google Trends interest score (0-100)
- **Direction** — Trend direction: increasing, stable, or declining
- **Peak Interest** — Maximum interest score in the timeframe
- **Top Regions** — Top 5 Indian states by search interest

### How to Present Results

Present as a formatted table sorted by average interest (highest first):

| # | Keyword | Avg Interest | Direction | Peak | Top Region |
|---|---------|-------------|-----------|------|------------|

After showing results, offer: "Want me to run a full DPAP analysis for any of these keywords?"
