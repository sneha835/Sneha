---
name: dpap-research
description: Run the full DPAP (Data-driven Product Acceptance Protocol) pipeline for any BabyOrgano product. Covers Google Trends, Amazon, e-commerce, kids wellness assessment, customer survey, and social media research. Use when the user says "research [product]", "validate [product]", "run DPAP", "should we launch [product]", "check market for [product]", or "analyze [product]".
allowed-tools: Bash Read
argument-hint: <product name to research>
---

## DPAP Research Skill — BabyOrgano Product Validation

Run the full 6-step Data-driven Product Acceptance Protocol for any BabyOrgano product concept.

### CRITICAL: If no product is provided in `$ARGUMENTS`, you MUST ask the user what product they want to research before proceeding. Do NOT guess or assume a product.

### What It Does

1. **Google Trends** — Search interest, seasonal patterns, regional demand across India
2. **Amazon India** — Competitor listings, ratings, Ayurvedic white space analysis
3. **E-commerce Presence** — Flipkart, Nykaa, FirstCry, Apollo, 1mg, PharmEasy, quick commerce
4. **Kids & Ayurvedic Assessment** — Category mapping, ingredient recommendations, positioning
5. **Customer Survey** — 7-question survey with BabyOrgano-specific benchmarks
6. **Social Media** — YouTube, Reddit, Google News sentiment and trend analysis

### Usage

Activate the virtual environment and run the pipeline:

```bash
cd /home/user/Sneha && source .venv/bin/activate && python scripts/dpap_research.py --product "$ARGUMENTS" --output report
```

### Parameters

- `--product` (REQUIRED): Product name to research
- `--steps`: Which steps to run — `all` (default) or comma-separated: `trends,amazon,ecommerce,kids,survey,social`
- `--output`: Output format — `report` (human-readable) or `json` (machine-readable)
- `--yt-count`: Number of YouTube results (default: 10)

### Examples

```bash
# Full DPAP pipeline
python scripts/dpap_research.py --product "kids immunity gummies" --output report

# Specific steps only
python scripts/dpap_research.py --product "ashwagandha drops" --steps trends,amazon,kids --output report

# JSON output for piping to other tools
python scripts/dpap_research.py --product "baby hair oil" --output json
```

### Brand Context

- **Brand:** BabyOrgano
- **Category:** Ayurvedic Kids Health & Wellness, India
- **Price Range:** Rs 300-900
- **Competitors:** MamaEarth Kids, Himalaya Baby, Dabur Honitus, Baidyanath Kids, The Moms Co, SattvikBaby, Carbamide Forte Kids, Wellbeing Nutrition Kids, Pediasure, Zandu Baby

### How to Present Results

1. **Recommendation first** — Show PROCEED / CONDITIONAL / REJECT at the top
2. **Step-by-step findings** — Show each step's results
3. **Checklist** — Show pass/fail for each step
4. **Pending actions** — What needs to be addressed before launch
5. **Always ask:** "Want me to send the YouTube URLs to NotebookLM for deeper analysis and an infographic?"
