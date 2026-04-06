---
name: wealth-management
description: "Wealth management tools: financial planning, portfolio rebalancing, client reporting, tax-loss harvesting, client reviews, and investment proposals."
allowed-tools: Bash Read
argument-hint: <client name or portfolio>
---

# Wealth Management Plugin

Wealth management and financial advisory tools from [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins). Covers client advisory workflows.

## Available Skills

Each skill is in `skills/<name>/SKILL.md`:

| Skill | Description |
|-------|-------------|
| `financial-plan` | Comprehensive financial planning |
| `portfolio-rebalance` | Portfolio rebalancing analysis |
| `client-report` | Generate client reports |
| `client-review` | Client meeting preparation and review |
| `tax-loss-harvesting` | Identify tax-loss harvesting opportunities |
| `investment-proposal` | Draft investment proposals |

## Available Commands

Commands are in `commands/<name>.md`:

- `/financial-plan [client]` — Build a financial plan
- `/rebalance [portfolio]` — Portfolio rebalancing
- `/client-report [client]` — Generate client report
- `/client-review [client]` — Client meeting prep
- `/tlh [portfolio]` — Tax-loss harvesting
- `/proposal [client]` — Investment proposal

## How to Use

1. Read the relevant skill file: `skills/<skill-name>/SKILL.md`
2. Read the relevant command file: `commands/<command>.md`
3. Follow the workflow instructions in those files
