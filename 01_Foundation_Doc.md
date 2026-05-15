# OPENCLAW — FOUNDATION DOCUMENT

---
document_id: OPENCLAW-FOUND-001
version: v6.0
last_updated: 2026-05-14
status: ACTIVE
---

## 🎯 PROJECT OBJECTIVE

Build a trusted, client-grade PR intelligence system that produces accurate, verifiable, and reliable daily reports.

---

## 🏗 SYSTEM ARCHITECTURE

### Pipeline

Trigger
→ Retrieval (Brave + Baidu)
→ Orchestrator (normalize, dedup, filter)
→ Agent (signal generation, source-number citations)
→ **Resolver (resolve_source_numbers.py — maps source numbers → result_ids)**
→ **Scrubber (deterministic cleanup, uncited bullet removal)**
→ Validator (strict verification)
→ **Delivery Gate (PASS/WARN/FAIL)**
→ Lark (result_ids substituted with publisher/date by citation_sub.py)

---

## 🔷 PHASE STATUS

Phase 1–5: COMPLETE
Phase 6.1: COMPLETE
Phase 6.2: COMPLETE
Phase 6.3: COMPLETE (operator approved 2026-05-03)
Phase 6.4: COMPLETE (operator approved 2026-05-05)
Phase 6.5: COMPLETE (operator approved 2026-05-06)
Phase 6.6: COMPLETE (operator approved 2026-05-07)
Phase 6.7: COMPLETE (operator approved 2026-05-07)
Phase 6.8: COMPLETE (operator approved 2026-05-07)
Phase 6.9–6.11: SUPERSEDED — not required
Phase 7 Entry: ACTIVE — Phase C (Brain Lite & Client Config Implementation), operator-authorized 2026-05-11

---

## 🔧 PHASE 6 — CORE ARCHITECTURE

### Key Principle

> The model is allowed to be imperfect.
> The system is not.

---

## 🧠 AGENT BEHAVIOR

* Agent is probabilistic
* Generates claims with [source_numbers: N] citations from numbered VALID_SOURCES list
* Agent cites by source number — does NOT write result_ids directly
* May cite incorrect or out-of-range source numbers — caught by Resolver and Scrubber
* Agent output format is governed by the Phase 6.8 numbered-source citation schema
* Agent must select only from the numbered VALID_SOURCES list provided in the agent input
* Citation behavior is treated as a selection task, not a generation task
* Resolver (resolve_source_numbers.py) maps source numbers → result_ids after agent execution

---

## 🧹 SCRUBBER LAYER

### Purpose

Deterministically clean resolved agent output before validation.

### Precondition

Resolver must run before Scrubber. Scrubber operates on post-resolver output containing result_id citations only.

### Behavior

* Parses locked citation syntax: [result_ids: ...] and [based_on: ...]
* Extracts all result_id tokens
* Keeps only IDs present in retrieval_package
* Removes invalid/fabricated IDs
* Rewrites citation groups
* Removes bullets with no valid citation remaining (uncited claim removal)

### Outcomes

* Valid groups preserved
* Invalid groups removed
* Unsupported groups flagged
* Uncited bullets removed before delivery

---

## ✅ VALIDATOR LAYER

### Purpose

Final authority on correctness.

### Validation Hierarchy

**result_id matching is the primary validation mechanism.** The validator confirms that all result_ids cited in scrubbed_output.txt exist in retrieval_package.json. Publisher and URL checks are secondary verification layers, subordinate to result_id matching. A citation is valid if its result_id maps to a retained retrieval result — publisher and URL fields provide additional traceability but do not override result_id status.

### Behavior

* Confirms all result_ids exist in retrieval_package
* Rejects fabricated citations
* Produces PASS / WARN / FAIL

---

## 🚦 DELIVERY CONTROL

**The Delivery Gate is the sole and final authority on whether output is delivered.** No other layer may permit or block delivery. Control Layer and Validator produce inputs to the Delivery Gate decision; the Delivery Gate alone acts on those inputs.

### Rules

* PASS → deliver
* WARN → deliver (acceptable degradation)
* FAIL → block

---

## ⚖️ TOLERANCE MODEL

### Definitions

* citation_groups_seen = total claims with citations
* unsupported_groups = claims with zero valid IDs

### Logic

* If ALL groups unsupported → FAIL
* If SOME groups unsupported → WARN → deliver
* If NONE unsupported → PASS → deliver

---

## 🎯 SYSTEM STRATEGY

### High Recall → Cleanup → Validation

* Agent over-generates citations
* Scrubber removes invalid
* Validator guarantees correctness

### Numbered-Source Citation Architecture (Phase 6.8 — COMPLETE)

* Agent cites by source number from VALID_SOURCES list ([source_numbers: N])
* System provides numbered VALID_SOURCES via build_agent_input_slim.py
* Resolver maps source numbers → result_ids (resolve_source_numbers.py)
* Scrubber removes invalid IDs and uncited bullets
* Validator confirms retained IDs exist in retrieval_package
* citation_sub.py substitutes result_id tokens with publisher/date strings in Lark delivery
* Fabrication rate 0% observed across latest validated run set (Phase 6.8, confirmed 2026-05-07/08)

---

## 🔒 GUARANTEES

* No fabricated citations reach output
* All delivered result_ids are valid
* System does not depend on model precision

---

## 📈 CURRENT STATE

* System stable — HIGH
* Citation integrity: fabrication rate 0% across latest validated run set
* Numbered-source architecture operational — agent cites by source number; resolver maps to result_ids
* Dual-provider retrieval operational — Brave + Baidu both confirmed stable
* Citation substitution active — result_ids replaced with publisher/date strings in Lark delivery
* Conflict detection active — three tiers (⚠/↔/~) operational
* Phase 6 Soft Layer (6.1–6.8) complete — 2026-05-07
* Phase 7 Entry active — Phase C (Brain Lite & Client Config Implementation), operator-authorized 2026-05-11
* Content quality (source authority calibration, freshness signalling, advisory tone) — Phase 7 editorial workstream