# Demand Engine Analysis: Which Acquisition Mechanisms Create Durable Demand?

**Purpose:** This report closes the highest-priority evidence gap identified in `outputs/d2c-marketing-forensics-audit.md` — the missing branded-vs-non-branded search split — and extends the same discipline across ten other demand engines, for a small, prioritized set of companies where real data is available. It does not expand the company universe or rewrite the methodology.

**The question this report answers:** which demand engines appear to create durable customer acquisition and/or better economics, and which claims about that are actually supported by evidence versus merely plausible?

**What this report explicitly does not conclude:** "SEO is better than Meta," "organic traffic causes profitability," "creators reduce CAC," or "offline reduces CAC." Where evidence for a mechanism's effect on economics does not exist, this report says so.

**Companies covered:** Minimalist, Mamaearth (Honasa), The Moms Co., Mother Sparsh, Beardo, Plix, Wakefit — plus Native, Warby Parker, and e.l.f. Beauty as global comparisons. Not every company is forced into every section; where data is unavailable for a company in a given section, it is skipped rather than filled with inference.

---

## 1. What We Can Actually Measure

Before answering anything, an honest inventory of what our actual tools can and cannot see:

| Data type | Available? | Tool/source | Caveat |
|---|---|---|---|
| Organic keyword-level traffic share (domain) | **Yes** | Semrush `resource_organic` | Semrush's own traffic-share estimate, not verified analytics; captures only the *visible sample* (we pulled top 30 keywords by traffic share per domain), not the full long tail |
| Organic vs. paid-*search* traffic (Google Ads) at the domain level | **Yes** | Semrush `domain_rank` | This is Google Ads paid *search* only — it is **not** Meta/paid-social spend, and must never be read as such |
| Semrush's built-in "branded" keyword flag | **Tested, rejected as unreliable** | Semrush `resource_organic` filter | See methodology note below — this flag does not reliably identify a domain's *own* brand terms |
| Direct traffic, referral traffic, paid-social traffic, channel-mix breakdown | **Unavailable** | Semrush `traffic_overview` | Explicitly returns "your current plan does not support this feature" — confirmed by direct test, not assumed |
| Meta-specific ad spend (any company) | **Unavailable** | — | No company in this entire research program has disclosed this; confirmed absent again in this pass |
| Filed A&P/revenue ratios | **Partially available** | Company filings (from prior research passes) | Available for Minimalist, Mamaearth, Wakefit, Plum Goodness, WOW Skin Science, mCaffeine, Sugar Cosmetics, Warby Parker, e.l.f. Beauty. Not disclosed at brand level for Plix/Beardo (Marico doesn't break out by brand), Mother Sparsh, or The Moms Co. |
| Repeat purchase / retention / CRM metrics | **Mostly unavailable, one exception** | Founder statements, vendor case studies | Mother Sparsh's WhatsApp open-rate figure is a real, sourced number; nothing comparable exists for the others in this set |
| Campaign-level reach/sales lift | **Available for two companies only** | Founder/company statements | Mother Sparsh (#FirstTimeMom, #PlantAndPure) and Marico's own investor-call quotes (Plix/Beardo) |

**Methodology note on the "branded" filter:** Semrush's `resource_organic` report exposes a `branded` field. We tested it directly on Minimalist's domain with `branded=1` and `branded=0` filters. The results did not correspond to "contains the word Minimalist" — `branded=1` surfaced keywords like "myntra skin analyzer" and "alpha arbutin ordinary" (which reference *other* companies' brand names — Myntra, The Ordinary — not Minimalist's own), while the domain's single largest keyword ("minimalist," 53.87% of traffic) appeared in *neither* the branded=1 nor branded=0 result set. **This flag is unreliable for identifying a domain's own brand terms and was discarded.** All branded/non-branded classification below was instead done manually, by inspecting whether each keyword's text contains the company's own brand or product-line name — the same method the audit itself recommended ("Minimalist serum" vs. "niacinamide serum").

---

## 2. Branded vs. Non-Branded Search

For each domain, the top 30 organic keywords by traffic share were pulled and manually classified. Because this is a sample (not the full keyword list), the "captured" row shows what share of *total site organic traffic* the top-30 sample accounts for — the remainder is long-tail traffic not classified here.

| Domain | Branded (top-30 sample) | Non-branded, product-category (top-30 sample) | Non-branded, audience-adjacent* | Captured by sample | Uncaptured long tail |
|---|---|---|---|---|---|
| **Minimalist** (beminimalist.co) | ~65.9% | ~5.0% | 0% | ~71% | ~29% (of 4,746 total keywords) |
| **Native** (nativecos.com) | ~95%+ (virtually every visible keyword contains "native") | ~0% visible in top 30 | 0% | ~high | Not separately isolated |
| **Mamaearth** (mamaearth.in) | ~42.3% | ~4.2% (moisturizing cream, face mask, hair growth oil, best sunscreen, aloe vera gel, rice water, multani mitti benefits, high-porosity hair) | 0% | ~46.5% | ~53.5% (of 39,987 total keywords) |
| **Mother Sparsh** (mothersparsh.com) | ~46.9% | ~7.4% (baby wipes, wet wipes, diaper rash cream, baby care) | **~7.2% (baby-names blog content — see finding below)** | ~61.6% | ~38.4% (of 3,942 total keywords) |
| **The Moms Co.** (themomsco.com) | **~100% of visible top-30** | **0%** | 0% | high | small (only 209 total keywords) |
| **Beardo** (beardo.in) | ~46.6% | ~15.9% (italian beard, beard, trimmer for men, hair serum for men, beard oil, face/hair wax for men) | 0% | ~62.5% | ~37.5% (of 8,463 total keywords) |
| **Plix** (plixlife.com) | **~100% of visible top-30** | **0%** | 0% | high | Not separately isolated (4,559 total keywords) |
| **Wakefit** (wakefit.co) | ~48.9% | ~11.3% (study table, mattress, study chair, computer table, sofa set, wardrobe, blanket, folding mattress) | 0% | ~60.2% | ~39.8% (of 23,811 total keywords) |
| **Warby Parker** (warbyparker.com, global) | ~39%+ in top 13 alone | ~1.0% (hazel eyes, grey eyes, how to fix loose glasses, google glasses — all from its "Learn" content hub) | 0% | — | large (256,884 total keywords — the biggest long tail in this set by far) |
| **e.l.f. Beauty** (elfcosmetics.com, global) | Nearly all of top 30 | ~0.6% ("color analysis" quiz content) | 0% | — | large (87,256 total keywords) |

*Audience-adjacent = non-branded content that targets the same audience but is not about the product category itself (explained below).

### The most important correction this section produces

**Mother Sparsh's organic traffic — cited in the prior report as "the strongest and most directly transferable evidence for BabyOrgano" — is substantially a baby-names content farm, not ingredient/trust education.** Roughly as much of its visible top-30 organic traffic comes from generic parenting-adjacent content ("boy names with meaning," "unique boy names," "islamic baby boy names," "telugu baby names," "a to z baby girl names hindu," some of it dated back to 2017–2021 and never refreshed) as comes from actual product-category terms (baby wipes, diaper rash cream). This is a **generic top-of-funnel SEO tactic any parenting/lifestyle blog could run** — it has nothing to do with the founder's stated trust/Ayurveda-adjacent positioning, hospital sampling, or ingredient transparency. The prior report's implicit inference — that Mother Sparsh's high organic:paid ratio reflects a superior trust-building content strategy — is **significantly weakened** by this finding: at least some, possibly much, of that "organic" traffic advantage over Mamaearth/The Moms Co. is generic name-content SEO, which any brand (including one with no distinctive positioning at all) could replicate.

**A second correction:** The Moms Co.'s visible top-30 keywords are **essentially 100% branded** — there is no meaningful category-term visibility to point to at all, before or after the collapse. This materially strengthens one specific alternative explanation flagged in the audit: if The Moms Co. never had much non-branded organic demand to begin with, then its post-2024 traffic collapse is more consistent with a **branded-search collapse** (fewer people searching the brand by name because it became less visible/relevant as Good Glamm's distress became public) than with "content/trust marketing failed" — because there was little content/trust-driven non-branded traffic to fail in the first place.

**A third finding, in the other direction:** Beardo and Mamaearth show meaningfully *higher* non-branded, product-category-term visibility (~16% and ~4-11% respectively, depending on measurement) than Minimalist (~5%), Native, Plix, or The Moms Co. (all near-zero in the visible sample). Beardo's "italian beard" / "italian beard style" ranking (a grooming-guide blog page, 4.6%+0.84% of its total traffic) is a genuine, verifiable example of category-content-driven non-branded organic demand — better evidenced than Minimalist's.

**A fourth, distinct category worth naming on its own:** Warby Parker's and e.l.f.'s small non-branded shares are not general category terms but **specific educational/content-hub pages** ("Learn" hub explainers on eye colors, glasses-repair how-tos; a color-analysis quiz) — a different, narrower mechanism than a broad SEO-content-cluster strategy, and small in visible share (~1% or less) even for brands known for content marketing.

---

## 3. Organic Demand

Per the audit's instruction: **if only total organic traffic is available, this cannot distinguish brand demand from category demand — say so explicitly.** For every company below, we now have the breakdown from Section 2, so this section states what it does and doesn't establish.

- **Minimalist:** total organic traffic (~816K/month, Semrush estimate) is now known to be majority brand-demand (≥66% in the visible sample), not majority category-demand. This means the earlier report's citation of Minimalist's "~700x domain-rank growth" as evidence of a successful education/content strategy **conflates two different things**: brand-search growth (which could simply track the brand's growing fame/revenue, independent of content quality) and category-demand capture (which would be the actual test of whether the content model works as an acquisition mechanism). The data cannot currently separate how much of that 700x growth is each.
- **Beardo:** shows the most credible non-branded organic-content evidence in the India set — an actual grooming-guide blog page ranking for a real style-category term ("italian beard"). This is **observed**, not inferred: the URL serving that keyword is a dated blog post (`/blogs/grooming-guide/italian-beard-style-guide`), not the homepage.
- **Mother Sparsh:** its favorable organic:paid ratio (35:1) is now shown to be **partly explained by a mechanism unrelated to its brand positioning** (baby-names content). The remaining product-category share (~7.4%) is real but smaller than the ratio alone implied.
- **Backlinks, content volume, domain age:** none of these were measured in this pass for any company — Semrush's backlinks_research and audience_research toolkits were not queried given the scope-discipline instruction to prioritize the highest-value gap (branded/non-branded) first. This remains an open gap, listed in Section 10.

---

## 4. Paid Acquisition

**Meta-specific spend: unavailable for every company in this set, as in every prior pass of this research program.** No exception found.

**Google Ads paid-search traffic vs. organic traffic (Semrush `domain_rank`, a real, if narrow, proxy for search-specific paid dependency — not total ad spend):**

| Domain | Organic traffic (est.) | Google Ads paid-search traffic (est.) | Organic : paid-search ratio |
|---|---|---|---|
| Wakefit | 1,363,043 | 7 | ~194,720 : 1 (near-zero Google Search ad buying) |
| Beardo | 478,126 | 15,442 | ~31 : 1 |
| Native | 372,926 | 10,013 | ~37 : 1 |
| Mother Sparsh | 165,498 | 4,786 | ~35 : 1 |
| Mamaearth | 975,296 | 48,758 | ~20 : 1 |
| Minimalist | 816,663 | 52,000 | ~15.7 : 1 |
| e.l.f. Beauty | 1,085,932 | 86,375 | ~12.6 : 1 |
| Plix | 522,288 | 41,775 | ~12.5 : 1 |
| The Moms Co. | 24,411 | 1,846 | ~13.2 : 1 |
| Warby Parker | 1,825,266 | 438,756 | **~4.2 : 1** |

**What this table can and cannot say:** it measures Google *Search* Ads specifically, which is one channel among several (Meta, other social, affiliate, display, video). It says nothing about Meta dependency directly. **Wakefit's near-zero Google Ads paid-search buying is a genuinely new, verifiable data point** (not previously in this research program) — it confirms that whatever ad spend Wakefit does report (7–9% of revenue per its filings) is concentrated almost entirely outside Google Search, consistent with, though not proof of, a social/content-first spend allocation. **Warby Parker stands out as the most Google-Search-paid-dependent brand in this entire set** by a wide margin — a new finding not surfaced in the prior report, which had only noted its *filed* ad-spend-to-revenue ratio (flat ~12–14%) without this channel-level detail.

**Filed A&P/revenue ratios, multi-year, where disclosed (carried over from prior passes, not re-derived here):**

| Company | FY | A&P / Revenue | Source |
|---|---|---|---|
| Minimalist | FY22→FY25 | 30.6% → 35.3% → 33.7% → 29.9% | Filings [A] |
| Mamaearth | FY24→FY25 | 34.4% → 36.0% (rising) | Filings [A] |
| Wakefit | 9M FY25 → FY26 | ~8.5% → rising to ~7.3–9% | Filings + management commentary [A] |
| Plum Goodness | FY24→FY25 | 45.9% → 34.6% (cut) | Filings [B] |
| Warby Parker | multi-year | flat ~12–14% | SEC filings [A] |
| e.l.f. Beauty | multi-year | 9.2% → 22.1% (rising continuously) | SEC filings [A] |

Plix, Beardo, and Mother Sparsh: **A&P/revenue is not disclosed at brand level and is not estimated here** — Marico does not break this out by brand, and neither Plix's nor Mother Sparsh's own filings (where they exist) disclose it separately from other costs in what we were able to access this pass. The Moms Co.: not disclosed.

**Was total advertising dependence increasing or decreasing?** Answerable only for the six companies with filed A&P data above. Rising: Mamaearth, e.l.f. Beauty. Falling (at least in the specific window measured): Minimalist (FY24→FY25 only — FY22→FY23 rose), Wakefit, Plum Goodness. Flat: Warby Parker. **For Plix, Beardo, Mother Sparsh, and The Moms Co., this question cannot currently be answered from disclosed data.**

---

## 5. Creator Acquisition

Classifying observed creator use by function, per company, where evidence exists:

| Company | Creator mechanism observed | Function (evidenced) | Repeatable system or isolated campaign? |
|---|---|---|---|
| **Beardo** | Celebrity ambassador sequence: Suniel Shetty → Yash → KL Rahul/Hrithik Roshan → Vicky Kaushal → Aditya Roy Kapur → Bobby Deol → Hrithik Roshan (return) → Pushpa 2 tie-in, 2017–2024 | **Awareness** (evidenced — sustained, dated, near-annual cadence). **Conversion:** not evidenced — no campaign-level reach or sales data was ever disclosed for any single partnership. | **Repeatable system** — the cadence and creative format (a fresh celebrity/campaign roughly annually) is consistent enough over 7+ years to call a system, not one-off spend. |
| **Mother Sparsh** | Momfluencer campaigns at scale: #FirstTimeMom (100+ momfluencers, ~3M impressions, +10% sales), #PlantAndPure (~8M reach, +15–20% sales) | **Awareness + measured conversion lift** — this is the *only* case in this entire set with a disclosed, campaign-specific sales-lift number attributable to creator activity. [B/C — company-reported, real dated campaigns] | Evidenced as at least two distinct, repeated campaigns using the same many-small-creators format — a real, if narrow, repeatable pattern. |
| **Native** | Pre-acquisition: simple factual comparison ad format, not creator-led. Post-acquisition (per ad-library scrape): 62% of current ads are video, UGC-style creator content | **UGC production** (current) — but this is inferred from ad-format classification (GoMarble tool), not confirmed as creator partnerships specifically vs. brand-made UGC-style content. | Unknown whether this is a repeatable creator program or an ad-agency creative style — not distinguished by the available evidence. |
| **e.l.f. Beauty** | #eyeslipsface: detected ~3M organic views, then paid to amplify (commissioned song, became TikTok's first paid hashtag challenge) | **Detection + paid amplification**, not creator-seeding in the traditional sense — the mechanism is watching for organic creator activity and funding it further, not commissioning creators from scratch. | This specific mechanism (detect-then-amplify) is documented as repeatable in trade press across multiple e.l.f. campaigns, not a one-off. |
| **Minimalist, Plix, Wakefit, The Moms Co.** | **Not deeply mapped this pass** | Unavailable | Unavailable — flagged as a gap, not assumed absent |

**What can be said about creators and economics specifically:** only Mother Sparsh has a disclosed, campaign-attributed sales lift (+10% to +20%) tied to a specific creator mechanism. Beardo's celebrity spend, despite being the most visually prominent creator strategy in this entire report, has **zero disclosed conversion or sales evidence** — its function is evidenced only as far as "awareness," not further down the funnel. This is an important, deliberately unresolved gap, not a finding that celebrity spend doesn't work.

---

## 6. PR / Earned Distribution

| Company | Campaign | Evidenced outputs | What is NOT evidenced |
|---|---|---|---|
| **True Elements** (Marico cluster) | "Food That Does Not Lie" (Dec 2022, TBWA\India, 4 films) | Real, dated, agency-attributed campaign; stated target reach 5 crore Indians | Whether the 5-crore reach target was achieved; any direct sales/traffic lift attributable to the campaign specifically |
| **Wakefit** | Sleep Internship (annual stunt) | Trade-press-reported spikes in direct traffic (100–150%) and "Wakefit" Google searches (~150%) around each announcement [B/C] | Whether these spikes converted to sales, or simply reflect curiosity/press-driven branded search that faded afterward |
| **Warby Parker** | Fashion-press-first launch (GQ "Netflix of eyewear") | Real, independently corroborated across retrospectives; caused a 48-hour order flood forcing Home Try-On to suspend | Exact revenue/order figures are not independently audited — figures come from retrospective accounts, not filings |
| **e.l.f. Beauty (Halo Glow)** | Independent BeautyTok dupe comparison to a $44 Charlotte Tilbury product | Genuinely organic — zero brand mechanic — 500M+ views across dupe-comparison content [C] | Sales lift specifically attributable to this moment (e.l.f.'s overall ad spend kept rising through this period, so it cannot be isolated as "this replaced paid spend") |

**Do PR moments generate backlinks/branded search/traffic?** Directionally yes, per the Wakefit and Warby Parker evidence above — this is the best-evidenced link in the PR chain. **Does PR coverage equate to sales?** Not established for any company in this set — every case above stops at traffic/search/attention, not verified revenue impact.

---

## 7. Marketplace / Offline Discovery

Distinguishing **revenue channel** from **customer acquisition channel**, where evidence exists:

- **Mamaearth:** has meaningful offline/modern-trade distribution (documented in prior research passes) alongside marketplace presence (Amazon/Flipkart/Nykaa). **Critical point from this pass's methodology note (Section 1):** Semrush's domain analysis captures *website* traffic only — it cannot see marketplace or offline discovery at all. This means Mamaearth's declining *website* organic traffic (noted in the prior report) says nothing about whether marketplace or offline discovery is growing, shrinking, or stable — **this is a revenue-channel question our tools cannot answer, not a resolved "decline."**
- **Beardo/Plix (Marico cluster):** offline/general-trade expansion is explicitly described by Marico's own CEO as "test and learn" for Beardo's salon channel — Marico itself has not declared this a proven acquisition channel, only a revenue-channel experiment in progress. [B — direct quote, already documented in prior research]
- **mCaffeine (comparison case, prior research):** ~65% marketplace-dependent — the clearest evidenced case in this whole research program of marketplace functioning primarily as a **revenue channel without owned customer relationships** (no CRM/retention data exists for mCaffeine either, consistent with a rented-audience model).
- **Wakefit:** offline retail (23→165 stores across the observed period) is well-documented as a deliberate, funded (IPO-proceeds) expansion — but whether these stores function as *discovery* (new customers walking in cold) or *conversion of already-aware online customers* (showrooming) is **not distinguished by any evidence gathered in this or prior passes.** This is a genuine, specific gap.
- **The Moms Co.:** marketplace/offline footprint not verified this pass.

**What can be safely said:** marketplace and offline are, for every company where we have any evidence, at minimum functioning as revenue/inventory-movement channels. **Whether any of them function as a genuine discovery/acquisition channel — as opposed to a channel that monetizes demand generated elsewhere — is not established by the evidence gathered in this research program**, for any company.

---

## 8. Retention / CRM

| Company | Evidence | Status |
|---|---|---|
| **Mother Sparsh** | WhatsApp-led CRM (via Zoko) replacing email, ~95% open rate vs. <5% for email [B] | The only real, sourced retention/CRM mechanism in this entire set — but this is an *engagement* metric (open rate), not a *repeat-purchase* or *retention-rate* metric. Do not conflate the two. |
| **Plix / Beardo** (Marico cluster) | Marico's own words, pre-acquisition: "our LTV by CAC and repeat rate... is pretty high and best in class" [A — direct investor-call quote] | Strongest-quality retention claim in the set (Strength 1/Quality A per the marketing-mechanism evidence score), but it is a qualitative superlative, not a disclosed number — no actual repeat-rate percentage or LTV figure was given. |
| **Minimalist** | Circulating repeat-rate figures (42%, 45%, 60%, 65%) | **Explicitly rejected** in the prior audit as untraceable to any credible source — restated here as still rejected, not softened. |
| **Wakefit** | No retention/repeat-purchase metric found disclosed | Unavailable |
| **Mamaearth, The Moms Co.** | No retention/repeat-purchase metric found disclosed in this pass | Unavailable |

**No private CRM flows, segmentation logic, or lifecycle-email programs are invented here for any company** — where not observable, marked unavailable, per instruction.

---

## 9. What Appears Durable

Ranking by evidence quality (not by fame), what can be called *durable* (i.e., evidenced across multiple time points or independent of continued spend) versus merely *observed once*:

| Mechanism | Durability evidence | Strength/Quality |
|---|---|---|
| Beardo's grooming-guide content ranking for "italian beard" | Sustained enough to be a top-traffic keyword years after presumed publication — durable, low-marginal-cost organic asset | 2/A — directly observed in live keyword data |
| Wakefit's near-zero Google Search ad spend alongside high organic-search dominance | Consistent with its filed low overall ad-spend ratio (7-9%) — durable *pattern*, though the underlying cause (deliberate strategy vs. simply not needing to bid on its own highly branded, low-competition category terms) is not established | 2/B |
| Marico's disclosed manufacturing/procurement in-sourcing mechanism for Beardo | A structural, operational change (not a campaign) — durable by construction, evidenced directly by CFO quote and sustained EBITDA-margin data over several years | 1/A |
| Plix/Beardo's pre-acquisition repeat-rate/LTV strength (Marico's own characterization) | Cited as already established *before* acquisition and sustained after — but only as a qualitative claim, no number | 2/B |
| Mother Sparsh's momfluencer sales-lift campaigns | Evidenced twice (#FirstTimeMom, #PlantAndPure) with different, specific numbers — suggests a repeatable format, though only two data points | 2/B |

**What is NOT shown to be durable, on inspection:** Mother Sparsh's organic-traffic advantage, once the baby-names-content confound is accounted for, is a *smaller and less brand-specific* durable asset than the prior report implied — a real but more modest finding. The Moms Co.'s near-total absence of non-branded organic demand means it had, in retrospect, very little durable organic asset to lose in the first place — its "collapse" is better understood as the disappearance of a *rented* (branded-search, likely ad/PR-driven) asset than the failure of a durable one.

---

## 10. What We Cannot Prove

Explicit, itemized, per the audit's own gap list plus what this pass additionally surfaced:

1. **Meta-specific spend, for any company, in any pass of this entire research program.** Confirmed absent again.
2. **Direct traffic, referral traffic, or any channel-mix breakdown** for any company — `traffic_overview` is confirmed unavailable on this Semrush plan (tested directly, not assumed).
3. **Whether Minimalist's, Plix's, or Beardo's non-branded organic traffic (where it exists) actually converts to sales, at what rate, or at what cost** — Semrush traffic-share data says nothing about conversion.
4. **Whether marketplace/offline channels function as genuine discovery mechanisms or merely monetize demand generated elsewhere**, for any company in this set.
5. **Backlink profiles, content-publishing volume/cadence, or domain-age-controlled growth-curve comparisons** — not measured in this pass for any company; this remains the largest unaddressed confound from the original audit's Mother Sparsh/Mamaearth/Moms Co. comparison.
6. **Whether Beardo's, Native's, or e.l.f.'s creator/celebrity spend measurably lowers CAC or raises conversion** — awareness function is evidenced; conversion/economics function is not, for any of the three.
7. **Whether Wakefit's near-zero Google-Search-ad-spend is a deliberate strategic choice or simply reflects low competitive bidding pressure on its own brand terms** — the pattern is real; the cause is not established.
8. **The exact size of the long tail beyond the top-30-keyword sample used throughout this report** — for large domains (Warby Parker: 256,884 total keywords; e.l.f.: 87,256; Mamaearth: 39,987), the visible sample captures well under half of total organic keyword volume, and the non-branded share of the *uncaptured* tail is unknown in either direction.

---

## 11. Implications for Moving Beyond Meta

This section does not recommend a strategy — it states only what the evidence in this report actually licenses, distinguishing OBSERVED from INFERRED from UNKNOWN throughout.

- **OBSERVED:** every company in this set, without exception, shows organic search traffic that is majority-to-overwhelmingly *branded* in its visible top-keyword sample. Even brands with genuine, verifiable category-content assets (Beardo's grooming guide, Mamaearth's ingredient/how-to blog posts, Warby Parker's/e.l.f.'s "Learn"/quiz content hubs) show that content producing a **small minority** share of visible top-line organic traffic relative to brand-name search. **This means "build content/SEO instead of Meta" cannot currently be evidenced as a traffic-replacement strategy at the scale Meta typically operates — the non-branded organic layer that exists in this data is real but thin.**
- **OBSERVED:** where a company has both a real category-content asset (Beardo) and a real celebrity/creator-awareness engine (also Beardo) running simultaneously, our evidence cannot separate their respective contributions to the brand's overall demand — they coexist, and Marico's own disclosed profitability mechanism for Beardo is manufacturing/procurement in-sourcing and paid-media *efficiency*, not a shift toward organic/content acquisition.
- **INFERRED, not observed:** that Mother Sparsh's momfluencer-and-sampling model is more durable or more transferable than a paid-heavy model, *specifically because* of its marketing mechanism. What's observed is two campaigns with disclosed sales lifts and a WhatsApp engagement metric — a real, useful, but narrower base of evidence than "durable demand engine" implies.
- **UNKNOWN:** whether any of the observed non-branded organic assets (Beardo's grooming content, Mamaearth's how-to blog posts, Wakefit's category-term rankings) were built as a *deliberate substitute* for paid-social spend, or arose incidentally alongside continued (or rising, in Mamaearth's case) paid spend. Nothing in this dataset establishes intent or substitution — only coexistence.
- **UNKNOWN, and likely to remain so without primary access:** whether reducing Meta dependence, for BabyOrgano specifically, would need to be funded by (a) a slow-build content/SEO asset (evidenced as thin relative to brand search across this entire set), (b) a Mother-Sparsh-style field/sampling program (evidenced as effective at small scale, twice, but not proven to scale or to be cheaper than paid social at scale), or (c) some combination — the evidence gathered here is not sufficient to rank these options against each other on cost or durability, only to describe what has been observed elsewhere.

**The single most defensible statement this report can make:** every demand engine examined here has *some* real, verifiable evidence behind it for *some* company, at the level of awareness or traffic — but almost none of them have evidence connecting them all the way through to conversion, retention, or profit, for any company, in this dataset. That gap — not a ranking of channels — is the honest finding to carry into any BabyOrgano strategy discussion.

---

## Appendix: Sources and Method

- All keyword-level and domain-level figures: Semrush `resource_organic` and `domain_rank` reports, India database (`in`) for Minimalist, Mamaearth, Mother Sparsh, The Moms Co., Beardo, Plix, Wakefit; US database (`us`) for Native, Warby Parker, e.l.f. Beauty. Pulled directly in this session — [D, Semrush estimate tool, not verified analytics].
- Domains verified directly (not assumed): beardo.in (not beardo.com — confirmed via `phrase_organic` SERP lookup on "beardo"), plixlife.com (not plix.co.in or myplix.com — confirmed via `domain_rank` resolution).
- `traffic_overview` unavailability: confirmed via direct tool call this session, not inferred from documentation.
- Filed A&P/revenue, celebrity timelines, campaign sales-lift figures, and Marico investor-call quotes: carried over from `research/india/d2c-acquired-brands-marketing-strategy-verified.md`, `research/global/d2c-acquired-profitable-dependency.md`, and underlying round-2 scratchpad findings — not re-verified in this pass, cited at the same evidence-quality label as originally assigned.
