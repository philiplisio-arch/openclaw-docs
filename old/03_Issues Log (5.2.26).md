# OPENCLAW — ISSUES LOG

---
document_id: OPENCLAW-ISSUES-001
version: 5.2.26
last_updated: 2026-05-02
---

## CONTEXT

This log covers Issues #34 onward. Issues #1–#33 are recorded in historical
daily status and session handover documents in `/old/`. Issue numbering is
cumulative across the project lifecycle. The current log retains only active
and recently resolved issues.

## OPEN ISSUES SUMMARY

| # | Title | Status |
|---|-------|--------|
| 35 | result_id Generation Drift Under Citation Padding | IN PROGRESS — Delivery #1 of 2 achieved (2026-05-02 08:26 Shanghai) |
| 36 | Agent Format Non-Determinism in Live Cron Runs | MONITORING — locked format confirmed in 08:26 delivery |
| 37 | Offline Script Missing Agent Output Save Step | OPEN — operator decision required |

## RESOLVED ISSUES SUMMARY

| # | Title | Status |
|---|-------|--------|
| 34 | Citation System Instability | ✅ RESOLVED |

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

### Resolution Plan

1. Lock agent output format ✔ COMPLETE
2. Add VALID_RESULT_IDS to agent input (build_agent_input_slim.py) ✔ COMPLETE
3. Require citation syntax:
   - [result_ids: ...] ✔ COMPLETE
   - [based_on: ...] ✔ COMPLETE
4. Prohibit repeated freeform result_id groups ✔ COMPLETE
5. Scrubber updated to parse locked format ✔ COMPLETE (2026-05-02)
6. Validator updated to parse locked format ✔ COMPLETE (2026-05-02)

### Session 2026-05-01 Progress

- VALID_RESULT_IDS injection implemented in build_agent_input_slim.py
- Locked citation syntax rules added to system prompt
- Output format template updated with concrete locked-format examples
- Three offline test runs completed — all confirmed correct format and zero
  fabricated IDs
- Full scrubber + validator chain executed without errors

### Session 2026-05-02 Progress

- Scrubber and validator output file paths confirmed
- Scrubber CITATION_RE updated to recognise locked format ([result_ids:] /
  [based_on:]) and old format — operator approved as phase completion item
- Validator CITATION_RE and group reference updated to match — operator
  approved as phase completion item
- GREEN PASS confirmed on live cron output (2026-05-02 08:01 Shanghai)
- Scrubber: 7 citation groups, 0 unsupported, output deliverable
- Validator: 8 citations checked, 8 matched, 0 failures
- Live cron run used old citation format — locked format non-determinism
  flagged as Issue #36
- Manual live run at 08:26 Shanghai confirmed locked format end-to-end —
  GREEN PASS, delivered to Lark — Delivery #1 of 2 achieved

### Status

IN PROGRESS — Delivery #1 achieved (2026-05-02 08:26 Shanghai); one
consecutive locked-format delivery remaining for Phase 6.3a exit

### Success Criteria

- Agent uses locked citation syntax ✔ CONFIRMED in live delivery
- Invalid result_ids are reduced or eliminated ✔
- Scrubber can parse all citation groups deterministically ✔ CONFIRMED
- Validator returns PASS or controlled WARN ✔ CONFIRMED
- Two consecutive successful locked-format Lark deliveries → 1 of 2 COMPLETE

---

## Issue #36 — Agent Format Non-Determinism in Live Cron Runs

### Status
OPEN

### Description

The agent produced locked citation format ([result_ids:] / [based_on:])
consistently in three offline test runs on 2026-05-01 and in the manual
offline run on 2026-05-02 at 07:40 Shanghai. The live cron run at 08:01
Shanghai on 2026-05-02 produced old format citations (result_id: ...) despite
the same build_agent_input_slim.py being called by both paths. The LLM is
not consistently following the locked format instruction.

### Root Cause

Unconfirmed. Possible causes: (1) LLM non-determinism — the model reverts to
old format under certain retrieval conditions or context lengths; (2) the
VALID_RESULT_IDS injection in build_agent_input_slim.py is reaching the agent
differently in the live path vs. offline test; (3) the live cron run used
different results (4 vs. 8) which may have triggered different agent behaviour.

### Impact

Phase 6.3a exit requires two consecutive locked-format deliveries. Until
format consistency is confirmed in live runs, exit criteria cannot be met.

### Next Action

Monitor next cron run output. If old format recurs, investigate
build_agent_input_slim.py output in the live path and compare agent prompt
received in live vs. offline runs.

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
