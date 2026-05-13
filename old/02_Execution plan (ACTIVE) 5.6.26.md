# OPENCLAW — EXECUTION PLAN

---
document_id: OPENCLAW-EXEC-001
version: 5.6.26
last_updated: 2026-05-07
status: ACTIVE
---

## 🔷 PHASE 6 — CURRENT WORK

### Phase 6 Soft Layer: COMPLETE (6.1–6.8) — next phase pending operator decision

---

## ✅ COMPLETED

* Retrieval pipeline stable
* Orchestrator deterministic
* Agent integrated
* Validator implemented
* Numbered-source citation system active (Phase 6.8)
* Scrubber layer implemented — uncited claim removal active (Phase 6.7)
* Citation substitution active — result_ids → publisher/date in Lark output (Phase 6.6)

---

## 🔧 6.3c — STABILIZATION (COMPLETE)

✔ High-recall citation strategy enforced
✔ Scrubber removes invalid IDs
✔ Validator verifies all citations
✔ Partial failure tolerated
✔ Delivery stable

---

## ⚙️ CURRENT SYSTEM BEHAVIOR

* Agent cites [source_numbers: N] — no raw result_ids in agent output
* Resolver (resolve_source_numbers.py) maps source numbers → result_ids deterministically
* Scrubber removes any invalid result_ids and uncited bullets
* All cited bullets trace to a verified source in retrieval_package.json
* Output remains valid and safe; fabrication rate 0% on Phase 6.8 close runs

---

## 🎯 GUARANTEES

* No fabricated citations delivered
* All result_ids verified by scrubber + validator
* No uncited bullet in EXECUTIVE TAKE or ADVISORY LAYER delivered
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

✔ Live pipeline test complete (10:22 Shanghai) — unsupported_groups=0, ids_removed=2,
  15/15 GREEN PASS, delivered. No placeholder text in output. Issue #41 fix active.

---

## ✅ PHASE 6.5 — CONFLICT HANDLING UPGRADE (COMPLETE)

### Objective

Surface factual conflicts across sources to the operator. No silent conflict
suppression. Conflict classification logged per run.

### Implementation (COMPLETE)

✔ Agent prompt extended with conditional CONFLICTS output section (omitted if
  no conflicts detected)
✔ Scrubber updated — split_conflicts() extracts CONFLICTS block, writes
  conflict_log.json per run
✔ Delivery script updated — reads conflict_count, injects tiered CONFLICT FLAGS
  into Lark when conflict_count > 0

### Work Completed (2026-05-05)

✔ Three-layer implementation complete via Claude Code
✔ Live test (10:44 Shanghai) — conflict_count=0, clean delivery,
  conflict_log.json written correctly. Zero-conflict path confirmed.

### Work Completed (2026-05-06)

✔ 06:30 run (2026-05-06) reviewed — citation syntax 6/6 PASS, zero conflicts,
  clean delivery. Baidu absent — Issue #42 identified and resolved.

✔ Issue #42 resolved — SerpAPI key not loaded by cron due to env var fallback
  pattern in run_light_to_lark.sh. Key hardcoded directly. Baidu restored:
  result_count=46, error_count=1 on manual test. Validator GREEN PASS, 9/9
  citations matched. Operator authorized 2026-05-06.

✔ Phase 6.6 scope decided — citation substitution (post-validation result_id →
  publisher/date replacement in delivery script). Opens after Phase 6.5 formal
  close. Operator decision 2026-05-06.

### Work Completed (2026-05-06, continued)

✔ Synthetic test complete — conflict_count=3, all three prefix tiers confirmed
  (⚠ FACTUAL / ↔ DIRECTIONAL / ~ NUMERIC). Non-zero conflict path verified.

✔ Phase 6.5 formally closed — operator approved 2026-05-06.

---

## ✅ PHASE 6.6 — CITATION SUBSTITUTION (COMPLETE)

### Objective

Replace result_id citation tokens in Lark-delivered output with human-readable
publisher and date strings. result_ids are retained in all log artifacts
(retrieval_package.json, scrubber_report.json, validation_result.json) for
full verification traceability.

### Scope

- Post-validation substitution step in delivery script
- Lookup: result_id → publisher + date from retrieval_package.json
- Output format example: `(result_id: res_abc123)` → `(Reuters, 6 May 2026)`
- Single layer — delivery script only
- No changes to retrieval, scrubber, validator, or agent

### Out of Scope

- Changes to citation enforcement or validation logic
- Changes to retrieval_package.json structure
- Agent prompt changes

### Exit Criteria — ALL CONFIRMED

1. result_id tokens replaced with publisher/date strings in all delivered
   Lark output ✔
2. Substitution lookup confirmed against retrieval_package.json — no invented
   publisher names ✔
3. Validator and scrubber logs continue to use result_ids unchanged ✔
4. Two consecutive successful deliveries with human-readable citations ✔
5. No delivery failures introduced by substitution step ✔

### Work Completed (2026-05-06)

✔ citation_sub.py written to /root/openclaw_phase6/citation_sub.py
✔ run_light_to_lark.sh updated — substitution step inserted after delivery
  skip gate, before curl call
✔ Smoke test passed — substitutions_made=5, missing_ids=0, multi-ID groups correct
✔ Live run 1 (10:13 Shanghai) — 11/11 substitutions, HTTP 200, delivered;
  no result_ids in Lark output; exit criteria 1, 2, 3, 5 confirmed

### Work Completed (2026-05-07)

✔ Exit criterion 4 confirmed — 06:30 cron run: validator PASS, HTTP 200,
  substitutions_made=2, missing_ids=0, no result_ids in Lark output.
  Second consecutive clean delivery confirmed.
✔ Phase 6.6 formally closed — operator approved 2026-05-07.

---

## ✅ PHASE 6.7 — UNCITED CLAIM REMOVAL (COMPLETE)

### Objective

Remove any bullet point in EXECUTIVE TAKE or ADVISORY LAYER that has no
citation remaining after scrubbing. Ensures every delivered claim is
traceable to a verified source.

### Scope

- Single change to scrub_result_ids.py
- Post-scrub pass over EXECUTIVE TAKE and ADVISORY LAYER
- Bullets with no (result_id: ...) token removed from output
- Removed bullets logged via uncited_claims_removed counter in cron log
- If EXECUTIVE TAKE contains zero cited bullets after removal, delivery blocked

### Exit Criteria — ALL CONFIRMED

1. No uncited bullet in EXECUTIVE TAKE or ADVISORY LAYER reaches delivery ✔
2. Removed bullets logged (uncited_claims_removed count in cron log) ✔
3. Validator GREEN PASS maintained ✔
4. No new delivery failures introduced ✔
5. Delivery block confirmed when EXECUTIVE TAKE empty ✔

### Work Completed (2026-05-07)

✔ Implementation complete — remove_uncited_bullets() function added to
  scrub_result_ids.py; CITATION_PRESENT_RE check added; exec_take_cited
  counter and delivery block added
✔ Synthetic test passed — correct removal behavior confirmed on 06:32 run
  artifacts; 6 uncited bullets removed, 2 retained with valid citations
✔ Live test confirmed delivery block — EXECUTIVE TAKE empty after scrub
  (root cause: Issue #43 agent fabrication); block fired correctly
✔ Phase 6.7 formally closed — operator approved 2026-05-07.
  Closure basis: mechanism proven correct; delivery block working as designed;
  root cause of block (Issue #43) addressed by Phase 6.8.

---

## ✅ PHASE 6.8 — AGENT CITATION PRECISION (COMPLETE)

### Objective

Reduce agent result_id fabrication rate to near zero. Original fabrication
rate ~48% (Issue #43) caused uncited claims and valid sources going
unrepresented in delivered output (Issue #44).

### Scope (final — expanded from original single-file definition)

Three files modified/created:
- build_agent_input_slim.py — results rendered as SOURCE 1..N blocks;
  agent cites [source_numbers: N] / [based_on_sources: N]
- resolve_source_numbers.py (new) — deterministic source number → result_id
  mapping; inserted before scrubber in pipeline
- run_light_to_lark.sh — resolver call inserted between agent output and scrubber

### Out of Scope

- Retrieval, validator logic, delivery gate, citation_sub.py, query templates

### Exit Criteria — ALL CONFIRMED

1. ids_removed rate below 15% across two consecutive runs ✔ (0% both runs)
2. Known valid sources cited in proportion to package presence ✔ (full output both runs)
3. Validator GREEN PASS maintained on both runs ✔
4. No delivery failures introduced ✔

### Work Completed (2026-05-07)

✔ Root cause confirmed — agent fabricating all result_ids; zero overlap with
  VALID_RESULT_IDS; VALID_RESULT_IDS injection confirmed present and correct
✔ Prompt hardening (test #1) — padding language removed; CITATION PRECISION RULE
  added; VALID_RESULT_IDS moved to recency anchor position; example IDs rendered
  from real package. Result: ids_kept=1/22, delivery unblocked but thin.
  Fabrication rate still ~95% — prompt-only approach insufficient.
✔ Numbered-source architecture designed, reviewed, and authorized
✔ Implementation complete (3 files):
  - build_agent_input_slim.py: results as SOURCE 1..N; agent cites source numbers
  - resolve_source_numbers.py: new deterministic resolver (120 lines)
  - run_light_to_lark.sh: resolver inserted at correct pipeline position
✔ Syntax checks passed on both Python files
✔ Test #1 — source_numbers_resolved=16/16, ids_removed=0, validator PASS 16/16,
  delivered (3 EXEC + 5 ADV bullets, full output)
✔ Test #2 — source_numbers_resolved=17/17, ids_removed=0, validator PASS 17/17,
  delivered (full output)
✔ Issue #43 resolved — fabrication rate 0% (from ~48% baseline)
✔ Phase 6.8 formally closed — operator approved 2026-05-07.

---

## ⏳ PHASE 6.9–6.11 — EXPANSION LAYER (BLOCKED)

Expansion layer phases blocked until Soft Layer stable.
Soft Layer (6.1–6.8) now complete — operator decision required to open.

Key open question raised 2026-05-07: source diversity in delivered output.
Retrieval brings ~86–99 raw results (Brave + Baidu); filter retains ~13 (15%).
The filter is the current bottleneck on source variety — not the citation layer.
Expansion layer and Phase 7 roadmap are the designated home for this work.

Refer to Phase 7 Execution Plan (canonical roadmap) for expansion scope.
