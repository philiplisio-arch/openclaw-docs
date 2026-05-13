# OPENCLAW — EXECUTION PLAN

---
document_id: OPENCLAW-EXEC-001
version: 5.4.26
last_updated: 2026-05-04
status: ACTIVE
---

## 🔷 PHASE 6 — CURRENT WORK

### Sub-Phase: 6.4 — Retrieval Quality Stabilization

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

* Baidu returning 0 results — SerpAPI key inactive; expected active 2026-05-05
* Issue #37 (offline script save step) pending operator decision

---

## ✅ PHASE 6.3a — LOCKED OUTPUT FORMAT ENFORCEMENT (COMPLETE)

### Objective

Convert result_id citation behavior from probabilistic generation into
constrained selection from VALID_RESULT_IDS.

### Resolution

Resolved. Two consecutive locked-format Lark deliveries confirmed:
- Delivery #1: 2026-05-02 08:26 Shanghai — GREEN PASS, 8/8 citations matched
- Delivery #2: 2026-05-03 06:30 Shanghai — GREEN PASS, 7/7 locked format

### Implementation

1. Update Agent Input Contract with locked output format ✔ DONE
2. Modify build_agent_input_slim.py to inject VALID_RESULT_IDS ✔ DONE
3. Require citation syntax:
   - [result_ids: ...] ✔ DONE
   - [based_on: ...] ✔ DONE
4. Preserve Scrubber + Validator enforcement ✔ UNCHANGED
5. Confirm scrubber and validator output ✔ CONFIRMED (2026-05-02)
6. Confirm PASS or acceptable WARN ✔ CONFIRMED (2026-05-02 and 2026-05-03)
7. Two consecutive successful deliveries ✔ CONFIRMED (2026-05-02 and 2026-05-03)

### Status

→ COMPLETE — operator approved 2026-05-03

---

## 🚧 PHASE 6.4 — RETRIEVAL QUALITY STABILIZATION (ACTIVE)

### Objective

Stabilize retrieval quality so the evidence pool consistently supports
high-quality agent output across all regions and providers.

### Exit Criteria (from OPENCLAW-PEC-001)

1. Brave retrieval consistently produces fresh, relevant results
2. Baidu contributing meaningful results (not stub / empty)
3. Query freshness enforced: past 24 hours / explicit date precision queries active
4. Filtering retains high-quality signals and discards noise reliably
5. retrieval_package contains adequate coverage for all defined regions
6. Partial retrieval (one provider down) handled gracefully without delivery failure

### Operating Methodology (LOCKED)

All Phase 6.4 work follows this strict sequence:

1. **Observe** — what did each provider return? what survived normalization, dedup, filtering?
2. **Explain** — why were results kept or removed? where in the pipeline did loss occur?
3. **Confirm** — is the explanation sufficient to act on?
4. **Adjust** — only after step 3 is confirmed. If step 3 fails, return to Observe.

If visibility is insufficient to answer step 2, fix observability first. A missing log
is an observability gap, not a retrieval problem — treat it as such.

For Baidu specifically: the correct diagnostic question is not "Baidu is broken" but
**"Where does Baidu signal disappear in the pipeline?"** Possible loss points:
retrieval (no results), normalization (malformed/discarded), dedup (merged away),
filtering (rejected), or scoring (not selected). Locate the loss point before acting.

### Hard Execution Rule (LOCKED)

No change may be made unless all three conditions are met:

1. The exact loss point is identified
2. The mechanism of loss is understood
3. The expected effect of the change is explicit

If any condition is missing — no action is taken.

### Success Criteria (Phase 6.4)

Success is NOT measured as better output, more sources, or stronger narrative.

Success is: **you can fully explain system behavior across runs.**

### Known Baseline Issues

- Baidu returning 0 results (6 errors per run) — SerpAPI key inactive, expected 2026-05-05
- Retrieval operating on Brave only — overall_status=partial on all runs
- Regional coverage dependent on single provider

### Work Completed (2026-05-04)

✔ Baidu failure root cause confirmed — SerpAPI 401 Unauthorized on all 6 queries;
  loss point is retrieval_source boundary; pipeline logic not implicated

✔ Issue #39 identified and resolved — `$FINAL` variable in run_light_to_lark.sh was
  not reloaded after scrubber promotion; Lark delivery was receiving pre-scrubber
  content; single-line fix applied and live-run verified (09:57 Shanghai, HTTP 200,
  GREEN PASS)

✔ Issue #40 identified and resolved — brave_executor.py was not passing `freshness`
  parameter to Brave API; query text time windows ("today", "past week") had no
  mechanical enforcement; fix applied: precision queries → `freshness=pd`,
  recall queries → `freshness=pw`; live-run verified (09:57 Shanghai, fresh content
  confirmed delivered)

### Remaining Work

→ Baidu investigation: confirm Baidu retrieval resumes when SerpAPI key activates
  (expected 2026-05-05). Diagnostic question: does Baidu return results at the
  retrieval_source layer, or does loss occur downstream?

→ Issue #37: offline script save step — operator decision pending

### Status

→ ACTIVE — Brave retrieval quality stabilized; Baidu investigation pending key activation

---

## 🧭 PHASE 6 EXIT CRITERIA

✔ End-to-end runs succeed
✔ Validator consistently passes
✔ Scrubber prevents invalid output
✔ Delivery reliable across runs
✔ Locked output format enforced (Phase 6.3a) ✔ COMPLETE

STATUS: IN PROGRESS

---

## ⏭ NEXT STEP

→ When SerpAPI key activates (2026-05-05), run single live test and bring
  baidu_raw.json here for post-run analysis.
