# OpenClaw Foundation Document (Final — v4)

Date: 2026-03-28

---

## 🎯 PURPOSE

This document defines:

1. The **current state of the OpenClaw system**
2. The **operating model for daily use**
3. The **roadmap for future development**

This project is built iteratively by a non-technical operator.

Core principle:

```
Build one working system → stabilize → layer improvements
```

---

## 🧭 SYSTEM OBJECTIVE

Build a **semi-automated PR intelligence engine** that produces:

* daily China-related strategic monitoring
* structured signal extraction
* advisory-level interpretation
* publication-ready content

Primary use case:

```
Multinational companies operating in or exposed to China
```

---

# 🔷 SYSTEM ARCHITECTURE (REAL STATE)

System flow:

```
OpenClaw → Agent → Relay → Lark Docx
```

### OpenClaw (Control + Execution Layer)

* Gateway-based control plane
* manages agents, sessions, tools, scheduling

### Agent Layer

* china_pr_monitor_light → signal generation
* enrichment → runtime prompt transformation

### Relay Layer (Flask)

* `/push` endpoint
* formats output for Lark

### Lark Docx (Output Layer)

* final storage and review surface
* strict block + formatting requirements

---

# 🔷 PHASE STRUCTURE (LOCKED)

## Phase 1 — Pipeline Layer

**Goal:** Reliable execution

✔ OpenClaw agent → relay → Lark
✔ cron automation
✔ stable output delivery

---

## Phase 2 — Signal Layer

**Goal:** High-quality structured intelligence

✔ Region segmentation:

* United States
* Europe
* Middle East

✔ Each region includes:

* 2 key developments
* 1 implication
* source lists
* evidence with URLs

---

## Phase 3 — Enrichment & Content Layer

**Goal:** Transform signal → advisory output

✔ Executive Take
✔ Advisory Layer
✔ LinkedIn Draft

⚠️ HARD RULE:

* NO new search
* NO new sources
* Input = Phase 2 output only

---

## Phase 4 — ChatGPT-Native Control Layer (NEXT)

**Goal:** Interface + control

* ChatGPT becomes control interface
* OpenClaw remains execution engine
* system becomes conversational

---

# ✅ CURRENT SYSTEM STATE

## Phase 1 — COMPLETE

## Phase 2 — COMPLETE

## Phase 3 — COMPLETE

System now runs:

```
Signal → Enrichment → Lark  
```

✔ Fully automated via cron
✔ Producing advisory-level output

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

> System behavior is controlled by runtime prompt design

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
* occasional "NOT AVAILABLE"

### 3. No resilience layer

* no retry logic
* no fallback behavior

### 4. Output segmentation

* briefing + LinkedIn + signal combined

---

# 🔧 REFINEMENT MODEL

System improves through:

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

System =

```
Research engine + first draft generator  
```

Produces:

* signal
* analysis
* draft content

---

## Role of Team

Team =

```
Editor + strategist + quality control  
```

Responsibilities:

* refine messaging
* validate positioning
* adjust tone
* finalize output

---

## Workflow Model

System → Lark → Team → Final Output

---

# 🚀 ADDENDUM — PHASE 3 COMPLETE

## RESULT

System produces:

* Executive Take
* Advisory Layer
* LinkedIn Draft
* Signal + Evidence

in a single automated pipeline.

---

## KEY INSIGHT

> Runtime prompt control > static agent configuration

---

## STATUS

✔ Fully integrated
✔ Production-ready
✔ Commercially usable

---

# 🔜 PHASE 4 — CONTROL LAYER

## PURPOSE

Transform system into:

```
interactive intelligence platform  
```

---

## TARGET MODEL

User → ChatGPT → OpenClaw → Lark

---

## CAPABILITIES

* trigger runs via chat
* adjust queries dynamically
* control agents conversationally
* eliminate terminal dependency

---

## STRATEGIC SIGNIFICANCE

Phase 4 transforms system into:

```
a true advisory operating system  
```

---

# 🧾 DAILY STATUS + ISSUE LOG PROTOCOL (MANDATORY)

---

## 🎯 PURPOSE

Ensure:

* consistent progress tracking
* visibility into issues
* structured documentation
* smooth team handoffs

---

## 🔷 TRIGGER

Triggered when operator says:

```
“we’re finished for the day”
```

---

## 🔷 REQUIRED OUTPUTS

### 1. DAILY STATUS REPORT

Using locked template:

OPENCLAW PROJECT — DAILY STATUS & ROADMAP (Locked Template)

---

### 2. ISSUE LOG

Each issue recorded as:

### Issue #[N]

**Category:**
Cron / Lark / Agent / Prompt / Output / Infra

**Description:**
What went wrong

**Root Cause:**
Why it happened

**Fix Applied:**
Exact action taken

**Status:**
Resolved / Partial / Unresolved

**Follow-up Required:**
Yes / No

---

### 3. KEY LEARNINGS

* concise
* actionable
* system-relevant

---

## 🔷 RULES

1. No skipping
2. No vague summaries
3. All fixes must be logged
4. Recurring issues tracked
5. This becomes system memory

---

## 🧠 STRATEGIC PURPOSE

This creates:

* cumulative system intelligence
* faster debugging
* team onboarding foundation
* operational continuity

---

## 🔷 FUTURE ROLE (PHASE 4+)

This log becomes:

* training material
* refinement input
* operational dashboard foundation

---

# 🔚 FINAL POSITION

The system is now:

✔ operational
✔ automated
✔ advisory-capable

This is not a prototype.

It is a functioning intelligence engine.

---

END OF DOCUMENT
