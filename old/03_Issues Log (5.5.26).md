# OPENCLAW — ISSUES LOG

---
document_id: OPENCLAW-ISSUES-001
version: 5.5.26c
last_updated: 2026-05-05
---

## CONTEXT

This log covers Issues #34 onward. Issues #1–#33 are recorded in historical
daily status and session handover documents in `/old/`. Issue numbering is
cumulative across the project lifecycle. The current log retains only active
and recently resolved issues.

## OPEN ISSUES SUMMARY

No open issues.

## RESOLVED ISSUES SUMMARY

| # | Title | Status |
|---|-------|--------|
| 34 | Citation System Instability | ✅ RESOLVED |
| 35 | result_id Generation Drift Under Citation Padding | ✅ RESOLVED (2026-05-03) |
| 36 | Agent Format Non-Determinism in Live Cron Runs | ✅ RESOLVED (2026-05-03) |
| 37 | Offline Script Missing Agent Output Save Step | ✅ RESOLVED (2026-05-05) |
| 39 | Lark Delivery Uses Pre-Scrubber Content | ✅ RESOLVED (2026-05-04) |
| 40 | 3-Day Filter Threshold Creates Fragility in Off-Schedule Runs | ✅ RESOLVED (2026-05-04) |
| 41 | Scrubber Placeholder Text Delivered to Lark on Unsupported Citation Format | ✅ RESOLVED (2026-05-05) |

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
   - (result_id: ...) ✔ COMPLETE
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
✅ RESOLVED — 2026-05-05, operator authorized

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

### Contributing Factor

Issue #37 also means the pre-scrubber agent output is not saved on live runs,
limiting post-run forensic analysis when issues like #41 occur.

### Resolution

Operator authorized 2026-05-05. `run_phase5_offline.sh` modified to pipe agent
output through `tee /root/openclaw_phase5/data/final_output.txt` at end of
docker exec block. `set -o pipefail` confirmed present — non-zero exit
propagates correctly through pipe. Syntax check passed (`bash -n`).

### Status
✅ RESOLVED — 2026-05-05, operator authorized

---

## Issue #39 — Lark Delivery Uses Pre-Scrubber Content

### Status
✅ RESOLVED — 2026-05-04, operator approved

### Description

In `run_light_to_lark.sh`, the variable `$FINAL` is built from the raw agent
output before the scrubber runs. After `scrub_result_ids.py` removes invalid
citations and promotes `final_output_scrubbed.txt` to `final_output.txt`,
`$FINAL` in memory is never reloaded from the updated file. The Lark push
sends `$FINAL` — the pre-scrubber content — not the scrubbed output.

### Root Cause

`$FINAL` is assigned once from raw output and never refreshed after scrubbing.

### Resolution

Operator authorized fix on 2026-05-04. Single line inserted in
`run_light_to_lark.sh` at line 168, immediately after the scrubber promotion
step:

```bash
FINAL=$(cat /root/openclaw_phase5/data/final_output.txt)
```

Verified via grep — line 168 confirmed present.

### Status
✅ RESOLVED — 2026-05-04, operator approved

---

## Issue #40 — 3-Day Filter Threshold Creates Fragility in Off-Schedule Runs

### Status
✅ RESOLVED — 2026-05-04, operator authorized, live run verified

### Description

The filter requires results to be within 3 days old. On the 2026-05-04 09:30
manual test run, Brave returned 60 results (50 after dedup), all from
2026-04-24 to 2026-04-27 — 7 to 10 days old. The filter correctly dropped
all 50 as stale.

### Root Cause

brave_executor.py passed no freshness or date parameters to the Brave API.
Query text time windows ("today", "past week") had no mechanical enforcement.

### Resolution

Added `freshness` parameter to the Brave API call, keyed by `query_type`:
- Precision queries: `"freshness": "pd"` — past 24 hours
- Recall queries: `"freshness": "pw"` — past 7 days

Live run verified 09:57 Shanghai 2026-05-04. Backup saved:
brave_executor.py.bak_20260504.

### Status
✅ RESOLVED — 2026-05-04, operator authorized, live run verified

### Identified
2026-05-04

---

## Issue #41 — Scrubber Placeholder Text Delivered to Lark on Unsupported Citation Format

### Status
✅ RESOLVED — 2026-05-05, operator authorized

### Description

When the scrubber encounters a citation group in an unrecognized format, it
replaces the group with the literal string `(UNSUPPORTED_RESULT_ID_REMOVED)`
rather than silently removing it. This placeholder propagates into
`final_output.txt`, passes the validator (which does not treat it as a
citation), passes the delivery gate, and is delivered to Lark subscribers
verbatim.

### Observed

2026-05-05 09:49 Shanghai run — `unsupported_groups=3`. Three bullets in the
delivered output contained `(UNSUPPORTED_RESULT_ID_REMOVED)` in place of a
citation group:

- EXECUTIVE TAKE — China EV bullet
- ADVISORY LAYER — European automotive bullet
- ADVISORY LAYER — China UN Security Council/Middle East diplomacy bullet

The claim text in each bullet is intact. The citation is absent. The
placeholder string is visible to Lark subscribers.

### Root Cause

The scrubber's fallback behavior for unrecognized citation formats inserts a
visible placeholder string instead of silently removing the group. The exact
unrecognized format used by the agent on this run is unknown — the pre-scrubber
agent output is not saved (Issue #37 gap). The agent produced a mixed citation
format on this run: 5 groups in the correct `(result_id: ...)` format, 3 in an
unrecognized format. LLM stochastic behavior.

### Impact

Client-facing Lark output contains visible `(UNSUPPORTED_RESULT_ID_REMOVED)`
text on any run where the agent produces a mixed citation format. Frequency is
unpredictable — depends on agent stochasticity. Confirmed once across four
runs observed today. No delivery failure — enforcement chain is sound.
Presentation quality is degraded.

### Contributing Factor

Issue #37 (offline script missing save step) means the pre-scrubber agent
output is not available for post-run inspection on live runs. The exact
unrecognized format cannot be confirmed retroactively.

### Resolution

Operator authorized 2026-05-05. `scrub_result_ids.py` line 35 changed:
- Before: `return "(UNSUPPORTED_RESULT_ID_REMOVED)"`
- After: `return ""`

Behavior: when a citation group matches CITATION_RE but contains no valid
result_ids after ID extraction and validation (Option A path), the group is
now silently removed. Claim text is retained; citation group is dropped with
no visible artefact. Synthetic test confirmed: valid citations preserved,
hallucinated and format-only groups silently removed,
`(UNSUPPORTED_RESULT_ID_REMOVED)` no longer generated.

Note: any `(UNSUPPORTED_RESULT_ID_REMOVED)` strings already present as plain
text in prior deliveries do not match CITATION_RE and pass through unchanged —
this is correct behavior.

### Identified
2026-05-05

### Status
✅ RESOLVED — 2026-05-05, operator authorized
