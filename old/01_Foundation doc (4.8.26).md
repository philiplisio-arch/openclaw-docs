# OpenClaw Foundation Document (Final — v9)

Date: 2026-04-08

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
→ Execution Layer (runtime / model / process control)
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

### Execution Layer (NEW — CRITICAL)

Controls:

* agent runtime behavior
* model execution lifecycle
* stdout / output return
* rate limit handling
* process termination

NOTE:
This is the current system bottleneck.

---

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

👉 Phase 5.6 — Execution Stabilization & Retrieval Optimization

---

### PHASE 5.1 — CHINA-NATIVE RETRIEVAL EXPANSION

* Baidu API integration
* Optional: Sogou / SERPAPI
* Retrieval comparison vs current stack
* Chinese-language source prioritization improvements

---

### Retrieval Orchestration Layer (CRITICAL)

All external retrieval must occur outside the agent.

Architecture:

Retrieval → Orchestrator → Structured Input → Agent

Rules:

* Agents DO NOT call search tools
* Agents DO NOT perform retrieval
* All retrieval is pre-processed and injected as structured data
* Multiple sources combined BEFORE agent execution

Purpose:

* Ensure determinism
* Maintain stability
* Enable multi-source integration

---

### PHASE 5.3 — Agent Integration — COMPLETE

Status: ✅ COMPLETE

* Agent receives ONLY structured package
* No direct retrieval inside agent
* Output structure stable

---

### PHASE 5.4 — PRODUCTION INTEGRATION — COMPLETE

Status: ✅ COMPLETE (Execution instability present)

System achieved:

Trigger (cron / webhook)
→ Retrieval Orchestrator
→ Agent
→ Relay
→ Lark

---

### PHASE 5.5 — OUTPUT STABILIZATION

Definition:

* Output structure correctness ONLY

Status: ⚠️ PARTIAL

✔ Executive Take stable  
✔ Advisory Layer stable  
✔ LinkedIn Draft stable  

---

### PHASE 5.6 — EXECUTION STABILIZATION & RETRIEVAL OPTIMIZATION

Status: 🔴 ACTIVE

Primary objective:

👉 Stabilize execution layer

Critical issues:

* Agent hang (process not exiting)
* Output not returned to stdout
* Rate limit (429) instability
* Reliance on log extraction

---

## 🔴 PHASE 6 — OPERATIONALIZATION & SCALE

### OBJECTIVE

Transform system into:

business-operating intelligence platform

---

### CORE FUNCTIONS

* Multi-client deployment
* Client-specific intelligence streams
* Content → business development loop
* Automated workflows
* Billing / reporting
* Persistent system memory

---

### ACTIVATION CONDITION

Phase 6 begins only after:

* Phase 5 execution is stable
* System is fully automatable

---

## ⚠️ NON-NEGOTIABLE RULE

NO new data sources until system is stable.

---

## 🧭 DAILY DECISION RULE

* Stability issue → Phase 5.6
* Capability improvement → later Phase 5
* Scaling → Phase 6

---

## 🧱 SYSTEM MENTAL MODEL

* Phase 4 = Trust the system
* Phase 5 = Build intelligence
* Phase 5.6 = Make it run reliably
* Phase 6 = Run the business on it

---

# ✅ CURRENT SYSTEM STATE

Phase 1 — COMPLETE  
Phase 2 — COMPLETE  
Phase 3 — COMPLETE  
Phase 4 — COMPLETE  
Phase 5.4 — COMPLETE  
Phase 5.5 — PARTIAL  
Phase 5.6 — ACTIVE  

---

## ⚙️ PRODUCTION BEHAVIOR

* Runs daily at 08:00 (Shanghai time)
* Writes to Lark
* Logs stored locally

---

## 📦 OUTPUT STRUCTURE

1. Executive Take  
2. Advisory Layer  
3. LinkedIn Draft  
4. Signal Layer  

---

# 🔑 CORE DESIGN PRINCIPLES

1. Signal ≠ Analysis  
2. Evidence must be verifiable  
3. Query design drives output quality  
4. Simplicity over complexity  
5. Stability before expansion  
6. Prompts control reasoning behavior  
7. Execution layer controls system reliability  

---

# ⚠️ CURRENT LIMITATIONS

### 1. Execution Layer Instability (PRIMARY)

* agent hang
* stdout issues
* rate limit handling

### 2. Chinese Source Depth

* inconsistent prioritization

### 3. No resilience layer

* no retry logic
* no fallback model

---

# 🔧 REFINEMENT MODEL

Human feedback → prompt refinement → system improvement

---

# 👥 TEAM MODEL

System = research + draft  
Team = edit + strategy  

---

# 🔚 FINAL POSITION

System is:

✔ Architecturally complete  
✔ Producing valid outputs  

BUT:

❌ Not execution-stable  
❌ Not fully automatable  

Current state:

👉 Execution stabilization phase (Phase 5.6)

---

END OF DOCUMENT