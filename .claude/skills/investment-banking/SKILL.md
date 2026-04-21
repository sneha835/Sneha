---
name: investment-banking
description: "Investment banking productivity tools: CIM drafting, teasers, merger modeling, pitch decks, buyer lists, deal tracking. Use for M&A and IB workflows."
allowed-tools: Bash Read
argument-hint: <company name or deal>
---

# Investment Banking Plugin

Investment banking workflow tools from [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins). Covers sell-side and buy-side IB workflows.

## Available Skills

Each skill is in `skills/<name>/SKILL.md`:

| Skill | Description |
|-------|-------------|
| `cim-builder` | Draft Confidential Information Memorandums |
| `teaser` | Create deal teasers / blind profiles |
| `merger-model` | M&A merger and accretion/dilution modeling |
| `pitch-deck` | Build investment banking pitch decks |
| `strip-profile` | Create company strip profiles |
| `buyer-list` | Compile strategic and financial buyer lists |
| `deal-tracker` | Track deal milestones and timelines |
| `process-letter` | Draft process letters for M&A transactions |
| `datapack-builder` | Build data packs for due diligence |

## Available Commands

Commands are in `commands/<name>.md`:

- `/cim [company]` — Draft a CIM
- `/teaser [company]` — Create a deal teaser
- `/merger-model [target] [acquirer]` — M&A valuation model
- `/buyer-list [criteria]` — Generate buyer list
- `/deal-tracker [deal-id]` — Track a live deal
- `/one-pager [company]` — Create a one-pager
- `/process-letter [deal]` — Draft a process letter

## How to Use

1. Read the relevant skill file: `skills/<skill-name>/SKILL.md`
2. Read the relevant command file: `commands/<command>.md`
3. Follow the workflow instructions in those files
