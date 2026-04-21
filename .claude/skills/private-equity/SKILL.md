---
name: private-equity
description: "Private equity tools: deal sourcing, due diligence, IC memos, returns analysis, unit economics, portfolio monitoring, and value creation planning."
allowed-tools: Bash Read
argument-hint: <company name or deal>
---

# Private Equity Plugin

Private equity workflow tools from [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins). Covers the full PE deal lifecycle.

## Available Skills

Each skill is in `skills/<name>/SKILL.md`:

| Skill | Description |
|-------|-------------|
| `deal-sourcing` | Source and discover potential deals |
| `deal-screening` | Screen and evaluate deal opportunities |
| `dd-checklist` | Due diligence checklists |
| `dd-meeting-prep` | Prepare for due diligence meetings |
| `unit-economics` | Analyze unit economics |
| `returns-analysis` | Calculate IRR, MOIC, and returns |
| `ic-memo` | Draft investment committee memos |
| `portfolio-monitoring` | Monitor portfolio company KPIs |
| `value-creation-plan` | Build value creation plans |
| `ai-readiness` | Assess AI readiness of target companies |

## Available Commands

Commands are in `commands/<name>.md`:

- `/source [criteria]` — Deal sourcing
- `/screen-deal [company]` — Screen a deal
- `/dd-checklist [company]` — Due diligence checklist
- `/dd-prep [company]` — DD meeting preparation
- `/unit-economics [company]` — Unit economics analysis
- `/returns [investment-id]` — Returns analysis
- `/ic-memo [company]` — Investment committee memo
- `/portfolio [company]` — Portfolio monitoring
- `/value-creation [company]` — Value creation plan
- `/ai-readiness [company]` — AI readiness assessment

## How to Use

1. Read the relevant skill file: `skills/<skill-name>/SKILL.md`
2. Read the relevant command file: `commands/<command>.md`
3. Follow the workflow instructions in those files
