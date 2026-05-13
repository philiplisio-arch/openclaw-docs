# OPENCLAW — EXECUTION PLAN

---
document_id: OPENCLAW-EXEC-001
version: 5.5.26
last_updated: 2026-05-05
status: ACTIVE
---

## 🔷 PHASE 6 — CURRENT WORK

### Sub-Phase: 6.5 — Conflict Handling Upgrade

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

* Pre-scrubber agent output not persisted on live cron runs (forensic gap on live pipeline)

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
   - (result_id: ...) ✔ DONE — enforced by validator phase6_v2_result_id_match
4. Preserve Scrubber + Validator enforcement ✔ UNCHANGED
5. Confirm scrubber and validator output ✔ CONFIRMED (2026-05-02)
6. Confirm PASS or acceptable WARN ✔ CONFIRMED (2026-05-02 and 2026-05-03)
7. Two consecutive successful deliveries ✔ CONFIRMED (2026-05-02 and 2026-05-03)

### Status

→ COMPLETE — operator approved 2026-05-03

---

## ✅ PHASE 6.4 — RETRIEVAL QUALITY STABILIZATION (COMPLETE)

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

1. **Observe** — what did each provider return? what survived normalization, dedup,
   filtering?
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

- ~~Baidu returning 0 results (6 errors per run) — SerpAPI key inactive~~ RESOLVED 2026-05-05
- ~~Retrieval operating on Brave only — overall_status=partial on all runs~~ RESOLVED 2026-05-05

### Work Completed (2026-05-04)

✔ Baidu failure root cause confirmed — SerpAPI 401 Unauthorized on all 6 queries;
  loss point is retrieval_source boundary; pipeline logic not implicated

✔ Issue #39 identified and resolved — $FINAL variable in run_light_to_lark.sh was
  not reloaded after scrubber promotion; Lark delivery was receiving pre-scrubber
  content; single-line fix applied and live-run verified (09:57 Shanghai, HTTP 200,
  GREEN PASS)

✔ Issue #40 identified and resolved — brave_executor.py was not passing freshness
  parameter to Brave API; query text time windows ("today", "past week") had no
  mechanical enforcement; fix applied: precision queries → freshness=pd,
  recall queries → freshness=pw; live-run verified (09:57 Shanghai, fresh content
  confirmed delivered)

### Work Completed (2026-05-05)

✔ Baidu diagnostic complete — SerpAPI key confirmed active; baidu_raw.json:
  result_count=54, error_count=0 across all 6 queries. Loss point confirmed as
  retrieval_source boundary only. Pipeline logic (normalization, dedup, filtering)
  confirmed functional on first live Baidu run.

✔ Dual-provider retrieval confirmed operational — live run at 08:59 Shanghai:
  valid_ids_loaded=11, 21/21 citations matched, GREEN PASS. Baidu contributing
  6 result_ids from 54 raw results. Chinese-language sources present in delivery.

✔ Validator Layer Spec updated — validator_version corrected to
  phase6_v2_result_id_match; citation format documented. Operator approved 2026-05-05.

✔ Issue #41 resolved — scrub_result_ids.py line 35 changed from
  `return "(UNSUPPORTED_RESULT_ID_REMOVED)"` to `return ""`. Operator authorized
  2026-05-05. Synthetic test confirmed silent removal behavior.

✔ Issue #37 resolved — run_phase5_offline.sh modified to pipe agent output
  through `tee /root/openclaw_phase5/data/final_output.txt`. Operator authorized
  2026-05-05. Syntax check passed.

### Remaining Work

✔ Live pipeline test complete (10:22 Shanghai) — unsupported_groups=0, ids_removed=2,
  15/15 GREEN PASS, delivered. No placeholder text in output. Issue #41 fix active.

→ Monitor dual-provider retrieval across successive scheduled 06:30 runs to
  confirm Baidu stability is sustained

### Status

→ COMPLETE — Operator approved 2026-05-05. All exit criteria satisfied. Dual-provider stable,
  issues resolved, live test confirmed clean.

---

---

## 🚧 PHASE 6.5 — CONFLICT HANDLING UPGRADE (ACTIVE)

### Objective

Surface conflicting claims across sources explicitly to the operator. Eliminate
silent conflict suppression. Log conflict classification per run.

### Exit Criteria (from OPENCLAW-PEC-001)

1. Conflicting claims across sources explicitly surfaced to operator
2. No silent conflict suppression
3. Conflict classification logged per run

### Scope (Operator Defined 2026-05-05)

- **Conflict type**: Factual contradictions only (not framing or emphasis differences)
- **Surfacing**: Conditional CONFLICT FLAGS section in Lark delivery + conflict_log.json per run
- **Classification**: Three tiers — FACTUAL/HIGH, DIRECTIONAL/MEDIUM, NUMERIC/LOW
- **Conditional**: Section omitted from Lark entirely when conflict_count = 0

### Implementation (Complete 2026-05-05)

Three layers modified via Claude Code:

1. **build_agent_input_slim.py** — CONFLICTS output section added to locked format.
   Agent outputs one line per conflict in typed format; section omitted if no conflicts.
   Format: `[TYPE:FACTUAL|SEVERITY:HIGH] Topic: <topic>. Claim A (result_id: ...): <claim>. Claim B (result_id: ...): <claim>.`

2. **scrub_result_ids.py** — `split_conflicts()` extracts CONFLICTS block (matched on
   `^CONFLICTS\s*$`), strips it from scrubbed body, writes conflict_log.json per run.
   New log lines: `conflicts_extracted=true/false`, `conflict_count=N`.

3. **run_light_to_lark.sh** — reads `conflict_count` from conflict_log.json after FINAL
   reload. If non-zero, reads `conflicts_raw`, pipes through sed to prefix lines with
   ⚠ (FACTUAL), ↔ (DIRECTIONAL), ~ (NUMERIC), appends CONFLICT FLAGS block to Lark message.
   Guard clauses (`|| echo 0`, `|| echo ""`) prevent delivery failure on missing log.

### Work Completed (2026-05-05)

✔ Scope defined — operator approved
✔ Three-layer implementation complete — agent prompt, scrubber, delivery script
✔ Live test (10:44 Shanghai) — conflict_count=0, clean delivery, conflict_log.json written
✔ Zero-conflict path confirmed

### Remaining Work

→ Synthetic test — inject non-zero conflict_log.json, verify CONFLICT FLAGS in Lark
  with correct ⚠/↔/~ prefixes

→ Monitor 06:30 scheduled run — dual-provider stability check

### Status

→ ACTIVE — implementation complete; synthetic test pending

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

→ Synthetic test — verify non-zero conflict path end-to-end
→ Monitor 06:30 scheduled run — dual-provider stability check
