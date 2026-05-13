# 🎯 PHASE EXIT CRITERIA — OPENCLAW PROJECT

---
document_id: OPENCLAW-PEC-001
version: 5.3.26a
last_updated: 2026-05-03
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

## ✅ PHASE 6.3 — EVIDENCE TRACEABILITY SYSTEM

**Status: COMPLETE** (as of 2026-05-03)

---

### ✅ 6.3s — Stabilization

**Status: COMPLETE** (confirmed via consecutive successful deliveries as of 2026-04-28)

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

### ✅ 6.3a — Locked Output Format Enforcement

**Status: COMPLETE** (operator approved 2026-05-03)

Exit criteria as operationally defined and confirmed:

1. ✔ Agent uses locked citation syntax ([result_ids: ...] / [based_on: ...]) in live cron runs
2. ✔ All cited IDs are parseable
3. ✔ Scrubber removes invalid IDs before validation
4. ✔ Validator returns PASS or acceptable WARN
5. ✔ No fabricated citation reaches Lark
6. ✔ Two consecutive successful locked-format Lark deliveries

Exit evidence:
- Delivery #1: 2026-05-02 08:26 Shanghai — GREEN PASS, 8/8 citations matched
- Delivery #2: 2026-05-03 06:30 Shanghai — GREEN PASS, 7/7 citation groups locked format
- Issues #35 and #36 closed

Reconciliation note (2026-05-03): Original PEC criteria specified 3+ runs and a standalone citation audit log artifact. Operational exit criteria were revised during the 5.1–5.3 session sequence with operator approval: exit threshold set at 2 consecutive locked-format deliveries; scrubber_report.json accepted as the citation audit trail in lieu of a separate artifact. The locked citation syntax requirement ([result_ids:] / [based_on:]) was added as the primary enforcement criterion, superseding the original result_id-from-retrieval_package framing. The original "No valid citation groups lost to scrubber error" criterion was satisfied in practice — scrubber preserves all valid groups and removes only invalid IDs.

---

### ✅ 6.3 Overall Exit

Phase 6.3 is complete when:

- ✔ All claims in agent output carry at least one valid result_id — CONFIRMED
- ✔ Every result_id in output maps to a retained retrieval result — CONFIRMED
- ✔ Scrubber + validator chain runs cleanly end-to-end — CONFIRMED
- ✔ Delivery is stable across multiple consecutive runs — CONFIRMED

---

## ✅ PHASE 6.4 — RETRIEVAL QUALITY STABILIZATION

**Status: COMPLETE** (operator approved 2026-05-05)

Exit criteria — all satisfied:

1. ✔ Brave retrieval consistently produces fresh, relevant results
2. ✔ Baidu contributing meaningful results — 54 results, 0 errors confirmed across successive runs (2026-05-05)
3. ✔ Query freshness enforced: precision queries past 24h, recall queries past 7 days
4. ✔ Filtering retains high-quality signals — GREEN PASS on all 4 runs 2026-05-05
5. ✔ retrieval_package contains adequate coverage — US/China, Europe, Middle East all represented; Chinese-language sources via Baidu
6. ✔ Partial retrieval handled gracefully — confirmed operational without delivery failure

---

## 🚧 PHASE 6.5–6.7 — SOFT LAYER

**Gate cleared** (6.1–6.4 all complete as of 2026-05-05)

### 🚧 6.5 — Conflict Handling Upgrade — ACTIVE

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

1. Run system across **2+ consecutive days**
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
