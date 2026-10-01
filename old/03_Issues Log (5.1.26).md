# OPENCLAW — ISSUES LOG

---
document_id: OPENCLAW-ISSUES-001
version: 5.1.26a
last_updated: 2026-05-01
---

## CONTEXT

This log covers Issues #34 onward. Issues #1–#33 are recorded in historical
daily status and session handover documents in `/old/`. Issue numbering is
cumulative across the project lifecycle. The current log retains only active
and recently resolved issues.

## OPEN ISSUES SUMMARY

| # | Title | Status |
|---|-------|--------|
| 35 | result_id Generation Drift Under Citation Padding | IN PROGRESS — implementation complete, confirmation pending |

## RESOLVED ISSUES SUMMARY

| # | Title | Status |
|---|-------|--------|
| 34 | Citation System Instability | ✅ RESOLVED |

---

## Issue #34 — Citation System Instability

---

### Status

✅ RESOLVED

---

## Issue #35 — result_id Generation Drift Under Citation Padding

---

### Description

Recent agent outputs showed continued invalid result_id usage despite
result_id-based citation architecture. The agent consistently used the
expected result_id format, but added invalid IDs inside otherwise plausible
citation groups through pattern-completion behavior.

---

### Root Cause

The agent was treating result_ids as generative text rather than controlled
evidence identifiers. Without a constrained list of valid IDs in the prompt,
the model learned the ID shape and generated similar-looking but fabricated
values.

---

### Resolution Plan

1. Lock agent output format ✔ COMPLETE
2. Add VALID_RESULT_IDS to agent input (build_agent_input_slim.py) ✔ COMPLETE
3. Require citation syntax:
   - [result_ids: ...] ✔ COMPLETE
   - [based_on: ...] ✔ COMPLETE
4. Prohibit repeated freeform result_id groups ✔ COMPLETE
5. Preserve scrubber removal of invalid IDs ✔ UNCHANGED
6. Preserve validator PASS/WARN/FAIL enforcement ✔ UNCHANGED

### Session 2026-05-01 Progress

- VALID_RESULT_IDS injection implemented in build_agent_input_slim.py
- Locked citation syntax rules added to system prompt
- Output format template updated with concrete locked-format examples
- Three offline test runs completed — all confirmed correct format and zero
  fabricated IDs
- Full scrubber + validator chain executed without errors
- Scrubber and validator output file paths not yet confirmed

---

### Status

IN PROGRESS — all implementation steps complete; confirmation of
scrubber/validator output and two consecutive successful deliveries pending

### Success Criteria

- Agent uses locked citation syntax ✔
- Invalid result_ids are reduced or eliminated ✔ (zero in all test runs)
- Scrubber can parse all citation groups deterministically → PENDING CONFIRMATION
- Validator returns PASS or controlled WARN → PENDING CONFIRMATION
- Two consecutive successful Lark deliveries → PENDING
