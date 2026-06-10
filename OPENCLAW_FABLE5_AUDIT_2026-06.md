# OPENCLAW — FULL PROJECT AUDIT — JUNE 2026

---
document_id: OPENCLAW_FABLE5_AUDIT_2026-06
version: v1.0
date: 2026-06-10
author: Claude Fable 5 (lead engineer / strategic auditor)
status: DRAFT — presented for operator review; not yet approved or committed
scope: Stage 1 of the commissioned three-stage engagement (AUDIT → MASTER PLAN → APPROVED EXECUTION)
companion: OPENCLAW_MASTER_EXECUTION_PLAN_2026-06.md
---

## EXECUTIVE SUMMARY (one page)

**Bottom line.** The trust machinery works — the morning of June 10 proved it, when the gates correctly blocked a defective run before anything reached the client. But the project is paused at the worst possible spot: the Phase D gate streak has been held at 3/10 for four days because the D13–D15 five-layer review hasn't happened, and meanwhile two new problems have appeared that no status document records. One of them can cause an unsupervised external delivery in four days.

**Risk level: ELEVATED — CONTAINED.** Nothing defective has reached a client. All containment is working as designed. But two time-sensitive exposures exist, and the thing blocking forward progress is operator review bandwidth, not engineering.

**The three urgent items (none of these is in any status document yet):**

1. **ALJ can deliver externally, unsupervised, on Sunday 2026-06-14.** The ALJ client config has `pilot_mode: false` (delivery ENABLED) while its own inline comment says output is held for review, and a crontab entry fires ALJ every Sunday. ADV-017 (operator-approved 2026-06-06) put ALJ in review-only/manual mode. These contradict each other; the runtime wins, so ALJ will push to the live Feishu doc on Sunday with no review. *Client impact: an unreviewed brief reaches a real external document. System risk: violates the ADV-017 allocation decision.*
2. **The June 10 run was blocked and nobody knows why yet.** Retrieval was healthy — 25 valid sources reached the agent, the best volume since the collapse — but the agent's output failed the completeness gate (missing required section; EXECUTIVE TAKE had zero cited bullets after uncited removal). The gates worked exactly as designed: P-01/P-02 honored, nothing sent. But the root cause is unknown, and the raw pre-gate agent output is not archived, so this failure class is currently invisible after the fact. Per P-10: diagnose before adjusting anything.
3. **The gate streak is held only by a review that hasn't happened.** D13–D15 await operator review under the ADV-017 five-layer standard. This is 1–2 hours of operator time and zero engineering. Until it happens, no delivery counts and the late-June paid-pilot target slips day by day.

**Recommended next action.** Approve Phase 0 of the companion Master Execution Plan: (a) decide the ALJ exposure before Sunday (re-enable `pilot_mode` or remove the cron line — 15 minutes), (b) authorize a diagnose-only investigation of the June 10 block, and (c) schedule the D13–D15 review.

**Approval needed: YES** — on the two safety decisions and the review scheduling above. This audit document itself changes nothing and requires only acknowledgment.

---

## A. VISION-TO-EXECUTION GAP

The end vision (Strategic Vision Memo 2026-05-15, Strategic Recap Memo 2026-05-18, ADV-002) is a trusted PR intelligence platform functioning as an "AE exoskeleton": scheduled push briefs plus on-demand pull briefs in the same trusted format, backed by accumulated intelligence (Brain Lite → Brain Medium → Brain Full; corpus + entity layers with provenance tiering).

Position against the five-layer model:

| Layer | Vision role | Current state |
|---|---|---|
| L1 Monitoring (push briefs) | Foundation revenue product | **Operational, in trust-repair.** WS1 daily cron delivering; gate streak 3/10 HELD. ALJ weekly in pilot/hold (but see urgent item 1). |
| L2 Content Intelligence | Brief quality engine | **Active.** Change packets CP-001–CP-025, content scorecard, feedback register, ADV-017 five-layer standard all live. |
| L3 Document Intelligence | The named bridge to everything beyond monitoring | **Not started — and no spec exists.** This is the largest unfunded gap between here and the vision. |
| L4 Memory (Brain) | Compounding asset / moat | **Brain Lite only** (injection live since 2026-05-16). Brain Medium corpus schema unspecified. |
| L5 Query / pull-mode | "Same trusted brief, on demand" | **Not started.** |

Three observations that change the picture:

1. **The ADV-016 traceability archive is unintentionally a proto-corpus.** Every run now archives raw retrieval, filter decisions, the filtered package, and final output with full provenance — exactly the substrate Brain Medium's corpus needs. The vision memo (§4) argues corpus schema and provenance tiering must be specified *before* seeding to avoid coupling problems. That spec is now the cheapest high-leverage Lane 2 work available.
2. **Pull-mode is architecturally closer than it looks.** `run_light_to_lark.sh --client_id X` is already an on-demand, parametrized trigger — the ALJ manual runs prove the path. What's missing is query parametrization and the corpus, not new plumbing.
3. **The binding constraint on the "paid pilot gate late June" target is operator review bandwidth, not engineering.** Every remaining gate item is an operator review or decision. CoWork review packets are the designed mechanism to reduce per-delivery review cost; the 2026-06-08 review request has had no report returned.

## B. PHASE D GATE PATH — FASTEST CREDIBLE PATH TO 10/10

The goal is ten consecutive clean external deliveries under the five-layer standard (system ran; citations structurally valid; source quality acceptable; claims supported by cited sources; output useful to client). Current streak: **3/10, HELD since 2026-06-06** (gate checklist v1.6).

Ordered path:

1. **D13–D15 operator review** (1–2h with a CoWork packet prepared for it). The only thing holding the streak. Zero engineering. Everything else waits behind this.
2. **Diagnose the June 10 block** before any other runtime work (P-10). Evidence in Appendix C. The failure is on the agent-output side, not retrieval — retrieval delivered its best pool since the collapse.
3. **Resolve CP-021 sequencing.** CP-021 (source-first output restructuring, operator-approved 2026-05-28) explicitly **restarts the streak on first live delivery** — a decision that pre-dates the ADV-017 hold. Recommendation put to the operator: defer CP-021 until the gate closes. Restarting a held streak with a format overhaul mid-trust-repair maximizes time-to-revenue delay.
4. **Keep the streak protected while it runs:** ADV-015 Option D spot-checks on each counted delivery; draft the Option B (snippet alignment) spec in parallel; ADV-014 Layers 1+2 already live (Layer 2 promoted to drop mode 2026-06-09 after a 0-flag confirmation run).
5. **Known streak threats**, in rough priority: misbinding recurrence (Issue #66 — the severity-4 risk; OPEN, high severity); Baidu pool quality producing thin briefs (CP-022 territory); topic repetition (CP-007/CP-018 mechanisms working); duplicate-content blocks (neutral — they don't break the streak, they just don't count); the new undiagnosed June 10 failure class.

## C. CONSISTENCY & HYGIENE FINDINGS

None of these block delivery; together they erode the "single source of truth" guarantee. Full inventory in Appendix B.

- **Master Document Index v5.4 is materially stale:** ~16 files on disk are unindexed; CP-010/011/012 are listed but the files are absent; it cites CoWork protocol v2.9 while the file on disk is v3.0. Document Versions Index v1.3 has the same staleness.
- **Phase 7 Execution Plan exists in two versions** (v1 canonical per Daily Status; v2 also on disk) with no supersession statement.
- **Board Dashboard is stale** (June 4 baseline, streak "1/10") while the CEO Dashboard (June 6) is correct. The ADV-017 §6 dashboard redesign packet was never drafted.
- **Change-packet files carry stale statuses** (e.g., CP-020's file says "pending" while Daily Status records deployed + accepted). Convention: Daily Status governs; packet files need closing status stamps.
- **Issue #47 is fixed in runtime but still OPEN in the Issues Log.** The 2026-06-09 namespacing patch resolved all 7 intermediate artifacts; the log was never updated, and legacy non-namespaced files still sit in `data/`.
- **CoWork review request (2026-06-08) has no returned report.**
- **The runtime code is under no version control at all.** ~40 `.bak` files are the only history. The docs repo is clean on main; the runtime that actually delivers to clients has nothing.

## D. ARCHITECTURE REVIEW

**The trust guarantees themselves are well-layered, deterministic, and should be preserved as-is.** The validator → scrubber → completeness-gate → delivery-block chain has now correctly blocked every defective run, including June 10.

The fragility is around the spine, not in the guarantees:

- The pipeline spine is a ~480-line bash script (`run_light_to_lark.sh`). It works, but: the config loader is a single point of failure with no fallback; the 540-second agent timeout and the Docker container name are hardcoded; completeness checks are regex heuristics; intermediates from a previous run can go stale between runs; heredoc patterns are SIGPIPE-prone; the orchestrator's exit=1 on ALJ runs (Issue #56) has never been explained; there are no tests.
- **There is no alerting.** Blocked runs are discovered by reading logs. June 10's block was found by this audit, not by any notification.
- **The raw pre-gate agent output is not archived** (ADV-016 archives post-gate artifacts), so agent-side failures like June 10 cannot be diagnosed after the fact.
- Simplifications that preserve the guarantees: put the runtime under git (kills the `.bak` sprawl); notify on blocked runs; archive raw agent output; delete legacy un-namespaced files; prune orphaned scripts.
- **Scale readiness:** the namespacing work (Issue #47 fix) holds for 2–5 clients. Per-client cron entries and env-threading need rework beyond that — correctly deferred for now.

## E. RISK REGISTER

| # | Risk | Likelihood / Impact | Mitigation (see Master Plan) |
|---|---|---|---|
| 1 | ALJ unsupervised Sunday delivery (2026-06-14) | HIGH if unaddressed / HIGH | Operator decision: re-enable `pilot_mode` or remove cron line (Phase 0) |
| 2 | Misbinding recurrence in a counted delivery (Issue #66) | MED / HIGH | ADV-015 Option D spot-checks + Option B spec (Phase 1) |
| 3 | Operator review bandwidth is the true critical path | HIGH / MED | CoWork packets to cut per-delivery review cost (Phase 0–1) |
| 4 | Undiagnosed failure class (June 10 block; cf. Issue #56) | MED / MED | Diagnose-first; raw agent-output archiving; blocked-run alerting (Phase 0–1) |
| 5 | Baidu pool quality → thin briefs | MED / MED | CP-022A diagnostic dry run (Phase 3) |
| 6 | No runtime version control; single VPS | LOW / HIGH | Runtime under git + backup (Phase 2) |
| 7 | Corpus schema unspecified before Brain Medium seeding | MED (long-range) | Lane 2 spec only, no build (Phase 4) |

---

## APPENDIX A — SPEC DRIFT TABLE

| Document says | Reality on disk / runtime | Severity |
|---|---|---|
| ALJ config comment: "All output held for operator review — no external delivery" | Same line sets `pilot_mode: false` (delivery ENABLED); Sunday cron `0 13 * * 0` live | **HIGH** |
| ADV-017: ALJ review-only/manual mode | ALJ on automated weekly cron with delivery enabled | **HIGH** |
| Issues Log: Issue #47 OPEN | All 7 intermediates namespaced 2026-06-09; runtime resolved | MED |
| Master Doc Index v5.4: CP-010/011/012 listed; CoWork protocol v2.9 | Files absent; protocol file is v3.0; ~16 disk files unindexed | MED |
| Daily Status: Phase 7 Execution Plan v1 CANONICAL | v2 also on disk, no supersession statement | MED |
| Board Dashboard: streak "1/10" (June 4) | Gate checklist: 3/10 HELD (June 6) | MED |
| CP-020 packet file: "pending" | Daily Status: deployed + accepted | LOW |
| `package_builder.py` status fields: `trigger_type: "manual_test"`, `workflow: ..._test` | Hardcoded on every run incl. production cron — not trustworthy metadata | LOW |

## APPENDIX B — HYGIENE INVENTORY

- ~16 files on disk unindexed in Master Document Index v5.4; Document Versions Index v1.3 equally stale.
- ~40 `.bak` files across runtime and docs (`/root/*.bak_*`, `config/*.bak*`, `specs/*.bak_*`) serving as the only change history.
- Legacy non-namespaced intermediates still present in `openclaw_phase5/data/` after the Issue #47 fix.
- Orphaned scripts from superseded pipeline stages (inventory before deletion; Phase 2 task).
- CoWork review request 2026-06-08 outstanding, no report.
- Untracked files in docs repo: 4 `.bak` config/spec copies (see `git status`).

## APPENDIX C — LIVE-STATE EVIDENCE (June 9–10 runs)

**June 9 (run_20260608T223001Z) — DELIVERED CLEAN.**
- Validator GREEN: 10 claims / 10 citations / 10 sources matched / 0 warnings / 0 failures.
- mapping_size=8 (up from the collapse floor; still below the 14–15 norm).
- Validates the 2026-06-08 Baidu freshness-window fix; remaining volume gap is retrieval-side pool quality (CP-022 territory), not filtering.
- Not yet recorded in Daily Status (last updated 2026-06-08); does not count toward the streak while the gate is HELD.

**June 10 (run_20260609T223001Z) — BLOCKED, undiagnosed.**
- Retrieval healthy: 159 filter decisions, **25 sources passed to agent** — best volume since the collapse.
- Agent output failed the completeness gate: `[FAIL] Phase 5 run blocked: missing required section (RE_2)` and `EXECUTIVE TAKE has zero cited bullets after uncited removal; delivery blocked` (light_to_lark.log, 22:32:35Z).
- Delivery correctly blocked; archived final output is the 194-byte block notice; **no validation_result archived** (run never reached the validator).
- Raw pre-gate agent output not archived anywhere — root-cause diagnosis requires the live VPS artifacts and/or reproducing the run. Diagnose-first per P-10; no adjustment proposed in this audit.

---

*End of audit. Companion document: OPENCLAW_MASTER_EXECUTION_PLAN_2026-06.md. No existing document has been modified; nothing has been committed.*
