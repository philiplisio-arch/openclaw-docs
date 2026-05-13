# OPENCLAW — FOUNDATION DOCUMENT

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
→ Delivery (Lark)

---

## 🔷 PHASE STATUS

Phase 1–5: COMPLETE
Phase 6: ACTIVE

---

## 🔧 PHASE 6 — CORE ARCHITECTURE

### Key Principle

> The model is allowed to be imperfect.
> The system is not.

---

## 🧠 AGENT BEHAVIOR

* Agent is probabilistic
* Generates claims + result_id citations
* May include incorrect or fabricated IDs

---

## 🧹 SCRUBBER LAYER (NEW — CRITICAL)

### Purpose

Deterministically clean agent output before validation.

### Behavior

* Extract all result_id tokens
* Keep only IDs present in retrieval_package
* Remove invalid/fabricated IDs
* Rewrite citation groups

### Outcomes

* Valid groups preserved
* Invalid groups removed
* Unsupported groups flagged

---

## ✅ VALIDATOR LAYER

### Purpose

Final authority on correctness.

### Behavior

* Confirms all result_ids exist in retrieval_package
* Rejects fabricated citations
* Produces PASS / WARN / FAIL

---

## 🚦 DELIVERY CONTROL

### Rules

* PASS → deliver
* WARN → deliver (acceptable degradation)
* FAIL → block

---

## ⚖️ TOLERANCE MODEL (NEW)

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

---

## 🔒 GUARANTEES

* No fabricated citations reach output
* All delivered result_ids are valid
* System does not depend on model precision

---

## 📈 CURRENT STATE

* System stable
* Delivery reliable
* Citation integrity guaranteed
* Content quality improvable (future phase)
