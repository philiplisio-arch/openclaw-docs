---
document_id: OPENCLAW-D-CP-006
version: 1.0
created: 2026-05-22
classification: PHASE D IMPLEMENTATION CHANGE PACKET — ALJ CLIENT RETRIEVAL
---

# OPENCLAW — Phase D Change Packet CP-006
# Baidu-Only Retrieval — ALJ China Auto Weekly Brief

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-006 |
| Date raised | 2026-05-22 |
| Raised by | Operator |
| Client ID | alj_china_auto_001 (new client — does not affect china_monitor_001) |
| Feedback items addressed | N/A — new client capability, not a content feedback item |
| Feedback recurrence threshold met? | N/A |
| Implementation layer | Client config + config loader schema + orchestrator shell script |
| Status | IMPLEMENTED — validation pending (first ALJ pilot run + next china_monitor_001 cron) |

**Note:** This is an implementation change packet, not a content change packet.
It enables a new per-client retrieval provider configuration capability.
It spans three coordinated files. All three edits are required — they cannot
be applied independently. The china_monitor_001 default behavior is preserved
in full by defaulting OPENCLAW_RETRIEVAL_PROVIDERS to brave,baidu when the
field is absent.

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

The retrieval orchestrator calls brave_executor.py and baidu_executor.py as a
fixed hard-coded pair on every run, regardless of client config. There is no
mechanism to skip Brave for a client that requires Baidu-only retrieval.

The ALJ China Auto Weekly Brief (alj_china_auto_001) requires Baidu-only
retrieval. Chinese / China-market source integrity is a non-negotiable product
requirement for this client. Brave retrieval surfaces international sources
(Reuters, CNBC, NYT, etc.) which are excluded from the ALJ source universe.

**Evidence:**

Claude Code audit — 2026-05-22:
- /root/openclaw_phase5/orchestrator/run_phase5_offline.sh:8
  python3 /root/openclaw_phase5/orchestrator/brave_executor.py
  Called unconditionally. No guard, no flag check, no skip path.
- run_light_to_lark.sh: reads loader.env but does not export or check any
  retrieval provider field. No provider flag exists in the current loader
  schema.
- The script uses set -euo pipefail — Brave failure aborts the entire run.

**Why this matters:**

Without this change, the ALJ client cannot run. Brave results would pollute
the retrieval package with international sources, violating the client's
source rules and the mandatory Chinese Source Appendix requirement.

---

## SECTION 2 — PROPOSED CHANGE

Three coordinated edits. All three must be implemented together.

---

### Edit A — Config loader schema (load_client_config.py + loader.env)

**Affected file:** /root/openclaw_phase7/config_loader/load_client_config.py

**Current behaviour:**
```
loader.env exposes: CLIENT_ID, ARTIFACT_NAMESPACE, BRAIN_CONTEXT,
DELIVERY_TYPE, CREDENTIALS_REF, QUERY_TEMPLATE, REPORT_TEMPLATE, PILOT_MODE
No retrieval provider field is emitted.
```

**Proposed behaviour:**
```
Add new field to loader.env output:
OPENCLAW_RETRIEVAL_PROVIDERS=brave,baidu   ← default (china_monitor_001 unchanged)

For alj_china_auto_001 (per client_config_alj_china_auto_001.yaml):
OPENCLAW_RETRIEVAL_PROVIDERS=baidu

The loader reads source_preferences.priority_providers from client_config.yaml
and emits the value as a comma-separated string.
Default: brave,baidu (preserves current behavior for all existing clients).
```

**Rationale:**
Keeps provider selection in client config where it belongs. Default value
ensures china_monitor_001 is completely unaffected.

---

### Edit B — Shell script export (run_light_to_lark.sh)

**Affected file:** /root/run_light_to_lark.sh

**Current behaviour:**
```
Script reads loader.env and exports ARTIFACT_NAMESPACE and PILOT_MODE.
OPENCLAW_RETRIEVAL_PROVIDERS is not read or exported — it would not
reach run_phase5_offline.sh (a subshell).
```

**Proposed behaviour:**
```
Add to the loader.env read block:
OPENCLAW_RETRIEVAL_PROVIDERS=$(grep '^OPENCLAW_RETRIEVAL_PROVIDERS=' \
  "$LOADER_ENV_FILE" | cut -d= -f2)
export OPENCLAW_RETRIEVAL_PROVIDERS

Default fallback (if field absent from loader.env):
OPENCLAW_RETRIEVAL_PROVIDERS="${OPENCLAW_RETRIEVAL_PROVIDERS:-brave,baidu}"
```

**Rationale:**
Without this export, the variable does not reach the orchestrator subshell.
The fallback default preserves existing behavior if the loader ever omits
the field.

---

### Edit C — Orchestrator conditional (run_phase5_offline.sh)

**Affected file:** /root/openclaw_phase5/orchestrator/run_phase5_offline.sh

**Current behaviour:**
```
Line 8:  python3 /root/openclaw_phase5/orchestrator/brave_executor.py
Line 9:  python3 /root/openclaw_phase5/orchestrator/baidu_executor.py
Both called unconditionally. set -euo pipefail at top of file.
```

**Proposed behaviour:**
```
Line 8 (replace with):
if [[ ",${OPENCLAW_RETRIEVAL_PROVIDERS:-brave,baidu}," == *",brave,"* ]]; then
  python3 /root/openclaw_phase5/orchestrator/brave_executor.py
else
  # Brave skipped for this client — write empty stub so downstream readers
  # do not abort on missing file
  echo '{"results":[]}' > \
    /root/openclaw_phase5/data/brave_raw_${OPENCLAW_ARTIFACT_NAMESPACE}.json
fi

Line 9: baidu_executor.py remains unconditional (always runs).
```

**Rationale:**
The empty stub approach is the safest path. It means normalize.py, dedup.py,
filter_results.py, and write_run_summary.py (lines 116, 152) all see a valid
(empty) brave_raw file — no downstream code changes required. Zero Brave
results flow through to the retrieval package for the ALJ client.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** MEDIUM

**Risk description:**

Primary risk: regression to china_monitor_001 if the OPENCLAW_RETRIEVAL_PROVIDERS
default is not correctly applied. Mitigation: the default `brave,baidu` is set
at two points — in the loader and in the shell script fallback — so a missing
field at either point preserves existing behavior.

Secondary risk: if any downstream script reads brave_raw.json by hardcoded
path (not namespaced), the stub write to the namespaced path would not satisfy
it. This should be verified during implementation (Claude Code grep for
brave_raw references in normalize.py, dedup.py, filter_results.py,
write_run_summary.py) before deployment.

Third risk: set -euo pipefail in run_phase5_offline.sh means any error in the
conditional block aborts the run. The stub write must succeed — the data
directory and namespace must exist before the stub is written.

**Rollback plan:**

Before any file is modified, Claude Code creates:
- run_phase5_offline.sh.bak_20260522_cp006
- run_light_to_lark.sh.bak_20260522_cp006
- load_client_config.py.bak_20260522_cp006

To roll back: restore the three .bak files. china_monitor_001 returns to
current behavior immediately. ALJ client would be non-operational until
CP-006 is re-applied.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. china_monitor_001 cron run following implementation: Brave results present
   in retrieval_package_china_monitor_001.json (provider count > 0 for Brave).
   No change to run behavior, citation count, or validation result.

2. ALJ manual pilot run: brave_raw_alj_china_auto_001.json exists and contains
   {"results":[]}. retrieval_package_alj_china_auto_001.json contains only
   Baidu results (retrieval_provider == "Baidu" for all entries).

3. No new issues in light_to_lark.log attributable to this change.

4. write_run_summary.py telemetry for china_monitor_001: brave_count unchanged
   from pre-implementation baseline.

**Number of runs required to validate:**
1 china_monitor_001 cron run (next scheduled) + 1 ALJ manual pilot run.

**How to confirm no regression:**
validation_result_china_monitor_001.json shows GREEN PASS on first post-
implementation cron run. Any WARN or FAIL triggers immediate rollback review.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change is confined to client retrieval provider selection — no content,
      no prompt, no validator, no scrubber, no delivery gate
- [x] Rollback path exists and is documented above (three .bak files)
- [x] Change is within Phase D scope (new client configuration capability;
      memo approved direction)

**Note on multi-layer scope:** This packet spans three files across config
loader, shell script, and orchestrator. The template expects single-layer
changes. This exception is justified: the three edits are a single atomic
capability (per-client provider selection) that cannot be split across
separate packets without leaving the system in a broken intermediate state.
Operator is aware of the multi-file nature.

**Forbidden change check:**

- [x] Does NOT alter china_monitor_001 retrieval behavior — default
      OPENCLAW_RETRIEVAL_PROVIDERS=brave,baidu preserves current behavior
- [x] Does NOT alter query logic or freshness parameters for any client
- [x] Does NOT weaken validator strictness
- [x] Does NOT weaken scrubber behavior
- [x] Does NOT bypass or modify the Delivery Gate decision
- [x] Does NOT affect client namespace isolation

**ALJ retrieval behavior change is intentional and client-scoped:**
brave_enabled: false is declared in client_config_alj_china_auto_001.yaml.
This packet implements that declared intent. It does not affect any other
client.

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-05-23 |
| Implementation assigned to | Claude Code / VPS operator |
| Implementation confirmed date | 2026-05-23 |
| Backup confirmed | Yes — load_client_config.py.bak_20260523_cp006 (5,533 bytes); run_light_to_lark.sh.bak_20260523_cp006 (12,437 bytes); run_phase5_offline.sh.bak_20260523_cp006 (2,167 bytes) |

**Pre-implementation check required before Claude Code begins:**
Claude Code must grep for all references to brave_raw.json (un-namespaced
and namespaced) in normalize.py, dedup.py, filter_results.py, and
write_run_summary.py. Confirm all reads use the namespaced path
(brave_raw_{client_id}.json) or tolerate an empty file, before Edit C
is applied.

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Date | Client | Outcome vs. validation criteria |
|-------|------|--------|----------------------------------|
| 1 | | china_monitor_001 | |
| 2 | | alj_china_auto_001 | |

**Overall outcome:** PENDING

---

## APPENDIX — SOURCE APPENDIX FIELD CONFIRMATION

Check 2 (Claude Code, 2026-05-22) confirmed all fields required for the
Complete Chinese Source Appendix are present in the retrieval package.

| Required field | Actual field name | Notes |
|----------------|-------------------|-------|
| title | title | Exact match |
| publisher | publisher | Present; some entries carry domain rather than brand name |
| publication date | timestamp | YYYY-MM-DD; distinct from retrieved_at |
| url | url | Exact match; also at trace.raw_url |
| snippet / blurb | summary | Named summary; contains raw HTML markup — strip before display |
| result_id | result_id | Exact match; stable per result |

Additional fields available for appendix enrichment (not required):
retrieval_provider, region, query_id, provider_rank, filter_reason.

**Action required before first ALJ pilot run:**
The source appendix generation step must strip HTML tags and entities from
the summary field before rendering. Content such as <strong>…</strong> and
&hellip; must be cleaned to plain text in the appendix output.

No retrieval package changes are required. All appendix fields are already
present.

---

*OPENCLAW-D-CP-006 | v1.0 | 2026-05-22 | IMPLEMENTED 2026-05-23 — validation pending*
*Implementation note (2026-05-23): Pre-check confirmed brave_raw.json is non-namespaced in normalize.py and write_run_summary.py; operator decision: write BOTH paths in Edit C stub (brave_raw.json + brave_raw_${NS}.json). Edit A: +10 lines; providers_csv emitted from source_preferences.priority_providers; WS1 emits brave,baidu, WS2 emits baidu; py_compile exit 0. Edit B: +3 lines; read + fallback + export in loader block; bash -n exit 0. Edit C: +5 lines; conditional block with two-path stub; bash -n exit 0. Issue #49 resolved in same session: 6 missing exports added (OPENCLAW_CLIENT_ID, OPENCLAW_BRAIN_CONTEXT, OPENCLAW_DELIVERY_TYPE, OPENCLAW_CREDENTIALS_REF, OPENCLAW_QUERY_TEMPLATE, OPENCLAW_REPORT_TEMPLATE); all 9 loader vars confirmed in subshell smoke test. ARTIFACTNAMESPACE typo: NOT PRESENT in current file — zero grep matches; spec line numbers were stale (Issue #53 exec redirect shifted lines); no edit required. Final line counts: load_client_config.py 131→141, run_light_to_lark.sh 328→340, run_phase5_offline.sh 57→62.*
*Client scope: alj_china_auto_001 only | china_monitor_001 unaffected*
*Drafted by: Claude CoWork | Implementation: Claude Code / VPS operator*
