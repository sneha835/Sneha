# Research Pipeline: YouTube → NotebookLM

Automated research pipeline that searches YouTube for videos on any topic and sends them to Google NotebookLM for analysis and deliverable generation.

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
- All Python scripts are in `.claude/skills/*/scripts/`
- All scripts output JSON to stdout for easy chaining

## Available Skills

### `/yt-research <topic>`
Search YouTube for videos on a topic. Returns structured metadata (title, URL, author, views, duration).
- If no topic is provided, **ask the user what topic they want to research**.

### `/notebooklm <action>`
Interact with NotebookLM: create notebooks, add sources, analyze content, generate artifacts.

## End-to-End Research Workflow

When a user asks to research a topic and send results to NotebookLM:

1. **Search YouTube** using `/yt-research` — get the video list as JSON
2. **Extract URLs** from the results
3. **Create a notebook** via `create_notebook.py --title "[Topic] Research"`
4. **Add all video URLs** via `add_sources.py --notebook-id <ID> --urls <URLs>`
5. **Request analysis** via `ask_question.py --notebook-id <ID> --question "Provide a comprehensive analysis of the key themes, insights, and trends across all sources"`
6. **Generate artifact** via `generate_artifact.py --notebook-id <ID> --type <type> --style "<style>"`
7. **Present results** to the user

## Example Command

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
