# RETRIEVAL QUERY TEMPLATES
OpenClaw Project

---
document_id: OPENCLAW-RQT-001
version: v5.0
status: ACTIVE — wired into live pipeline
---

## PURPOSE

Define the exact query templates used by the Retrieval Orchestrator for Brave and Baidu.

These templates are the live query bundle used in production.

---

## CORE RULE

Each run uses one fixed query bundle.

Regions:
- United States
- Europe
- Middle East

Per region:
- 1 precision query
- 1 recall query

Total:
- 6 queries per run

All queries must reflect:
- China relevance
- region relevance
- business / regulatory / commercial relevance
- Freshness windows by query type:
  - Precision queries: today / past 24 hours (Brave: freshness=pd; Baidu: query-text)
  - Recall queries: past 7 days (Brave: freshness=pw; Baidu: query-text)

---

## QUERY TEMPLATE STRUCTURE

Each query slot contains:

- query_id
- region
- query_type
- logical_query
- Brave_template
- Baidu_template
- purpose

---

# UNITED STATES

---

## 1. us_p1

query_id: us_p1
region: United States
query_type: precision
time_window: today / past 24 hours

logical_query:
China-related business, regulatory, financial, or geopolitical developments today or in the past 24 hours that materially affect U.S. companies, U.S.-China commercial relations, or multinational operating conditions.

Brave_template:
China developments affecting U.S. companies regulation trade export controls finance today

Baidu_template:
今天 中国 影响 美国企业 贸易 监管 出口管制 金融 动态

purpose:
High-precision capture of fresh commercially relevant China developments tied to the United States.

---

## 2. us_r1

query_id: us_r1
region: United States
query_type: recall

logical_query:
Recent China-United States developments in the past 7 days with potential business, market, or regulatory significance.

Brave_template:
China U.S. business developments past week

Baidu_template:
过去一周 中美 商业 动态

purpose:
Broader recall layer for U.S.-linked developments that may be missed by the precision query.

---

# EUROPE

---

## 3. eu_p1

query_id: eu_p1
region: Europe
query_type: precision
time_window: today / past 24 hours

logical_query:
China-related business, regulatory, trade, industrial policy, or market access developments today or in the past 24 hours that materially affect European companies or Europe-China commercial relations.

Brave_template:
China developments affecting Europe companies trade regulation industrial policy market access today

Baidu_template:
今天 中国 影响 欧洲企业 贸易 监管 产业政策 市场准入 动态

purpose:
High-precision capture of fresh commercially relevant China developments tied to Europe.

---

## 4. eu_r1

query_id: eu_r1
region: Europe
query_type: recall

logical_query:
Recent China-Europe developments in the past 7 days with potential business, market, or regulatory significance.

Brave_template:
China Europe business developments past week

Baidu_template:
过去一周 中欧 商业 动态

purpose:
Broader recall layer for Europe-linked developments that may be missed by the precision query.

---

# MIDDLE EAST

---

## 5. me_p1

query_id: me_p1
region: Middle East
query_type: precision
time_window: today / past 24 hours

logical_query:
China-related investment, energy, finance, payments, or commercial integration developments today or in the past 24 hours that materially affect Middle East-China business relations or multinational operating conditions.

Brave_template:
China Middle East developments investment energy finance payments business today

Baidu_template:
今天 中国 中东 投资 能源 金融 支付 商业 动态

purpose:
High-precision capture of fresh commercially relevant China developments tied to the Middle East.

---

## 6. me_r1

query_id: me_r1
region: Middle East
query_type: recall

logical_query:
Recent China-Middle East developments in the past 7 days with potential business, market, or regulatory significance.

Brave_template:
China Middle East business developments past week

Baidu_template:
过去一周 中国 中东 商业 动态

purpose:
Broader recall layer for Middle East-linked developments that may be missed by the precision query.

---

## TEMPLATE DESIGN RULES

### 1. SAME LOGICAL INTENT ACROSS PROVIDERS
Brave and Baidu versions must search the same topic intent.

Allowed differences:
- language
- syntax
- wording style

Not allowed to differ:
- region
- time window
- topic intent
- business relevance

---

### 2. TIME WINDOWS BY QUERY TYPE

Precision queries:
- Window: today / past 24 hours
- Equivalent wording: today, 今天
- Brave API enforcement: `freshness=pd` (active as of 2026-05-04)

Recall queries:
- Window: past 7 days
- Equivalent wording: past week, past 7 days, 过去一周, 过去7天
- Brave API enforcement: `freshness=pw` (active as of 2026-05-04)

Time windows must be consistent between Brave and Baidu for the same query type.

Note: As of 2026-05-04, Brave time windows are enforced mechanically via the
`freshness` parameter in brave_executor.py. Query text wording alone is a
ranking hint only — it does not constrain Brave's result date range. Baidu
time windows are query-text only; Baidu retrieval is operational as of Phase 6.4.

---

### 3. NO SOURCE BIASING
Do NOT include publisher names in default query templates.

Do NOT hardcode:
- Reuters
- Bloomberg
- CNBC
- 21世纪经济报道
- 第一财经
- etc.

Source selection belongs to retrieval + filtering, not query bias.

---

### 4. NO DYNAMIC EXPANSION IN V1
These six queries are the entire query bundle.

Do NOT:
- add query variants mid-run
- retry with expanded wording
- add provider-specific extras
- create subqueries inside the agent

---

### 5. REGION DISCIPLINE
Each region query must remain focused on that region’s commercial relevance.

Avoid:
- general geopolitics without business implications
- generic “China news”
- overly narrow company-specific wording
- forcing cross-region material into the wrong bucket

---

## EXECUTION ORDER

Recommended orchestrator order:

1. Build full query bundle
2. Assign query IDs
3. Generate Brave query strings
4. Generate Baidu query strings
5. Freeze bundle
6. Execute both providers in parallel

---

## TRACEABILITY RULE

Every retained result must be traceable back to:
- query_bundle_id
- query_id
- provider query string
- retrieval provider

This is mandatory for debugging, comparison, and future source weighting.

---

## V1 SUCCESS STANDARD

These templates are successful if they produce retrieval that is:

- bounded
- commercially relevant
- region-aligned
- comparable across providers
- stable across repeated runs
- suitable for orchestrator filtering and deduplication

---

## WHAT NOT TO DO

Do NOT:
- let the agent alter these queries
- let Baidu use a different mission than Brave
- inject raw query text into prompts as instructions
- expand the bundle beyond 6 queries without architecture update
- optimize for one provider by breaking cross-provider comparability

---

## FINAL PRINCIPLE

The query templates are the front door of the Retrieval Orchestration Layer.

If query design is sloppy:
- retrieval gets noisy
- normalization gets harder
- conflicts increase
- agent quality drops

If query design is disciplined:
- retrieval stays bounded
- comparison is possible
- orchestration remains stable
- agent reasoning improves

---

END