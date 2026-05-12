---
document_id: OPENCLAW-BRAIN-LITE-DESIGN
version: 1.1
date: 2026-05-09
status: APPROVED — 2026-05-09; revised per OPENCLAW-OPERATOR-RESPONSE-BRAIN-LITE-OPTIONS
source: Phase 7 Execution Plan; Brain Lite Options Memo v1.0
---

# OPENCLAW — Brain Lite Implementation Design

## Architecture Decision

Option A approved in principle. Option B rejected. Option C rejected
as primary implementation model.

Approved architecture:
```
Deterministic VPS-resident Brain Lite code writes run summaries.
Deterministic digest builder creates a bounded seven-day digest.
Digest is injected into agent input only as context enrichment.
CoWork reads Brain Lite artifacts but does not generate or modify them.
Validator, scrubber, control layer, and delivery gate remain unchanged.
```

This preserves the permanent architectural rule:
```
CoWork may analyze Brain Lite.
CoWork may not become Brain Lite.
```

---

## 1. Two-Function Design

Brain Lite is two distinct deterministic functions:

**Function 1: Post-run summary writer**
```
Script:  write_run_summary.py
Trigger: after delivery completes with allowed final_decision
Input:   validation_result.json, conflict_log.json,
         delivery log, retrieval_package.json,
         final delivered output, scrubber metrics from cron log
Output:  run_summary_{client_id}_YYYYMMDD.json
Path:    /root/openclaw_phase7/brain_lite/run_summaries/
```
Note: scrubber_report.json is not an input — it was never implemented
(T-06, resolved 2026-05-11). Scrubber metrics are sourced from stdout
captured in the cron log.

**Function 2: Pre-run digest builder**
```
Script:  build_brain_digest.py
Trigger: before agent is invoked, at next run start
Input:   last seven run_summary files for client_id
Output:  brain_digest_{client_id}.txt
Path:    /root/openclaw_phase7/brain_lite/
```

**Support files:**
```
schema_run_summary_v1.json  — locked 14-field schema
                              (see OPENCLAW-BRAIN-LITE-SCHEMA-v1)
```

**Directory structure (Phase C):**
```
/root/openclaw_phase7/brain_lite/
  write_run_summary.py
  build_brain_digest.py
  schema_run_summary_v1.json
  run_summaries/
    run_summary_{client_id}_YYYYMMDD.json
```

The exact file paths may be finalized during Phase C implementation
planning. The conceptual split between the two functions is locked.

---

## 2. Triggering Model

Brain Lite summary writing is triggered by the delivery decision,
not by shell exit code alone.

**Required trigger condition:**
```
final_decision ∈ { delivered | delivered_with_warning }
```

**Required call site in run_light_to_lark.sh (Phase C implementation):**
```
→ run normal pipeline
→ complete validator / delivery gate
→ if final_decision = delivered or delivered_with_warning:
      call write_run_summary.py
→ if Brain Lite summary write fails:
      log the error
      do not affect already-completed delivery
```

**Required log tags:**
```
[BRAIN_LITE] summary_write_started
[BRAIN_LITE] summary_write_completed
[BRAIN_LITE] summary_write_failed
```

Note: The conceptual sketch `&& python3 /root/brain_lite.py` in the
prior memo is not the final approved design. The trigger must be
conditional on final_decision, not merely on prior exit code.

Brain Lite failure must not retroactively affect a completed delivery.

---

## 3. Failure Model

Brain Lite is an enrichment layer, not an enforcement layer.
Failure at either function must be non-blocking.

**Summary writer failure:**
```
Log [BRAIN_LITE] summary_write_failed.
Do not affect completed delivery.
Omit failed summary from future digests.
```

**Digest builder failure:**
```
Log [BRAIN_LITE] digest_unavailable.
Continue with brain_context = disabled_for_this_run.
Do not block retrieval.
Do not block agent.
Do not block validation.
Do not block delivery.
```

Validator, scrubber, control layer, and delivery gate remain the
trust mechanism. Brain Lite status does not gate any of these.

---

## 4. Digest Injection Point

The seven-day digest is injected into the agent context window at:

```
File:     build_agent_input_slim.py
Position: after VALID_SOURCE_NUMBERS block (~line 165)
          before full_prompt write to OUTPUT_PATH (~line 169)
```

Note: design doc previously referenced VALID_RESULT_IDS — corrected
2026-05-11. Phase 6.8 replaced VALID_RESULT_IDS with the numbered-
source architecture. The live token is VALID_SOURCE_NUMBERS, confirmed
via Claude Code audit of build_agent_input_slim.py on 2026-05-11.

This keeps the digest separated from instruction text and prevents
it from being treated as system instruction. The digest must be
structured text, not free-form narrative.

---

## 5. Schema Validation

Every generated run_summary.json must be validated against the locked
schema before being written or marked usable.

**Required validation checks:**
```
All 14 fields present
No extra fields unless operator-approved
Correct data types per schema_run_summary_v1.json
topics_covered max 8 items; max 60 chars each
sources_cited max 12 items
conflicts_flagged max 5 items; max 120 chars each
validator_status ∈ { GREEN | WARN | FAIL }
delivery_status ∈ { delivered | blocked }
```

**If validation fails:**
```
Write rejected summary to quarantine or error log.
Do not include it in seven-day digest.
Log [BRAIN_LITE] summary_schema_invalid.
Continue pipeline without Brain Lite context if necessary.
```

The locked 14-field schema is defined in OPENCLAW-BRAIN-LITE-SCHEMA-v1.
No additional fields may be added without formal operator approval.

---

## 6. Digest Budget Enforcement

The digest builder must enforce the 1,200-token limit before
injection. No semantic summarization by CoWork or other LLM is
approved. Truncation must be deterministic.

**Approved prioritization if budget is exceeded:**
```
1. sources_cited from the most recent three runs
2. topics_covered trend
3. conflicts_flagged from the most recent run
```

Items are dropped in reverse priority order until the digest fits
within the 1,200-token budget. No partial items — if an item does
not fit, the entire item is dropped.

---

## 7. Disable Switch

Brain Lite has a simple disable mechanism via client_config.yaml:

```yaml
brain_context: true   # inject digest if available
brain_context: false  # skip digest injection entirely
```

This aligns with the existing client_config schema.
Currently set to `false` in client_config_china_monitor_001.yaml.
Set to `true` only when Phase C confirms Brain Lite stable.

The operator may set `brain_context: false` at any time to disable
Brain Lite for a specific client without pipeline modification.

---

## 8. Write Ownership and Permissions

**Approved rule:**
```
run_summary writer:  deterministic Brain Lite runtime code only
run_summary reader:  CoWork and operator
run_summary editor:  none
```

**Preferred storage path (Phase C):**
```
/root/openclaw_phase7/brain_lite/run_summaries/
```

Runtime code has write access. CoWork (openclaw_cowork user) has
read access only. No write access for CoWork to this path.

If `/root/openclaw_cowork/run_summaries/` is used as an alternative,
file permissions must explicitly enforce:
```
runtime write access
openclaw_cowork read-only access
```

The key principle: CoWork must not write any artifact later injected
into the pipeline.

---

## 9. Phase C Pre-Implementation Checklist

Before Phase C Brain Lite implementation may begin:

```
□ Phase B gate formally closed by operator
□ Phase C explicitly opened by operator
□ schema_run_summary_v1.json approved
   (see OPENCLAW-BRAIN-LITE-SCHEMA-v1)
□ Hardcoded artifact path audit complete and approved
   (per OPENCLAW-TEST-HARNESS-DESIGN Section 3)
□ Injection point in build_agent_input_slim.py confirmed
   (VALID_RESULT_IDS block located and verified in code)
□ /root/openclaw_phase7/brain_lite/ directory structure confirmed
□ Permission model for run_summaries/ confirmed
□ BRAIN_LITE log tag format confirmed
```

---

## 10. What This Design Does Not Authorize

Not authorized until Phase C opens with explicit operator approval:
```
cron modification
run_light_to_lark.sh modification
build_agent_input_slim.py modification
write_run_summary.py deployment
build_brain_digest.py deployment
digest injection
run_summary writing
permission changes
```

---

*OPENCLAW-BRAIN-LITE-DESIGN v1.1 | 2026-05-09 | APPROVED*
*Revised per OPENCLAW-OPERATOR-RESPONSE-BRAIN-LITE-OPTIONS.*
*No implementation authorized until Phase C opens.*
*No system changes take effect without explicit operator approval.*
