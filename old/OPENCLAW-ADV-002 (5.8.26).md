---
document_id: OPENCLAW-ADV-002
date: 2026-05-08
revised: 2026-05-08
to: OpenClaw Project Operator
from: Claude CoWork
re: Project Status & Phase 7 Execution Roadmap
status: OPERATOR-APPROVED ADVISORY ROADMAP — no runtime pipeline changes
        authorized by this approval
---

# OPENCLAW — Advisory Memorandum
## Project Status & Phase 7 Execution Roadmap

---

## Executive Summary

OpenClaw has completed the full Phase 6 Soft Layer (6.1–6.8) as of May 7,
2026. The pipeline is operational, deterministic, and delivering cited
intelligence to Lark on a daily automated schedule. Known Phase 6
citation-control issues appear resolved based on the latest validated runs.
Observed agent citation fabrication in delivered output has been reduced to
0% across the latest validated run set.

This memo sets out where the project stands, what has been built, and a
simplified sequential roadmap through Phase 7 to first controlled paid pilot
and beyond. The roadmap is linearised for a solo operator. Each step is
completed before the next begins.

**Path to first controlled paid pilot: approximately 2–3 months from today.**
**Full platform: approximately 8–10 months out.**

---

## Current System Status

| Field              | Value                                                    |
|--------------------|----------------------------------------------------------|
| Date               | May 8, 2026                                              |
| Phase              | Phase 6 Soft Layer complete — Phase 7 entry pending      |
| Last cron run      | 2026-05-08 06:32 Shanghai — clean delivery confirmed     |
| Validator          | GREEN PASS — 23/23 citations matched                     |
| Fabrication rate   | 0% observed across latest validated run set              |
| Open issues        | Known Phase 6 citation-control issues appear resolved    |
| Providers          | Brave + Baidu — both operational                         |
| Delivery           | substitutions_made=23, missing_ids=0, HTTP 200           |

The 2026-05-08 delivery included 3 Executive Take bullets and 5 Advisory
Layer bullets across 6 distinct publishers, including multiple Sina Finance
and finance.sina.cn entries. Chinese-language sources are now surfacing in
delivery, but authority calibration and source diversity remain Phase 7
editorial-quality workstreams.

---

## What Phase 6 Built

Phase 6 transformed OpenClaw from a prototype with unreliable output into
a citation-enforced, validator-gated, deterministic intelligence pipeline.
The following are now in production:

- **Locked citation architecture** — agent cites source numbers; resolver
  maps to verified result_ids; scrubber removes any invalid IDs before
  delivery.
- **Uncited claim removal** — any bullet without a verified citation is
  removed before delivery; delivery blocked if Executive Take runs empty.
- **Citation substitution** — result_id tokens replaced with human-readable
  publisher/date strings in delivered output; result_ids retained in logs
  for full traceability.
- **Conflict detection** — three-tier classification (factual / directional
  / numeric) extracted per run, logged, and injected into delivery when
  present.
- **Dual-provider retrieval** — Brave and Baidu both operational;
  Chinese-language sources present in delivery.
- **Validator enforcement** — every citation traced to a verified source
  before the delivery gate opens.

These capabilities are the foundation Phase 7 builds on. They should not
be redesigned absent a specific failure, but they remain subject to
regression monitoring.

---

## Execution Roadmap — Sequential Steps

Steps in order. No step begins until the previous one is confirmed complete
and operator-approved.

---

### STEP 1 — Close Phase A Gate
**Timing:** Passive — 2 days

Monitor cron runs on 2026-05-09 and 2026-05-10. Three clean runs confirmed
so far. Two more close the five-consecutive-run client-facing trust gate
required before any pilot client engagement begins.

---

### STEP 2A — VPS Documentation Repository Setup
**Timing:** 1 session

Create the canonical documentation directories on the VPS:
/root/openclaw_docs/ for system documents and /root/openclaw_cowork/ for
CoWork working files. Initialise a Git repository with a proper .gitignore
confirming no secrets, credentials, API keys, or runtime scripts are
included. Migrate all current system documents. Make a baseline commit
before any CoWork edits begin.

**Rollback requirement:** The baseline commit must be verifiable and
restorable before CoWork starts editing any system document on the VPS.
If the baseline state cannot be restored from Git, CoWork does not proceed
to Step 2B.

---

### STEP 2B — CoWork Access and Permission Boundary
**Timing:** 1 session (follows 2A confirmation)

Configure CoWork access limited strictly to:
- READ: /root/openclaw_docs/, /root/openclaw_logs/,
  /root/openclaw_phase5/data/, /root/openclaw_phase6/validation/
- WRITE: /root/openclaw_cowork/ only

CoWork must not receive write access to runtime scripts, cron configuration,
secrets, or any production pipeline file. This boundary is enforced
structurally by filesystem permissions — not by behavioral instruction.
Operator confirms the permission model before CoWork VPS access is enabled.

---

### STEP 3 — Client Config Schema
**Timing:** 1 session

Draft and approve client_config.yaml. The full field set is already defined
in the Phase 7 plan. This also addresses editorial quality items — topic
focus, report template, and region scoping are all config fields.

---

### STEP 4 — CoWork Daily Report Format
**Timing:** 1 session

Approve the 11-field daily post-run report template. Once VPS access is
configured this replaces the manual per-session analysis with an automated
daily artifact written to /root/openclaw_cowork/reports/.

---

### STEP 5 — Multi-Client Test Harness Design
**Timing:** 1 session

Specify how a synthetic second client runs through the pipeline without
touching the live client's artifact namespace. Design document only — no
implementation at this step.

> ✓ Steps 1–5 complete: Phase B closed. Infrastructure ready.
> No pipeline changes made.

---

### STEP 6 — Brain Lite Implementation
**Timing:** 2–3 weeks

Build the run summary store (14-field JSON per delivery) and seven-day
digest injection into the agent input, token-budgeted at 1,200 tokens.
Confirm non-disruptive across five consecutive runs before advancing.

---

### STEP 7 — Client Configuration Implementation
**Timing:** 1–2 weeks

Implement the config loader. Namespace all artifacts by client ID. Run a
synthetic second client end-to-end. Confirm zero cross-client contamination
across all artifact types before advancing.

> ✓ Steps 6–7 complete: Phase C closed. System ready for first external
> client.

---

### STEP 8 — Controlled Pilot — First Paid Client
**Timing:** 4–6 weeks

One real client. China-focused monitoring brief. Operator review gate on
every delivery for the first two weeks or ten deliveries. Ten consecutive
clean external deliveries with client confirmation = first revenue.

> ★ Step 8 complete: FIRST CONTROLLED PAID PILOT. Target: ~Month 3.

---

### STEP 9 — Document Intelligence Lab
**Timing:** 3–4 months (after Step 8 stable)

Internal development track only. Document ingestion, passage-level citation
enforcement, document scrubber and validator. Not client-facing until ten
consecutive zero-uncited-claim internal test reports are confirmed.

---

### STEP 10 — Full Platform
**Timing:** Month 8–10

Brain Full activation. Multi-client scaling. Document intelligence
client-facing. Operator dashboard across all active clients. Commercial
launch of OpenClaw as a multi-client business intelligence platform.

> ★ Step 10 complete: FULL PLATFORM OPERATIONAL. Target: ~Month 8–10.

---

## Content Quality — Editorial Improvements Ahead

Phase 6 focused on citation integrity. The next editorial layer begins at
Step 3 and matures through Steps 6–7:

- **Freshness signalling** — distinguish 24-hour precision material from
  7-day recall context. Addressable via report template at Step 3.
- **Source authority calibration** — classify sources by tier (official /
  financial press / platform contributor) and frame claims accordingly.
  Addressable via client config and scoring in Steps 6–7.
- **Chinese-source diversity** — expand coverage across official, state
  media, financial press, and sector-specific outlets. Steps 6–7.
- **Advisory language tone** — match claim strength to evidence. Remove
  'must immediately' / 'unprecedented' framing unless directly supported.
  Agent prompt at Step 6.
- **Middle East anchoring** — coverage should connect to China exposure or
  China-linked conditions. Topic focus config at Step 3.

---

## Key Risks

| Risk                                            | Mitigation                                                             | Level  |
|-------------------------------------------------|------------------------------------------------------------------------|--------|
| Brain Lite scope creep extends Phase C          | Field set locked at 14 fields. Any addition requires formal decision.  | Medium |
| Multi-client artifact isolation failure         | Zero cross-contamination is a Phase C exit criterion.                  | High   |
| Secrets exposed during VPS co-location          | VPS Phase B gated on secrets isolation and structural permissions.     | Medium |
| Rollback not verifiable before Step 2B begins   | Baseline Git commit confirmed restorable before CoWork edits enabled.  | Medium |
| Operator review gate erodes under time pressure | Gate is a protocol requirement. Lifting it requires formal decision.   | Medium |
| Document intelligence quality below standard   | Phase E requires 10 consecutive zero-uncited-claim internal reports.   | Medium |

---

## Governing Rules — Unchanged Across All Phases

- The pipeline is deterministic. CoWork is not placed inside the live
  delivery pipeline under any circumstances.
- Only one production layer may be modified at a time.
- No client onboarding before the Phase A five-consecutive-run gate is
  confirmed.
- Client namespace isolation is a non-negotiable exit criterion for all
  multi-client phases.
- Document intelligence is not client-facing until the ten-run exit
  criterion is met.
- No document update takes effect without explicit operator approval.

---

## Accepted Direction (Operator-Confirmed)

Phase A gate closure → controlled VPS doc/repo setup (Steps 2A/2B) →
CoWork reporting layer → Brain Lite → client configuration and namespace
isolation → controlled paid pilot.

No runtime pipeline change is authorized by this approval.

---

## Immediate Actions

| # | Action                                                                                   |
|---|------------------------------------------------------------------------------------------|
| 1 | Monitor 2026-05-09 and 2026-05-10 cron runs. Share logs to close Phase A gate.          |
| 2 | Run find command on VPS to verify scrubber_report.json path (T-06).                      |
| 3 | Confirm: proceed to Step 2A (VPS documentation repository setup).                        |
| 4 | Update Operating Protocol phase lock once phase direction confirmed.                     |

---

*This memo reflects operator-approved advisory direction as of May 8, 2026.
No system changes, pipeline modifications, or phase advancements take effect
without explicit operator approval at each step.*

*OPENCLAW-ADV-002 (revised) | Claude CoWork | May 8, 2026*
