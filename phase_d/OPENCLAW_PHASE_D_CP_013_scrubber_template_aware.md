---
document_id: OPENCLAW-D-CP-013
version: 1.0
created: 2026-05-24
classification: PHASE D CHANGE PACKET — SCRUBBER
---

# OPENCLAW — Phase D Change Packet CP-013
# Scrubber Template-ization for Non-WS1 Report Templates — scrub_result_ids.py

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-013 |
| Date raised | 2026-05-24 |
| Raised by | Operator (ALJ pilot run 2026-05-24 18:56 UTC) |
| Client ID | alj_china_auto_001 (does not affect china_monitor_001) |
| Feedback items addressed | N/A — ALJ pipeline blocker |
| Recurrence threshold met? | N/A |
| Implementation layer | Scrubber (scrub_result_ids.py) — section header set and required-cited gate |
| Depends on | CP-012 (merged — established OPENCLAW_REPORT_TEMPLATE routing in run_light_to_lark.sh) |
| Status | APPROVED — implementation pending |

**Note:** This CP is a pre-run blocker for ALJ. Without it, every ALJ
pilot run fails at the scrubber even when citations are 100% clean.
The failure is structural — the scrubber hardcodes WS1 section headers
and will never see a valid EXECUTIVE TAKE section in an ALJ report.

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

`scrub_result_ids.py` hardcodes WS1 section headers and a WS1-specific
cited-section gate. The ALJ report template uses SECTION 1 through
SECTION 8, so the scrubber's section-tracking never engages, the
required-cited gate fires unconditionally, and every ALJ run exits 1.

**Root cause:**

`scrub_result_ids.py` line 20:
```python
SECTION_HEADERS = {"EXECUTIVE TAKE", "ADVISORY LAYER"}
```

And the cited-section gate at lines 134–136:
```python
if exec_take_cited_remaining == 0:
    print("[FAIL] EXECUTIVE TAKE has zero cited bullets after uncited removal; delivery blocked")
    sys.exit(1)
```

The section-tracking logic increments `exec_take_cited` only when
`current_section == "EXECUTIVE TAKE"`. For ALJ output, `current_section`
never enters `SECTION_HEADERS` → `exec_take_cited` stays 0 for the
entire run → gate fires.

**Evidence (ALJ pilot run 2026-05-24 18:56 UTC, scrubber replay):**

```
valid_ids_loaded=9
citation_groups_seen=8
ids_seen=15
ids_kept=15
ids_removed=0
unsupported_groups=0
uncited_claims_removed=0
[FAIL] EXECUTIVE TAKE has zero cited bullets after uncited removal; delivery blocked
scrubber exit=1
```

Citations resolved 15-for-15. The failure is entirely structural — the
scrubber does not recognise ALJ section headers.

**Why this matters:**

Every ALJ pilot run will fail at this point until CP-013 is applied.
The ALJ product spec (CP-009) mandates 8 specific output sections.
None of them are named EXECUTIVE TAKE or ADVISORY LAYER. The scrubber
cannot be made to pass ALJ output without this change.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `/root/openclaw_phase6/validation/scrub_result_ids.py`

**Change description:**

Read `OPENCLAW_REPORT_TEMPLATE` from the environment at the top of the
script. Select two pieces of template-specific behavior from a config
dict defined at the top of the file:

1. `SECTION_HEADERS` — the set of section header strings the scrubber
   recognises when walking the report. Drives section-tracking and the
   scope of uncited-bullet removal.

2. `REQUIRED_CITED_SECTION` — the single section that must contain ≥1
   cited bullet after scrubbing for the run to be deliverable. The
   gate message is parameterised from this value.

**Template config dict (add near top of file, after imports):**

```python
import os

_TEMPLATE_CONFIG = {
    "alj_china_auto_weekly_v1": {
        "section_headers": {
            "SECTION 1", "SECTION 2", "SECTION 3",
            "SECTION 4", "SECTION 5", "SECTION 6",
            "SECTION 7", "SECTION 8",
        },
        "required_cited_section": "SECTION 1",
    },
}

_DEFAULT_CONFIG = {
    "section_headers": {"EXECUTIVE TAKE", "ADVISORY LAYER"},
    "required_cited_section": "EXECUTIVE TAKE",
}

_report_template = os.environ.get("OPENCLAW_REPORT_TEMPLATE", "")
_cfg = _TEMPLATE_CONFIG.get(_report_template, _DEFAULT_CONFIG)

SECTION_HEADERS = _cfg["section_headers"]
REQUIRED_CITED_SECTION = _cfg["required_cited_section"]
```

**Gate change (replace hardcoded EXECUTIVE TAKE gate):**

Before:
```python
if exec_take_cited_remaining == 0:
    print("[FAIL] EXECUTIVE TAKE has zero cited bullets after uncited removal; delivery blocked")
    sys.exit(1)
```

After:
```python
if exec_take_cited_remaining == 0:
    print(f"[FAIL] {REQUIRED_CITED_SECTION} has zero cited bullets after uncited removal; delivery blocked")
    sys.exit(1)
```

**Counter variable rename (optional but recommended for readability):**

`exec_take_cited` → `required_section_cited` throughout the file.
This is a pure rename — no logic change. If the reviewer considers it
scope creep, skip the rename and leave `exec_take_cited` as-is; the
gate change above works either way.

**WS1 preservation:** The default path (any template value not in
`_TEMPLATE_CONFIG`) receives `_DEFAULT_CONFIG` — identical to the
current hardcoded values. No existing behaviour changes for
`china_monitor_001`.

---

## SECTION 3 — DESIGN CONSTRAINTS

All constraints carried verbatim from operator brief:

- **Do not weaken citation enforcement.** `unsupported_groups`,
  `ids_seen/ids_kept/ids_removed` counting, and the "all groups
  unsupported → FAIL" gate are untouched.
- **Do not bypass uncited-claim removal.** `remove_uncited_bullets`
  still runs for every template; only the set of sections it scopes
  over becomes template-driven.
- **Do not alter validator strictness.** CP-013 does not touch
  `validator.py` or `validation_result_*.json`.
- **Do not alter Delivery Gate behaviour.** `run_light_to_lark.sh`
  lines 200–204 (scrubber exit handling) and delivery decision logic
  are untouched.
- **Only make the scrubber aware of valid section headers and the
  minimum cited-section rule for each report template.**
- **Default behaviour for china_monitor_001 must remain unchanged.**
- **ALJ template recognises SECTION 1 through SECTION 8.**
- **ALJ required-cited gate: SECTION 1 must contain ≥1 cited bullet**
  after scrubbing. Operator confirmed 2026-05-24.

---

## SECTION 4 — RISK ASSESSMENT

**Risk level:** LOW–MEDIUM

- Low for `china_monitor_001`: default branch is byte-identical to
  current hardcoded values. Regression-check step in validation plan
  catches any drift.
- Medium for ALJ: the cited-section gate semantics are a product
  choice. Operator confirmed SECTION 1 as the gate on 2026-05-24.
  First ALJ pilot run in pilot_mode=true will validate the choice.
- No risk to validator, delivery gate, or citation enforcement — all
  out of scope.

**Rollback plan:**

Before any modification, Claude Code creates:
```
/root/openclaw_phase6/validation/scrub_result_ids.py.bak_20260524_cp013
```

Rollback: restore from backup. ALJ returns to scrubber-FAIL behavior
(same as current — no crash in WS1, WS1 unaffected in either direction).

---

## SECTION 5 — VALIDATION METHOD

**Validation criteria:**

1. **py_compile exit 0** on modified `scrub_result_ids.py`
2. **Scrubber replay against existing ALJ artifacts** (no re-run needed;
   artifacts already on disk from the 2026-05-24 18:56 UTC run):
   ```
   OPENCLAW_ARTIFACT_NAMESPACE=alj_china_auto_001 \
   OPENCLAW_REPORT_TEMPLATE=alj_china_auto_weekly_v1 \
   python3 /root/openclaw_phase6/validation/scrub_result_ids.py
   ```
   Expected: `citation_groups_seen=8`, `ids_kept=15`,
   `unsupported_groups=0`, `uncited_claims_removed=0`, exit 0,
   `final_output_scrubbed_alj_china_auto_001.txt` written.
3. **WS1 regression:** replay scrubber against most-recent
   china_monitor artifacts with `OPENCLAW_REPORT_TEMPLATE` unset.
   Expected: identical behavior — same counters, same exit code.
4. **End-to-end ALJ pilot run** with `OPENCLAW_PILOT_MODE=true`:
   ```
   /root/run_light_to_lark.sh --client_id alj_china_auto_001
   ```
   Expected: scrubber exits 0, validator runs, delivery decision is
   `delivered` or `delivered_with_warning`, pilot_mode gate fires
   `[SKIP] pilot_mode=true`. Final scrubbed output written.
5. **WS1 end-to-end regression:** next scheduled cron tick or one
   manual run. Expected: unchanged versus pre-CP-013.

**Runs required to validate:** 1 ALJ pilot run + 1 WS1 regression.

---

## SECTION 6 — SCOPE COMPLIANCE CHECK

- [x] Change confined to one file (`scrub_result_ids.py`) — config dict + gate parameterisation only
- [x] Rollback path documented
- [x] Within Phase D scope (ALJ pipeline unblock — WS2 capability)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT alter WS1 (china_monitor_001) behavior — default branch unchanged
- [x] Does NOT weaken citation enforcement
- [x] Does NOT bypass uncited-claim removal
- [x] Does NOT alter validator strictness
- [x] Does NOT alter Delivery Gate behavior
- [x] Does NOT touch run_light_to_lark.sh (CP-014 covers the log-fix)
- [x] Does NOT affect client namespace isolation

---

## SECTION 7 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-05-24 |
| ALJ cited-gate confirmed | SECTION 1, ≥1 cited bullet (confirmed 2026-05-24) |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | |
| Backup confirmed | |

**Pre-implementation checklist:**
- [ ] `scrub_result_ids.py.bak_20260524_cp013` created
- [ ] `_TEMPLATE_CONFIG` dict inserted, `SECTION_HEADERS` and `REQUIRED_CITED_SECTION` derived from env
- [ ] Gate message parameterised with `REQUIRED_CITED_SECTION`
- [ ] `py_compile` exit 0
- [ ] Scrubber replay against ALJ artifacts exits 0 with expected counters
- [ ] WS1 scrubber regression confirms unchanged behavior

---

## SECTION 8 — POST-IMPLEMENTATION RESULTS

| Run # | Client | Date | Scrubber exit | ids_kept | unsupported_groups | uncited_removed | Validator | Pilot gate |
|-------|--------|------|--------------|----------|--------------------|-----------------|-----------|------------|
| 1 | alj_china_auto_001 | | | | | | | |
| 2 | china_monitor_001 | | | N/A (regression) | N/A | N/A | | N/A |

**Overall outcome:** PENDING

---

*OPENCLAW-D-CP-013 | Version 1.0 | Created: 2026-05-24 | Status: APPROVED — implementation pending*
*Client scope: alj_china_auto_001 scrubber template-ization; china_monitor_001 unaffected*
*Drafted by: Claude CoWork | Implementation: Claude Code / VPS operator*
*Depends on: CP-012 (merged 2026-05-24)*
