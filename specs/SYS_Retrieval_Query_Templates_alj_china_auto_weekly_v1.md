# RETRIEVAL QUERY TEMPLATES — ALJ CHINA AUTO WEEKLY BRIEF
OpenClaw Project

---
document_id: OPENCLAW-RQT-002
version: v1.0
status: PROPOSED — awaiting operator approval
client: alj_china_auto_001
created: 2026-05-22
---

## PURPOSE

Define the exact query templates used by the Retrieval Orchestrator for the
ALJ China Auto Weekly Brief (client_id: alj_china_auto_001).

These templates are Baidu-only. Brave retrieval is disabled for this client
profile (brave_enabled: false in client_config_alj_china_auto_001.yaml).

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
multinational automotive distributor.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
中国 汽车 市场 本周 新能源汽车 销量 价格

purpose:
Core weekly signal capture — China auto market conditions, NEV sales volumes,
and pricing developments over the past 7 days.

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
OEMs relevant to ALJ — including sales, product launches, pricing, and
strategic moves by BYD, Geely, Changan, SAIC, GAC, and Chery.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
丰田 中国 新能源汽车 比亚迪 吉利 长安 销量 出口 本周

purpose:
Captures weekly OEM and partner developments relevant to ALJ's Toyota/Lexus
relationship and competitive positioning against Chinese OEMs.

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
relevance to Saudi Arabia, the GCC, or MENA — including export volumes,
competitive moves by Chinese OEMs in Gulf markets, and logistics or
market-entry signals.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
中国 汽车 出口 沙特 中东 海湾 本周

purpose:
Primary signal for Chinese OEM activity in ALJ's core operating markets.
Captures export strategy, Gulf-market competition, and MENA distribution
developments directly relevant to ALJ's business.

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
中国 汽车 出口 中东 非洲 市场 战略 过去一个月

purpose:
30-day context for sustained Chinese OEM export trends into MENA and Africa.
Used only when a multi-week pattern is needed to explain the week's signal.

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
中国 汽车 经销商 库存 利润 降价 售后 新能源 本周

purpose:
Captures dealer-channel stress signals from China that may preview conditions
ALJ faces in its own distribution network — pricing pressure, inventory risk,
aftersales readiness for NEV platforms, and margin dynamics.

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
export policy, MIIT product standards, and MOFCOM commercial vehicle or
distribution rules relevant to a multinational automotive distributor.

Brave_template:
N/A — Brave disabled for this client profile.

Baidu_template:
工信部 商务部 新能源汽车 政策 补贴 出口 汽车 本周

purpose:
Captures official policy signals from Chinese regulatory bodies that affect
NEV adoption, export volumes, and market conditions relevant to ALJ's
OEM relationships and distribution strategy.

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

Source selection belongs to retrieval and filtering, not query bias.

---

### 5. NO DYNAMIC EXPANSION IN V1
These 7 queries are the entire query bundle for v1.

Do NOT:
- add query variants mid-run
- retry with expanded wording
- add extras for specific OEM names
- create subqueries inside the agent

Query refinement is permitted after the first 2–3 pilot runs through a
formal template update submitted for operator approval.

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

## V1 SUCCESS STANDARD

These templates are successful if they produce retrieval that is:

- bounded to Chinese / China-market auto-sector sources
- commercially relevant to ALJ's distribution and OEM context
- topic-aligned across all 5 groups
- stable across repeated weekly runs
- suitable for source appendix traceability
- refined and improved after the first 2–3 pilot runs

---

## REFINEMENT SCHEDULE

v1 is a starting point. After the first 2–3 pilot runs, the following
should be reviewed for operator-approved update:

- Whether 7 queries are sufficient or whether specific OEM groups warrant
  separate precision queries
- Whether the 30-day context queries are returning useful background or
  duplicating precision results
- Whether Baidu query wording needs tuning based on actual retrieval output
- Whether a dedicated Farizon / commercial vehicle query is warranted

Any changes to this template require a new version submitted for operator
approval before deployment.

---

END

*OPENCLAW-RQT-002 | v1.0 | 2026-05-22 | PROPOSED — operator approval required*
*Client: alj_china_auto_001 | Baidu-only | Weekly cadence*
*Drafted by: Claude CoWork | No system changes — proposed document only*
