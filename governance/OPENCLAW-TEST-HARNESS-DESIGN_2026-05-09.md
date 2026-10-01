---
document_id: OPENCLAW-TEST-HARNESS-DESIGN
version: 1.1
date: 2026-05-09
status: APPROVED — 2026-05-09 (Step 5); revised per OPENCLAW-OPERATOR-RESPONSE-STEP5
source: Phase 7 Execution Plan, Section B-7 and Section 6.2
---

# OPENCLAW — Multi-Client Test Harness Design

## Purpose

This document defines the design of a synthetic test framework that
can run a named client_config.yaml through the full OpenClaw pipeline
without affecting the live client's artifact namespace. It covers:

1. How client_id is injected into the pipeline at runtime
2. How artifacts are isolated by client
3. Pre-implementation hardcoded-filename audit (required before Phase C)
4. The synthetic second client specification
5. Cross-contamination verification protocol
6. The verification protocol for Phase C exit criteria

This is a design document only. No implementation is authorized
until Phase C opens with explicit operator approval.

---

## 1. Client ID Injection Model

**APPROVED AS DRAFTED — 2026-05-09**

At Phase C implementation, the pipeline entry point
(run_light_to_lark.sh) accepts client_id as a CLI argument:

```bash
./run_light_to_lark.sh --client_id china_monitor_001
```

The script reads the matching client_config.yaml and passes client_id
as an environment variable to all downstream pipeline components:

```bash
export CLIENT_ID="china_monitor_001"
```

Each pipeline component (orchestrator, agent input builder, resolver,
scrubber, validator, delivery gate) reads CLIENT_ID and uses it for:
- Locating the correct client_config.yaml at startup
- Naming all artifact output files
- Routing delivery to the correct channel

The live cron job continues to call the script with the default
client_id:

```bash
# cron: runs at 06:30 CST daily
./run_light_to_lark.sh --client_id china_monitor_001
```

The test harness calls the same script with the synthetic client_id:

```bash
# test harness: manual invocation only, never in live cron
./run_light_to_lark.sh --client_id test_client_001
```

**Constraint:** The synthetic client MUST NOT be added to cron.
Test runs are manual invocations only. Operator authorizes each test
run explicitly. This is not a Phase B implementation item — it is a
Phase C operating rule.

---

## 2. Artifact Isolation Model

**APPROVED WITH REVISION — 2026-05-09**

All artifact writes are namespaced by client_id. The data directory
holds multiple clients' artifacts side by side. No per-client
subdirectory is created — isolation is by filename, not by path.

**Artifact naming convention (Phase C):**

```
/root/openclaw_phase5/data/
  retrieval_package_{client_id}.json
  final_output_{client_id}.txt
  final_output_scrubbed_{client_id}.txt
  agent_input_{client_id}.txt
  agent_input_slim_{client_id}.txt
  conflict_log_{client_id}.json

/root/openclaw_phase6/validation/
  scrubber_report_{client_id}.json
  validation_result_{client_id}.json
```

**Default client artifacts (pre-Phase C naming → Phase C naming):**
```
retrieval_package.json          → retrieval_package_china_monitor_001.json
final_output.txt                → final_output_china_monitor_001.txt
scrubber_report.json            → scrubber_report_china_monitor_001.json
validation_result.json          → validation_result_china_monitor_001.json
conflict_log.json               → conflict_log_china_monitor_001.json
```

Migration of existing artifact names is a Phase C implementation
decision. The test harness assumes the namespaced convention is
already in place before synthetic client runs begin.

**Risk note:** If any pipeline component has a hardcoded output
filename (not parameterized on CLIENT_ID), it will silently overwrite
the previous client's artifact rather than writing a new one. This
risk is addressed by the mandatory pre-implementation audit in
Section 3 below.

---

## 3. Pre-Implementation Hardcoded-Filename Audit

**REQUIRED before Phase C implementation may proceed.**

Before any Phase C implementation work begins, the operator must run
the following audit to identify every hardcoded artifact path in the
pipeline codebase:

```bash
grep -R "retrieval_package.json\|scrubber_report.json\|validation_result.json\|conflict_log.json\|final_output.txt\|final_output_scrubbed.txt\|agent_input_slim.txt" \
  /root/openclaw_phase5 \
  /root/openclaw_phase6 \
  /root/run_light_to_lark.sh
```

Every artifact read/write path identified must be classified before
Phase C implementation is approved:

```
A. Must be client-namespaced
   — Paths that write output artifacts; must incorporate CLIENT_ID

B. May remain global
   — Shared config or reference files not specific to any client run

C. Must remain global
   — Paths intentionally shared across clients (e.g., schema files,
     static reference data)

D. Needs operator decision
   — Paths whose correct classification is ambiguous
```

Any path classified A that still contains a hardcoded filename must
be corrected during Phase C implementation before synthetic-client
testing proceeds. Any path classified D must be resolved by operator
decision before implementation continues.

This audit produces a classification table that is submitted to the
operator for review. No implementation begins until the table is
approved.

---

## 4. Synthetic Second Client Specification

The synthetic client is designed to produce maximally distinct output
from china_monitor_001, making cross-contamination easy to detect.

```yaml
# client_config.yaml — Synthetic Test Client
# FOR TESTING ONLY — not a real client

client_id: test_client_001
client_name: "Synthetic Test Client — Phase C Isolation Verification"

artifact_namespace: test_client_001

topic_focus:
  - "Southeast Asia technology policy and digital economy"
  - "ASEAN trade agreements and supply chain realignment"
  - "India manufacturing sector and foreign direct investment"

regions:
  - "southeast_asia"
  - "south_asia"

query_template_set: "test_client_v1"
report_template:    "test_brief_v1"

delivery_channel:
  type: lark
  credentials_ref: "/root/openclaw_secrets/lark_webhook_test_client_001"
  # NOTE: test channel — delivers to an isolated test Lark group,
  # not visible to any external recipient

schedule: "manual only — never added to cron"

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

pilot_mode: true    # Operator review required before any delivery
```

**Why these topic choices:** Southeast Asia / South Asia topics produce
content with no thematic overlap with China Monitoring Brief output.
If any China-specific publisher, topic, or source appears in
test_client_001 artifacts, it is unambiguous contamination.

**Why Baidu is retained as a provider:** Testing that the same provider
produces correctly namespaced artifacts for two different clients is
part of what the harness verifies. Using a different provider set for
the synthetic client would allow a provider-level routing bug to go
undetected.

---

## 5. Cross-Contamination Verification Protocol

After a synthetic client run, the following verification steps confirm
zero cross-contamination. These checks are run manually by the operator
(or by CoWork with read access to both artifact sets).

### Step 5.1 — Artifact filename audit

Confirm all artifacts carry the correct client_id suffix and no
unsuffixed (legacy) artifacts exist:

```bash
ls -la /root/openclaw_phase5/data/ | grep "china_monitor_001"
ls -la /root/openclaw_phase5/data/ | grep "test_client_001"
ls -la /root/openclaw_phase6/validation/ | grep "china_monitor_001"
ls -la /root/openclaw_phase6/validation/ | grep "test_client_001"
```

Expected: both china_monitor_001 and test_client_001 artifacts are
present with correct suffixes. Any file without a client_id suffix is
a namespacing failure.

### Step 5.2 — Post-run cross-identifier contamination check

Inspect artifact content for cross-client identifier bleed:

```bash
grep -R "test_client_001" \
  /root/openclaw_phase5/data/*china_monitor_001* \
  /root/openclaw_phase6/validation/*china_monitor_001*

grep -R "china_monitor_001" \
  /root/openclaw_phase5/data/*test_client_001* \
  /root/openclaw_phase6/validation/*test_client_001*
```

Expected result: zero matches in both directions. No synthetic client
identifier appears in default-client artifacts. No default-client
identifier appears in synthetic-client artifacts.

### Step 5.3 — Content cross-check: test client artifacts

Search test_client_001 artifacts for any content from china_monitor_001
topic set (US-China, Europe, Middle East):

```bash
grep -i "china\|US-China\|Europe\|Middle East\|Sina\|Reuters\|CCTV\|Baidu" \
  /root/openclaw_phase5/data/final_output_test_client_001.txt
```

Expected: zero matches. Any match is a cross-contamination failure.

### Step 5.4 — Content cross-check: live client artifacts

Search china_monitor_001 artifacts for any content from test_client_001
topic set (Southeast Asia, India, ASEAN):

```bash
grep -i "ASEAN\|Southeast Asia\|India\|south_asia\|test_client" \
  /root/openclaw_phase5/data/final_output_china_monitor_001.txt
```

Expected: zero matches. Any match is a cross-contamination failure.

### Step 5.5 — Validator artifact cross-check

Confirm each validation_result.json references only its own client's
citations (result_ids from the correct client's retrieval_package).
This check requires a script that extracts result_ids from both files
and diffs them. Script design deferred to Phase C implementation.

### Step 5.6 — Brain Lite store cross-check (Phase C, if active)

Confirm that run_summaries are written to separate namespaced files:
```
/root/openclaw_cowork/run_summaries/run_summary_china_monitor_001_YYYYMMDD.json
/root/openclaw_cowork/run_summaries/run_summary_test_client_001_YYYYMMDD.json
```

No shared fields, no shared source lists, no shared topic entries
across the two clients' run_summary files.

---

## 6. Phase C Exit Criteria — Harness Confirmation

Per the Phase 7 Execution Plan (Section 6.2), the test harness must
confirm all four exit criteria before Phase C closes:

| Exit Criterion | Verification Method | Pass Condition |
|----------------|---------------------|----------------|
| Default client unaffected post-config loader | 5 consecutive clean runs after implementation | ids_removed=0, validator GREEN PASS throughout |
| Synthetic client runs end-to-end with namespaced artifacts | Inspect all artifact filenames | client_id present in all artifact paths |
| Zero cross-client data in any artifact | Steps 5.2, 5.3, and 5.4 above | grep returns zero matches in all directions |
| Harness operational and confirmed correct | Run harness; confirm isolation | All verification steps pass |

**Failure handling:** If any cross-contamination is detected at any
verification step, the test run is halted, the contamination is logged
as a new issue, and no real client goes live until the issue is
resolved and the full verification protocol passes cleanly.

---

## 7. What This Design Does Not Cover

The following are out of scope for Phase B design and are deferred to
Phase C implementation:

- The config loader implementation (how client_config.yaml is parsed
  at runtime startup)
- The artifact rename/migration script for pre-Phase C artifacts
- The automated diff script for Step 5.5 (validator artifact cross-check)
- The test Lark channel setup for test_client_001 delivery
- cron configuration for any additional client (prohibited until
  Phase C is confirmed stable)
- Execution of the hardcoded-filename audit in Section 3 (a Phase C
  pre-implementation requirement, not a Phase B action)

---

*OPENCLAW-TEST-HARNESS-DESIGN v1.1 | 2026-05-09 | APPROVED*
*Revised per OPENCLAW-OPERATOR-RESPONSE-STEP5: hardcoded-filename audit*
*elevated to required Section 3; post-run contamination checks updated.*
*Design only — no implementation authorized until Phase C opens.*
*No system changes take effect without explicit operator approval.*
