---
document_id: OPENCLAW-D-CP-014
version: 1.0
created: 2026-05-24
classification: PHASE D CHANGE PACKET — SHELL / LOGGING
---

# OPENCLAW — Phase D Change Packet CP-014
# Scrubber Failure Logging Accuracy — run_light_to_lark.sh

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-014 |
| Date raised | 2026-05-24 |
| Raised by | Operator (ALJ pilot run 2026-05-24 — misdiagnosis via hardcoded FAIL message) |
| Client ID | All clients (logging fix — no client-specific behavior) |
| Feedback items addressed | N/A — operational quality fix |
| Recurrence threshold met? | N/A |
| Implementation layer | Shell runner (run_light_to_lark.sh) — scrubber stdout capture only |
| Depends on | None (independent of CP-013) |
| Status | APPROVED — implementation pending |

**Note:** This CP has zero behavioral impact on delivery, validator,
scrubber logic, or pilot_mode gate. It is a logging fix. The shell-side
`[SCRUBBER] FAIL — unsupported citation groups` message is hardcoded
and fires regardless of the actual scrubber failure reason, causing
misdiagnosis. During the 2026-05-24 ALJ pilot session, this message
directed ~10 minutes of investigation down the wrong path before the
real failure (`EXECUTIVE TAKE has zero cited bullets`) was found by
replaying the scrubber manually.

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

`run_light_to_lark.sh` runs the scrubber with no stdout capture and
stamps a hardcoded failure reason in the run log regardless of why the
scrubber actually failed.

**Root cause:**

Lines 197–204 of `run_light_to_lark.sh`:
```bash
SCRUBBER_EXIT=0
python3 /root/openclaw_phase6/validation/scrub_result_ids.py || SCRUBBER_EXIT=$?
printf "[SCRUBBER] exit=%s\n" "$SCRUBBER_EXIT" >> "$RUN_LOG"
if [ "$SCRUBBER_EXIT" -ne 0 ]; then
  echo "[SCRUBBER] FAIL — unsupported citation groups"
  printf "[SCRUBBER] FAIL — unsupported citation groups\n" >> "$RUN_LOG"
  exit 0
fi
```

The scrubber has two distinct `sys.exit(1)` paths:
1. "EXECUTIVE TAKE has zero cited bullets after uncited removal" (or
   equivalent `REQUIRED_CITED_SECTION` gate after CP-013)
2. "all citation groups unsupported"

Both paths produce the same shell log message:
`[SCRUBBER] FAIL — unsupported citation groups`

The scrubber's own informative stdout is not teed to the run log.

**Evidence:**

ALJ pilot run 2026-05-24: real failure was the cited-section gate.
Shell log said "unsupported citation groups." Operator spent time
investigating citation resolution before discovering the actual error.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `/root/run_light_to_lark.sh`

**Change description:**

Tee scrubber stdout/stderr into the run log while preserving the exit
code via `${PIPESTATUS[0]}`. Wrap in `set +o pipefail` / `set -o
pipefail` to prevent `pipefail` (active at line 2) from aborting the
shell on a non-zero scrubber exit before `SCRUBBER_EXIT` is captured.

**Before:**
```bash
SCRUBBER_EXIT=0
python3 /root/openclaw_phase6/validation/scrub_result_ids.py || SCRUBBER_EXIT=$?
printf "[SCRUBBER] exit=%s\n" "$SCRUBBER_EXIT" >> "$RUN_LOG"
if [ "$SCRUBBER_EXIT" -ne 0 ]; then
  echo "[SCRUBBER] FAIL — unsupported citation groups"
  printf "[SCRUBBER] FAIL — unsupported citation groups\n" >> "$RUN_LOG"
  exit 0
fi
```

**After:**
```bash
SCRUBBER_EXIT=0
set +o pipefail
python3 /root/openclaw_phase6/validation/scrub_result_ids.py 2>&1 | tee -a "$RUN_LOG"
SCRUBBER_EXIT=${PIPESTATUS[0]}
set -o pipefail
printf "[SCRUBBER] exit=%s\n" "$SCRUBBER_EXIT" >> "$RUN_LOG"
if [ "$SCRUBBER_EXIT" -ne 0 ]; then
  echo "[SCRUBBER] FAIL — see scrubber output above"
  printf "[SCRUBBER] FAIL — see scrubber output above\n" >> "$RUN_LOG"
  exit 0
fi
```

**Net effect:** The real scrubber `[FAIL] ...` line lands in `$RUN_LOG`
immediately above the generic shell stamp, so the actual failure reason
is one `grep` away in any future diagnosis session.

**Fallback (if tee considered too invasive):**

Change only the hardcoded message string:
- `unsupported citation groups` → `see scrubber output above`

Operators would still need to replay the scrubber manually, but the
shell log would no longer assert a false failure reason. Not recommended
— loses the actual scrubber stdout.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** NEGLIGIBLE

This is a log-formatting and stdout-routing change only. It does not
touch delivery decision, validator, scrubber logic, hash dedup, citation
enforcement, or pilot_mode gate.

The only behavioral change is `$RUN_LOG` growing by ~10 lines per
scrubber invocation (scrubber stdout is now teed in).

**pipefail guard rationale:** `set -euo pipefail` is in effect at line 2
of the script. Without the guard, a non-zero scrubber exit causes
`pipefail` to abort the shell before `SCRUBBER_EXIT=${PIPESTATUS[0]}`
runs — defeating the purpose of the tee. The `set +o pipefail` /
`set -o pipefail` wrapper scopes the relaxation to exactly the tee pipe
and immediately restores strict mode.

**Rollback plan:**

Before any modification, Claude Code creates:
```
/root/run_light_to_lark.sh.bak_20260524_cp014
```

Rollback: restore from backup. Shell returns to hardcoded FAIL message
(same as current behavior — no crash, just misleading log). No state
migration required.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. **bash -n exit 0** on modified `run_light_to_lark.sh`
2. **Forced-fail scenario** — run ALJ pilot before CP-013 is merged
   (scrubber will still fail on cited-section gate):
   ```
   /root/run_light_to_lark.sh --client_id alj_china_auto_001
   ```
   Expected in `$RUN_LOG`: scrubber's full stdout including the literal
   line `[FAIL] EXECUTIVE TAKE has zero cited bullets after uncited
   removal; delivery blocked`, followed by `[SCRUBBER] exit=1` and
   `[SCRUBBER] FAIL — see scrubber output above`. Shell exits 0
   (delivery skipped, not error-exit) — unchanged from pre-patch.
3. **Success scenario** — run `china_monitor_001` (scrubber passes).
   Expected: scrubber stdout teed into `$RUN_LOG` (~10 additional lines),
   `[SCRUBBER] exit=0`, delivery proceeds normally. Shell exit code
   unchanged.
4. **PIPESTATUS verification** — step 2 above exercises the non-zero
   path and confirms `${PIPESTATUS[0]}` captures the python exit code
   correctly.

**Runs required to validate:** 1 ALJ run (forced-fail) + 1 WS1 run
(success path).

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to one block in one file (run_light_to_lark.sh scrubber invocation)
- [x] Rollback path documented
- [x] Within Phase D scope (operational logging quality)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT alter WS1 or ALJ delivery behavior
- [x] Does NOT alter scrubber logic
- [x] Does NOT alter validator strictness
- [x] Does NOT weaken citation enforcement
- [x] Does NOT alter Delivery Gate behavior
- [x] Does NOT affect client namespace isolation
- [x] Does NOT affect pilot_mode gate

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-05-24 |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | |
| Backup confirmed | |

**Pre-implementation checklist:**
- [ ] `run_light_to_lark.sh.bak_20260524_cp014` created
- [ ] `set +o pipefail` / tee / `PIPESTATUS[0]` / `set -o pipefail` block applied
- [ ] Hardcoded message updated to `see scrubber output above`
- [ ] `bash -n` exit 0
- [ ] Forced-fail run confirms real scrubber reason visible in log

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Client | Date | Scrubber outcome | Real reason in log? | Shell exit | Delivery behavior unchanged? |
|-------|--------|------|-----------------|--------------------|-----------|-----------------------------|
| 1 | alj_china_auto_001 | | FAIL (pre-CP-013) | | 0 | |
| 2 | china_monitor_001 | | PASS | N/A | 0 | |

**Overall outcome:** PENDING

---

*OPENCLAW-D-CP-014 | Version 1.0 | Created: 2026-05-24 | Status: APPROVED — implementation pending*
*Client scope: All clients — logging fix only, no delivery behavior change*
*Drafted by: Claude CoWork | Implementation: Claude Code / VPS operator*
*Independent of CP-013 — can be applied in either order*
