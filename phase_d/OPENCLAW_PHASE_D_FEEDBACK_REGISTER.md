---
document_id: OPENCLAW-PHASE-D-FEEDBACK-001
version: 1.4
created: 2026-05-20
last_updated: 2026-05-22
status: ACTIVE
classification: OPERATIONAL — PHASE D FEEDBACK REGISTER
---

# OPENCLAW — Phase D Feedback Register

## PURPOSE

Central repository for operator and client feedback on delivered output
during Phase D controlled pilot. Every feedback item must be logged here
before action is taken. Entries are cumulative and append-only.

The operator review workflow — including the standard delivery review prompt,
CoWork output format, and change packet threshold — is defined in:
`OPENCLAW_PHASE_D_OPERATOR_REVIEW_PROCEDURE.md`

---

## FEEDBACK ID FORMAT

Feedback items are assigned sequential IDs in the format `D-FB-NNN` (e.g.,
D-FB-001, D-FB-002). IDs are assigned in order of logging and never reused.

---

## FEEDBACK CLASSIFICATION

| Code | Category |
|------|----------|
| A | Delivery-blocking |
| B | Editorial / prompt improvement |
| C | Source-quality / authority |
| D | Format / user experience |
| E | Client preference |

## SEVERITY SCALE

| Level | Meaning |
|-------|---------|
| 1 | Minor — noticeable but does not materially affect usefulness |
| 2 | Moderate — affects quality; change packet warranted after recurrence |
| 3 | Material — meaningfully degrades client-grade output |
| 4 | Delivery-blocking — must be resolved before next delivery |

## BATCHING RULE

One-off feedback should not generate a Content Change Packet unless the
operator explicitly marks it delivery-blocking (Severity 4). Non-blocking
feedback (Severity 1–3) should be batched after recurring pattern
confirmation across 3–5 reviewed deliveries.

## STATUS VALUES

New → Accepted / Rejected → Batched → Implemented → Validated / Reopened → Closed / Deferred

---

## REGISTER

| Feedback ID | Date | Run ID | Client ID | Section | Severity | Comment | Example from output | Why it matters | Classification | Proposed fix type | Client confirmed? | Disposition rationale | Status | Validation rule | Owner | Notes |
|------------|------|--------|-----------|---------|----------|---------|---------------------|----------------|----------------|-------------------|-------------------|-----------------------|--------|-----------------|-------|-------|
| D-FB-001 | 2026-05-21 | run_20260520T223002Z | china_monitor_001 | Full output | 3 | Thin retrieval package — mapping_size=7 (vs norm 14–15); 12 source numbers out of range; 4 citation groups unsupported; 4 bullets removed by scrubber | Delivered 2 ET + 2 AL bullets; expected 3 ET + 5 AL | Phase D Delivery 1 arrived materially shorter than standard; client received degraded brief on first pilot delivery | A | Diagnostic — read retrieval_package_china_monitor_001.json; investigate package assembly from raw results | Pending | Material quality event on first Phase D delivery; investigation required before pattern assessment | Monitoring — did not recur Delivery 2 or 3 | mapping_size ≥ 12; source_numbers_dropped = 0 | Operator | Did not recur on 2026-05-22 Delivery 2 (full 8-bullet brief, 25/25 citations) or 2026-05-23 Delivery 3 (19/19 citations). Two consecutive clean runs — candidate for closure pending operator decision. |
| D-FB-002 | 2026-05-22 | run_20260521T223002Z | china_monitor_001 | Logging | 2 | light_to_lark.log gap — 2026-05-22 run absent from log; pipeline completion confirmed by artifacts only | Log has 1525 lines ending with 2026-05-21 run; no 2026-05-22 entries present | Post-run analysis depends on log for resolver and scrubber metrics; gap creates partial observability loss | A | VPS investigation — check /root/openclaw_logs/ for rotated log file; update scp sync if rotation confirmed | Confirmed — not reproduced | Snapshot timing artefact — scp pulled mid-run; run present at lines 1526–1559; no log rotation | Closed | Run confirmed in log via Claude Code VPS audit | Operator | Issue #51 RESOLVED. Mitigation: run scp after 06:35 to avoid mid-run pull. No logrotate configured — file grows indefinitely; setup recommended. |
| D-FB-003 | 2026-05-23 | run_20260522T223001Z | china_monitor_001 | Full output | 3 | Topic repetition across all three Phase D deliveries — same three story clusters (US-China summit, EU-China trade, Middle East/global macro) across 2026-05-21, 2026-05-22, 2026-05-23 | run_summary topics_covered character-for-character identical across D2 and D3; D1 also same clusters | A daily brief repeating identical topics provides no incremental intelligence; core product value proposition fails | B | CP-007 — add TOPIC DIFFERENTIATION RULE to system_rules in build_agent_input_slim.py; rebuild Brain Lite digest as prerequisite. Root cause also has retrieval-side component (D-FB-004). | No | Recurrence confirmed across 3 deliveries (run_summary topics_covered); threshold met | Accepted — Batched (CP-007) | topics_covered in run_summary shows at least one cluster distinct from prior run's topics_covered across 2 consecutive runs | CoWork | Root cause is dual: (1) retrieval queries surface same dominant story clusters; (2) no agent instruction to seek differentiation. CP-007 addresses agent-side. D-FB-004 Part B addresses retrieval-side. Brain Lite digest must be rebuilt before CP-007 validates. |
| D-FB-004 | 2026-05-23 | run_20260522T223001Z | china_monitor_001 | Full output | 3 | Old articles — content in delivered brief sourced from articles published before 2026-05-22; today's brief should contain nothing older than the prior business day | Operator confirmed articles older than 48 hours present in Delivery 3 evidence pool | A daily intelligence brief presenting week-old developments as current intelligence fails its freshness promise and undermines client trust | C | Split implementation: Part A (in scope) — CP-007 adds FRESHNESS RULE to system_rules (agent preference for recent sources, language calibration when using older material). Part B (out of scope for CoWork) — operator + Claude Code retrieval investigation: inspect retrieval_package publication dates; tighten Baidu freshness filter if old articles confirmed in package. | No | Operator-confirmed on Delivery 3 | Accepted — Part A batched (CP-007); Part B parallel track (operator/Claude Code) | Part A: no Executive Take bullet frames a development >72 hours old as breaking news (operator spot-check against retrieval_package timestamps). Part B: retrieval_package timestamp audit shows no sources >48 hours in package. | Operator / CoWork | Root cause has two layers. Agent instruction (Part A) is a mitigation when retrieval returns older material. Retrieval filter tightening (Part B) is the structural fix. Both are needed. Part B requires VPS SSH access and retrieval layer inspection — out of CoWork implementation scope. |
| D-FB-005 | 2026-05-23 | run_20260522T223001Z | china_monitor_001 | Full output | 3 | No source URLs provided to reader — delivered brief attributes claims to publisher/date but provides no links; client cannot verify any claim | All three Phase D deliveries (D1, D2, D3) contain zero URLs; reader has no path to primary sources | Source accessibility is a foundational requirement of a trusted intelligence product; without URLs the brief cannot be independently verified | D | CP-008 — append SOURCES section (publisher, date, URL per cited result_id) to citation_sub.py output; all required fields confirmed present in retrieval_package (CP-006 Appendix, 2026-05-22 audit) | No | Absent across all three Phase D deliveries; three-delivery pattern confirmed | Accepted — Batched (CP-008) | SOURCES section present in delivered Lark output; all entries contain publisher + date + URL; operator URL spot-check confirms links resolve; validator result unchanged | CoWork | All retrieval_package fields required for implementation already confirmed (title, publisher, timestamp, url, result_id). HTML stripping required on title field (per CP-006 Appendix). try/except wrapper required to ensure SOURCES logic is never delivery-blocking. |

---

## OPEN ITEM COUNTS

| Category | New | Accepted | Batched | Implemented | Validated | Deferred | Total Open |
|----------|-----|----------|---------|-------------|-----------|----------|------------|
| A — Delivery-blocking | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| B — Editorial / prompt | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| C — Source-quality | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| D — Format / UX | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| E — Client preference | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **1** | **1** | **2** | **0** | **0** | **1** | **4** |

---

*OPENCLAW-PHASE-D-FEEDBACK-001 | Version 1.5 | Created: 2026-05-20 | Status: ACTIVE*

*v1.5 changes (2026-05-23): D-FB-001 updated — did not recur Delivery 3; two consecutive clean runs; candidate for closure. D-FB-003 added — topic repetition across all three Phase D deliveries; Category B Severity 3; batched to CP-007. D-FB-004 added — old articles / freshness; Category C Severity 3; Part A batched to CP-007; Part B parallel retrieval investigation track. D-FB-005 added — no source URLs; Category D Severity 3; batched to CP-008. Open item counts updated.*

*v1.4 changes (2026-05-22): D-FB-001 status updated — did not recur Delivery 2; moved to Monitoring. D-FB-002 added — light_to_lark.log gap (2026-05-22); Category A Severity 2; Issue #51 logged. Open item counts updated.*

*v1.3 changes (2026-05-21): D-FB-001 added — Phase D Delivery 1 (2026-05-21); thin retrieval package; mapping_size=7; 4 bullets removed; Category A Severity 3. Open item counts updated.*

*v1.2 changes (2026-05-20): Cross-reference to OPENCLAW_PHASE_D_OPERATOR_REVIEW_PROCEDURE.md added to PURPOSE section.*

*v1.1 changes (2026-05-20): Feedback ID format added. Severity scale (1–4) defined. Batching rule added. Client confirmed? and Disposition rationale columns added to register table.*
