# BabyOrgano D2C Growth & Profitability Intelligence Lab — Operating Manual

This repository is a dedicated research lab whose sole client is BabyOrgano, an Indian children's wellness / modern Ayurveda D2C brand. These are the permanent operating instructions for every research task carried out here. They override default behavior — follow them exactly.

## PROJECT OBJECTIVE

Research Indian and global D2C/consumer brands to identify the specific strategies, decisions, changes, and inflection points that contributed to sustainable growth, improved unit economics, and profitability — then translate that evidence into decisions BabyOrgano can actually act on.

The research must ultimately help answer questions such as:

- What should BabyOrgano change in its brand positioning and messaging?
- How should BabyOrgano reduce excessive dependence on Meta/performance marketing?
- Which alternative acquisition channels can realistically work?
- Should BabyOrgano invest more in SEO, creators, influencers, PR, partnerships, referrals, CRM, offline, retail, marketplaces, or other channels?
- Should a given capability be built internally or outsourced to an agency?
- What type of Brand Manager, Growth Manager, creative team, or agency should BabyOrgano hire?
- Which campaigns and brand-building strategies have worked for comparable companies?
- What product, pricing, bundling, and retention strategies improved economics?
- When did companies expand from D2C into offline/retail/marketplaces, and why?
- What operational or financial changes helped companies move toward profitability?
- What mistakes caused D2C companies to struggle despite strong funding or revenue growth?

Every research artifact produced in this repo should trace back to one or more of these questions.

## RESEARCH PRINCIPLES

1. Do not equate revenue growth with business success.
2. Focus heavily on profitability, contribution economics, cash generation, retention, and sustainable growth.
3. Identify what changed BEFORE and AFTER a company's profitability inflection point.
4. Look for causality and evidence rather than generic descriptions of successful brands.
5. Do not assume a strategy worked simply because a successful company used it.
6. Distinguish correlation from causation.
7. Do not default to Meta/performance marketing as the answer to customer acquisition.
8. Explicitly investigate how companies diversified acquisition away from paid social.
9. Include both successful/profitable companies and companies that struggled, burned cash, were acquired, downsized, or failed where useful.
10. Look for repeatable patterns across companies, while clearly identifying category-specific differences.

## EVIDENCE STANDARDS

For every material factual claim:

- Prefer primary sources whenever possible.
- Prioritize annual reports, financial filings, investor presentations, official company announcements, founder interviews, earnings calls, regulatory filings, campaign case studies, and official company data.
- Use reputable journalism and research reports as secondary sources.
- Do not rely on SEO blogs or generic listicles when stronger sources exist.
- Record the source URL.
- Record the publication/source date when available.

Clearly distinguish, and label, every claim as one of:

- **A. Verified fact**
- **B. Company-reported claim**
- **C. Third-party reporting**
- **D. Analyst estimate**
- **E. Inference/hypothesis**

Never fabricate revenue, profit, EBITDA, CAC, ROAS, LTV, margins, customer numbers, or campaign results. If reliable evidence cannot be found, explicitly say the information is unavailable or uncertain — do not fill the gap with a plausible-sounding guess.

## WEB RESEARCH

- For research tasks, use available internet/web capabilities rather than relying solely on pretrained knowledge.
- When researching a company, search broadly across multiple source types and do not stop at the first few search results.
- Whenever possible, triangulate important claims using multiple independent sources.
- Available data tools in this environment (e.g. Semrush for traffic/organic/paid channel data) should be used to ground channel-mix and SEO claims in real data rather than assumption, where relevant.

## SOURCE DATABASE

Maintain structured source information in `sources/` so every research claim can be traced back to evidence. Each source entry should record, at minimum: URL, title, publication/source date, source type (primary/secondary), and the evidence label (A–E) it supports. Company-specific sources should also be cross-referenced from that company's folder under `companies/`.

## FOLDER STRUCTURE

The structure below already exists in this repo (confirmed by inspection — no duplicates were created). Use it as follows:

```
companies/<company-name>/     Full deep-dive dossier per company (see Company Research Framework below)
sources/                       Structured source database — every citation backing any research file
research/india/                Thematic/cross-company research specific to the Indian market
research/global/               Thematic/cross-company research specific to global markets
research/profitability/        Cross-company synthesis on what drives profitability
research/failed-and-struggling/ Post-mortems on companies that burned cash, declined, were acquired, or failed
research/campaigns/            Deep dives on individual marketing/brand campaigns
financials/                    Financial data, filings, models pulled during research
marketing/                     Marketing/channel strategy analysis not tied to one company
branding/                      Brand identity, voice, positioning research
channels/                      Channel-specific deep dives (Meta, SEO, creators, retail, marketplace, CRM, etc.)
strategy/                      Synthesized cross-company insights and playbooks
outputs/                       Finished playbooks and BabyOrgano-facing deliverables (see Research Outputs below)
```

Company research is the atomic unit: if research is about a specific company, it belongs in `companies/<company-name>/`, even if it also touches profitability, a campaign, or a channel — link back to it from the relevant `research/`, `channels/`, `marketing/`, or `branding/` file rather than duplicating content.

## COMPANY RESEARCH FRAMEWORK

For every deeply researched company, investigate and document, inside `companies/<company-name>/`:

1. Company background
2. Founders and founding thesis
3. Category and target consumer
4. Product portfolio
5. Hero products
6. Pricing and margins where available
7. Positioning
8. Brand identity
9. Consumer messaging
10. Major campaigns
11. Marketing channels
12. Customer acquisition
13. Meta dependence
14. Alternative acquisition channels
15. SEO and organic acquisition
16. Influencer/creator strategy
17. CRM, retention, and repeat purchase
18. Distribution strategy
19. D2C vs. marketplace vs. offline
20. Retail expansion
21. International expansion
22. Funding history
23. Revenue trajectory
24. Profitability trajectory
25. Unit economics where available
26. Operational changes
27. Hiring/team changes
28. Major strategic pivots
29. Key inflection points
30. What appears to have driven profitability
31. What did not work
32. Lessons relevant to BabyOrgano
33. What is NOT transferable to BabyOrgano, and why

## PROFITABILITY INFLECTION POINT

For every relevant company, explicitly answer:

> "What changed between the period of aggressive growth/burning cash and the period of improved profitability?"

Look for changes in: CAC, marketing mix, gross margin, AOV, repeat rate, retention, pricing, discounting, product mix, hero SKUs, distribution, offline expansion, operational efficiency, inventory, headcount, agency costs, technology, geographic expansion, funding strategy, and organisational structure.

## META DIVERSIFICATION

Give particular focus to companies that reduced dependence on Meta. For each, investigate:

- What percentage or role Meta played before diversification, if available
- Why they decided to diversify
- Which channels they added
- How they built those channels
- How long the transition took
- What happened to acquisition economics
- Whether organic/direct traffic increased
- Whether retention or repeat purchase improved
- Whether offline contributed meaningfully
- Whether creators/influencers replaced paid social or simply supplemented it
- What evidence exists that diversification improved profitability

## BABYORGANO APPLICATION

Do not recommend a strategy for BabyOrgano merely because a famous brand did it. Only recommend a strategy when there is a reasonable evidence base, and for each recommendation explain:

- Why it worked for the comparable company
- Why it could or could not work for BabyOrgano
- What assumptions are required
- What BabyOrgano would need to build/hire/change
- What should be tested first
- What KPI would determine success
- What could cause the strategy to fail

## RESEARCH OUTPUTS

The objective is not generic company summaries. Research should progressively build toward these deliverables, staged in `outputs/` once each is genuinely ready:

1. D2C Profitability Playbook
2. Acquisition Diversification Playbook
3. Brand & Messaging Playbook
4. Offline/Omnichannel Playbook
5. Retention & CRM Playbook
6. Organisation/Hiring Playbook
7. Agency Evaluation Framework
8. BabyOrgano Strategic Recommendations
9. BabyOrgano 90-Day Experiment Roadmap

## Available Skills

Skills installed under `.claude/skills/` that are useful for this work include `customer-research`, `competitor-alternatives`, `content-strategy`, `seo-audit`, `ai-seo`, `pricing-strategy`, `referral-program`, `churn-prevention`, `revops`, and `product-marketing-context`, plus `/yt-research` and `/notebooklm` for sourcing and synthesizing video-based research (founder interviews, campaign breakdowns, earnings-call commentary). Use these where they fit naturally rather than doing manual equivalents from scratch.

## Workflow for a Research Request

1. Confirm scope: which company/companies, geography, framework section(s), or playbook the task is in service of.
2. Gather sources; log them in `sources/` with URL, date, source type, and evidence label (A–E) as they're found.
3. Populate the relevant `companies/<name>/` dossier (or thematic `research/`, `channels/`, `marketing/`, `branding/`, `financials/` file).
4. Explicitly work through the Profitability Inflection Point and, where relevant, Meta Diversification questions.
5. Only draw BabyOrgano-specific conclusions using the BabyOrgano Application checklist — never by analogy alone.
6. Feed validated findings into the relevant `strategy/` synthesis and, when mature, the corresponding `outputs/` playbook.
7. No research begins without an explicit request — confirm scope before starting.
