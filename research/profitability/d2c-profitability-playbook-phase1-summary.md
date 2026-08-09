# The D2C Profitability Playbook — India + Global — Phase 1 Summary

Status: Phase 1 (research universe) complete. Deep-dive research (Company Research Framework, full forensic sourcing) has NOT started. This document, plus the candidate database and scoring/selection files it links to, is the Phase 1 deliverable.

Related files:
- `research/profitability/d2c-profitability-playbook-candidate-database.md` — full 76-company structured database
- `research/profitability/d2c-profitability-playbook-scoring-and-selection.md` — full scoring + selected 18
- `sources/d2c-profitability-playbook-phase1-sources.md` — source log

## 1. Research methodology

Three parallel live-search discovery passes (India; US; UK/Europe/Australia) were run, each explicitly instructed not to rely on memory/reputation — every candidate had to be grounded in a specific article, filing reference, or interview found via search in that session. This produced 76 candidates (25/25/26) spanning four profitability-status categories and a deliberate mix of famous and lesser-known names. CLAUDE.md's Forensic Research Mode was applied at screening depth (Level 1 discovery + a lightweight Level 2 check per candidate); full Level 2–4 forensic sourcing (primary filings, triangulation, contradictory-evidence search) is reserved for the 18 companies selected for deep dive.

## 2. Definitions (Phase 2)

**D2C (direct-to-consumer):** A brand that sells its own manufactured/formulated products directly to end consumers as a primary channel (own website, own app, or owned retail), rather than being purely a reseller or marketplace. Brands that sell primarily through marketplaces/wholesale but originated as and still centrally identify as D2C are included with that caveat noted.

**Consumer brand:** Any company selling a branded physical product (or a subscription/service wrapped tightly around one) to individual consumers. Pure marketplaces, food-delivery aggregators, and SaaS are excluded even if consumer-facing.

**Profitable (Category A):** Credible evidence of **net profit or operating profit** (not gross or contribution margin alone) for at least one recent full fiscal year, from a source stronger than a bare press release — filed accounts, an audited annual report, or journalism citing filed numbers. A single EBITDA-positive quarter, a contribution-margin claim, or a funding-round valuation is explicitly insufficient.

**Recently profitable / profitability transition (Category B):** Credible evidence of a move from loss-making to profitable (or from deep losses to near-breakeven) within roughly 1–4 years, with *both* the before and after states evidenced.

**High-growth, loss-making (Category C):** Evidence of real growth/traction alongside continued, disclosed losses, with no credible profitability claim yet.

**Struggling/failed (Category D):** Evidence of shutdown, insolvency/administration, distressed acquisition, major financially-driven layoffs, a funding crisis, or a governance/accounting problem.

**Metric hierarchy applied to every profitability claim:** gross profit → contribution profit/margin → EBITDA/operating profit → net profit → free cash flow, per CLAUDE.md's Financial Forensics section. Claims resting only on gross or contribution margin are flagged, not accepted as "profitable."

## 3–4. Candidate universe &amp; database

76 candidates total: 25 India, 25 US, 26 UK/Europe/Australia. Full structured database (Company, Country, Category, Founded, Business model, Current status, Revenue, Revenue growth, Profitability bucket, Profit/loss, Funding, Investors, Inflection point, Evidence quality, Why included, Key sources) is in `d2c-profitability-playbook-candidate-database.md`.

Approximate bucket distribution across all 76: A (clearly profitable) ≈15, B (recent transition) ≈18, C (high-growth, loss-making) ≈22, D (struggled/failed) ≈21 — several borderline/conflicting cases flagged inline rather than forced into one bucket.

Baby/kids/wellness-adjacent candidates found (BabyOrgano's category): 15 across the universe — Slurrp Farm, SuperBottoms, R for Rabbit, FirstCry, Good Glamm Group/The Moms Co., Kapiva, HealthKart (India); Bobbie, Once Upon a Farm, AG1, Ritual, Brandless (US); Mamas &amp; Papas, JoJo Maman Bébé, Bugaboo (UK/EU).

## 5. Selection scoring (Phase 4)

Each candidate scored 0–3 across 10 criteria (max 30): profitability-evidence quality, financial-info availability, strategic-info availability, founder/interview availability, marketing/campaign-info availability, customer/channel-info availability, D2C relevance, BabyOrgano relevance, comparison/control value, geographic diversity. Full scores for all 76 are in `d2c-profitability-playbook-scoring-and-selection.md`.

One explicit methodological override is documented there: strict score-ranking within region would have produced zero non-UK European/Australian representation (UK's Companies House disclosure regime produces far stronger evidence than the mostly founder/agency-claimed figures found for German/French/Australian candidates — a genuine finding, not an artifact). Two UK slots were deliberately traded for Adore Beauty (Australia) and About You (Germany) to honor the brief's explicit geographic-diversity requirement.

## 6–7. Recommended 18 companies for deep dive, and why

| # | Company | Country | Bucket | Score |
|---|---|---|---|---|
| 1 | Good Glamm Group (feat. The Moms Co.) | India | D | 27 |
| 2 | FirstCry (Brainbees Solutions) | India | B | 26 |
| 3 | HealthKart | India | A | 26 |
| 4 | Mamaearth (Honasa Consumer) | India | B | 26 |
| 5 | Kapiva | India | C | 23 |
| 6 | Hims &amp; Hers | US | B | 26 |
| 7 | e.l.f. Beauty | US | A | 25 |
| 8 | Warby Parker | US | B | 24 |
| 9 | Vital Farms | US | A | 23 |
| 10 | Morphe (Forma Brands) | US | D | 23 |
| 11 | Bobbie | US | A | 22 |
| 12 | Gymshark | UK | A | 25 |
| 13 | Bloom &amp; Wild | UK | B | 25 |
| 14 | JoJo Maman Bébé | UK | A | 25 |
| 15 | Made.com | UK | D | 24 |
| 16 | Mamas &amp; Papas | UK | D | 24 |
| 17 | Adore Beauty | Australia | B | 20 |
| 18 | About You | Germany | D | 20 |

Full one-paragraph rationale per company is in the scoring/selection file. In brief, this set was built to guarantee: all four profitability buckets represented; at least one primary-filing testbed per major jurisdiction (India BSE/NSE, US SEC, UK Companies House, Germany public filings, Australia ASX); six companies directly in BabyOrgano's category (Good Glamm/Moms Co., FirstCry, Kapiva, Bobbie, Mamas &amp; Papas, JoJo Maman Bébé); at least one matched success/failure pair in the same category and country (JoJo Maman Bébé vs. Mamas &amp; Papas); and at least one clean case of failure caused by something other than marketing/CAC (Made.com's freight-cost shock) and by influencer/creator over-reliance specifically (Morphe) — both essential for the brief's instruction to actively hunt for contradictory evidence rather than defaulting to a Meta/CAC story.

## 8. Important data gaps

- **Almost all revenue/profit figures for private companies are evidence label C (third-party reporting), not A.** Even where journalism describes a figure as "filed," this screening has not yet independently pulled the underlying filing. This is the single most important gap to close at the start of each deep dive — pull the actual MCA filing / Companies House accounts / SEC 10-K / ASX announcement / Bundesanzeiger-Handelsregister/Infogreffe-BODACC filing directly, rather than relying on the aggregator journalism cited here.
- **Two explicit unresolved contradictions carried forward:** Sugar Cosmetics' FY24 profit/loss status (sources disagree), and Sézane's revenue figure (€250m vs. ~€500m across sources, unresolved).
- **Legal entity names are unconfirmed for roughly a third of the India candidates** ("not confirmed this pass" in the database) — needed before any MCA-level primary-source hunt.
- **Continental European and Australian evidence is systematically weaker** than UK/US/India in this pass — several candidates (Typology, Sézane, SNOCKS, Koala, Bugaboo) rest on founder or agency claims rather than filed accounts, and are flagged rather than treated as verified.
- **No company in the universe yet has a verified, primary-source-confirmed Meta/paid-social spend figure** — every "Meta dependence" or "ad spend" data point found so far (Mokobara, Traya, Ro, etc.) is a total marketing-spend or revenue-growth proxy, not an actual platform-level breakdown. This is a known, likely-permanent limitation (platforms don't disclose this, and companies rarely do either) rather than something the deep-dive phase is expected to fully resolve — but it means causal claims about "Meta reduction" will often have to be inferred from channel-mix and CAC/margin changes rather than stated directly.
- **PDF-based primary sources (annual reports, investor decks, 10-Ks, ASX PDFs) have not yet been pulled and read** for any of the 18 — this environment's PDF extraction capability (confirmed working in the environment audit) has not yet been exercised on a real filing in this project.

## 9. Initial hypotheses worth testing in the deep-dive phase

These are explicitly hypotheses, not conclusions — Phase 6/7 forensic work should actively try to falsify each, per CLAUDE.md's negative-evidence discipline.

1. **"Explicit, stated pivots (Bloom &amp; Wild, Licious) produce more durable profitability than organic/gradual improvement (Mamaearth, Traya)."** Testable by comparing profit trajectories 2+ years after each company's stated or inferred inflection point.
2. **"Companies that diversify into retail/wholesale reach profitability faster or more durably than DTC-only peers in the same category."** Candidate test: Huel/JoJo Maman Bébé/Bondi Sands/Ritual (diversified) vs. Typology/Sézane (stayed DTC-only, weaker evidence of durable profit) — though the DTC-only comparators have weaker evidence and this needs care.
3. **"Failure is at least as often driven by supply-chain, cost-structure, or partnership risk as by CAC/Meta dependence."** Made.com (freight costs) and Morphe (influencer dependency) already provide direct counter-evidence to a Meta-centric failure narrative before any deep dive begins — this hypothesis is partially supported even at Phase 1.
4. **"Headline 'profit' or 'loss' figures frequently diverge from underlying operating performance due to one-off items, and this divergence is common enough to require checking, not assuming."** Adore Beauty, THG, and Rent the Runway all show this pattern already at the screening stage.
5. **"Category leadership/scale does not reliably predict profitability, and public markets will fund an IPO without it."** FirstCry (India), About You (Germany), and Once Upon a Farm/Koala (fresh IPOs, US/Australia) are the test cases.
6. **"Baby/kids/wellness category companies that stay narrowly D2C-only struggle to reach profitability, while ones that add retail/omnichannel (JoJo Maman Bébé, R for Rabbit, HealthKart's multi-channel model) do better."** This is the hypothesis most directly relevant to BabyOrgano and deserves the most rigorous testing across the six baby/wellness-category companies selected.

## Stop condition for Phase 1

This phase stops here per the brief's explicit instruction not to begin deep research yet. The universe is broad and diverse enough (76 candidates, 4 buckets, 3 regions, both famous and lesser-known names, explicit rejected-candidate lists showing real screening discipline) that further discovery searching is unlikely to materially change the shape of the selected 18; remaining uncertainty (see Data Gaps above) is documented rather than resolved.
