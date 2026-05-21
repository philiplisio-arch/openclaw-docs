OPENCLAW — ARCHITECTURE PHILOSOPHY & LAYERING STRATEGY
(Search Layer vs. AI Control Layer)

---
document_id: OPENCLAW-PHIL-001
version: 5.3.26a
last_updated: 2026-05-03
status: REFERENCE — reflects current system state as of Phase 6.4
---

---

⚠ SNAPSHOT WARNING — REFERENCE ONLY
This document reflects the Phase 6.4 system state (last updated 2026-05-03).
It does not include Phase 6.8 changes (numbered-source citation architecture,
Resolver layer). It is classified REFERENCE — not governing. For current
pipeline definition, see 00_System_Constitution.md and specs/08_Architecture_Map.md.

---

## 🎯 PURPOSE OF THIS DOCUMENT

This document explains:

1. The architectural philosophy of OpenClaw
2. The separation between the Search (Retrieval) Layer and the Agent (Reasoning) Layer
3. Why the system is being built in this sequence
4. Why this approach is strategically superior for long-term scalability, reliability, and quality

---

## 🧠 CORE ARCHITECTURAL PRINCIPLE

> Separate Retrieval from Reasoning

OpenClaw is built on a strict separation:

- **Retrieval Layer** → responsible for gathering, filtering, and structuring information
- **Agent Layer (LLM)** → responsible for interpreting and synthesizing information
- **Control Layer (Claude CoWork)** → responsible for post-run analysis, documentation, and operator interface

---

## 🏗️ SYSTEM STRUCTURE (CURRENT — PHASE 6.4)

### Production Pipeline

```
Trigger (cron / webhook)
→ Retrieval Orchestrator
→ Structured Retrieval Package (retrieval_package.json)
→ Agent (LLM)
→ Scrubber (deterministic citation cleanup)
→ Validator (evidence integrity check)
→ Delivery Gate (PASS/WARN/FAIL)
→ Lark Output
```

Claude CoWork operates **outside and after** this pipeline. It reads artifacts and produces analysis. It does not execute, modify, or influence any pipeline step.

---

## 🔍 LAYER DEFINITIONS

### 1. RETRIEVAL LAYER (ORCHESTRATOR)

Owned by: Orchestrator

Components:
- Query Builder
- Brave Executor
- Baidu Executor (partial — returns results when available)
- Normalization
- Deduplication
- Filtering (freshness window, relevance)
- Conflict Detection
- Package Builder

Responsibilities:
- Generate queries
- Retrieve raw data
- Clean and normalize data
- Remove duplicates
- Filter for relevance and quality
- Output structured, validated information

Constraints:
- No interpretation
- No narrative generation

---

### 2. AGENT LAYER (LLM)

Responsibilities:
- Interpret structured retrieval_package
- Generate: Executive Take, Advisory Layer, LinkedIn Draft, Regional Source List
- Cite claims using locked syntax: [result_ids: ...] / [based_on: ...]
- Select result_ids exclusively from VALID_RESULT_IDS

Constraints:
- No browsing
- No retrieval
- No hallucinated sourcing
- No external context beyond input package

---

### 3. SCRUBBER LAYER

Responsibilities:
- Extract all result_id tokens from agent output
- Validate each against retrieval_package
- Remove invalid / fabricated IDs
- Rewrite citation groups
- Produce scrubber_report.json

Constraints:
- Does NOT judge claim meaning
- Does NOT perform evidence matching
- Does NOT produce delivery decisions

---

### 4. VALIDATOR LAYER

Responsibilities:
- Confirm all retained result_ids map to retrieval_package entries
- Classify run as PASS / WARN / FAIL
- Produce validation_result.json
- Gate delivery

Constraints:
- Does NOT rewrite output
- Does NOT perform retrieval
- Does NOT use LLM judgment

---

### 5. CONTROL LAYER (CLAUDE COWORK)

Current role: Claude CoWork operates as the analysis and documentation layer.

Responsibilities:
- Read pipeline output artifacts
- Produce structured per-run analysis (per OPENCLAW-OPS-001)
- Draft document updates for operator review
- Recommend next steps within current phase scope

Hard constraints:
- Does NOT execute the pipeline
- Does NOT modify pipeline code or configuration
- Does NOT update documents without explicit operator approval
- Governed by OPENCLAW-OPS-001 (CoWork Operating Protocol)

---

## 🧠 CURRENT SYSTEM STATE (AS OF PHASE 6.4)

Completed:
- Architecture design ✔
- Orchestrator build ✔
- Agent integration ✔
- Scrubber layer ✔
- Validator layer ✔
- Delivery Gate ✔
- Full production integration ✔
- Cron-based automation ✔
- Output delivery to Lark ✔
- Claude CoWork as control layer ✔
- VALID_RESULT_IDS injection into build_agent_input_slim.py ✔
- Locked citation syntax enforcement ([result_ids: ...] / [based_on: ...]) ✔
- Two consecutive locked-format live cron deliveries confirmed ✔ (Phase 6.3a exit)

Active (Phase 6.4):
- Retrieval quality stabilization
- Baidu contribution (currently returning empty results)
- Query freshness enforcement
- Partial retrieval resilience

---

## ⚖️ KEY DESIGN DECISION

### Question:
Should the AI control layer (Claude CoWork) be integrated into the execution pipeline?

### Answer:
No. Claude CoWork sits above the pipeline, not inside it.

Reasons:
1. The pipeline is deterministic. Claude CoWork is a non-deterministic reasoning layer. These are incompatible at execution level.
2. Embedding reasoning in the execution path risks architectural drift and debugging ambiguity.
3. Clean separation enables each layer to evolve independently.

---

## 🔥 RATIONALE FOR CURRENT SEQUENCING

### 1. Retrieval Quality is the Foundation

If retrieval is weak, the agent produces weak output. No reasoning layer can fix missing or poor evidence.

Therefore: Improve the engine before relying on the control layer for quality.

### 2. Architectural Separation Enables Safe Iteration

Because retrieval is isolated:
- Baidu can be improved independently
- Query logic can be refined without affecting agent behavior
- Filtering can be tuned without touching output logic

### 3. Avoid Layer Contamination

If the control layer is added too early or too deeply, risks include:
- Retrieval logic drifting into prompt engineering
- Debugging becomes ambiguous
- System loses determinism

### 4. Deterministic System First, Adaptive Layer Second

Current system is:
- Deterministic
- Traceable
- Modular

Claude CoWork adds:
- Flexible interpretation
- Documentation
- Operator interface

These are complementary, not competing.

---

## 📊 BENEFITS OF THIS ARCHITECTURE

1. **Modularity** — Each layer can evolve independently
2. **Scalability** — New sources can be added without rewriting the system
3. **Reliability** — Failures are isolated and diagnosable
4. **Quality Control** — Only validated data reaches the agent
5. **Operator Safety** — Control layer cannot corrupt execution

---

## 🧭 FINAL POSITION

The current approach — retrieval first, validation second, adaptive control layer above — is:

✔ Architecturally correct
✔ Lower risk
✔ More scalable
✔ Easier to debug
✔ Better for long-term system quality

---

## 🧠 SUMMARY

> OpenClaw is intentionally designed as a retrieval-first intelligence system, not a prompt-driven system.

The AI control layer (Claude CoWork) is:
- an analysis and documentation layer
- not the core engine
- not embedded in the execution path

> The system maintains determinism and traceability by keeping the reasoning layer outside the execution pipeline.

---

END
