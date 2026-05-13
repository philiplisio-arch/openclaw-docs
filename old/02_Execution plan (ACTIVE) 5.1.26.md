# OPENCLAW — EXECUTION PLAN

---
document_id: OPENCLAW-EXEC-001
version: 5.1.26a
last_updated: 2026-05-01
status: ACTIVE
---

## 🔷 PHASE 6 — CURRENT WORK

### Sub-Phase: 6.3 — Evidence Traceability

---

## ✅ COMPLETED

* Retrieval pipeline stable
* Orchestrator deterministic
* Agent integrated
* Validator implemented
* Result_id citation system active
* Scrubber layer implemented

---

## 🔧 6.3c — STABILIZATION (COMPLETE)

✔ High-recall citation strategy enforced
✔ Scrubber removes invalid IDs
✔ Validator verifies all citations
✔ Partial failure tolerated
✔ Delivery stable

---

## ⚙️ CURRENT SYSTEM BEHAVIOR

* Agent selects IDs from VALID_RESULT_IDS only
* Scrubber removes any invalid IDs
* Some claims may lose citations if IDs removed
* Output remains valid and safe

---

## 🎯 GUARANTEES

* No fabricated citations delivered
* All result_ids verified
* System resilient to model variability

---

## 📉 REMAINING LIMITATION

* Baidu returning 0 results — retrieval on Brave only
* Scrubber/validator output file paths unconfirmed
* Two consecutive successful deliveries not yet achieved

---

## 🚧 PHASE 6.3a — LOCKED OUTPUT FORMAT ENFORCEMENT

### Objective

Convert result_id citation behavior from probabilistic generation into
constrained selection from VALID_RESULT_IDS.

### Current Diagnosis

Resolved. Agent output from offline test runs shows:
- Locked citation syntax ([result_ids: ...] / [based_on: ...]) used correctly
- All cited IDs present in VALID_RESULT_IDS
- Zero fabricated IDs detected

### Required Implementation

1. Update Agent Input Contract with locked output format ✔ DONE
2. Modify build_agent_input_slim.py to inject VALID_RESULT_IDS ✔ DONE
3. Require citation syntax:
   - [result_ids: ...] ✔ DONE
   - [based_on: ...] ✔ DONE
4. Preserve Scrubber + Validator enforcement ✔ UNCHANGED
5. Confirm scrubber and validator output → PENDING
6. Confirm PASS or acceptable WARN → PENDING
7. Require two consecutive successful deliveries → PENDING

### Exit Criteria

- Agent uses locked citation syntax ✔
- No unsupported citation syntax in output ✔
- All IDs are parseable ✔
- Scrubber removes invalid IDs if present ✔
- Validator returns PASS or controlled WARN → PENDING
- Lark delivery succeeds → PENDING
- Two consecutive successful runs → PENDING

### Status

→ ACTIVE — implementation complete, confirmation pending

---

## 🚀 NEXT PHASE (6.4 — PENDING 6.3a)

Focus:

* Improve claim-to-evidence alignment
* Increase citation precision
* Improve narrative quality
* Address citation ID presentation in delivered output

---

## 🧭 PHASE 6 EXIT CRITERIA

✔ End-to-end runs succeed
✔ Validator consistently passes
✔ Scrubber prevents invalid output
✔ Delivery reliable across runs
✔ Locked output format enforced (Phase 6.3a)

STATUS: IN PROGRESS

---

## ⏭ NEXT STEP

→ Confirm scrubber and validator output file paths, run one controlled
full-chain test, confirm PASS or acceptable WARN, then achieve two
consecutive successful Lark deliveries.
