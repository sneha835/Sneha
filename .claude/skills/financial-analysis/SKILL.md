---
name: financial-analysis
description: "Core financial modeling and analysis tools: DCF, comps, LBO, 3-statement models, competitive analysis, and deck QC. Use when users need financial valuations, modeling, or analysis."
allowed-tools: Bash Read
argument-hint: <company name or ticker>
---

# Financial Analysis (Core Plugin)

Core financial modeling and analysis toolkit from [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins). Provides institutional-quality financial models and analysis tools.

## Available Skills

Each skill is in `skills/<name>/SKILL.md` — load the relevant one based on user request:

| Skill | Description |
|-------|-------------|
| `comps-analysis` | Comparable company analysis with trading multiples |
| `dcf-model` | Discounted cash flow valuation models |
| `lbo-model` | Leveraged buyout modeling |
| `3-statement-model` | Integrated 3-statement financial models |
| `competitive-analysis` | Industry competitive landscape analysis |
| `ib-check-deck` | Presentation quality control and review |
| `deck-refresh` | Update and refresh existing presentations |
| `ppt-template-creator` | Create PowerPoint templates for firm use |
| `audit-xls` | Audit Excel models for errors |
| `clean-data-xls` | Clean and normalize spreadsheet data |
| `skill-creator` | Create new custom skills |

## Available Commands

Commands are in `commands/<name>.md`:

- `/comps [company]` — Comparable company analysis
- `/dcf [company]` — DCF valuation model
- `/lbo [company]` — Leveraged buyout model
- `/3-statement-model [company]` — Build 3-statement financials
- `/competitive-analysis [company/industry]` — Competitive landscape
- `/check-deck [file]` — QC a presentation
- `/ppt-template [file]` — Register a PowerPoint template
- `/debug-model [file]` — Debug an Excel model

## How to Use

1. Read the relevant skill file: `skills/<skill-name>/SKILL.md`
2. Read the relevant command file: `commands/<command>.md`
3. Follow the workflow instructions in those files
4. Use MCP data servers (configured in `.mcp.json`) for live financial data

## MCP Data Servers

This plugin connects to 11 financial data providers (see `.mcp.json`):
Daloopa, Morningstar, S&P Global, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, Egnyte
