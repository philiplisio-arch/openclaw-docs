# 🎯 PHASE EXIT CRITERIA — OPENCLAW PROJECT

---
document_id: OPENCLAW-PEC-001
version: 4.28.26a
last_updated: 2026-04-28
status: ACTIVE
---

## 📌 PURPOSE
Define exactly when a phase is considered **complete** so work does not drift or overextend.

---

# 🔷 PHASE 6 — TRUST & VALIDATION LAYER

**Objective:** Move system from high output capability → high trust, client-grade intelligence system.

---

## 🔷 PHASE 6 STRUCTURE

```
Hard Gates (sequential):
6.1 → 6.2 → 6.3 → 6.4

Soft Layer (requires Hard Gates stable):
6.5 → 6.6 → 6.7

Expansion Layer (blocked until all above stable):
6.8 → 6.9 → 6.10
```

---

## ✅ PHASE 6.1 — VALIDATOR LAYER

**Status: COMPLETE**

Exit criteria satisfied:
- Validator runs every report
- validation_result.json produced every run
- GREEN / YELLOW / RED visible in logs
- PASS allows delivery
- WARN allows delivery with internal warning
- FAIL blocks Lark delivery
- Fabricated citation test triggers FAIL
- Missing source test triggers FAIL
- Publisher alias test triggers WARN
- Normal report triggers PASS or controlled WARN

---

## ✅ PHASE 6.2 — VALIDATION-AWARE DELIVERY GATE

**Status: COMPLETE**

Exit criteria satisfied:
- Validator FAIL prevents Lark delivery
- PASS / WARN allows delivery
- Logs clearly show decision path
- No silent delivery

---

## 🚧 PHASE 6.3 — EVIDENCE TRACEABILITY SYSTEM

**Status: IN PROGRESS**

---

### 6.3s — Stabilization

✅ **Status: COMPLETE** (confirmed via consecutive successful deliveries as of 2026-04-28)

Exit criteria satisfied:

1. ✔ Model path reliable
2. ✔ Non-empty output
3. ✔ Control layer passes
4. ✔ Validator passes (PASS or WARN)
5. ✔ Delivery succeeds
6. ✔ Two consecutive successful end-to-end runs
7. ✔ No silent failures
8. ✔ No blocked_control_fail

---

### 6.3a — result_id Validation Stabilization

**Status: ACTIVE** (6.3s gate cleared)

Exit criteria:

1. Agent uses only result_ids drawn from retrieval_package
2. Scrubber successfully removes all invalid / fabricated IDs
3. Validator confirms zero fabricated citations across 3+ runs
4. No valid citation groups lost to scrubber error
5. Citation audit log produced each run

---

### 6.3 Overall Exit

Phase 6.3 is complete when:

- All claims in agent output carry at least one valid result_id
- Every result_id in output maps to a retained retrieval result
- Scrubber + validator chain runs cleanly end-to-end
- Delivery is stable across multiple consecutive runs

---

## ⏳ PHASE 6.4 — RETRIEVAL QUALITY STABILIZATION

**Status: BLOCKED by 6.3**

Exit criteria:

1. Brave retrieval consistently produces fresh, relevant results
2. Baidu contributing meaningful results (not stub / empty)
3. Query freshness enforced: past 24 hours / explicit date precision queries active
4. Filtering retains high-quality signals and discards noise reliably
5. retrieval_package contains adequate coverage for all defined regions
6. Partial retrieval (one provider down) handled gracefully without delivery failure

---

## ⏳ PHASE 6.5–6.7 — SOFT LAYER

**Blocked until 6.1–6.4 stable**

### 6.5 — Conflict Handling Upgrade

- Conflicting claims across sources explicitly surfaced to operator
- No silent conflict suppression
- Conflict classification logged per run

### 6.6 — Low-Signal Handling Refinement

- System correctly identifies and labels low-signal runs
- Agent reduces certainty language under degraded retrieval
- No over-synthesis when evidence is sparse

### 6.7 — Output Consistency Hardening

- All required output sections present across 10+ consecutive runs
- Formatting consistent without manual intervention
- Section structure matches defined output contract

---

## ⏳ PHASE 6.8–6.10 — EXPANSION LAYER

**Blocked until all above stable**

### 6.8 — Model Architecture Optimization
- Model path evaluated and optimized for quality / cost / reliability

### 6.9 — Source Expansion
- Additional retrieval sources integrated (e.g. Sogou, others TBD)

### 6.10 — Channel Expansion
- Output delivered to additional channels (Discord, WeChat, or equivalent)

---

## ⚠️ ALLOWED IMPERFECTIONS (PHASE 6)

The following do NOT block Phase 6 sub-phase completion:

- Some claims weakly supported (WARN acceptable)
- Baidu not yet contributing (non-blocking until 6.4)
- Output narrative quality not yet "excellent"
- LinkedIn Draft not fully citation-enforced in V1
- Minor metadata gaps in retrieval results

---

## 🧪 VALIDATION METHOD

To confirm a Phase 6 sub-phase complete:

1. Run system across **2–3 consecutive days**
2. Verify all exit criteria for that sub-phase
3. Confirm no manual intervention required
4. Review logs: no silent failures, clear pass/warn/fail decisions

---

## 🚪 EXIT DECISION RULE

A Phase 6 sub-phase is complete when:

👉 All exit criteria for that sub-phase are satisfied  
👉 Across consecutive runs  
👉 Without intervention  
👉 Hard gate dependency is clear before proceeding

---

## 🧠 FINAL PRINCIPLE

**Do not wait for perfection.**

If the system is:
- Stable
- Deterministic
- Delivering trusted output

👉 Move to the next sub-phase.

Perfection comes later. Trust comes first.
