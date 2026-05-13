# OPENCLAW — FOUNDATION DOCUMENT

---
document_id: OPENCLAW-FOUND-001
version: 5.3.26a
last_updated: 2026-05-03
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
→ Agent (signal generation)
→ **Scrubber (deterministic cleanup)**
→ Validator (strict verification)
→ **Delivery Gate (PASS/WARN/FAIL)**
→ Lark

---

## 🔷 PHASE STATUS

Phase 1–5: COMPLETE
Phase 6.1: COMPLETE
Phase 6.2: COMPLETE
Phase 6.3: COMPLETE (as of 2026-05-03)
Phase 6.4: COMPLETE (as of 2026-05-05)
Phase 6.5: ACTIVE

---

## 🔧 PHASE 6 — CORE ARCHITECTURE

### Key Principle

> The model is allowed to be imperfect.
> The system is not.

---

## 🧠 AGENT BEHAVIOR

* Agent is probabilistic
* Generates claims + result_id citations
* May include incorrect or fabricated IDs — caught by Scrubber and Validator
* Agent output format is governed by the Phase 6.3 locked citation schema
* Agent must select result_ids from VALID_RESULT_IDS only
* Agent must not generate, infer, mutate, or fabricate result_ids
* Citation behavior is treated as a selection task, not a generation task

---

## 🧹 SCRUBBER LAYER

### Purpose

Deterministically clean agent output before validation.

### Behavior

* Parses locked citation syntax: [result_ids: ...] and [based_on: ...]
* Extracts all result_id tokens
* Keeps only IDs present in retrieval_package
* Removes invalid/fabricated IDs
* Rewrites citation groups

### Outcomes

* Valid groups preserved
* Invalid groups removed
* Unsupported groups flagged

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

### Locked Output Format Strategy (Phase 6.3 — COMPLETE)

* Citations are controlled evidence references
* Agent selects from approved result_ids only (VALID_RESULT_IDS)
* System provides VALID_RESULT_IDS via build_agent_input_slim.py
* Scrubber removes invalid IDs
* Validator confirms retained IDs
* Delivery gate blocks or warns on unsupported output
* Two consecutive locked-format deliveries confirmed (2026-05-02 and 2026-05-03)

---

## 🔒 GUARANTEES

* No fabricated citations reach output
* All delivered result_ids are valid
* System does not depend on model precision

---

## 📈 CURRENT STATE

* System stable — HIGH
* Citation integrity guaranteed — locked format confirmed across live cron runs
* Dual-provider retrieval operational — Brave + Baidu confirmed stable (Phase 6.4 complete)
* Content quality improvable — addressed in Phase 6.5+ (soft layer)
