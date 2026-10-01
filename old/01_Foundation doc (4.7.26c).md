# OpenClaw Foundation Document (Final — v8)

Date: 2026-04-07

---

## 🎯 PURPOSE

This document defines:

1. The current state of the OpenClaw system
2. The operating model for daily use
3. The roadmap for future development

This project is built iteratively by a non-technical operator.

Core principle:

Build one working system → stabilize → layer improvements

---

## 🧭 SYSTEM OBJECTIVE

Build a semi-automated PR intelligence engine that produces:

* daily China-related strategic monitoring
* structured signal extraction
* advisory-level interpretation
* publication-ready content

Primary use case:

Multinational companies operating in or exposed to China

---

# 🔷 SYSTEM ARCHITECTURE (REAL STATE)

System flow:

Trigger
→ Retrieval Layer
→ Retrieval Orchestrator
→ Agent Layer
→ Relay
→ Lark Docx

### Retrieval Layer

* Brave Search API
* Baidu API (Phase 5 integration)
* future China-native sources

### Retrieval Orchestrator (CRITICAL)

* executes retrieval across sources
* normalizes outputs
* deduplicates results
* preserves source traceability
* produces structured input for agent

### Agent Layer

* china_pr_monitor_light → signal generation
* enrichment → advisory transformation

### Relay Layer (Flask)

* /push endpoint
* formats output for Lark

### Lark Docx (Output Layer)

* final storage and review surface
* strict block + formatting requirements

---

# 🔷 PHASE STRUCTURE (LOCKED)

---

# 🔒 PHASE DEFINITIONS — LOCKED (GOVERNING RULES)

---

## 🎯 PHASE 4 — SYSTEM STABILITY & CONTROL

### OBJECTIVE

Build a stable, controllable, and trustworthy system using the current architecture and data sources only.

---

## ✅ PHASE 4 COMPLETION CRITERIA (ALL REQUIRED)

### 1. RUN CONSISTENCY (CRITICAL)

* Multiple runs (≥3) produce:

  * consistent structure
  * consistent depth
  * no degradation pattern
* No “first run strong → later runs weaker”

---

### 2. LOW-SIGNAL INTEGRITY

* When no real developments exist:

  * system outputs:
    “No significant new developments in the past 7 days”
* No forced insights
* No fabricated narratives

---

### 3. EVIDENCE RELIABILITY

* Every bullet / implication:

  * supported by real source
  * includes valid URL
  * correctly mapped
* No hallucinated citations
* No placeholder links

---

### 4. SYSTEM STABILITY

* Cron runs reliably
* No duplicate executions
* Logging is clean and usable
* No manual intervention required

---

### 5. CONTROL LAYER FUNCTIONAL

* Commands operational:

  * RUN_FULL_MONITOR
  * RUN_SIGNAL_ONLY
  * RUN_LINKEDIN_ONLY
* Proper return codes (incl. 429 handling)
* Output consistently delivered to Lark

---

## 🚫 EXPLICITLY OUT OF SCOPE (PHASE 4)

* Baidu API integration
* Sogou / SERPAPI expansion
* GSData or premium data sources
* Multi-provider ranking logic
* New agents or architecture expansion
* Retrieval optimization beyond validation

---

## 🔵 PHASE 5 — SYSTEM EXPANSION & INTELLIGENCE

### OBJECTIVE

Upgrade system capability after stability is achieved.

---

### CURRENT STATUS (UPDATED — SOURCE OF TRUTH)

Phase 5 is ACTIVE.

Current stage:

👉 Phase 5.4 — Production Integration

Reference:

* Execution Plan
* Daily Status
* Issue Log

---

### PHASE 5.1 — CHINA-NATIVE RETRIEVAL EXPANSION

* Baidu API integration
* Optional: Sogou / SERPAPI
* Retrieval comparison vs current stack
* Chinese-language source prioritization improvements

STATUS UPDATE (2026-04-06):

* Baidu retrieval tested via SerpAPI (functional)
* Wrapper-based integration tested (non-invasive)
* Integration into core pipeline deferred pending architecture design

Key Insight:
Direct injection into agent prompt risks system instability

Next Step:
Define structured integration approach before implementation

---

### Retrieval Orchestration Layer (NEW — CRITICAL)

All external retrieval must occur outside the agent.

Architecture:

Retrieval → Orchestrator → Structured Input → Agent

Rules:

* Agents DO NOT call search tools
* Agents DO NOT perform retrieval
* All retrieval is pre-processed and injected as structured data
* Multiple sources (Brave, Baidu, etc.) are combined BEFORE agent execution

Purpose:

* Ensure determinism
* Maintain stability
* Enable multi-source integration without breaking system behavior

---

### PHASE 5.2+

* Source weighting / ranking
* Multi-agent specialization
* Data ingestion (Factiva, GSData, etc.)
* Advisor layer (ChatGPT inside OpenClaw)
* Interface expansion (Discord → WeChat)

---

### PHASE 5.3 — Agent Integration (OFFLINE) — COMPLETE

Status: ✅ COMPLETE (Offline validated)

Architecture achieved:

Query Bundle
→ Retrieval (Brave + Baidu)
→ Normalize
→ Dedup
→ Filter (strict, recent only)
→ Conflict Detection
→ Package Builder
→ Agent Input Builder (slim)
→ Agent (china_pr_enrichment)

Key properties:

* Agent receives ONLY structured JSON package
* No direct retrieval inside agent
* No mixing of signal + context layers
* Output includes:

  * EXECUTIVE TAKE
  * ADVISORY LAYER
  * Evidence tags: [Source: Outlet, YYYY-MM-DD]

Critical breakthrough:

* URL date parsing expanded to include:

  * /YYYY/MM/DD/
  * -YYYY-MM-DD

Impact:

* Signal increased from ~2–3 → ~7 high-quality results
* Enabled consistent multi-region coverage (US / EU / ME)

System now supports:

deterministic retrieval → structured signal → controlled reasoning → advisory output

---

### PHASE 5.4 — PRODUCTION INTEGRATION (ACTIVE)

Objective:

Connect orchestrator pipeline to full system execution layer.

Target flow:

Trigger (cron / webhook)
→ Retrieval Orchestrator
→ Agent
→ Relay
→ Lark / Discord

Success condition:

* One trigger runs full pipeline
* No manual execution required
* Legacy pipeline removed
* System fully automated

---

## 🔴 PHASE 6 — OPERATIONALIZATION & SCALE

### OBJECTIVE

Transform the system into a:

business-operating intelligence platform

---

### CORE FUNCTIONS

* Multi-client deployment
* Client-specific intelligence streams
* Content → business development loop
* Automated communication workflows
* Commercial infrastructure support (tracking, billing, reporting)
* Persistent system memory (client context, historical insight)

---

### STRATEGIC ROLE

Phase 6 converts the system from:

tool → operating engine

---

### ACTIVATION CONDITION

Phase 6 begins only after:

* Phase 4 stability is fully achieved
* Phase 5 intelligence and retrieval layers are operational

---

### KEY PRINCIPLE

Do not scale until system output is consistently reliable and trusted.

---

## ⚠️ NON-NEGOTIABLE RULE

NO new data sources may be introduced until Phase 4 is complete.

(Note: Phase 4 is now complete. Rule remains for historical integrity.)

---

## 🧭 DAILY DECISION RULE

* If task improves stability → Phase 4
* If task adds capability → Phase 5

---

## 🧱 SYSTEM MENTAL MODEL

* Phase 4 = Trust the system
* Phase 5 = Upgrade the system
* Phase 6 = Run the business on the system

---

## Phase 1 — Pipeline Layer

Goal: Reliable execution

* OpenClaw agent → relay → Lark
* cron automation
* stable output delivery

---

## Phase 2 — Signal Layer

Goal: High-quality structured intelligence

Region segmentation:

* United States
* Europe
* Middle East

Each region includes:

* 2 key developments
* 1 implication
* source lists
* evidence with URLs

---

## Phase 3 — Enrichment & Content Layer

Goal: Transform signal → advisory output

* Executive Take
* Advisory Layer
* LinkedIn Draft

HARD RULE:

* NO new search
* NO new sources
* Input = Phase 2 output only

---

## Phase 4 — System Stability & Control Layer

Goal: Stability, consistency, and controllability

---

# ✅ CURRENT SYSTEM STATE

Phase 1 — COMPLETE
Phase 2 — COMPLETE
Phase 3 — COMPLETE
Phase 4 — COMPLETE
Phase 5 — ACTIVE (Stage 5.4 — Production Integration)

---

## ⚙️ PRODUCTION BEHAVIOR

* Runs daily at 08:00 (Shanghai time)
* Single pipeline execution
* Writes to Lark (top insertion)
* Logs stored locally

---

## 📦 OUTPUT STRUCTURE

Each daily entry contains:

### 1. Executive Take

* cross-region synthesis
* strategic meaning

### 2. Advisory Layer

* implications for multinational companies
* risk / opportunity framing

### 3. LinkedIn Draft

* publication-ready content
* executive tone

### 4. Signal Layer

* region-based breakdown
* evidence-backed
* verifiable sources

---

# 🔑 CORE DESIGN PRINCIPLES

1. Signal ≠ Analysis
2. Evidence must be verifiable
3. Query design drives output quality
4. Simplicity over complexity
5. Stability before expansion
6. Prompts control behavior (NOT infrastructure)

---

# 🧠 CRITICAL ARCHITECTURAL INSIGHT

System behavior is controlled by runtime prompt design.

Implications:

* AGENTS.md is secondary
* prompts are the true control layer
* improvements = prompt refinement

---

# ⚠️ CURRENT LIMITATIONS

### 1. Chinese source prioritization

* inconsistent selection
* over-reliance on international summaries

### 2. Evidence layer gaps

* missing Chinese URLs
* occasional “NOT AVAILABLE”

### 3. No resilience layer

* no retry logic
* no fallback behavior

### 4. Output segmentation

* briefing + LinkedIn + signal combined

---

# 🔧 REFINEMENT MODEL

## Human Feedback Loop

For each weak output:

* better source
* better URL
* better query
* better framing

→ feeds prompt refinement

---

## PRIORITY IMPROVEMENTS

### 1. Chinese Source Depth (TOP PRIORITY)

* prioritize Chinese-language sources
* ensure Chinese URLs
* reduce reliance on Reuters/Bloomberg

---

### 2. Output Quality

* tighter Executive Take
* stronger Advisory Layer
* consistent LinkedIn tone

---

# 👥 TEAM INTEGRATION MODEL

## Role of System

System = Research engine + first draft generator

---

## Role of Team

Team = Editor + strategist + quality control

---

## Workflow Model

System → Lark → Team → Final Output

---

# 🔚 FINAL POSITION

The system is:

* operational
* automated (partial — integration in progress)
* advisory-capable

Current state:

👉 Pre-production system entering full automation phase

---

END OF DOCUMENT
