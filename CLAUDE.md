# BabyOrgano Research Intelligence System

Automated research pipeline for **BabyOrgano** — Ayurvedic Kids Health & Wellness brand, India. Combines YouTube research, social media analysis, e-commerce intelligence, Google Trends, and customer survey generation with NotebookLM for deliverable creation.

## Brand Context

- **Brand:** BabyOrgano
- **Category:** Ayurvedic Kids Health & Wellness, India
- **Competitors:** MamaEarth Kids, Himalaya Baby, Dabur Honitus, Baidyanath Kids, The Moms Co, SattvikBaby, Carbamide Forte Kids, Wellbeing Nutrition Kids, Pediasure, Zandu Baby
- **Price Range:** Rs 300–900
- **Product Formats:** Drops, Gummies, Syrup, Chewable tablets, Powder
- **Sign-off Team:** Dr. Urvi (R&D), Sneha (Marketing), Ripul Sharma & Riddhi Sharma (Founders), Ghazal (CS)

## Ayurvedic Ingredient Map

| Category | Key Ingredients |
|----------|----------------|
| Immunity | Tulsi, Giloy, Amla, Ashwagandha, Neem, Turmeric |
| Growth | Ashwagandha, Shatavari, Bala, Amalaki, Brahmi |
| Digestion | Triphala, Ajwain, Fennel, Ginger, Haritaki |
| Brain | Brahmi, Shankhpushpi, Ashwagandha, Vacha |
| Sleep | Ashwagandha, Brahmi, Jatamansi, Tagara |
| Nutrition | Amla, Shatavari, Moringa, Ashwagandha, Amalaki |

## Setup

```bash
bash setup.sh
```

Then authenticate with NotebookLM in a separate terminal:

```bash
source .venv/bin/activate && notebooklm login
```

## Important

- Always activate the virtual environment before running scripts: `source .venv/bin/activate`
- Scripts are in `scripts/` (DPAP pipeline) and `.claude/skills/*/scripts/` (NotebookLM)
- All scripts output JSON to stdout for easy chaining

## Default Behaviour

- **When any product is mentioned**, always run the full DPAP pipeline: `python scripts/dpap_research.py --product "PRODUCT" --output report`
- **Output order:** Recommendation (PROCEED/CONDITIONAL/REJECT) first, then Steps 1–6 findings, then checklist, then pending actions
- **After every DPAP run**, ask: "Want me to send the YouTube URLs to NotebookLM for deeper analysis and an infographic?"

## Available Skills

### DPAP Research — `research [product]`
Full 6-step product validation pipeline. Triggers on: "research [product]", "run DPAP for [product]", "validate [product]", "check market for [product]", "should we launch [product]"

```bash
python scripts/dpap_research.py --product "PRODUCT" --output report
python scripts/dpap_research.py --product "PRODUCT" --steps trends,amazon,kids --output report
```

### `/yt-research <topic>`
Search YouTube for videos on a topic. Returns structured metadata (title, URL, author, views, duration).
- If no topic is provided, **ask the user what topic they want to research**.

```bash
python scripts/yt_research.py --query "TOPIC" --count 25 --output summary
```

### Social Media Research
Multi-platform research across YouTube, Reddit, Google News, Instagram, Quora.

```bash
python scripts/dpap_social_research.py --product "PRODUCT" --platforms youtube,reddit,google --output report
```

### `/notebooklm <action>`
Interact with NotebookLM: create notebooks, add sources, analyze content, generate artifacts.

## End-to-End Research Workflow

When a user asks to research a topic and send results to NotebookLM:

1. **Run DPAP** using `python scripts/dpap_research.py` — get full market analysis
2. **Search YouTube** using `/yt-research` — get the video list as JSON
3. **Extract URLs** from the results
4. **Create a notebook** via `create_notebook.py --title "[Topic] Research"`
5. **Add all video URLs** via `add_sources.py --notebook-id <ID> --urls <URLs>`
6. **Request analysis** via `ask_question.py --notebook-id <ID> --question "Provide a comprehensive analysis of the key themes, insights, and trends across all sources"`
7. **Generate artifact** via `generate_artifact.py --notebook-id <ID> --type <type> --style "<style>"`
8. **Present results** to the user

## Example Commands

> "Research kids immunity gummies" → Runs full DPAP pipeline

> "Should we launch ashwagandha drops for babies?" → Runs full DPAP pipeline

> "Use the yt-research skill to find the 25 latest trending videos on AI agents. Once we have those videos, send them over to NotebookLM using the notebooklm skill. Give me its analysis on the top findings, then have NotebookLM create an infographic in a handwritten / chalkboard style depicting that analysis."

## Marketing Skills

35 marketing skills from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) are installed in `.claude/skills/`. Categories:

- **CRO**: page-cro, signup-flow-cro, onboarding-cro, form-cro, popup-cro, paywall-upgrade-cro
- **Content & Copy**: copywriting, copy-editing, cold-email, email-sequence, social-content, lead-magnets
- **SEO & Discovery**: seo-audit, ai-seo, programmatic-seo, site-architecture, competitor-alternatives, schema-markup, content-strategy
- **Paid & Measurement**: paid-ads, ad-creative, ab-test-setup, analytics-tracking
- **Growth & Retention**: referral-program, free-tool-strategy, churn-prevention, community-marketing
- **Sales & GTM**: revops, sales-enablement, launch-strategy, pricing-strategy
- **Strategy**: marketing-ideas, marketing-psychology, customer-research, product-marketing-context

### Foundation: Product Marketing Context
Run `/product-marketing-context` first to set up your product/audience context — all other marketing skills reference this for consistency.

### Marketing Tools
CLI tools and integration guides are in `.claude/tools/`. See `.claude/tools/REGISTRY.md` for the full index.
