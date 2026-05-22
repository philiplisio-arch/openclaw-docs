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

| Feedback ID | Date | Run ID | Client ID | Section | Severity | Comment | Example from output | Why it matters | Classification | 