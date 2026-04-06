---
name: equity-research
description: "Equity research tools: earnings analysis, initiating coverage reports, thesis tracking, morning notes, sector overviews, and idea screening."
allowed-tools: Bash Read
argument-hint: <company name, ticker, or sector>
---

# Equity Research Plugin

Equity research workflow tools from [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins). Covers the full equity research lifecycle.

## Available Skills

Each skill is in `skills/<name>/SKILL.md`:

| Skill | Description |
|-------|-------------|
| `earnings-analysis` | Post-earnings update reports |
| `earnings-preview` | Pre-earnings preview reports |
| `initiating-coverage` | Full initiating coverage reports |
| `thesis-tracker` | Track and maintain investment theses |
| `catalyst-calendar` | Track upcoming catalysts and events |
| `morning-note` | Draft morning research notes |
| `sector-overview` | Sector and industry overview reports |
| `idea-generation` | Stock screening and idea generation |
| `model-update` | Update financial models post-earnings |

## Available Commands

Commands are in `commands/<name>.md`:

- `/earnings [company] [quarter]` — Earnings update report
- `/earnings-preview [company]` — Pre-earnings preview
- `/initiate [company]` — Initiating coverage report
- `/thesis [company]` — Investment thesis
- `/catalysts [company]` — Catalyst tracking
- `/morning-note [criteria]` — Morning note
- `/sector [sector]` — Sector overview
- `/screen [criteria]` — Idea screening
- `/model-update [company]` — Update financial model

## How to Use

1. Read the relevant skill file: `skills/<skill-name>/SKILL.md`
2. Read the relevant command file: `commands/<command>.md`
3. Follow the workflow instructions in those files
