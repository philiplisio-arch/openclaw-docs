# RETRIEVAL QUERY TEMPLATES — ALJ CHINA AUTO WEEKLY BRIEF
OpenClaw Project

---
document_id: OPENCLAW-RQT-002
version: v1.2
status: APPROVED — operator approved 2026-06-04; supersedes v1.1; pending Claude Code deployment
client: alj_china_auto_001
created: 2026-05-22
proposed: 2026-06-04
prior_version: v1.1 (approved 2026-06-02)
---

## PURPOSE

Define the exact query templates used by the Retrieval Orchestrator for the
ALJ China Auto Weekly Brief (client_id: alj_china_auto_001).

These templates are Baidu-only. Brave retrieval is disabled for this client
profile (brave_enabled: false in client_config_alj_china_auto_001.yaml).

---

## RATIONALE FOR v1.2

Pilot Run 4 (2026-06-04) confirmed 3 of 7 query strings returning zero results
from Baidu despite the CP-026 freshness window fix being active. Root cause:
query strings too restrictive for Baidu's index.

- oem_watch_p1: stacked 4 OEM names (丰田/比亚迪/吉利/长安) plus market terms —
  combination too restrictive; no results returned
- export_gulf_c1: heavy overlap with export_gulf_p1; 过去一个月 framing not
  matching Baidu index well; zero results
- policy_p1: 工信部 anchor too narrow; no MIIT policy news this week passed;
  zero results

v1.2 changes (3 query strings only; all other queries unchanged):
1. oem_watch_p1 — replace 4-OEM stack with umbrella term 中国车企; add 市场竞争
   for competitive framing; retain 新能源 and 本周
2. export_gulf_c1 — replace overlap query with brand-presence angle; specific
   OEM names (比亚迪/吉利/奇瑞) used as subject not filter; 经销商/合作 to pull
   Gulf distribution/partnership news; 近期 replaces 过去一个月
3. policy_p1 — remove 工信部 anchor; broaden to 行业规范 监管 to capture
   policy/regulatory layer without requiring specific ministry activity

No queries added or removed. Structure remains 7 queries across 5 groups.

---

## CORE RULE

Each weekly run uses one fixed query bundle.

Topic groups:
- China auto market — weekly trend
- OEM / partner watch
- Export / Saudi / GCC relevance
- Dealer / distributor economics
- Policy / regulation

Per group:
- 1 precision query (primary lookback: past 7 days)
- 1 context query for strategic groups only (context window: past 30 days)

Total:
- 7 queries per run

All queries must reflect:
- China auto-market relevance
- ALJ business relevance (distribution, OEM relationships, Saudi/GCC exposure)
- Baidu-only retrieval (no Brave templates)
- Time windows by query type:
  - Precision queries: past 7 days (Baidu: query-text time signal)
  - Context queries: past 30 days (Baidu: query-text time signal; major
    strategic developments only)

---

## QUERY TEMPLATE STRUCTURE

Each query slot contains:

- query_id
- topic_group
- query_type
- logical_query
- Brave_template
- Baidu_template
- purpose
- version change note

---

# GROUP 1 — CHINA AUTO MARKET WEEKLY TREND

---

## 1. auto_market_p1

query_id: auto_market_p1
topic_group: China auto market — weekly trend
query_type: precision
time_window: past 7 days

logical_query:
China auto market developments in the past 7 days — sales volumes, new energy
vehicle trends, pricing movements, and market conditions relevant to a
multinational automotive distributor. Prioritise industry association data
(CPCA/乘联会, CAAM/中汽协) and automotive press over general economic news.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
中国 汽车 销量 新能源汽车 本周 乘联会 中汽协

purpose:
Core weekly signal capture — China auto market conditions, NEV sales volumes,
and pricing developments over the past 7 days. Industry association anchors
(乘联会/CPCA, 中汽协/CAAM) pull Baidu toward automotive data sources rather
than generic economic news.

v1.2 change note:
Unchanged from v1.1.

---

# GROUP 2 — OEM / PARTNER WATCH

---

## 2. oem_watch_p1

query_id: oem_watch_p1
topic_group: OEM / partner watch
query_type: precision
time_window: past 7 days

logical_query:
Developments in the past 7 days involving Chinese OEMs relevant to ALJ —
including sales volumes, market share, competitive dynamics, product launches,
and pricing. Focus on the broader competitive landscape facing a multinational
distributor with Toyota/Lexus relationships.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
中国车企 新能源 销量 市场竞争 品牌 本周

purpose:
Captures weekly OEM competitive dynamics relevant to ALJ's positioning.
Using 中国车企 (Chinese automakers) as umbrella term instead of stacking
individual OEM names reduces query restrictiveness while retaining automotive
relevance. 市场竞争 pulls competitive framing; 品牌 anchors on brand-level
coverage.

v1.2 change note:
Replaced 丰田 比亚迪 吉利 长安 汽车市场 销量 市场份额 with 中国车企 新能源
销量 市场竞争 品牌. Prior query stacked 4 OEM names producing zero results —
too restrictive for Baidu's index. Umbrella term approach consistent with
how Chinese automotive press frames OEM competitive coverage.

---

## 3. oem_watch_c1

query_id: oem_watch_c1
topic_group: OEM / partner watch
query_type: context
time_window: past 30 days

logical_query:
Strategic developments in the past 30 days involving Toyota China and major
Chinese OEM overseas expansion — for background context on recurring trends
and major strategic shifts.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
丰田 中国 战略 中国车企 海外扩张 中东 过去一个月

purpose:
30-day context window for OEM strategic developments. Used only for major
recurring trends or background necessary to explain the week's signal.
Not to be treated as primary weekly signal.

v1.2 change note:
Unchanged from v1.1. This query returned 1 result in Pilot Run 4 — working.

---

# GROUP 3 — EXPORT / SAUDI / GCC RELEVANCE

---

## 4. export_gulf_p1

query_id: export_gulf_p1
topic_group: Export / Saudi / GCC relevance
query_type: precision
time_window: past 7 days

logical_query:
Chinese automotive export developments in the past 7 days with direct
relevance to Saudi Arabia, the GCC, or MENA — including NEV export volumes,
competitive moves by Chinese OEMs in Gulf markets, and logistics or
market-entry signals.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
中国 新能源汽车 出口 沙特阿拉伯 海湾 车企 本周

purpose:
Primary signal for Chinese OEM activity in ALJ's core operating markets.
Captures export strategy, Gulf-market competition, and MENA distribution
developments directly relevant to ALJ's business.

v1.2 change note:
Unchanged from v1.1. This query returned 2 results in Pilot Run 4 — working.

---

## 5. export_gulf_c1

query_id: export_gulf_c1
topic_group: Export / Saudi / GCC relevance
query_type: context
time_window: past 30 days

logical_query:
Chinese OEM brand establishment, dealership partnerships, and market presence
in the Middle East and Gulf over the past 30 days — for background context
on sustained competitive positioning in ALJ's territories.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
比亚迪 吉利 奇瑞 中东 经销商 合作 海外布局 近期

purpose:
30-day context for Chinese OEM distribution and brand-presence activity in
MENA. Focuses on dealership/partnership angles (经销商/合作) rather than
export volumes (covered by export_gulf_p1). Specific OEM names (比亚迪/吉利/
奇瑞) used as subject anchors to pull brand-specific Gulf activity.

v1.2 change note:
Replaced 中国 汽车 出口 海湾 车企 海外布局 中东 过去一个月 — prior query
overlapped heavily with export_gulf_p1 and returned zero results. New query
differentiates by focusing on brand presence/distribution partnerships.
近期 replaces 过去一个月 for better Baidu index matching at the 30-day window.

---

# GROUP 4 — DEALER / DISTRIBUTOR ECONOMICS

---

## 6. dealer_economics_p1

query_id: dealer_economics_p1
topic_group: Dealer / distributor economics
query_type: precision
time_window: past 7 days

logical_query:
Chinese auto dealer and distributor conditions in the past 7 days — inventory
pressures, profitability, discounting behavior, aftersales economics, and
NEV-specific service and battery issues relevant to a distributor operating
in Saudi Arabia and the GCC.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
中国 汽车 经销商 库存 降价 售后 经营 经销商协会 本周

purpose:
Captures dealer-channel stress signals from China that may preview conditions
ALJ faces in its own distribution network — pricing pressure, inventory risk,
aftersales readiness for NEV platforms, and margin dynamics. 经销商协会
(dealer association) anchors retrieval toward industry association data.

v1.2 change note:
Unchanged from v1.1. This query returned 3 results in Pilot Run 4 — working.

---

# GROUP 5 — POLICY / REGULATION

---

## 7. policy_p1

query_id: policy_p1
topic_group: Policy / regulation
query_type: precision
time_window: past 7 days

logical_query:
Chinese government policy and regulatory developments in the past 7 days
affecting the automotive sector — including NEV subsidies, trade-in incentives,
product standards, and distribution rules relevant to a multinational
automotive distributor.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
新能源汽车 政策 补贴 行业规范 监管 本周

purpose:
Captures policy and regulatory signals affecting NEV adoption, market
conditions, and distributor compliance requirements. Broadened beyond MIIT
(工信部) to capture the full policy/regulatory layer regardless of which
ministry or body is active in a given week.

v1.2 change note:
Replaced 工信部 新能源汽车 政策 补贴 乘用车 汽车行业 with 新能源汽车 政策
补贴 行业规范 监管. Prior query anchored on 工信部 specifically — returned
zero results when no MIIT news was available. 行业规范 监管 broadens to
industry standards and regulatory activity across all relevant bodies.
乘用车 汽车行业 removed as redundant given 新能源汽车 anchor.

---

## TEMPLATE DESIGN RULES

### 1. BAIDU-ONLY FOR THIS CLIENT PROFILE
Brave retrieval is disabled (brave_enabled: false in client config).
All Brave_template fields are marked N/A.
If Brave is re-enabled for this client in a future change packet, all
Brave_template fields must be populated before deployment.

---

### 2. TOPIC-BASED STRUCTURE (NOT REGIONAL)
This template replaces the regional structure (US/EU/ME) of china_monitor_v1
with a topic-group structure specific to the ALJ auto-market brief.
Topic groups map to ALJ's core intelligence requirements, not geographic
retrieval buckets.

---

### 3. TIME WINDOWS BY QUERY TYPE

Precision queries:
- Window: past 7 days
- Equivalent Baidu wording: 本周, 过去一周, 过去7天

Context queries:
- Window: past 30 days
- Equivalent Baidu wording: 过去一个月, 本月, 近期
- For major strategic developments and background context only.
- Context query results must not displace precision query results as
  primary weekly signal.

---

### 4. NO SOURCE BIASING
Do NOT include publisher names in query templates.

Do NOT hardcode:
- Gasgoo / 盖世汽车
- Yiche / 易车
- Dongchedi / 懂车帝
- Sina Auto / 新浪汽车
- 36Kr Auto / 36氪
- LatePost / 晚点
- Caixin / 财新
- or any other named publication

Industry association names (乘联会, 中汽协, 经销商协会) are permitted — they
are official bodies, not publishers, and function as topical signal anchors
rather than source bias.

---

### 5. NO DYNAMIC EXPANSION IN V1.2
These 7 queries are the entire query bundle.

Do NOT:
- add query variants mid-run
- retry with expanded wording
- add extras for specific OEM names
- create subqueries inside the agent

Query refinement after pilot runs should follow the same approval process:
new version submitted for operator approval.

---

### 6. ALJ RELEVANCE DISCIPLINE
Each query must remain focused on developments that could affect ALJ's
distribution strategy, OEM relationships, NEV positioning, Saudi/GCC
competitive positioning, dealer economics, or client communications.

Avoid:
- general China auto news without distributor relevance
- domestic China consumer trends without export or OEM implication
- technology content without commercial or distributor relevance
- forcing non-automotive content into auto-market queries

---

## EXECUTION ORDER

Recommended orchestrator order:

1. Build full query bundle (7 queries)
2. Assign query IDs
3. Generate Baidu query strings
4. Freeze bundle
5. Execute Baidu retrieval
6. Filter retained results to Chinese / China-market sources only
   (source_filter: chinese_only per client config)

---

## TRACEABILITY RULE

Every retained result must be traceable back to:
- query_bundle_id
- query_id
- Baidu query string
- retrieval provider (Baidu)

This is mandatory for the Complete Chinese Source Appendix — result_ids
and query_ids from this bundle are the source trail for the appendix.

---

## V1.2 SUCCESS STANDARD

These templates are successful if the next pilot run produces:
- All 5 query families returning at least 1 result
- At least 12 distinct result_ids in the retrieval package
- At least 3 of Sections 1–7 with substantive, distinct content
- No single result_id accounting for >40% of citations
- T-04 compliant output

---

## REFINEMENT SCHEDULE

After the next two pilot runs, review:
- Whether oem_watch_p1 umbrella term (中国车企) is pulling specific OEM
  competitive data or remaining too generic
- Whether export_gulf_c1 brand-presence angle (比亚迪/吉利/奇瑞 经销商) is
  returning Gulf-specific distribution content
- Whether policy_p1 broadened framing is surfacing genuine policy signal
  or generic regulatory noise
- Whether a dedicated Toyota/Lexus precision query is warranted

Any changes require a new version submitted for operator approval.

---

END

*OPENCLAW-RQT-002 | v1.2 | 2026-06-04 | APPROVED — operator approved 2026-06-04*
*Client: alj_china_auto_001 | Baidu-only | Weekly cadence*
*Drafted by: Claude CoWork*
*Prior version: v1.1 approved 2026-06-02 — superseded*
*Claude Code to deploy to VPS; confirm py_compile exit 0 before next pilot run.*
