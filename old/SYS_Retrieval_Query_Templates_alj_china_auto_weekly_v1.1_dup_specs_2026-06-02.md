# RETRIEVAL QUERY TEMPLATES — ALJ CHINA AUTO WEEKLY BRIEF
OpenClaw Project

---
document_id: OPENCLAW-RQT-002
version: v1.1
status: APPROVED — operator approved 2026-06-02; supersedes v1.0; pending Claude Code deployment
client: alj_china_auto_001
created: 2026-05-22
proposed: 2026-06-02
prior_version: v1.0 (approved 2026-05-23)
---

## PURPOSE

Define the exact query templates used by the Retrieval Orchestrator for the
ALJ China Auto Weekly Brief (client_id: alj_china_auto_001).

These templates are Baidu-only. Brave retrieval is disabled for this client
profile (brave_enabled: false in client_config_alj_china_auto_001.yaml).

---

## RATIONALE FOR v1.1

First pilot run (2026-06-01) confirmed a retrieval quality problem: the v1.0
query bundle surfaced CCTV TV video pages and generic EU-China trade / Middle
East energy news rather than China auto-market content. Sections 2 (OEM Watch),
3 (NEV/Battery), and 5 (Dealer/Distributor) were empty. Only 3 unique result_ids
were used across the entire brief.

Root cause: v1.0 Baidu query wording was broad enough for Baidu's algorithm to
prioritise high-volume general news pages ahead of automotive press and industry
data. Query terms like 市场, 出口, 中东, and 商务部 are returning economic and
trade news, not automotive sector content.

v1.1 changes:
1. auto_market_p1 — add 乘联会 / 中汽协 as industry association anchors
2. oem_watch_p1 — add 市场份额 and 汽车市场 to pull automotive market data
3. export_gulf_p1 — replace 中东 with 沙特阿拉伯; add 新能源汽车 for NEV
   export specificity
4. export_gulf_c1 — add 车企 and 海外布局 to pull OEM strategic content
5. dealer_economics_p1 — add 经销商协会 as industry association anchor
6. policy_p1 — remove 商务部 as primary anchor (too broad; pulls general
   trade news); add 乘用车 for passenger vehicle specificity

No queries are added or removed. Structure remains 7 queries across 5 groups.

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
- v1.1 change note

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

v1.1 change note:
Replaced 市场 价格 with 乘联会 中汽协 as specificity anchors. These are
industry body names (not publisher names) and are permitted per Rule 4.

---

# GROUP 2 — OEM / PARTNER WATCH

---

## 2. oem_watch_p1

query_id: oem_watch_p1
topic_group: OEM / partner watch
query_type: precision
time_window: past 7 days

logical_query:
Developments in the past 7 days involving Toyota, Lexus, and major Chinese
OEMs relevant to ALJ — including sales volumes, market share, product launches,
pricing, and strategic moves by BYD, Geely, Changan, SAIC, GAC, and Chery.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
丰田 比亚迪 吉利 长安 汽车市场 销量 市场份额 本周

purpose:
Captures weekly OEM and partner developments relevant to ALJ's Toyota/Lexus
relationship and competitive positioning against Chinese OEMs. Adding 汽车市场
and 市场份额 increases the likelihood of pulling automotive market data platforms
(e.g. Dongchedi, Yiche, Gasgoo) over general news pages.

v1.1 change note:
Removed 新能源汽车 (has dedicated NEV query) and 出口 (has dedicated export
query). Added 汽车市场 and 市场份额 to anchor on automotive market data.

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

v1.1 change note:
Unchanged from v1.0. 中东 retained here as context signal for OEM overseas
strategy (distinct from the export_gulf queries where it was pulling conflict
news ahead of auto content).

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

v1.1 change note:
Replaced 中东 with 沙特阿拉伯 (Saudi Arabia specifically) to reduce retrieval
of Middle East conflict/energy news. Added 新能源汽车 and 车企 to anchor on
automotive export content rather than general trade news.

---

## 5. export_gulf_c1

query_id: export_gulf_c1
topic_group: Export / Saudi / GCC relevance
query_type: context
time_window: past 30 days

logical_query:
Chinese automotive export strategy and Middle East / Africa market
positioning over the past 30 days — for background context on sustained
competitive trends in ALJ's territories.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
中国 汽车 出口 海湾 车企 海外布局 中东 过去一个月

purpose:
30-day context for sustained Chinese OEM export trends into MENA and Africa.
Used only when a multi-week pattern is needed to explain the week's signal.

v1.1 change note:
Added 车企 (automaker) and 海外布局 (overseas market positioning) to pull
automotive-specific strategic content. 中东 retained for geographic context
at 30-day window where it is less likely to dominate with short-term
conflict/energy noise.

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

v1.1 change note:
Added 经销商协会 as industry association anchor. Replaced 利润 (profit) with
经营 (operations — broader term that captures more dealer-channel content).
Removed 新能源 (covered adequately in other queries).

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
MIIT product standards, and MOFCOM commercial vehicle or distribution rules
relevant to a multinational automotive distributor.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
工信部 新能源汽车 政策 补贴 乘用车 汽车行业 本周

purpose:
Captures official policy signals from Chinese regulatory bodies that affect
NEV adoption, export volumes, and market conditions relevant to ALJ's
OEM relationships and distribution strategy.

v1.1 change note:
Removed 商务部 as primary anchor — MOFCOM is too broad and was pulling
general trade/tariff news (EU steel, US-China agriculture) ahead of auto
sector policy. 工信部 (MIIT) is automotive-specific and retained as primary
anchor. Added 乘用车 (passenger vehicle) and 汽车行业 for sector specificity.
出口 removed (covered in export queries).

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
- Equivalent Baidu wording: 过去一个月, 本月
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

Industry association names (乘联会, 中汽协, 经销商协会, 工信部) are
permitted — they are official bodies, not publishers, and function as
topical signal anchors rather than source bias.

Source selection belongs to retrieval and filtering, not query bias.

---

### 5. NO DYNAMIC EXPANSION IN V1.1
These 7 queries are the entire query bundle.

Do NOT:
- add query variants mid-run
- retry with expanded wording
- add extras for specific OEM names
- create subqueries inside the agent

Query refinement after the second and third pilot runs should follow the
same approval process: new version submitted for operator approval.

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

## V1.1 SUCCESS STANDARD

These templates are successful if the next pilot run produces:
- At least 2 of Sections 2, 3, 5 with substantive content (not empty/thin)
- At least 5 distinct result_ids across the brief
- At least 1 Tier 1–3 automotive source (CAAM, CPCA, Gasgoo, Yicai Auto,
  36Kr, Sina Auto, Dongchedi, or equivalent)
- No tv.cctv.com / tv.cctv.cn URLs as primary cited sources
- Reduced source concentration (no single result_id accounting for >50%
  of citations)

---

## REFINEMENT SCHEDULE

After the second and third pilot runs, review:
- Whether additional OEM-specific queries (e.g. dedicated Toyota/Lexus
  precision query) are warranted given retrieval results
- Whether 乘联会 / 中汽协 anchors are consistently pulling CPCA/CAAM
  data or need further adjustment
- Whether a dedicated Farizon / commercial vehicle query is warranted
- Whether 沙特阿拉伯 in export_gulf_p1 is narrowing retrieval too much
  (if Gulf content is thin, revert to broader 中东 with 汽车 anchor)

Any changes require a new version submitted for operator approval.

---

END

*OPENCLAW-RQT-002 | v1.1 | 2026-06-02 | APPROVED — operator approved 2026-06-02*
*Client: alj_china_auto_001 | Baidu-only | Weekly cadence*
*Drafted by: Claude CoWork*
*Prior version: v1.0 approved 2026-05-23 — superseded*
*Claude Code to deploy to VPS; confirm py_compile / bash -n exit 0 before next pilot run.*
