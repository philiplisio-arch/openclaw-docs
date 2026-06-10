# OPENCLAW — MASTER EXECUTION PLAN — JUNE 2026

---
document_id: OPENCLAW_MASTER_EXECUTION_PLAN_2026-06
version: v1.0
date: 2026-06-10
author: Claude Fable 5 (lead engineer / strategic auditor)
status: DRAFT — presented for operator approval; nothing in this plan is authorized until approved
basis: OPENCLAW_FABLE5_AUDIT_2026-06.md (Stage 1 audit)
governance: Constitution P-01–P-10; per-item approval per P-06/P-07. Lanes — 1: routine doc update; 2: governance/protocol; 3: runtime/code/pipeline.
---

## HOW TO READ THIS PLAN

Every item carries **Lane / size / dependency / approval gate**. Phases are dependency-ordered, not calendar-locked; Phase 2 runs in parallel with Phase 1. Approving this plan approves the *sequence*; each Lane 2/3 item still gets its own go/no-go per the Constitution.

**Bottom line:** two safety decisions and one operator review unblock everything. The rest is sequenced behind them.

---

## PHASE 0 — SAFETY & UNBLOCK (days 1–2; before Sunday 2026-06-14)

| # | Item | Lane | Size | Depends on | Approval |
|---|---|---|---|---|---|
| 0.1 | **ALJ exposure decision**: re-enable `pilot_mode: true` in `client_config_alj_china_auto_001.yaml` **or** remove the Sunday cron line. Recommendation: re-enable `pilot_mode` (keeps the cron exercising the pipeline, output held, matches ADV-017). | 3 | 15 min | — | **Operator decision required before 2026-06-14** |
| 0.2 | **Diagnose June 10 block — report only.** Inspect live VPS artifacts, attempt reproduction, identify why agent output lost a required section and all ET citations. No fix without separate approval (P-10). | 3 (diagnose) | 1–2 h | — | Authorize diagnosis |
| 0.3 | **D13–D15 five-layer review** by operator, with a CoWork review packet prepared to cut review time. Recording the outcome in the gate checklist is Lane 1. | 1 (record) | 1–2 h operator | packet prep (30 min) | Operator schedules; outcome recorded after |

## PHASE 1 — GATE CLOSURE (~2–3 weeks calendar)

| # | Item | Lane | Size | Depends on | Approval |
|---|---|---|---|---|---|
| 1.1 | Resume streak count; daily five-layer reviews with CoWork packets per delivery | 1 | ~20 min/day operator | 0.3 | Standing, per ADV-017 |
| 1.2 | ADV-015 **Option B (snippet alignment) spec** — spec only, no build | 2 | 1 day | — | Spec review |
| 1.3 | **Archive raw pre-gate agent output** (extends ADV-016; additive, gated on same env var) | 3 | ~2 h | 0.2 findings | Per-item |
| 1.4 | **Blocked-run notification** (alert on any `[FAIL]`/block instead of silent log) | 3 | ~2 h | — | Per-item |
| 1.5 | **CP-021 timing decision.** It restarts the streak on first live delivery (approved 2026-05-28, pre-dates ADV-017 hold). **Recommendation: defer until gate closes.** | 2 | decision only | 0.3 | **Operator decision** |

## PHASE 2 — STABILITY & HYGIENE (parallel with Phase 1; low risk)

| # | Item | Lane | Size | Depends on | Approval |
|---|---|---|---|---|---|
| 2.1 | **Runtime under git** — init repo over runtime tree, initial commit, no behavior change | 3 | 1 h | — | Per-item |
| 2.2 | **Doc reconciliation pass**: Master Doc Index, Document Versions Index, Issue #47 closure, Board Dashboard refresh, Execution Plan v2 supersession statement, CP status stamps | 1 | 1 session | — | Batch approval (P-07) |
| 2.3 | `.bak` / legacy non-namespaced files / orphaned-script cleanup (inventory presented before any deletion) | 1/3 | 1 h | 2.1 (git first) | Per-item |
| 2.4 | Issue #56 root-cause (orchestrator exit=1), timeboxed | 3 | 2 h cap | 0.2 | Per-item |

## PHASE 3 — PILOT OPERATIONS (after gate progress)

| # | Item | Lane | Size | Depends on | Approval |
|---|---|---|---|---|---|
| 3.1 | CP-022A query-family **dry run in held mode** (diagnostic only) | 3 | 1 session | 1.1 underway | Per-item |
| 3.2 | CP-022 WS1 query-family expansion | 3 | per packet | gate closed, 3.1 | Per packet |
| 3.3 | ALJ resumes **per ADV-017 only** — after WS1 trust repair proven; includes the deferred controlled delivery test (operator present) | 3 | per ADV-017 | gate closed, 0.1 | **Operator authorization** |

## PHASE 4 — BRAIN MEDIUM GROUNDWORK (spec only, no build)

| # | Item | Lane | Size | Depends on | Approval |
|---|---|---|---|---|---|
| 4.1 | **Corpus schema + provenance-tier spec**, explicitly designed to seed from the ADV-016 traceability archive | 2 | 2–3 sessions | — (can start anytime) | Spec review |
| 4.2 | Pull-query interaction spec | 2 | deferred | 4.1 approved | Deferred |

## DROP / MERGE RECOMMENDATIONS

- **Fold CP-024 into CP-021's implementation session** — same files, one streak restart instead of two.
- **Hold CP-023 (ALJ query expansion)** until the WS1 gate closes, per ADV-017's 70/20/10 allocation.
- **Browser retrieval stays narrowed** to claim verification; no expansion proposed.

---

## APPROVALS REQUESTED

1. **Before Sunday 2026-06-14 (time-critical):** Item 0.1 — ALJ exposure. Recommended: set `pilot_mode: true`.
2. Item 0.2 — authorize diagnose-only investigation of the June 10 block.
3. Item 0.3 — schedule the D13–D15 review (I will prepare the CoWork packet on approval).
4. Item 1.5 — CP-021 deferral until gate closure (recommendation: defer).
5. This plan's overall sequence (Phases 0–4), with per-item Lane 2/3 approvals to follow individually.

Nothing executes until the corresponding approval above is given. This document and the audit are presented uncommitted; committing them to the docs repo is itself a Lane 1 action awaiting approval.

---

*End of plan. Stage 3 (lane-governed execution) begins only on operator approval of specific items above.*
