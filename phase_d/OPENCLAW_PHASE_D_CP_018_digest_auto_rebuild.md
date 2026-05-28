---
document_id: OPENCLAW-D-CP-018
version: 1.0
created: 2026-05-28
classification: PHASE D CHANGE PACKET — BRAIN LITE / PIPELINE ORCHESTRATION
---

# OPENCLAW — Phase D Change Packet CP-018
# Auto-Rebuild Brain Lite Digest After Each Successful Run

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-018 |
| Date raised | 2026-05-28 |
| Raised by | CoWork (D5/D6 session analysis) |
| Client ID | china_monitor_001 |
| Feedback items addressed | D-FB-006 (topic repetition D5/D6 — stale digest) |
| Feedback recurrence threshold met? | Yes — D5 and D6 delivered identical content; operator-confirmed 2026-05-28 |
| Implementation layer | Pipeline orchestration script (run_light_to_lark.sh) — post-Brain Lite call only |
| Status | APPROVED |

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

D5 (2026-05-25) and D6 (2026-05-26) delivered byte-identical content to
Lark. CP-007's TOPIC DIFFERENTIATION RULE was active on both runs, but
it had no effect because the Brain Lite digest injected into the agent
context was stale — it covered only D1–D3 (last rebuilt 2026-05-23) and
did not include D4's topic history. The agent had no knowledge of what D4
or D5 covered, so it could not differentiate.

**Root cause:**

The Brain Lite digest (`brain_digest_china_monitor_001.txt`) is built
manually by the operator. It is not rebuilt as part of the automated
pipeline after each run. As a result, the digest is always at least one
run behind, and after a gap between sessions it can be several runs stale.

CP-007's TOPIC DIFFERENTIATION RULE is architecturally sound but
operationally dependent on a current digest. Without an auto-rebuild,
the rule will continue to fail whenever the digest is not freshly rebuilt
before the cron run.

**Evidence:**

- D5 run_summary topics_covered: crude oil / EU steel / Nvidia H20
- D6 run_summary topics_covered: identical (byte-match confirmed)
- Digest last rebuilt: 2026-05-23 (covering D1–D3 only)
- D4 topics (Shanghai gold -17%, 600 beef companies, Nvidia H200) absent
  from digest at time D5 and D6 ran
- Operator confirmed D5 and D6 content identical — 2026-05-28

**Why this matters:**

The topic differentiation capability is entirely dependent on the digest
being current. Without auto-rebuild, every gap between operator sessions
creates a window where the agent has no yesterday-context. For a daily
brief product, this is structurally unacceptable.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `/root/run_light_to_lark.sh`

**Affected section:** Post-Brain Lite call block (after
`[BRAIN_LITE] summary_write_completed`).

**Current behaviour:**

After write_run_summary.py completes, the pipeline exits. The digest is
never rebuilt automatically. build_brain_digest.py must be run manually.

**Proposed behaviour:**

After a successful Brain Lite write, run_light_to_lark.sh calls
build_brain_digest.py with the current client_id. The call is
non-blocking (same pattern as the existing Brain Lite call): exit
status is captured but a non-zero exit does not abort the pipeline.
A log tag is emitted on completion or failure.

**Proposed addition to run_light_to_lark.sh** (immediately after the
existing Brain Lite write block):

```bash
# CP-018 — Auto-rebuild Brain Lite digest after each successful write
log "[BRAIN_LITE] digest_rebuild_started client_id=${CLIENT_ID}"
python3 /root/openclaw_phase7/brain_lite/build_brain_digest.py \
  --client_id "${CLIENT_ID}" >> "${RUN_LOG}" 2>&1
DIGEST_EXIT=$?
if [ ${DIGEST_EXIT} -eq 0 ]; then
  log "[BRAIN_LITE] digest_rebuild_completed client_id=${CLIENT_ID}"
else
  log "[BRAIN_LITE] digest_rebuild_failed exit=${DIGEST_EXIT} (non-blocking)"
fi
```

**Change scope:** ~10 lines added to run_light_to_lark.sh in the
post-Brain Lite block. No other files modified. Non-blocking — digest
rebuild failure does not affect delivery outcome.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** LOW

The change adds a non-blocking call after delivery is already confirmed.
build_brain_digest.py is an existing, validated script with no pipeline
side effects. It writes only to
`/root/openclaw_phase7/brain_lite/brain_digest_china_monitor_001.txt`.
It does not modify retrieval packages, agent input, validation results,
or delivery artifacts.

The only risk is marginal: if build_brain_digest.py takes more than a
few seconds on some runs, it adds to overall cron run duration. Based on
prior manual runs (3–4KB output, sub-second execution), this is not a
concern.

**Rollback plan:**

Before modification, Claude Code creates:
```
/root/run_light_to_lark.sh.bak_20260528_cp018
```
Rollback: restore from backup. build_brain_digest.py is unmodified.
No other files affected.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. bash -n exit 0 on modified run_light_to_lark.sh
2. First post-implementation cron run: `[BRAIN_LITE] digest_rebuild_completed`
   appears in sidecar log
3. brain_digest_china_monitor_001.txt mtime matches the cron run timestamp
   (confirm digest was freshly written)
4. Second post-implementation cron run: run_summary topics_covered shows
   at least one topic cluster distinct from the prior run's topics_covered
5. Delivery confirmed GREEN on both validation runs; T-04 compliant

**Runs required to validate:** 2 consecutive post-implementation runs
showing digest_rebuild_completed and distinct topics_covered.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to one layer (run_light_to_lark.sh — post-delivery block)
- [x] Rollback path documented
- [x] Within Phase D scope (Brain Lite enrichment operational improvement)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT alter retrieval behavior
- [x] Does NOT weaken validator strictness
- [x] Does NOT weaken scrubber behavior
- [x] Does NOT bypass or modify the Delivery Gate decision
- [x] Does NOT affect client namespace isolation
- [x] Does NOT introduce schema changes to run_summary or Brain Lite

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-05-28 |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | 2026-05-28 |
| Backup confirmed | /root/run_light_to_lark.sh.bak_20260528_cp018 (14227 bytes) |

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Date | digest_rebuild_completed in log? | digest mtime matches run? | topics distinct from prior? | Validator |
|-------|------|----------------------------------|---------------------------|-----------------------------|-----------|
| 1 | | | | | |
| 2 | | | | | |

**Implementation notes (Claude Code 2026-05-28):**
- No `log` function exists in run_light_to_lark.sh. Script logs via bare `echo`
  (stdout timestamped via exec redirection on line 4). Used `echo` instead of
  `log` throughout the inserted block to match existing Brain Lite style.
- No `summary_write_completed` log line exists in the original script. Brain Lite
  block only emits `summary_write_started` and `summary_write_failed`. New block
  placed inside the `if [ "$DELIVERY_DECISION" = "delivered" ]` block immediately
  after the write_run_summary.py call — matching spec intent (after each successful
  write) and keeping digest rebuild gated on delivery success.
- Inserted at lines 371–381.

**Overall outcome:** IMPLEMENTED — validation pending D9 cron run

---

*OPENCLAW-D-CP-018 | Version 1.0 | Created: 2026-05-28 | Status: IMPLEMENTED*
*Raised by: Claude CoWork — D5/D6 session analysis 2026-05-28*
*Operator approved: 2026-05-28 | Implemented: 2026-05-28*
