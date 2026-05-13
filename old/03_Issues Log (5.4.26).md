# OPENCLAW — ISSUES LOG

---
document_id: OPENCLAW-ISSUES-001
version: 5.4.26
last_updated: 2026-05-04
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
| 40 | 3-Day Filter Threshold Creates Fragility in Off-Schedule Runs | ✅ RESOLVED (2026-05-04) |

## RESOLVED ISSUES SUMMARY

| # | Title | Status |
|---|-------|--------|
| 34 | Citation System Instability | ✅ RESOLVED |
| 35 | result_id Generation Drift Under Citation Padding | ✅ RESOLVED (2026-05-03) |
| 36 | Agent Format Non-Determinism in Live Cron Runs | ✅ RESOLVED (2026-05-03) |
| 39 | Lark Delivery Uses Pre-Scrubber Content | ✅ RESOLVED (2026-05-04) |
| 40 | 3-Day Filter Threshold Creates Fragility in Off-Schedule Runs | ✅ RESOLVED (2026-05-04) |

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

---

## Issue #39 — Lark Delivery Uses Pre-Scrubber Content

### Status
OPEN — operator decision required

### Description

In `run_light_to_lark.sh`, the variable `$FINAL` is built from the raw agent
output before the scrubber runs. After `scrub_result_ids.py` removes invalid
citations and promotes `final_output_scrubbed.txt` to `final_output.txt`,
`$FINAL` in memory is never reloaded from the updated file. The Lark push
sends `$FINAL` — the pre-scrubber content — not the scrubbed output.

### Impact

The scrubber and validator are working correctly. The enforcement chain ran on
the 2026-05-04 delivery and correctly removed `res_791abd0e2ace` from the
scrubbed file. The validator confirmed PASS on the clean output. However, Lark
received `$FINAL` (pre-scrubber), which retained `res_791abd0e2ace` in two
citation groups (Executive Take Middle East claim; Advisory Layer energy
advisory). The fabricated citation bypassed enforcement at the final delivery
step.

Confirmed via:
- `res_791abd0e2ace` NOT PRESENT in `final_output_scrubbed.txt`
- validator returned PASS on 8 valid citations (no res_791abd0e2ace)
- `res_791abd0e2ace` present in Lark delivery

### Root Cause

`$FINAL` is assigned once from raw output and never refreshed after scrubbing.
The scrubber's sanitized output exists on disk but is not reloaded into the
delivery variable.

### Fix

Reload `$FINAL` from `final_output.txt` immediately after the scrubber
promotes the scrubbed output:

```bash
FINAL=$(cat /root/openclaw_phase5/data/final_output.txt)
```

Single-line change to `run_light_to_lark.sh`. Requires operator authorization
as a pipeline script modification.

### Resolution

Operator authorized fix on 2026-05-04. Single line inserted in
`run_light_to_lark.sh` at line 168, immediately after the scrubber promotion
step:

```bash
FINAL=$(cat /root/openclaw_phase5/data/final_output.txt)
```

Verified via grep — line 168 confirmed present. From the next run, Lark will
receive the scrubbed output, not the raw agent output.

### Status
✅ RESOLVED — 2026-05-04, operator approved

---

## Issue #40 — 3-Day Filter Threshold Creates Fragility in Off-Schedule Runs

### Status
OPEN — Phase 6.4 investigation

### Description

The filter requires results to be within 3 days old (`within_last_3_days`:
`0 <= delta.days <= 3`). Dates are extracted from URL patterns. The
`timestamp: None` field in normalized_results.json is not the cause — the
filter extracts dates from URLs directly and does not use the normalizer's
timestamp field.

On the 2026-05-04 09:30 manual test run, Brave returned 60 results (50 after
dedup). All URLs contained dates from 2026-04-24 to 2026-04-27 — 7 to 10 days
old as of 2026-05-04. The filter correctly dropped all 50 as stale.

### Root Cause

The 3-day threshold is calibrated for the 06:30 Shanghai scheduled run, which
executes at 22:30 UTC (still May 3 UTC). At that time, April 30 content is
exactly 3 days old — within threshold. By 09:30 Shanghai (01:30 UTC May 4),
"today" has advanced to May 4 and the same April 30 content would be 4 days
old — outside threshold.

Off-schedule runs also hit a different Brave result profile. The 09:30 run
returned content from April 24–27 — older articles that would fail the
threshold regardless of run time.

The system's reliability therefore depends on two conditions both being true:
1. The run occurs close enough to 06:30 Shanghai (22:30 UTC) that "today"
   is still the prior UTC date
2. Brave serves content from the past 3 calendar days at that time

### Impact

Off-schedule runs will consistently produce overall_status=empty when Brave
serves content outside the 3-day window. Scheduled 06:30 runs are not
currently affected. No delivery failure — the fallback output is produced
correctly. But manual test runs cannot be relied on to produce real content.

### Note

The filter behaviour is correct. No filter bug is present. This is a
calibration and coverage question for Phase 6.4.

### Resolution

Root cause confirmed via code inspection: `brave_executor.py` passed no
freshness or date parameters to the Brave API. Brave ranked by relevance,
returning results regardless of age. The query text ("today", "past week")
had no mechanical effect on date filtering.

Fix applied 2026-05-04 with operator authorization. Added `freshness` parameter
to the Brave API call, keyed by `query_type`:
- Precision queries (`us_p1`, `eu_p1`, `me_p1`): `"freshness": "pd"` — past 24 hours
- Recall queries (`us_r1`, `eu_r1`, `me_r1`): `"freshness": "pw"` — past 7 days

Verified: all 6 queries carry correct `query_type` field; freshness routing
confirmed correct for every query slot. Backup saved:
`brave_executor.py.bak_20260504`.

Live run verification complete — manual run at 09:57 Shanghai on 2026-05-04 confirmed.
Brave returned fresh content (CNN Business EV article, Canton Fair/Xinhua). Filter passed
results, scrubber exit=0, validator GREEN PASS (4/4 citations matched), HTTP 200 delivered.

### Status
✅ RESOLVED — 2026-05-04, operator authorized, live run verified

### Identified
2026-05-04
