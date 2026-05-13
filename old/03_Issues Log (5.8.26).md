# OPENCLAW — ISSUES LOG

---
document_id: OPENCLAW-ISSUES-001
version: 5.8.26
last_updated: 2026-05-08
---

## CONTEXT

This log covers Issues #34 onward. Issues #1–#33 are recorded in historical
daily status and session handover documents in `/old/`. Issue numbering is
cumulative across the project lifecycle. The current log retains only active
and recently resolved issues.

## OPEN ISSUES SUMMARY

No open issues.

## TRACKED INPUTS — FUTURE PHASE

| # | Title | Origin |
|---|-------|--------|
| T-01 | Freshness signaling not distinguished in output | Advisory note 2026-05-08 |
| T-02 | Source authority classification — lower-authority sources uncalibrated | Advisory note 2026-05-08 |
| T-03 | Chinese-source diversity — not yet consistently rich across categories | Advisory note 2026-05-08 |
| T-04 | Advisory language calibration — claim strength exceeds evidence in places | Advisory note 2026-05-08 |
| T-05 | Middle East content drift — coverage not consistently anchored to China linkage | Advisory note 2026-05-08 |
| T-06 | scrubber_report.json not found at expected path on 2026-05-08 06:32 run | Log observation 2026-05-08 |

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
| 42 | SerpAPI Key Invalid — Baidu Retrieval Failure | ✅ RESOLVED (2026-05-06) |
| 43 | Agent Result ID Fabrication Rate Elevated | ✅ RESOLVED (2026-05-07) |
| 44 | Valid Sources Not Surfacing in Delivered Output | ✅ RESOLVED (2026-05-08) |

---

## Tracked Input T-01 — Freshness Signaling Not Distinguished in Output

### Origin
Advisory note 2026-05-08

### Description

The delivered report mixes precision-window (past 24 hours) and recall-window
(past 7 days) material without distinguishing them. For a daily intelligence
product, the Executive Take should privilege fresh material and clearly signal
which bullets are based on same-day developments vs. continuing context.

### Context

The current dual-window query design (precision=pd, recall=pw) is intentional
and correctly implemented per Phase 6.4. The gap is in how this material is
presented to the end reader — not in retrieval behavior.

### Scope

Agent prompt or output format concern. Does not require retrieval changes.
Phase 6.9–6.11 or Phase 7 territory.

---

## Tracked Input T-02 — Source Authority Classification Uncalibrated

### Origin
Advisory note 2026-05-08

### Description

Lower-authority platform/contributor content (e.g., `caifuhao.eastmoney.com`)
is cited alongside tier-1 sources (Reuters, CCTV) without qualification. For a
client-grade intelligence product, source authority should be visible or at
minimum inform how claims are framed.

### Recommended Classification Framework

- **Higher-authority / official:** CCTV, Xinhua, official ministries/regulators,
  state outlets
- **Established financial/business press:** Sina Finance, Yicai, Caixin,
  21st Century Business Herald, Securities Times, China Securities Journal
- **Platform/contributor or lower-authority:** caifuhao.eastmoney.com and
  similar creator/contributor pages

### Scope

Retrieval filtering/scoring or agent prompt guidance. Must not be addressed
via source biasing in query templates (prohibited per current query rules).
Phase 6.9–6.11 or Phase 7 territory.

---

## Tracked Input T-03 — Chinese-Source Diversity Not Yet Consistently Rich

### Origin
Advisory note 2026-05-08

### Description

Chinese-language sources are present and improving (confirmed in 2026-05-08
delivery), but coverage is not yet consistently distributed across source
categories. A mature China monitoring brief should draw from official/regulatory
sources, state media, Chinese financial press, market-data/brokerage platforms,
and credible sector-specific outlets.

### Constraint

Source diversity must not be addressed by hardcoding preferred publishers into
query templates. Source selection belongs to retrieval/filtering/scoring.

### Scope

Expansion layer (Phase 6.9–6.11) or Phase 7 territory.

---

## Tracked Input T-04 — Advisory Language Calibration

### Origin
Advisory note 2026-05-08

### Description

Several phrases in the 2026-05-08 delivered output are stronger than the
cited evidence directly supports: "must immediately re-evaluate," "urgently
accelerate innovation," "unprecedented risks," "heightened and prolonged
volatility." Client-grade advisory output should match claim strength to
the evidence base.

### Preferred Style Example

> Companies should review whether current compliance frameworks account for
> potentially conflicting U.S. and Chinese legal obligations.

Rather than:

> Companies must immediately re-evaluate compliance frameworks.

### Scope

Agent prompt guidance — advisory language calibration. Phase 6.9–6.11 or
Phase 7 territory.

---

## Tracked Input T-05 — Middle East Content Drift

### Origin
Advisory note 2026-05-08

### Description

The Middle East section in the 2026-05-08 delivery included Shell profits,
U.S. crude exports, Strait of Hormuz risk, and UAE capital projects without
consistently anchoring these items to China exposure, Chinese company
involvement, or multinational operating conditions tied to China-Middle East
relations. Generic energy volatility without China linkage drifts from the
product's core brief.

### Scope

Query intent or agent framing guidance. Middle East coverage should be
anchored to: China energy demand, Chinese company operations, China-Middle
East trade/payments/investment, or multinational conditions involving China.
Phase 6.9–6.11 or Phase 7 territory.

---

## Tracked Input T-06 — scrubber_report.json Not Found at Expected Path

### Origin
Log observation 2026-05-08

### Description

On the 2026-05-08 06:32 cron run, `cat /root/openclaw_phase5/data/scrubber_report.json`
returned `No such file or directory`. Scrubber counters (`ids_removed`,
`valid_ids_loaded`, `ids_seen`, `ids_kept`, `unsupported_groups`) were also
absent from the cron log grep output.

### Impact

Low urgency. The 2026-05-08 run was clean — validator 23/23 PASS, delivered,
substitutions_made=23, missing_ids=0. No delivery risk. However, the scrubber
report path should be verified to maintain full observability across runs.

### Possible Causes

- scrubber_report.json is written to a different path on live cron runs
- Report generation step has a silent path bug
- Log format changed and counters are written elsewhere

### Scope

Observability verification. Confirm the correct path for scrubber_report.json
on live cron runs before Phase 7. Low priority.

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

`$FINAL` was assigned once from raw output and never refreshed after scrubbing.

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
now silently removed. Claim text is retained; citation group is dropped.

### Status
✅ RESOLVED — 2026-05-05, operator authorized

---

## Issue #42 — SerpAPI Key Invalid — Baidu Retrieval Failure

### Status
✅ RESOLVED — 2026-05-06, operator authorized

### Description

The 06:30 scheduled run on 2026-05-06 produced zero Baidu results.
baidu_raw.json showed result_count=0, error_count=6 — all six queries returned
401 Unauthorized: "Invalid API key." All regions failed (us_p1, us_r1, eu_p1,
eu_r1, me_p1, me_r1). Pipeline delivered Brave-only; validator GREEN PASS;
delivery proceeded without failure.

### Root Cause

`run_light_to_lark.sh` line 4 sets the key as:
`export SERPAPI_KEY="${SERPAPI_KEY:-REDACTED_IF_UNSET}"`

Cron does not source `.bashrc`, so `$SERPAPI_KEY` is unset at cron execution
time. The fallback value `REDACTED_IF_UNSET` is used instead of the real key,
producing a 401 on all SerpAPI calls. Same failure class as the pre-Phase-6.4
outage but different root cause: the prior outage was an inactive SerpAPI
account; this outage was an env var not loaded by cron.

### Impact

Baidu absent from 06:30 delivery. Chinese-perspective sourcing not represented.
Brave-only run. Validator GREEN PASS — 8/8 citations matched. Clean delivery,
no pipeline failure.

### Diagnostic Note

During investigation, `validation_result.json` was confirmed to write to
`/root/openclaw_phase6/validation/` — not `/root/openclaw_phase5/data/` where
other run artifacts live. Path discrepancy should be kept in mind for future
diagnostics.

### Resolution

Operator authorized 2026-05-06. `run_light_to_lark.sh` line 4 updated to
hardcode the active SerpAPI key directly, removing the env var fallback
pattern. Manual test confirmed Baidu restored: result_count=46, error_count=1.
Validator GREEN PASS, 9/9 citations matched, clean delivery.

### Status
✅ RESOLVED — 2026-05-06, operator authorized

---

## Issue #43 — Agent Result ID Fabrication Rate Elevated

### Status
✅ RESOLVED — 2026-05-07, operator approved

### Description

Despite VALID_RESULT_IDS injection (Phase 6.3a), the agent continued to
fabricate result_ids at a significant rate. In the 2026-05-06 10:13 Shanghai
run: ids_seen=21, ids_kept=11, ids_removed=10 — a 48% fabrication rate. The
agent was generating ID-shaped strings rather than selecting exact codes from
the approved list it was given.

### Impact

- Claims in EXECUTIVE TAKE and ADVISORY LAYER lost citations when fabricated
  IDs were scrubbed, appearing in the delivered report without source attribution
- Valid sources available in the retrieval package went uncited (see Issue #44)
- Elevated ids_removed rate in every scrubber report

### Root Cause

Partial recurrence of Issue #35. VALID_RESULT_IDS injection reduced fabrication
from ~100% to ~48%, but agent prompt instruction was insufficient to prevent
approximate ID generation. The agent treated result_ids as generative text
rather than exact strings to be copied.

### Resolution

Phase 6.8 — Numbered-Source Architecture. Three files modified/created:
- `build_agent_input_slim.py`: results rendered as SOURCE 1..N blocks; agent
  cites [source_numbers: N] / [based_on_sources: N]
- `resolve_source_numbers.py` (new): deterministic source number → result_id
  mapping; inserted before scrubber in pipeline
- `run_light_to_lark.sh`: resolver call inserted between agent output and scrubber

Test #1: source_numbers_resolved=16/16, ids_removed=0, validator PASS 16/16.
Test #2: source_numbers_resolved=17/17, ids_removed=0, validator PASS 17/17.
Fabrication rate: 0% across two consecutive runs.

### Status
✅ RESOLVED — 2026-05-07, operator approved (Phase 6.8)

### Identified
2026-05-06

---

## Issue #44 — Valid Sources Not Surfacing in Delivered Output

### Status
✅ RESOLVED — 2026-05-08, log-confirmed

### Description

In the 2026-05-06 10:13 Shanghai run, 6 Baidu sources were present in
retrieval_package.json. Only 3 (all CCTV) were cited in the delivered output.
The 3 Sina Finance sources were not cited and their content did not appear
in any bullet point:

- Sina Finance (2026-05-06): China blocking injunction — legal angle
- Sina Finance (2026-05-03): US-China high-level diplomatic contacts surge
- finance.sina.cn (2026-05-05): Chips, Strait of Hormuz, three-department
  policy deployment

### Root Cause

Issue #43 (agent fabrication). The agent attempted to cite these sources using
fabricated result_ids, which were then scrubbed. Confirmed by resolution
pattern: Phase 6.8 fix brought fabrication rate to 0%, and Sina Finance /
finance.sina.cn sources surfaced in the subsequent 2026-05-08 06:32 delivery.

### Resolution Confirmation

2026-05-08 06:32 cron run:
- Sina Finance and finance.sina.cn cited in multiple bullets across both
  EXECUTIVE TAKE and ADVISORY LAYER
- validator 23/23 PASS, substitutions_made=23, missing_ids=0
- Root cause (Issue #43) confirmed resolved; surface behavior confirmed resolved

### Status
✅ RESOLVED — 2026-05-08, log-confirmed
Dependent resolution of Issue #43 (Phase 6.8, 2026-05-07).

### Identified
2026-05-06
