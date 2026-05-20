# OPENCLAW — ISSUES LOG

---
document_id: OPENCLAW-ISSUES-001
version: v2.0
last_updated: 2026-05-20
status: OPERATIONAL
---

## CONTEXT

This log covers Issues #34 onward. Issues #1–#33 are recorded in historical
daily status and session handover documents in `/old/`. Issue numbering is
cumulative across the project lifecycle. The current log retains only active
and recently resolved issues.

## OPEN ISSUES SUMMARY

| # | Title | Status |
|---|-------|--------|
| 46 | OPENCLAW_ARTIFACT_NAMESPACE not propagating to scrubber subprocess | ✅ RESOLVED — 2026-05-20 |
| 47 | Intermediate retrieval artifacts not client-namespaced | 🟡 OPEN — operator decision required |
| 48 | Delivery relay not client-namespaced — test runs deliver to live channel | ✅ RESOLVED — 2026-05-20 |
| 49 | run_light_to_lark.sh — OPENCLAW_CLIENT_ID and other loader vars assigned without export | 🟡 OPEN — pre-production tightening required |

## TRACKED INPUTS — FUTURE PHASE

| # | Title | Origin |
|---|-------|--------|
| T-01 | Freshness signaling not distinguished in output | Advisory note 2026-05-08 |
| T-02 | Source authority classification — lower-authority sources uncalibrated | Advisory note 2026-05-08 |
| T-03 | Chinese-source diversity — not yet consistently rich across categories | Advisory note 2026-05-08 |
| T-04 | Advisory language calibration — claim strength exceeds evidence in places | ✅ CLOSED — 2026-05-19 |
| T-05 | Middle East content drift — coverage not consistently anchored to China linkage | Advisory note 2026-05-08 |
| T-06 | scrubber_report.json not found at expected path on 2026-05-08 06:32 run | ✅ RESOLVED — 2026-05-11 |
| T-07 | LinkedIn Draft non-refresh — identical output across consecutive runs | Content observation 2026-05-11 |
| T-08 | Double [BRAIN_LITE] summary_write_started on first confirmation run | ✅ RESOLVED — 2026-05-11 |
| T-09 | CoWork VPS direct access not implemented — daily post-run report not operational | ✅ RESOLVED — 2026-05-13 |
| T-10 | Brain Lite metrics_unavailable — ids_seen/ids_kept/ids_removed = 0 in run_summary | ✅ RESOLVED — 2026-05-13 |

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
| 45 | 2026-05-19 delivery failure — Step 9.3/9.4 deployment sequence | ✅ RESOLVED (2026-05-19) |

---

## Issue #48 — Delivery Relay Not Client-Namespaced

### Status
🔴 OPEN — Phase C gate decision required

### Discovered
2026-05-20 — Step 9.7 manual test run

### Description

The delivery relay at `http://127.0.0.1:8787/push` is not client-aware. The curl
call in `run_light_to_lark.sh` (line 283) posts to the relay with no `client_id`
or webhook parameter. The relay delivers to a single hardcoded Lark channel
regardless of which client triggered the run. `pilot_mode: true` in
`client_config_test_client_002.yaml` has no effect — the delivery gate does not
read `pilot_mode` from the client config.

During the Step 9.7 test run, `test_client_002` content was delivered to the live
china_monitor_001 Lark channel at 10:10 Shanghai. The content was real China
Monitor content (not synthetic garbage) because `test_client_002` used
`query_template_set: china_monitor_v1`, which ran live Brave/Baidu queries and
retrieved current China news. The subscriber received an unscheduled second brief.

### Impact

Any manual test run on any non-default client will deliver to the live channel
until resolved. This is a live client experience issue if real subscribers are
present.

### Phase C Gate Implication

Namespace isolation at the delivery layer is not confirmed. Phase C gate requires
operator decision: is delivery-layer namespacing in scope for Phase C, or does
Phase C close on artifact-layer isolation only with delivery namespacing deferred?

### Resolution

Resolved 2026-05-20 — operator confirmed delivery namespacing in Phase C scope.
Two patches applied to `run_light_to_lark.sh`:
1. `export OPENCLAW_PILOT_MODE=$(grep '^OPENCLAW_PILOT_MODE=' "$LOADER_ENV_FILE" | cut -d= -f2)` added at line 21.
2. Pilot mode delivery gate added at line 285: if `OPENCLAW_PILOT_MODE=true`, print `[SKIP]` and `exit 0` before curl call.
Backup: `run_light_to_lark.sh.bak_20260520_pre_pilot_mode`.
Confirmed: Step 9.7 re-run shows `[SKIP] pilot_mode=true — delivery blocked for client_id=test_client_002`. Live Lark channel not touched.

---

## Issue #49 — run_light_to_lark.sh Loader Variables Not Fully Exported

### Status
🟡 OPEN — pre-production tightening required

### Discovered
2026-05-20 — Claude Code side observation during Fix 1 investigation

### Description

`run_light_to_lark.sh` lines 19–22 read variables from `loader.env` (CLIENT_ID,
ARTIFACT_NAMESPACE, PILOT_MODE, etc.) via grep/cut assignment. Only
`OPENCLAW_ARTIFACT_NAMESPACE` and `OPENCLAW_PILOT_MODE` have been explicitly
exported (patches applied 2026-05-20). Other variables (e.g. `OPENCLAW_CLIENT_ID`)
are assigned as shell variables only and are not visible to child processes.
Child subprocesses that need CLIENT_ID may fall back to hardcoded defaults
rather than the loader.env value.

### Impact

Not currently blocking — confirmed test_client_002 run produced correct namespaced
artifacts with current export set. Risk increases when additional clients and
pipeline components are added in production.

### Resolution Required

Audit all loader.env variables read in `run_light_to_lark.sh` lines 19–22 and
confirm each is either exported or not needed by child processes. Add `export`
to any that are consumed by subprocesses. Pre-production requirement before
second real client goes live.

---

## Issue #46 — OPENCLAW_ARTIFACT_NAMESPACE Not Propagating to Scrubber Subprocess

### Status
✅ RESOLVED — 2026-05-20

### Discovered
2026-05-20 — Step 9.7 manual test run

### Description

During the Step 9.7 manual test run (`./run_light_to_lark.sh --client_id test_client_002`),
the config loader correctly set `artifact_namespace=test_client_002` and the [CONFIG] log
line confirmed `client_id=test_client_002 artifact_namespace=test_client_002`. However,
the scrubber (`scrub_result_ids.py`) defaulted to `china_monitor_001`, writing its output
to `final_output_scrubbed_china_monitor_001.txt` instead of `final_output_scrubbed_test_client_002.txt`.
The subsequent `cp` in `run_light_to_lark.sh` failed with "cannot stat
final_output_scrubbed_test_client_002.txt". The pipeline aborted before reaching delivery.

### Impact

`final_output_scrubbed_china_monitor_001.txt` was overwritten with degraded content
(ids_removed=17 vs confirmed 0 from morning cron). Morning delivery was unaffected
(completed at 06:31, three hours prior). Tomorrow's 06:30 cron will regenerate all
artifacts from scratch — no live client impact.

### Root Cause (working hypothesis)

`OPENCLAW_ARTIFACT_NAMESPACE` is exported by `run_light_to_lark.sh` after sourcing
`loader.env`, but is not being inherited by the `scrub_result_ids.py` subprocess.
Python subprocess env inheritance or the source/export sequence in the shell script
is the likely fault location. Requires VPS investigation.

### Resolution

Two bugs found and patched 2026-05-20:
1. Line 20: `OPENCLAW_ARTIFACT_NAMESPACE` assigned but not exported — fixed with `export`.
2. Line 191: typo `${OPENCLAW_ARTIFACT_NAMESPAC}` (missing `E`) — fixed via sed.
Backup: `run_light_to_lark.sh.bak_20260520_pre_ns_export`.
Re-run of Step 9.7 confirmed scrubber wrote to correct namespace (test_client_002).
Note: lines 190 and 193 have a further typo `${OPENCLAW_ARTIFACTNAMESPACE}` (missing
underscore) — did not block this run but requires a follow-up patch.

---

## Issue #47 — Intermediate Retrieval Artifacts Not Client-Namespaced

### Status
🟡 OPEN — operator decision required

### Discovered
2026-05-20 — Step 9.7 investigation

### Description

Intermediate retrieval artifacts (`brave_raw.json`, `baidu_raw.json`,
`query_bundle.json`, `normalized/`, `filtered_results.json`) are written to
shared paths with no client_id suffix. Two concurrent client runs would overwrite
each other's retrieval data silently. Confirmed during the Step 9.7 investigation:
two sequential `test_client_002` runs both wrote to the same intermediate paths,
producing a mixed artifact state in the data directory.

### Impact

Not a current operational risk — cron runs only one client (china_monitor_001) on
a fixed schedule. Concurrent manual runs are the only exposure path, and those are
operator-controlled. Becomes a real risk when a second client is added to cron or
when parallel manual testing is conducted.

### Scope Note

The hardcoded-filename audit (2026-05-18) classified `build_agent_input.py` and
`run_phase5_offline.sh` as NO (no namespacing required). The intermediate retrieval
files were not explicitly classified in that audit. This may require a scope
decision before Phase C closes.

### Resolution Required

Operator decision: are intermediate retrieval artifacts in scope for Phase C
namespacing, or deferred to a later phase? If in scope, classification table
must be updated and implementation authorized before Phase C gate closes.

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

Agent prompt guidance — advisory language calibration. Phase 7 editorial
workstream.

### Resolution

Deployed 2026-05-13. Two additions made to
/root/openclaw_phase5/orchestrator/build_agent_input_slim.py:

1. ADVISORY LANGUAGE CALIBRATION block added to system_rules — prohibits
   imperative constructions ("must", "must immediately", "urgently",
   "immediately accelerate") and alarm-grade superlatives ("unprecedented",
   "extreme", "crisis-level", "heightened and prolonged") unless that exact
   framing appears in a cited retained source; mandates conditional advisory
   framing with PREFERRED/NOT ALLOWED examples.

2. Advisory language rules block added to output_format — explicit
   per-section framing constraints; match advisory strength to evidential
   strength; one implication per bullet.

py_compile exit 0 — syntax valid. Validates on next cron run (2026-05-14).

### Status
✅ CLOSED — 2026-05-19. Validated across five consecutive cron runs
(2026-05-14 through 2026-05-18). All 5 AL bullets confirmed conditional/
hedged framing on each run. No imperative constructions or alarm-grade
superlatives observed. Compliance confirmed by CoWork post-run analysis.

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

## Tracked Input T-08 — Double [BRAIN_LITE] summary_write_started

### Status
✅ RESOLVED — 2026-05-11

### Origin
Brain Lite confirmation Run 1, 2026-05-11

### Description

First manual confirmation run of run_light_to_lark.sh produced two
`[BRAIN_LITE] summary_write_started` markers per run. The shell script
(run_light_to_lark.sh line 290) echoed `[BRAIN_LITE] summary_write_started`
immediately before invoking write_run_summary.py, which also emitted the same
marker via `log("summary_write_started")` at line 132. Both fired on every run.

### Root Cause

Implementation brief specified the shell script echo as a log tag, and
write_run_summary.py was independently implemented to also emit summary_write_started
at the top of main(). Duplicate not caught in Step 7 testing (test ran
write_run_summary.py directly, not via run_light_to_lark.sh).

### Resolution

Removed `log("summary_write_started")` from write_run_summary.py line 132.
Shell script retains the echo (owns started/failed markers). Python retains
metrics_unavailable and summary_write_completed. Expected sequence after fix:
`[BRAIN_LITE] summary_write_started` (shell) →
`[BRAIN_LITE] metrics_unavailable` (python) →
`[BRAIN_LITE] summary_write_completed` (python).

Second confirmation run verified: correct single-marker sequence confirmed.

---

## Tracked Input T-06 — scrubber_report.json Not Found at Expected Path

### Status
✅ RESOLVED — 2026-05-11

### Origin
Log observation 2026-05-08

### Root Cause Confirmed

Claude Code audit of /root/openclaw_phase6/validation/scrub_result_ids.py
(2026-05-11, Phase C pre-implementation hardcoded-filename audit):

scrubber_report.json was never implemented. scrub_result_ids.py writes
exactly two artifacts — final_output_scrubbed.txt (line 112) and
conflict_log.json (line 119). No JSON scrubber report is produced or
expected anywhere in the pipeline. Scrubber metrics (ids_seen, ids_kept,
ids_removed, unsupported_groups) are emitted to stdout and captured by
the cron log only.

No pipeline gap — system functions correctly without a JSON scrubber
report. No namespacing action required for Phase C implementation.

### Secondary Finding

scrub_result_ids.py lives at /root/openclaw_phase6/validation/, not
/root/openclaw_phase5/data/ as previously assumed. Future audit scope
should include /root/openclaw_phase6/validation/ alongside phase5/.

---

## Tracked Input T-09 — CoWork VPS Direct Access Not Implemented

### Origin
Execution Plan Sections 10.2 and 10.3 — gap identified 2026-05-13

### Description

The Phase 7 Execution Plan specifies that CoWork should have direct SSH
access to the VPS as the openclaw_cowork non-root user, and should produce
daily post-run reports automatically written to
/root/openclaw_cowork/reports/run_review_YYYYMMDD.md after each 06:30 cron
run.

Current state: CoWork has no SSH connection to the VPS. All VPS interaction
this session required the operator to run commands manually and paste output
into chat. The daily post-run report has never been written. CoWork is
operating in relay mode — not in the co-located model the plan specifies.

### What Was Completed (Step 2B, 2026-05-09)
- openclaw_cowork system user created (uid=999)
- Filesystem permission boundary configured structurally

### What Is Missing
- SSH keypair not generated for openclaw_cowork user
- CoWork has no credentials to authenticate to VPS as openclaw_cowork
- Daily post-run report not operational
- Section 10.3 safeguard completion status unclear:
    1. SerpAPI key moved to secrets location outside CoWork read path — status unknown
    2. Git pre-commit hook installed in openclaw_docs/ and openclaw_cowork/ — status unknown
    3. Written access control model reviewed and signed off — status unknown

### Why It Matters
Section 7.1 of the Execution Plan lists "VPS Phase B active: CoWork
co-located with read access to logs and validation outputs; daily post-run
report operational" as a hard prerequisite for Phase D (controlled pilot).
This gap must be closed before pilot begins.

### Scope
VPS configuration + CoWork SSH setup. Two parts:
1. Verify/complete the three Section 10.3 safeguards (Claude Code)
2. Generate SSH keypair for openclaw_cowork; configure CoWork access;
   test connection and daily report write (Claude Code + one session)

### Resolution

Completed 2026-05-13 across two sessions:

**Section 10.3 safeguards — all three complete:**
1. SerpAPI key moved from hardcoded run_light_to_lark.sh to
   /root/.secrets/openclaw.env (mode 600, root-owned); run_light_to_lark.sh
   line 4 updated to `source /root/.secrets/openclaw.env`.
2. Git pre-commit hooks installed in both /root/openclaw_docs/.git/hooks/
   and /root/openclaw_cowork/.git/hooks/ — require commit messages before
   applying to production.
3. Access control model: openclaw_cowork (uid=999) permission boundary
   enforced structurally per Step 2B. Shell changed from /usr/sbin/nologin
   to /bin/bash to allow SSH.

**SSH keypair:**
- ed25519 keypair generated; public key installed in
  /home/openclaw_cowork/.ssh/authorized_keys (chmod 600).
- Private key saved to workspace at config/cowork_key; shredded from VPS.
- pubkeyauthentication yes confirmed in sshd.

**VPS sync pattern (replaces direct SSH from CoWork):**
- CoWork bash sandbox is fully network-isolated — direct SSH not achievable.
- Resolution: operator runs PowerShell scp block at session start to pull
  VPS artifacts to config/vps_sync/ on local machine.
- CoWork reads from config/vps_sync/ locally. No networking required from
  CoWork side.
- Pattern tested and confirmed 2026-05-13: light_to_lark.log (88KB),
  validation_result.json (5.9KB), two run_summary JSONs all verified readable.
- Protocol documented at config/VPS_SYNC_PROTOCOL.md.

### Status
✅ RESOLVED — 2026-05-13

---

## Tracked Input T-10 — Brain Lite metrics_unavailable

### Origin
Brain Lite confirmation Run 2 (2026-05-12), confirmed Run 3 (2026-05-13)

### Status
✅ RESOLVED — 2026-05-13

### Description

write_run_summary.py had metrics hardcoded to 0 (C1 condition — placeholder
pending scrubber change). Fields ids_seen, ids_kept, ids_removed wrote as 0
on every run. `[BRAIN_LITE] metrics_unavailable` emitted on every execution.

Actual validator metrics were correct and available in validation_result.json
and the cron log. The gap was exclusively in what Brain Lite wrote to the
run_summary.

### Evidence

Run 2 (2026-05-12): `[BRAIN_LITE] metrics_unavailable` in cron log; run_summary
ids_seen=0, ids_kept=0, ids_removed=0.
Run 3 (2026-05-13): same pattern. validation_result.json confirmed actual
values were 30/30/0.

### Root Cause

validation_result.json metrics are nested under `d["summary"]`. Original patch
read from top-level `d`, where `"failures"` is an empty list `[]` — causing
`int()` TypeError. Corrected to read from `d["summary"]` block.

### Resolution

Patch deployed 2026-05-13 to write_run_summary.py:
- `get_validator_metrics()` function added — reads claims_checked,
  sources_matched, failures from validation_result.json `summary` block
- Mapping: claims_checked → ids_seen; sources_matched → ids_kept;
  failures → ids_removed
- `log("metrics_unavailable")` moved to fallback path only (file unreadable)
- `log("summary_write_completed")` retained as success marker
- Backup: write_run_summary.py.bak_20260513
- py_compile: OK
- Manual verification (2026-05-13): ids_seen=30 | ids_kept=30 | ids_removed=0

Confirms on Run 4 (2026-05-14 cron). uncited_claims_removed remains 0 —
scrubber does not emit this count to a readable file; separate workstream
if required.

---

## Tracked Input T-07 — LinkedIn Draft Non-Refresh Across Consecutive Runs

### Origin
Content observation 2026-05-11 (two-run comparison)

### Description

The LinkedIn Draft section of the 2026-05-10 and 2026-05-11 delivered outputs
is word-for-word identical, despite meaningfully different EXECUTIVE TAKE and
ADVISORY LAYER bullet content across the two runs. The LinkedIn section did not
update to reflect the specific sourced content of each run.

### Context

The LinkedIn Draft is generated by the agent as part of the same output pass
as EXECUTIVE TAKE and ADVISORY LAYER. The non-refresh pattern suggests the
agent is producing a generic synthesis for the LinkedIn section rather than a
daily-refreshed summary grounded in the specific run's sourced bullets.

This is related in nature to T-04 (advisory language calibration) and T-01
(freshness signaling) — all are agent prompt behavior patterns affecting
output quality rather than pipeline correctness.

### Scope

Agent prompt guidance — LinkedIn section grounding instructions. Phase 7
editorial-quality workstream. Does not require retrieval or pipeline changes.

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

---

## Issue #45 — 2026-05-19 Delivery Failure — Step 9.3/9.4 Deployment Sequence

### Status
✅ RESOLVED — 2026-05-19

### Origin
2026-05-19 06:30 cron run analysis

### Description

The 2026-05-19 06:30 cron run failed to deliver. The config loader executed
successfully (client_id=china_monitor_001, artifact_namespace=china_monitor_001
confirmed). The resolver and scrubber ran but wrote to non-namespaced artifact
paths (Step 9.4 not yet deployed). run_light_to_lark.sh (Step 9.3) then
attempted to cp final_output_scrubbed_china_monitor_001.txt — which did not
exist because scrub_result_ids.py still wrote to the non-namespaced filename.
The script aborted. Validator and delivery gate were not reached. Brain Lite
run_summary was not written.

### Root Cause

Step 9.3 (shell script namespacing) was deployed on 2026-05-18 without Step
9.4 (Python script namespacing). The shell script expected namespaced artifact
filenames that the Python scripts were not yet producing. Partial deployment
created a broken handoff at the scrubber output step.

### Resolution

Rollback executed same session: run_light_to_lark.sh restored from
run_light_to_lark.sh.bak_20260518_pre_config_loader. Steps 9.3 and 9.4
prepared as a combined patch set, reviewed by CoWork, operator-approved, and
deployed as a single unit on 2026-05-19. All 7 files (6 Python scripts +
shell script) verified: py_compile exit 0 / bash -n exit 0. Step 9.4
confirmation run expected 2026-05-20 06:30.

### Identified
2026-05-19
