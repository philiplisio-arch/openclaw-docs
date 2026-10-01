🧠 OPENCLAW — ISSUES LOG (UPDATED)

---

## 🔴 ACTIVE ISSUES

---

### Issue #24 — Baidu Output Path Bug

Status: OPEN

Observed:

• Baidu executor writes to:
`/rootopenclaw_phase5/data/baidu_raw.json`
• Missing slash after `/root`

Impact:

• Baidu results not persisted correctly
• retrieval_package may exclude Baidu
• Breaks multi-source integrity

Root Cause:

• Incorrect file path in baidu_executor.py

Next Step:

• Fix path:
`/root/openclaw_phase5/data/baidu_raw.json`

Validation Required:

• Confirm baidu_raw.json is written
• Confirm Baidu results appear in normalized_results.json
• Confirm presence in retrieval_package.json

---

## 🟡 MONITORING

---

### Issue #25 — Agent Intermittent No Reply

Status: MONITOR

Observed:

• Intermittent "No reply from agent"

Root Cause:

• Provider instability / overload

Fix:

• Default model switched to:
google/gemini-2.5-pro

• Timeout tuning applied

Current State:

• Improved but not guaranteed stable

Monitoring Rule:

• Watch logs for:
"No reply from agent"

---

## 🟢 RESOLVED ISSUES

---

### Issue #26 — Validator Layer (Phase 6.1 — V1)

Status: ✅ RESOLVED

---

#### Summary

Validator successfully implemented and validated under:

✔ PASS path
✔ WARN path
✔ FAIL path

---

#### Capabilities Confirmed

✔ Citation extraction
✔ Publisher matching
✔ Fabrication detection
✔ Chinese alias support (basic)
✔ Deterministic validation (no LLM)

---

#### Control Layer Hardening

✔ Structural completeness now requires real section headers
✔ Meta-output no longer passes validation
✔ sed → awk extraction fix implemented

---

#### Validation Proof

PASS:

✔ Real run → citations matched → GREEN

FAIL:

✔ FakeNews test → 0 matches → RED

WARN:

✔ Missing citations → YELLOW

---

#### Known Limitation (NEW — IMPORTANT)

Validator currently relies on:

→ exact or alias-based publisher string matching

Limitations:

• New publishers may require alias expansion
• Domain vs publisher mismatch possible
• Chinese-language publisher normalization incomplete

Impact:

• May produce WARN/FAIL for valid but unnormalized sources

Classification:

→ Expected Phase 6.1 limitation (NOT a defect)

---

#### Status

Phase 6.1 EXIT CRITERIA:

✔ Met
✔ Validated under real runs
✔ Validated under adversarial tests

→ Phase 6.1 CLOSED

---

## 🔵 SYSTEM STATUS SUMMARY

---

Phase 5.6: ✅ COMPLETE
Phase 6.1: ✅ COMPLETE

System is now:

✔ Deterministic
✔ Observable
✔ Recoverable
✔ Evidence-validated (V1)
✔ Protected against fabricated citations

---

## 🔷 NEXT PHASE

---

### Phase 6.2 — Validation-Aware Delivery Gate

---

### Objective

Introduce delivery logic combining:

• Control Layer (structure)
• Validator Layer (evidence)

---

### Target Behavior

Control PASS + Validator PASS/WARN → deliver

Control PASS + Validator FAIL → block

Control FAIL → block

---

## 🔶 NEXT CRITICAL ACTION

---

→ Implement Delivery Gate logic using validator_result.json

END
