# OPENCLAW — CLIENT CONFIG LOADER SPECIFICATION

---
document_id: OPENCLAW-SPEC-CONFIG-LOADER-001
version: v1.2
created: 2026-05-13
last_updated: 2026-05-18
status: OPERATOR APPROVED — 2026-05-18
author: CoWork (drafted for operator review)
governing_doc: OpenClaw_Phase7_Execution_Plan.docx (Section 6.2, Section 13)
consultant_review: APPROVED AS DESIGN SPECIFICATION — 2026-05-13
  Rating: 9/10. v1.1 resolves all three design concerns from v1.0.
  eval risk removed; retrieval-scope drift constrained; Phase C gate
  language corrected; implementation gates explicit.
  Remaining required control: hardcoded-filename audit scope defined
  in Section 9.1 (expanded per consultant sign-off).
---

## STATUS: OPERATOR APPROVED — 2026-05-18
##
## Implementation gates (all must be satisfied before Step 9.1 may begin):
## (a) Operator approval of this spec
## (b) Brain Lite Runs 4–5 confirmed stable, OR explicit operator decision
##     to authorize Step 7 in parallel
## (c) Hardcoded-filename audit completed and reviewed (Step 9.1)

---

## 1. PURPOSE AND SCOPE

This document specifies the design for the Phase C client configuration loader
(Step 7 per 04_DAILY_STATUS.md NEXT STEP). The loader reads a per-client
`client_config.yaml` file at pipeline startup and passes its field values to
the appropriate pipeline components. It also defines artifact namespacing rules
and the synthetic second client test required as the Phase C exit gate.

**What this spec covers:**
- Config loader design and location
- Field mapping: which config field drives which pipeline component
- Artifact namespacing convention
- Runtime invocation change (how client_id flows through the pipeline)
- Synthetic second client configuration
- Isolation verification protocol (Phase C exit gate)
- Implementation sequencing

**What this spec does not cover:**
- Any changes to retrieval logic, scrubber logic, validator logic, or delivery
  gate behavior
- Brain Full features
- Phase D pilot client onboarding
- Credential migration (flagged in client_config.yaml as a separate step)

---

## 2. GOVERNING REQUIREMENTS (from Execution Plan Section 6.2)

> *"Implement config loader: reads client_config.yaml for the specified
> client_id at runtime startup."*

> *"Namespace all artifacts: retrieval_package_{client_id}.json,
> scrubber_report_{client_id}.json, validation_result_{client_id}.json,
> conflict_log_{client_id}.json, final_output_{client_id}.txt."*

> *"Create synthetic second client config: different topic_focus and region set;
> runs against live retrieval but delivers to a test channel only."*

> *"Isolation verification: confirm that no field from the synthetic client
> appears in the default client's artifacts, and vice versa. This is the
> Phase C exit gate."*

---

## 3. LOADER DESIGN

### 3.1 Location

```
/root/openclaw_phase7/config_loader/load_client_config.py
```

New directory. Not inside any existing phase directory. Does not modify any
existing pipeline script.

### 3.2 Invocation

The loader is called once at the start of `run_light_to_lark.sh`, before any
retrieval or orchestration step. It reads the client config and exports its
fields as environment variables consumed by downstream pipeline components.

`run_light_to_lark.sh` receives `--client_id` as a new argument:

```bash
bash run_light_to_lark.sh --client_id china_monitor_001
```

If `--client_id` is not supplied, it defaults to `china_monitor_001` —
preserving identical behavior for the existing cron entry.

### 3.3 Config File Path Convention

```
/root/openclaw_docs/config/client_config_{client_id}.yaml
```

The loader constructs this path from the supplied `client_id`. If the file
does not exist, the pipeline logs an error and exits before any retrieval
runs. No partial execution on missing config.

### 3.4 Loader Behavior

**Revised per consultant review (Point 3) — shell eval eliminated.**

The loader does not write to stdout for shell eval. Instead it writes all
resolved values to a fixed-path env file with a controlled key=value format.
The shell script reads individual named keys from this file — it does not
eval the file as a whole.

```
Loader output path: /root/openclaw_runtime/{client_id}/loader.env
Format: one KEY=value per line, no shell syntax, no subshells, no quotes
        with embedded commands. Values are validated as alphanumeric,
        path-safe strings before write.
```

Example env file content:
```
OPENCLAW_CLIENT_ID=china_monitor_001
OPENCLAW_ARTIFACT_NAMESPACE=china_monitor_001
OPENCLAW_BRAIN_CONTEXT=false
OPENCLAW_DELIVERY_TYPE=lark
OPENCLAW_CREDENTIALS_REF=/root/openclaw_secrets/lark_webhook_china_monitor_001
```

Shell script reads specific keys individually using `grep` + `cut`:
```bash
OPENCLAW_CLIENT_ID=$(grep '^OPENCLAW_CLIENT_ID=' "$LOADER_ENV_FILE" | cut -d= -f2)
OPENCLAW_ARTIFACT_NAMESPACE=$(grep '^OPENCLAW_ARTIFACT_NAMESPACE=' "$LOADER_ENV_FILE" | cut -d= -f2)
# ... one line per key; unknown keys are never read
```

The shell script reads only the specific named keys it expects. Any
unexpected content in the env file is ignored — never executed.

`topic_focus` and `regions` are multi-value fields — written separately to
`/tmp/openclaw_client_context_{client_id}.json`, read by retrieval scripts
directly via Python.

### 3.5 Validation

The loader validates all required fields before producing any output. If any
required field is missing or malformed, it exits with a non-zero code and logs
the specific field failure. The pipeline does not proceed.

Required fields: `client_id`, `artifact_namespace`, `topic_focus`, `regions`,
`query_template_set`, `report_template`, `delivery_channel.type`,
`delivery_channel.credentials_ref`, `brain_context`.

---

## 4. FIELD MAPPING

| Config Field | Consumer | How Used |
|---|---|---|
| `client_id` | All scripts | Passed as argument; used in artifact naming |
| `artifact_namespace` | All artifact writes | Suffix in all output filenames |
| `topic_focus` | `build_agent_input_slim.py` | Injected into agent system prompt topic context |
| `regions` | `brave_executor.py`, `baidu_executor.py` | Regional query routing |
| `query_template_set` | Retrieval orchestrator | Selects query template set |
| `report_template` | `build_agent_input_slim.py` | Selects output format block |
| `delivery_channel.type` | `run_light_to_lark.sh` | Delivery method selection |
| `delivery_channel.credentials_ref` | `run_light_to_lark.sh` | Credential path for delivery |
| `brain_context` | `build_agent_input_slim.py` | Gates Brain Lite digest injection |
| `source_preferences.priority_providers` | Retrieval orchestrator | Provider priority order |
| `output_sections` | `build_agent_input_slim.py` | Enables/disables output sections |
| `pilot_mode` | `run_light_to_lark.sh` | Gates external delivery (future) |

Fields not yet consumed (marked as future in config): `linkedin_draft`,
`regional_source_list`. These are read and validated but produce no effect
until Phase F.

---

## 5. ARTIFACT NAMESPACING

All pipeline artifact writes adopt the `_{client_id}` suffix pattern defined
in the Execution Plan. The table below shows the before/after filenames.

| Current Filename | Namespaced Filename |
|---|---|
| `retrieval_package.json` | `retrieval_package_{client_id}.json` |
| `brave_raw.json` | `brave_raw_{client_id}.json` |
| `baidu_raw.json` | `baidu_raw_{client_id}.json` |
| `final_output.txt` | `final_output_{client_id}.txt` |
| `final_output_scrubbed.txt` | `final_output_scrubbed_{client_id}.txt` |
| `conflict_log.json` | `conflict_log_{client_id}.json` |
| `validation_result.json` | `validation_result_{client_id}.json` |

**Location:** All namespaced artifacts remain in `/root/openclaw_phase5/data/`
for Phase C. A separate directory-per-client layout is a Phase F concern.

**Backward compatibility:** Existing scripts that hardcode the un-namespaced
filenames must be updated to read from `$OPENCLAW_ARTIFACT_NAMESPACE`. This
is the primary implementation change across the pipeline. A pre-implementation
hardcoded-filename audit (Claude Code grep) is required before any script
edits begin — to be submitted as a classification table for operator approval
before implementation proceeds.

---

## 6. RUN_LIGHT_TO_LARK.SH CHANGES (SUMMARY)

Three additions to the shell script:

1. **Argument parsing** — `--client_id` argument parsed at top of script;
   defaults to `china_monitor_001` if absent.
2. **Loader call** — loader is invoked; env file is written to
   `/tmp/openclaw_loader_{client_id}.env`; shell reads specific named keys
   individually (no eval). Pipeline exits if loader returns non-zero.
3. **Artifact path variables** — all hardcoded artifact filenames replaced with
   `$OPENCLAW_ARTIFACT_NAMESPACE`-parameterized equivalents.

No changes to retrieval logic, agent prompt content, scrubber logic, validator
logic, or delivery gate behavior.

### Retrieval Scope Constraint (consultant review Point 4)

`regions` and `source_preferences` from client config are passed to retrieval
scripts as **query-target selectors only** — they determine which geographic
API endpoints are called. They do not alter and must not be used to alter:

- Freshness parameters (`pd`/`pw` — hardcoded in retrieval scripts)
- Result ranking or scoring
- Filtering thresholds
- Provider weighting or fallback behavior
- Any other retrieval behavioral parameter

In Phase C, retrieval logic remains fully hardcoded. Config fields control
which clients and regions are targeted; they do not control how retrieval
operates. Any change to retrieval behavior requires a separate operator
decision and is explicitly out of scope for this spec.

---

## 7. SYNTHETIC SECOND CLIENT

### 7.1 Purpose

The synthetic second client tests namespace isolation end-to-end. It uses a
different `topic_focus` and `region` set from `china_monitor_001`. It delivers
to a test Lark channel only.

### 7.2 Proposed Config (for operator approval)

```yaml
# client_config_test_client_002.yaml
# Status: DRAFT — requires operator approval before deployment

client_id: test_client_002
client_name: "OpenClaw Test Client — Namespace Isolation"

artifact_namespace: test_client_002

topic_focus:
  - "European semiconductor supply chain"
  - "EU regulatory environment for technology companies"

regions:
  - "europe"

query_template_set: "china_monitor_v1"   # reuse existing templates
report_template:    "china_monitoring_brief_v1"

delivery_channel:
  type: lark
  credentials_ref: "/root/openclaw_secrets/lark_webhook_test_client_002"
  # NOTE: test channel webhook to be provisioned before synthetic run

schedule: "manual"   # not added to cron; triggered manually for test only

source_preferences:
  priority_providers:
    - brave
    - baidu

brain_context: false

output_sections:
  executive_take:       true
  advisory_layer:       true
  linkedin_draft:       false
  regional_source_list: false

pilot_mode: true   # external delivery gate required — test channel only
```

---

## 8. ISOLATION VERIFICATION PROTOCOL

Per Execution Plan Section 6.2, isolation verification is the Phase C exit
gate. The following verification steps must all pass before Phase C is
considered complete.

### 8.1 Test Procedure

**Step 1 — Run china_monitor_001:**
```bash
bash run_light_to_lark.sh --client_id china_monitor_001
```
Confirm all artifacts are namespaced `_china_monitor_001`. Confirm delivery
to china_monitor_001 Lark channel.

**Step 2 — Run test_client_002:**
```bash
bash run_light_to_lark.sh --client_id test_client_002
```
Confirm all artifacts are namespaced `_test_client_002`. Confirm delivery
to test_client_002 Lark channel only.

**Step 3 — Cross-contamination check:**
Run isolation verification script (to be drafted):
```bash
python3 /root/openclaw_phase7/config_loader/verify_isolation.py \
  --client_a china_monitor_001 \
  --client_b test_client_002
```

### 8.2 Isolation Checks (verify_isolation.py)

| Check | Pass Condition |
|---|---|
| No `_china_monitor_001` artifact contains any topic from `test_client_002.topic_focus` | Zero matches |
| No `_test_client_002` artifact contains any topic from `china_monitor_001.topic_focus` | Zero matches |
| `retrieval_package_china_monitor_001.json` and `retrieval_package_test_client_002.json` exist as separate files | Both present |
| `validation_result_china_monitor_001.json` and `validation_result_test_client_002.json` are distinct | Different run_ids |
| No `test_client_002` result_ids appear in `china_monitor_001` artifacts | Zero matches |
| No `china_monitor_001` result_ids appear in `test_client_002` artifacts | Zero matches |

All six checks must pass. Any failure blocks Step 7 completion.

**Phase C closure language (revised per consultant review Point 5):**
All 6 checks passing = Step 7 isolation criterion satisfied. Phase C closure
still requires Brain Lite stability confirmation (Runs 4–5 confirmed) and
explicit operator approval. Isolation verification is a necessary condition
for Phase C closure — it is not sufficient on its own.

---

## 9. IMPLEMENTATION SEQUENCING

The following order is required. No step may proceed until the prior step is
operator-approved and confirmed.

| Step | Action | Dependency |
|---|---|---|
| 9.1 | Hardcoded-filename audit — Claude Code grep across all pipeline scripts; classification table submitted for operator approval. Audit must cover every writer and reader of: retrieval_package.json, brave_raw.json, baidu_raw.json, final_output.txt, final_output_scrubbed.txt, conflict_log.json, validation_result.json, Brain Lite run_summary artifacts, citation substitution artifacts, validator artifact paths. | None — first step |
| 9.2 | Load_client_config.py — write and test locally; py_compile; submit for operator approval | 9.1 approved |
| 9.3 | run_light_to_lark.sh — argument parsing + loader call + `--client_id` default; submit for operator approval | 9.2 approved |
| 9.4 | Artifact namespacing — update all scripts per classification table from 9.1; submit as single patch for operator approval | 9.3 approved |
| 9.5 | test_client_002.yaml — deploy to VPS /root/openclaw_docs/ | Operator approval of config above |
| 9.6 | verify_isolation.py — write and submit for operator approval | 9.4 approved |
| 9.7 | Synthetic second client run — manual trigger; verify_isolation.py pass | 9.5, 9.6 complete |
| 9.8 | Operator confirmation of Phase C exit gate | 9.7 clean |

---

## 10. OUT OF SCOPE

The following are explicitly excluded from this spec. Any request to include
them requires a separate operator decision:

- Credential migration (Lark webhook from run_light_to_lark.sh to
  /root/openclaw_secrets/) — flagged in client_config.yaml; not a Phase C
  runtime change
- Directory-per-client artifact layout — Phase F concern
- Cron entry for test_client_002 — test client is manual-trigger only
- Any changes to retrieval query logic, scrubber, validator, or delivery gate
- Brain Full features

---

## 11. APPROVAL GATE

This document is a draft. No implementation step may begin until the operator
explicitly approves this spec. Upon approval:

- This document status updates to: APPROVED
- Implementation step 9.1 (hardcoded-filename audit) may begin
- Each subsequent step requires its own approval per Section 9

---

*OPENCLAW-SPEC-CONFIG-LOADER-001 | v1.2 | 2026-05-13 | CONSULTANT APPROVED*
*v1.1 changes: shell eval eliminated (Point 3 — env file + named key reads);*
*retrieval scope constraint added to Section 6 (Point 4); Phase C gate*
*language corrected in Section 8.2 (Point 5); implementation gates added*
*to status header (Points 1, 2). All changes per consultant review.*
*Consultant sign-off: APPROVED 2026-05-13. Rating 9/10. Audit scope*
*expanded in Section 9.1 per consultant final note.*
*v1.2 changes (operator approved 2026-05-18): Section 3.3 config path*
*corrected to /root/openclaw_docs/config/ (actual VPS location); Section 3.4*
*loader output path corrected to /root/openclaw_runtime/{client_id}/loader.env*
*(updated from /tmp/ per operator approval — improved durability and auditability).*
