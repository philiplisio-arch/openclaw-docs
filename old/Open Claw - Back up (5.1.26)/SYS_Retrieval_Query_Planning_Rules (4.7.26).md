# RETRIEVAL QUERY PLANNING RULES — PHASE 5.2
OpenClaw Project

---

## PURPOSE

Define how queries are structured, counted, and aligned across providers (Brave + Baidu) before retrieval execution.

This document completes the Retrieval Orchestration Layer design.

No implementation occurs at this stage.

---

## CORE RULE

One run = one query bundle.

The query bundle is created once per run by the orchestrator.

The agent does NOT:
- create queries
- modify queries
- select queries
- influence query structure

All queries are generated BEFORE retrieval.

---

## QUERY BUNDLE STRUCTURE

Each run produces:

- query_bundle_id
- run_id
- region_scope
- queries grouped by region

Each query includes:

- query_id
- query_type (precision | recall)
- logical_query
- provider_queries:
  - Brave
  - Baidu

---

## LOCKED QUERY COUNT (V1)

Regions:
- United States
- Europe
- Middle East

Per region:
- 1 precision query
- 1 recall query

Total:
- 6 queries per run

---

## NO DYNAMIC EXPANSION (V1)

Do NOT:
- add additional queries during execution
- generate follow-up queries
- retry queries with variations
- branch queries per provider

The query bundle is fixed once created.

---

## QUERY TYPES

### 1. PRECISION QUERY

Purpose:
- high-relevance signal capture
- concrete developments
- structured and targeted

Characteristics:
- region-specific
- China-related
- business / regulatory / financial relevance
- narrower scope

---

### 2. RECALL QUERY

Purpose:
- broaden coverage
- capture missed developments
- improve diversity of sources

Characteristics:
- region-specific
- China-related
- slightly broader scope
- lower precision, higher recall

---

## REGION STRUCTURE

Each region must have:

- 1 precision query
- 1 recall query

Regions:

### United States
Focus:
- regulation
- trade
- export controls
- finance
- corporate exposure to China

### Europe
Focus:
- trade
- industrial policy
- regulation
- market access
- EU-China business dynamics

### Middle East
Focus:
- investment
- energy
- finance
- bilateral China relations

---

## LOGICAL QUERY VS PROVIDER QUERY

Each query has:

1. Logical Query (master definition)
2. Provider-specific queries:
   - Brave version
   - Baidu version

Flow:

Logical Query
→ Brave Query
→ Baidu Query

---

## PROVIDER ADAPTATION RULES

### Brave
- English-oriented
- more structured phrasing

### Baidu
- may use Chinese language
- simplified structure if needed

---

## HARD RULE

Provider queries may differ in syntax or language  
BUT MUST NOT differ in:

- topic
- region
- time window
- business relevance intent

---

## TIME WINDOW RULE

Default:
- past 7 days

This must be consistent across:
- all regions
- all queries
- both providers

---

## QUERY NAMING CONVENTION

Format:

- us_p1
- us_r1
- eu_p1
- eu_r1
- me_p1
- me_r1

Where:
- us / eu / me = region
- p / r = precision / recall
- 1 = query index

---

## QUERY CONTENT REQUIREMENTS

Each query must include:

- region scope
- China relevance
- business/commercial relevance
- freshness window

---

## QUERY QUALITY RULE

Queries must be:

- not too broad (avoids noise)
- not too narrow (avoids empty results)
- commercially relevant
- consistent across runs

---

## CONSTRAINTS (LOCKED)

1. Bounded volume:
   - exactly 6 queries

2. No agent involvement:
   - agent does not generate or modify queries

3. Provider alignment:
   - Brave and Baidu share same logical intent

4. No mutation:
   - queries do not change mid-run

5. No source biasing:
   - avoid hardcoding publisher names in queries

---

## QUERY PLANNING WORKFLOW

1. Define run scope
2. Define region list
3. Create precision query per region
4. Create recall query per region
5. Generate Brave versions
6. Generate Baidu versions
7. Assign query_ids
8. Freeze query bundle
9. Pass to retrieval execution

---

## SUCCESS CRITERIA

A valid query plan must be:

- bounded
- region-aligned
- commercially relevant
- provider-consistent
- traceable
- stable across runs

---

## WHAT NOT TO DO

Do NOT:

- let agent generate queries
- dynamically expand queries
- give different topics to Brave vs Baidu
- over-specialize one region
- use freeform prompt-based retrieval
- change query count without architecture update

---

## FINAL LOCKED RULESET

- 1 query bundle per run
- 3 regions
- 2 queries per region
- 1 precision + 1 recall
- 6 total queries
- shared logical query across providers
- provider-specific syntax allowed
- no dynamic expansion
- no agent involvement
- fixed 7-day time window

---

## FINAL PRINCIPLE

Query design defines retrieval quality.

Retrieval quality defines system intelligence.

Therefore:

Query planning must be:
- controlled
- consistent
- explicit
- and fully external to the agent

---

END