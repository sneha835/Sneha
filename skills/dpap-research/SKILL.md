# DPAP Research Skill — BabyOrgano Product Validation

## Trigger Phrases
- "research [product]"
- "run DPAP for [product]"
- "validate [product]"
- "check market for [product]"
- "should we launch [product]"
- "analyze [product]"
- "market research [product]"

## What It Does
Runs the full Data-driven Product Acceptance Protocol (DPAP) pipeline for any BabyOrgano product concept. This is a 6-step automated research process covering:

1. **Google Trends** — Search interest, seasonal patterns, regional demand across India
2. **Amazon India** — Competitor listings, ratings, Ayurvedic white space analysis
3. **E-commerce Presence** — Flipkart, Nykaa, FirstCry, Apollo, 1mg, PharmEasy, quick commerce
4. **Kids & Ayurvedic Assessment** — Category mapping, ingredient recommendations, positioning
5. **Customer Survey** — 7-question survey with BabyOrgano-specific benchmarks
6. **Social Media** — YouTube, Reddit, Google News sentiment and trend analysis

## How to Run

```bash
source .venv/bin/activate

# Full DPAP (all 6 steps)
python scripts/dpap_research.py --product "PRODUCT NAME" --output report

# Specific steps only
python scripts/dpap_research.py --product "PRODUCT NAME" --steps trends,amazon,kids --output report

# JSON output for piping
python scripts/dpap_research.py --product "PRODUCT NAME" --output json
```

## Brand Context
- **Brand:** BabyOrgano
- **Category:** Ayurvedic Kids Health & Wellness, India
- **Price Range:** Rs 300–900
- **Formats:** Drops, Gummies, Syrup, Chewable tablets, Powder
- **Sign-off Team:** Dr. Urvi (R&D), Sneha (Marketing), Ripul Sharma & Riddhi Sharma (Founders), Ghazal (CS)

## After Every Run
- Present the PROCEED / CONDITIONAL / REJECT recommendation first
- Then show step-by-step findings
- Then show the checklist and pending actions
- **Always ask:** "Want me to send the YouTube URLs to NotebookLM for deeper analysis and an infographic?"
