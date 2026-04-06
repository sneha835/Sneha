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

## Financial Services Skills

Installed from [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins). Each plugin contains skills (auto-triggered domain knowledge) and commands (explicit user actions).

### `/financial-analysis <company>`
Core financial modeling: DCF, comps, LBO, 3-statement models, competitive analysis, deck QC.
- Commands: `/comps`, `/dcf`, `/lbo`, `/3-statement-model`, `/competitive-analysis`, `/check-deck`
- MCP data servers configured in `.mcp.json` (Daloopa, Morningstar, S&P Global, FactSet, Moody's, LSEG, PitchBook, etc.)

### `/investment-banking <company>`
IB workflows: CIM drafting, teasers, merger modeling, pitch decks, buyer lists, deal tracking.
- Commands: `/cim`, `/teaser`, `/merger-model`, `/buyer-list`, `/deal-tracker`, `/one-pager`

### `/equity-research <company>`
Research workflows: earnings analysis, initiating coverage, thesis tracking, morning notes, screening.
- Commands: `/earnings`, `/initiate`, `/thesis`, `/catalysts`, `/morning-note`, `/screen`, `/sector`

### `/private-equity <company>`
PE workflows: deal sourcing, due diligence, IC memos, returns analysis, portfolio monitoring.
- Commands: `/source`, `/screen-deal`, `/dd-checklist`, `/ic-memo`, `/returns`, `/portfolio`

### `/wealth-management <client>`
Advisory workflows: financial planning, portfolio rebalancing, client reporting, tax-loss harvesting.
- Commands: `/financial-plan`, `/rebalance`, `/client-report`, `/client-review`, `/tlh`

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
