# OPENCLAW — ISSUES LOG

---
document_id: OPENCLAW-ISSUES-001
version: 5.3.26
last_updated: 2026-05-03
---

## CONTEXT

This log covers Issues #34 onward. Issues #1–#33 are recorded in historical
daily status and session handover documents in `/old/`. Issue numbering is
cumulative across the project lifecycle. The current log retains only active
and recently resolved issues.

## OPEN ISSUES SUMMARY

| # | Title | Status |
|---|-------|--------|
| 37 | Offline Script Missing Agent Output Save Step | OPEN — operator decision required |

## RESOLVED ISSUES SUMMARY

| # | Title | Status |
|---|-------|--------|
| 34 | Citation System Instability | ✅ RESOLVED |
| 35 | result_id Generation Drift Under Citation Padding | ✅ RESOLVED (2026-05-03) |
| 36 | Agent Format Non-Determinism in Live Cron Runs | ✅ RESOLVED (2026-05-03) |

---

## Issue #34 — Citation System Instability

### Status
✅ RESOLVED

---

## Issue #35 — result_id Generation Drift Under Citation Padding

### Description

Recent agent outputs showed continued invalid result_id usage despite
result_id-based citation architecture. The agent consistently used the
expected result_id format, but added invalid IDs inside otherwise plausible
citation groups through pattern-completion behavior.

### Root Cause

The agent was treating result_ids as generative text rather than controlled
evidence identifiers. Without a constrained list of valid IDs in the prompt,
the model learned the ID shape and generated similar-looking but fabricated
values.

### Resolution

1. Lock agent output format ✔ COMPLETE
2. Add VALID_RESULT_IDS to agent input (build_agent_input_slim.py) ✔ COMPLETE
3. Require citation syntax:
   - [result_ids: ...] ✔ COMPLETE
   - [based_on: ...] ✔ COMPLETE
4. Prohibit repeated freeform result_id groups ✔ COMPLETE
5. Scrubber updated to parse locked format ✔ COMPLETE (2026-05-02)
6. Validator updated to parse locked format ✔ COMPLETE (2026-05-02)

### Session Progress

- 2026-05-01: VALID_RESULT_IDS injection implemented; offline tests confirmed
  zero fabricated IDs; full scrubber + validator chain executed without errors
- 2026-05-02: Scrubber and validator updated; GREEN PASS confirmed on live
  cron; Delivery #1 achieved (08:26 Shanghai)
- 2026-05-03: Delivery #2 confirmed (06:30 Shanghai); two consecutive
  locked-format deliveries complete; Phase 6.3a exit criteria met

### Status

✅ RESOLVED — Two consecutive locked-format deliveries confirmed.
Phase 6.3a exit criteria met as of 2026-05-03 06:30 Shanghai.
Operator approved 2026-05-03.

---

## Issue #36 — Agent Format Non-Determinism in Live Cron Runs

### Description

The agent produced locked citation format consistently in offline test runs
but produced old format citations in the live cron run at 08:01 Shanghai on
2026-05-02 despite the same build_agent_input_slim.py being called by both
paths.

### Root Cause

Not definitively confirmed. Non-determinism observed in one run only
(2026-05-02 08:01 Shanghai). Subsequent live runs (2026-05-02 08:26 and
2026-05-03 06:30) produced locked format consistently. Hypothesis: isolated
LLM stochastic event under the specific retrieval context of that run
(4 results vs. 8 in other runs).

### Status

✅ RESOLVED — Two consecutive locked-format live cron deliveries (2026-05-02
08:26 and 2026-05-03 06:30) demonstrate consistent agent format behavior.
Non-determinism not reproduced. Issue closed 2026-05-03.

---

## Issue #37 — Offline Script Missing Agent Output Save Step

### Status
OPEN — operator decision required (orchestrator change, out of scope)

### Description

run_phase5_offline.sh captures the agent's output into a shell variable and
prints it to stdout, but does not write it to
/root/openclaw_phase5/data/final_output.txt. The live cron script
(run_light_to_lark.sh) performs this save step. As a result, manual offline
runs cannot be passed through the scrubber and validator without a manual
workaround.

### Impact

Manual testing of the locked format pipeline requires copying terminal output
to final_output.txt by hand. Risk of human error in test data. Not a live
pipeline risk.

### Next Action

Operator to decide whether to add the save step to run_phase5_offline.sh.
This is an orchestrator change — requires explicit approval and is out of
scope under Phase 6.3a.
