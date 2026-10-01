# OPENCLAW — ALJ CHINA AUTO WEEKLY BRIEF
# Product Specification

---
document_id: OPENCLAW-SPEC-ALJ-CHINA-AUTO-001
version: v1.0
created: 2026-05-22
status: APPROVED — operator approved 2026-05-23
client_id: alj_china_auto_001
classification: Phase D Controlled Pilot — Workstream 2
author: CoWork (drafted for operator review)
governing_docs:
  - OPENCLAW-OPS-001 (Operating Protocol)
  - client_config_alj_china_auto_001.yaml
  - SYS_Retrieval_Query_Templates_alj_china_auto_weekly_v1.md
  - OPENCLAW-ADV-013 (Browser Retrieval Phase 1 — advisory only)
---

---

## 1. PRODUCT IDENTITY

**Product name:** ALJ China Auto Weekly Brief

**Client:** Abdul Latif Jameel / Jameel Motors

**Client ID:** alj_china_auto_001

**Primary audience:**
ALJ / Jameel Motors executives, strategy teams, OEM relationship managers,
distribution leadership, regional automotive teams, communications teams,
and market development teams.

**Purpose:**
Deliver a weekly China-source intelligence brief on the Chinese automobile
market, focused on developments relevant to ALJ's distribution strategy, OEM
partnerships, Toyota/Lexus positioning, Chinese OEM expansion, NEV/EV
competition, export flows, dealer economics, aftersales, and Saudi/GCC
competitive positioning.

**Phase D role:**
Phase D Workstream 2 — controlled pilot product. Runs in parallel with
china_monitor_001 (Workstream 1) without modifying it.

---

## 2. CADENCE AND DELIVERY

**Cadence:** Weekly

**Trigger:** Manual only — never added to cron

**Recommended delivery window:** Monday morning (sets the agenda for the week)

**Schedule field in config:** null

**Delivery channel:** Lark (pilot channel — operator-held)

**Pilot mode:** true — all output held for operator review before any
external delivery

**External delivery rule:** No output is sent to ALJ or any external
recipient without explicit per-delivery operator approval

---

## 3. SOURCE RULES

**Retrieval provider:** Baidu only (brave_enabled: false)

**Source universe:** Chinese / China-market sources only

**Lookback window:**
- Primary: 7 days (all precision queries)
- Context: 30 days (OEM watch and Export/Gulf context queries only —
  for major strategic developments and background necessary to explain
  the week's signal)

**Excluded sources:**
- Brave retrieval results
- Reuters, Bloomberg, CNBC, FT, Nikkei
- Western automotive press
- International sources of any kind in the initial version

**Permitted later — by explicit operator decision only:**
An international-source comparison section, clearly separated from the
Chinese-source evidence base. Not included in v1.

**Source authority tiers (for agent guidance and appendix classification):**

| Tier | Source Type | Examples |
|------|-------------|---------|
| 1 | Official / regulatory | MIIT, MOFCOM, NDRC, SAMR, Customs |
| 2 | Industry bodies / market data | CAAM, CPCA, auto dealer associations |
| 3 | Chinese automotive and business media | Gasgoo, Yicai auto, 36Kr Auto, LatePost Auto, Dongchedi, Yiche, Sina Auto, Securities Times auto, Caixin auto |
| 4 | OEM / company sources | Toyota China, FAW Toyota, GAC Toyota, BYD, SAIC/MG, GAC, Geely, Changan/Deepal, Chery/Omoda/Jaecoo, Farizon, CATL |
| 5 | Lower-authority platform sources | Eastmoney contributor pages, reposted articles, social/platform summaries |

Tier 5 sources may be used only with caution and must not support strong
claims unless corroborated by a higher-authority source.

All retained sources regardless of tier must appear in the Complete
Chinese Source Appendix.

---

## 4. MANDATORY PRODUCT REQUIREMENT — COMPLETE CHINESE SOURCE APPENDIX

The Complete Chinese Source Appendix is a non-negotiable product requirement.

A report without a complete source appendix must not be approved for
external delivery.

**Appendix title:** COMPLETE CHINESE SOURCE APPENDIX

**Required fields per source entry:**

| Field | Requirement |
|-------|-------------|
| Source number | Sequential [1], [2], [3]... |
| Chinese title | Preserved where available |
| English title | Translated or short descriptive title |
| Publisher | Source name |
| Publication date | Exact date |
| Full URL | Complete URL — no substitution with publisher/date label |
| Blurb / snippet | Retrieved snippet or short extract |
| Relevance to ALJ | Short note explaining why this article matters to ALJ |
| Used in report | Yes / No |
| Related section / bullet | If used: which section or bullet it supports |

**Appendix scope rule:**
The appendix must list every article/source retained for the report,
whether or not that source appears in a final narrative bullet. It is not
limited to cited sources only.

**Generation rule:**
The source appendix should be generated deterministically from the
retrieval package metadata where possible. The agent may write ALJ
relevance notes. Source title, publisher, date, URL, and snippet must
come from retrieval artifacts — not reconstructed or invented.

**Pre-production requirement:**
Before the first pilot run, confirm that the retrieval package carries
the required fields for each retained result:
- title
- publisher / source name
- publication date
- URL
- snippet / blurb
- result_id (for traceability)

If any field is absent from the retrieval artifact, identify the smallest
scoped change needed to preserve it. Submit as a Phase D change packet
before proceeding.

---

## 5. REPORT STRUCTURE

The report follows the alj_china_auto_weekly_v1 template.

---

**ALJ CHINA AUTO WEEKLY BRIEF**
Week Ending: [DATE]
Client: Abdul Latif Jameel / Jameel Motors
Source Basis: Chinese / China-market sources via Baidu

---

### Section 1 — EXECUTIVE TAKE

Three to five China auto-market signals that matter to ALJ this week.

Each bullet answers:
- What happened?
- Why does it matter to ALJ?
- What is the practical implication?

Bullets must be grounded in retrieved Chinese sources. Uncited bullets
are removed by the scrubber before delivery.

---

### Section 2 — OEM / PARTNER WATCH

Developments involving companies and relationships relevant to ALJ:

- Toyota / Lexus in China
- FAW Toyota / GAC Toyota
- BYD
- SAIC / MG
- GAC
- Geely
- Changan / Deepal
- Chery / Omoda / Jaecoo
- Farizon
- Hino / commercial vehicles (where relevant)
- Ford Trucks / other ALJ-relevant commercial vehicle partners (where relevant)

Focus: sales movements, pricing changes, product announcements, China
strategy shifts, and any developments that affect ALJ's OEM relationships
or competitive positioning.

---

### Section 3 — NEV / HYBRID / BATTERY TREND

Weekly developments in:
- Electric vehicles (BEV)
- Plug-in hybrids (PHEV)
- Conventional hybrids (HEV)
- Battery cost and chemistry
- Charging infrastructure
- Smart-driving / ADAS
- Software-defined vehicles
- NEV pricing and subsidy shifts

Focus: developments that could affect ALJ's product mix decisions,
aftersales readiness for NEV platforms, and customer conversations
about electrification.

---

### Section 4 — EXPORT & GULF RELEVANCE

Weekly developments in:
- Chinese OEM export strategy
- Saudi Arabia / GCC implications
- MENA and Africa distribution signals
- Product categories likely to affect ALJ's markets
- Chinese automaker competition in ALJ-relevant territories
- Tariff, logistics, localization, and market-entry signals

Focus: Chinese OEM activity in ALJ's core operating markets and
competitive threats to ALJ's distribution position.

---

### Section 5 — DEALER / DISTRIBUTOR IMPLICATIONS

Weekly signals in:
- Pricing pressure and discounting behavior
- Inventory risk
- Warranty and parts availability
- Technician training and service readiness for NEV
- Battery service economics
- Residual values
- Customer education and showroom implications
- Brand-positioning pressures

Focus: China dealer-channel dynamics that may preview conditions ALJ
faces in its own distribution network.

---

### Section 6 — COMMUNICATIONS / REPUTATION ANGLE

What ALJ may need to explain or prepare for in conversations with:
- OEM partners
- Customers
- Regulators
- Media
- Internal leadership
- Dealer teams
- Fleet customers

Focus: reputational, messaging, or relationship-management implications
of this week's China auto developments.

---

### Section 7 — ACTION NOTES FOR ALJ

One to three practical recommendations for ALJ this week.

Examples:
- Brief regional leadership on a China pricing trend.
- Ask OEM partner about export allocation or model timing.
- Monitor a Chinese competitor's Gulf expansion.
- Prepare talking points on hybrid versus EV adoption in Saudi market.
- Review aftersales readiness for Chinese NEV platforms.
- Compare Chinese domestic pricing moves against regional price strategy.

Action notes must be specific and grounded in the week's intelligence.
Generic recommendations should be removed or replaced.

---

### Section 8 — COMPLETE CHINESE SOURCE APPENDIX

Mandatory. Present at the bottom of every report.

Format (per Section 4 of this document):

    [1] Chinese Title:
        English Title:
        Publisher:
        Date:
        URL:
        Blurb:
        Relevance to ALJ:
        Used in Report:
        Related Section:

    [2] Chinese Title:
        ...

All retained sources listed. No URL omissions. No international sources
in the initial version.

---

## 6. RETRIEVAL AND QUERY DESIGN

Query template set: alj_china_auto_weekly_v1
(See: SYS_Retrieval_Query_Templates_alj_china_auto_weekly_v1.md)

7 Baidu queries across 5 topic groups:
- auto_market_p1 (7 days)
- oem_watch_p1 (7 days)
- oem_watch_c1 (30 days — context)
- export_gulf_p1 (7 days)
- export_gulf_c1 (30 days — context)
- dealer_economics_p1 (7 days)
- policy_p1 (7 days)

Queries are designed for topic-based retrieval, not regional retrieval.
Source filtering to Chinese / China-market sources applies post-retrieval
per source_filter: chinese_only in client config.

---

## 7. IMPLEMENTATION DEPENDENCIES

Before the first pilot run, the following must be confirmed or resolved:

### 7.1 Baidu-only retrieval path

Confirm whether brave_enabled: false can be handled by config alone, or
whether the retrieval orchestrator requires a scoped implementation change
to skip Brave execution for this client.

If a code change is required, it must be submitted as a Phase D change
packet for operator approval before any pilot run.

### 7.2 Source appendix field availability

Confirm that the retrieval package carries all required appendix fields
for each retained result:
- title
- publisher / source name
- date
- URL
- snippet / blurb
- result_id

If any field is missing, identify the smallest change needed and submit
as a Phase D change packet.

### 7.3 New config fields

The following fields in client_config_alj_china_auto_001.yaml are not
in the current Phase B approved schema:
- brave_enabled
- source_filter (chinese_only, source_region, source_language)
- lookback_days
- context_days
- require_complete_source_appendix

These fields are noted in the config file. Their effect depends on
whether the config loader and pipeline components read them. Where a
field has no current consumer, it is a declared intent — it will require
a Phase D change packet to wire up.

---

## 8. SCORING AND QUALITY CRITERIA

Reports are scored on the following dimensions:

| # | Dimension |
|---|-----------|
| 1 | Client relevance to ALJ |
| 2 | China auto-market specificity |
| 3 | Use of Chinese / China-market sources |
| 4 | OEM / partner relevance |
| 5 | NEV / hybrid / battery insight |
| 6 | Export / Saudi / GCC relevance |
| 7 | Dealer / distributor usefulness |
| 8 | Actionability |
| 9 | Source authority (tier quality) |
| 10 | Evidence density |
| 11 | Translation clarity |
| 12 | Executive readability |
| 13 | Complete source appendix present |
| 14 | All retained source URLs included |
| 15 | Source blurbs / snippets useful and readable |
| 16 | ALJ relevance note included for each source |

A report is not considered successful merely because it is accurate. It
is successful only if it helps ALJ think or act more effectively and
provides a transparent, complete source trail.

---

## 9. APPENDIX COMPLETENESS GATE

For this product, the following constitute delivery-quality judgements:

**FAIL:**
- No Complete Chinese Source Appendix
- URLs missing from appendix
- Appendix includes only publisher/date labels — no links
- Appendix omits retained sources
- Appendix includes sources not present in retrieval artifacts
- Appendix contains invented or reconstructed URLs
- Appendix does not include blurbs / snippets

**WARN:**
- Some translated titles are rough but usable
- Some relevance notes are generic but not misleading
- Source tier classification absent in early pilot versions
- A retained source has weak blurb quality due to thin retrieval snippet,
  but URL / title / publisher / date are present

**PASS:**
- Every retained source is listed
- Every source has title, publisher, date, URL, blurb/snippet, and
  ALJ relevance note
- Used / not-used status is clear for every entry
- Narrative bullets can be traced back to listed sources
- No international sources appear in the initial version

---

## 10. GUARDRAILS

The following guardrails apply throughout Phase D:

1. No change to china_monitor_001.
2. No global disabling of Brave — Baidu-only applies to alj_china_auto_001 only.
3. pilot_mode: true until operator explicitly approves external delivery.
4. No external delivery during initial buildout.
5. Complete Chinese Source Appendix is mandatory — no exceptions.
6. Source appendix generated from retrieval artifacts — not fabricated by agent.
7. No Browser Retrieval integration into agent input during Phase 1.
8. No retrieval_package modification from article_cache during Phase 1.
9. No changes to validator, scrubber, or delivery gate without separate
   operator-approved change packet.
10. No onboarding of alj_china_auto_001 as a live production client until
    open pre-production issues (#47, #49) are resolved.
11. All product changes reflected in Phase D feedback register, scorecard,
    and proposed document updates.

---

## 11. PRE-PRODUCTION BLOCKERS

The following open issues must be resolved before this product moves from
internal pilot testing to external delivery:

| Issue | Description |
|-------|-------------|
| #47 | Intermediate retrieval artifacts not client-namespaced |
| #49 | run_light_to_lark.sh loader variables not fully exported |
| Typo | OPENCLAW_ARTIFACTNAMESPACE missing underscore — run_light_to_lark.sh lines 190/193 |

These issues do not prevent internal pilot design, product specification,
or manual operator-held test runs. They prevent confident production use
with a second live client.

---

## 12. BROWSER RETRIEVAL COMPATIBILITY

The ALJ brief is designed to be article-cache compatible from day one.

Every retained source should carry a stable result_id, URL, title,
publisher, date, and snippet — enabling future article_cache files to
be mapped cleanly to each source.

Recommended future article cache path (advisory only):
/root/openclaw_phase7/article_cache/article_{result_id}.json

**Phase D / Browser Retrieval Phase 1 (current scope):**
- Baidu retrieval identifies candidate Chinese sources
- Browser retrieval may separately fetch full article text into article_cache
  for research review
- No agent input injection from article_cache
- No retrieval_package modification
- No production dependency

**Browser Retrieval Phase 2 (out of scope — requires separate operator decision):**
- article_cache becomes eligible for controlled enrichment of agent input
- Full article text may support better source appendix and insight generation
- Requires formal change packet and operator approval before any integration

---

## 13. GOVERNANCE SEQUENCE

Operator-approved steps before and during pilot:

| Step | Action | Status |
|------|--------|--------|
| 1 | Operator approval of product concept (ALJ memo) | Pending |
| 2 | Product specification (this document) | APPROVED 2026-05-23 |
| 3 | client_config_alj_china_auto_001.yaml | APPROVED 2026-05-23 |
| 4 | Query template set alj_china_auto_weekly_v1 | APPROVED 2026-05-23 |
| 5 | Confirm Baidu-only implementation path | COMPLETE — CP-006 implemented 2026-05-23 |
| 6 | Confirm source appendix field availability | COMPLETE — CP-006 Appendix confirmed 2026-05-22 |
| 7 | First manual pilot run — internal only | Pending |
| 8 | Score output against ALJ scorecard | Pending |
| 9 | Iterate 2–3 weekly pilot runs via approved change packets | Pending |
| 10 | Operator decision on external delivery | Pending |

---

*OPENCLAW-SPEC-ALJ-CHINA-AUTO-001 | v1.0 | 2026-05-22 | APPROVED 2026-05-23*
*Client: alj_china_auto_001 | Phase D Workstream 2*
*Drafted by: Claude CoWork | No system changes — proposed document only*
*No implementation step may begin until operator explicitly approves this spec.*
