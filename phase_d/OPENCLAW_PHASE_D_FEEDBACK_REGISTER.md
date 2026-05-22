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
| D-FB-001 | 2026-05-21 | run_20260520T223002Z | china_monitor_001 | Full output | 3 | Thin retrieval package — mapping_size=7 (vs norm 14–15); 12 source numbers out of range; 4 citation groups unsupported; 4 bullets removed by scrubber | Delivered 2 ET + 2 AL bullets; expected 3 ET + 5 AL | Phase D Delivery 1 arrived materially shorter than standard; client received degraded brief on first pilot delivery | A | Diagnostic — read retrieval_package_china_monitor_001.json; investigate package assembly from raw results | Pending | Material quality event on first Phase D delivery; investigation required before pattern assessment | Monitoring — did not recur Delivery 2 | mapping_size ≥ 12; source_numbers_dropped = 0 | Operator | Did not recur on 2026-05-22 Delivery 2 (full 8-bullet brief, 25/25 citations). Monitoring continues — one clean run insufficient to close. T-10 regression was separate issue (not linked to thin package). |
| D-FB-002 | 2026-05-22 | run_20260521T223002Z | china_monitor_001 | Logging | 2 | light_to_lark.log gap — 2026-05-22 run absent from log; pipeline completion confirmed by artifacts only | Log has 1525 lines ending with 2026-05-21 run; no 2026-05-22 entries present | Post-run analysis depends on log for resolver and scrubber metrics; gap creates partial observability loss | A | VPS investigation — check /root/openclaw_logs/ for rotated log file; update scp sync if rotation confirmed | Confirmed — not reproduced | Snapshot timing artefact — scp pulled mid-run; run present at lines 1526–1559; no log rotation | Closed | Run confirmed in log via Claude Code VPS audit | Operator | Issue #51 RESOLVED. Mitigation: run scp after 06:35 to avoid mid-run pull. No logrotate configured — file grows indefinitely; setup recommended. |

---

## OPEN ITEM COUNTS

| Category | New | Accepted | Batched | Implemented | Validated | Deferred | Total Open |
|----------|-----|----------|---------|-------------|-----------|----------|------------|
| A — Delivery-blocking | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| B — Editorial / prompt | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| C — Source-quality | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| D — Format / UX | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| E — Client preference | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **1** | **0** | **0** | **0** | **0** | **1** | **1** |

---

*OPENCLAW-PHASE-D-FEEDBACK-001 | Version 1.3 | Created: 2026-05-20 | Status: ACTIVE*

*v1.4 changes (2026-05-22): D-FB-001 status updated — did not recur Delivery 2; moved to Monitoring. D-FB-002 added — light_to_lark.log gap (2026-05-22); Category A Severity 2; Issue #51 logged. Open item counts updated.*

*v1.3 changes (2026-05-21): D-FB-001 added — Phase D Delivery 1 (2026-05-21); thin retrieval package; mapping_size=7; 4 bullets removed; Category A Severity 3. Open item counts updated.*

*v1.2 changes (2026-05-20): Cross-reference to OPENCLAW_PHASE_D_OPERATOR_REVIEW_PROCEDURE.md added to PURPOSE section.*

*v1.1 changes (2026-05-20): Feedback ID format added. Severity scale (1–4) defined. Batching rule added. Client confirmed? and Disposition rationale columns added to register table.*
