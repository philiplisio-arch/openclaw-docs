---
document_id: OPENCLAW-PHASE-D-SCORECARD-001
version: 1.4
created: 2026-05-20
last_updated: 2026-05-22
status: ACTIVE
classification: OPERATIONAL — PHASE D CONTENT SCORECARD
---

# OPENCLAW — Phase D Content Scorecard

## PURPOSE

Per-delivery content quality scoring for Phase D controlled pilot. One
entry per delivery. Scorecard rows are proposed by CoWork and
operator-confirmed. Scores inform the Phase D gate closure decision.

The operator review workflow — including the standard delivery review prompt
and CoWork output format — is defined in:
`OPENCLAW_PHASE_D_OPERATOR_REVIEW_PROCEDURE.md`

---

## SCORING RUBRIC

| Score | Meaning |
|-------|---------|
| 5 | Excellent — no issues |
| 4 | Good — minor issue, acceptable without change |
| 3 | Adequate — notable issue, change packet warranted |
| 2 | Poor — material deficiency, delivery marginal |
| 1 | Fail — delivery unacceptable |
| N/A | Feature not yet active (see dimension notes) |

---

## DIMENSION NOTES

| Dimension | Active from | Note |
|-----------|-------------|------|
| Relevance | Delivery 1 | |
| Freshness clarity | Delivery 1 | |
| Source authority | Delivery 1 | |
| China linkage | Delivery 1 | |
| Advisory usefulness | Delivery 1 | |
| Claim calibration | Delivery 1 | |
| Readability | Delivery 1 | |
| Source accessibility | Pending | N/A until Validated Sources Appendix implemented |
| Source specificity | Delivery 1 | Do bullets include concrete details — dollar amounts, dates, named entities, specific policies? Added 2026-05-21 based on pilot client interview |
| Source provenance clarity | Delivery 1 | Is it clear which insights derive from Chinese-language sources vs. international media? Core differentiator of product. Added 2026-05-21 |
| Industry coverage breadth | Delivery 1 | Does the brief surface sector-specific developments (AI, semiconductors, agriculture, etc.) relevant to company decision-making — not restricted to predetermined sectors. Added 2026-05-21 |
| Full retrieval transparency | Pending | N/A until full retrieved + validated source list implemented at bottom of brief. Added 2026-05-21 |
| LinkedIn usefulness | Delivery 1 | |
| Overall client readiness | Delivery 1 | Operator holistic score |

---

## SCORECARD

| Delivery # | Date | Run Timestamp | Scored by | Validator | Relevance | Freshness clarity | Source authority | China linkage | Advisory usefulness | Claim calibration | Readability | Source accessibility | Source specificity | Source provenance clarity | Industry coverage breadth | Full retrieval transparency | LinkedIn usefulness | Overall client readiness | Client reviewed? | Client usefulness confirmation | Top 3 strengths | Top 3 weaknesses | Delivery-blocking issues | Recommended action |
|-----------|------|---------------|-----------|-----------|-----------|-------------------|-----------------|---------------|--------------------|--------------------|-------------|----------------------|--------------------|--------------------------|--------------------------|----------------------------|--------------------|--------------------------|-----------------|---------------------------------|-----------------|-----------------|--------------------------|--------------------|
| 1 | 2026-05-21 | 06:31 | CoWork / Operator | GREEN 8/8/0 | 3 | 2 | 2 | 3 | 2 | 4 | 3 | N/A | 2 | 2 | 2 | N/A | 2 | 2 | Yes — PM interview | Relevant but too generic; sourcing not visible; advisory not actionable; no dollar amounts or dates | Citation discipline (0% fabrication, T-04 compliant); China linkage on all delivered bullets; Chinese-language sources present | Sourcing not visible to reader; bullets too generic (no dollar amounts/dates); advisory layer too generic to be actionable | Yes — thin retrieval (Issue #50, 4/8 bullets); sourcing not visible; external send not recommended | Hold from external send; implement CP-002/003/004; resolve Issue #50 before counting toward gate streak |
| 2 | 2026-05-22 | 06:32 | CoWork | GREEN 25/25/0 | 4 | 3 | 4 | 4 | 3 | 5 | 4 | N/A | 4 | 5 | 3 | N/A | 4 | 4 | No — pending | Pending | Full 8-bullet brief; [CN]/[INTL]/[CN+INTL] labels on all bullets; concrete figures in every ET/AL bullet | Industry coverage narrow (no tech/AI/semiconductors); freshness signaling absent; two AL action clauses generic | None — T-10 residual is Brain Lite only; not delivery-blocking | External send pending operator review; CP-005 deploy for T-10 validator_status fix |

---

## PHASE D GATE THRESHOLD

Required across the final 10 scored deliveries to close Phase D gate:

- No score of 1 (Fail) in any active dimension
- No more than 2 scores of 2 (Poor) across all dimensions and all 10 deliveries
- Average Overall client readiness score ≥ 3.5
- Zero delivery-blocking issues in final 10 deliveries
- Operator confirmation on each delivery
- Client confirmation that the brief is useful

---

## ROLLING AVERAGES (updated per delivery)

Rolling averages are manually maintained by the operator after each scored
delivery. Update the Average column by recalculating the mean across all
scored (non-N/A) entries for that dimension.

| Dimension | Deliveries scored | Average |
|-----------|-----------------|---------|
| Relevance | 2 | 3.5 |
| Freshness clarity | 2 | 2.5 |
| Source authority | 2 | 3.0 |
| China linkage | 2 | 3.5 |
| Advisory usefulness | 2 | 2.5 |
| Claim calibration | 2 | 4.5 |
| Readability | 2 | 3.5 |
| Source accessibility | N/A | N/A |
| Source specificity | 2 | 3.0 |
| Source provenance clarity | 2 | 3.5 |
| Industry coverage breadth | 2 | 2.5 |
| Full retrieval transparency | N/A | N/A |
| LinkedIn usefulness | 2 | 3.0 |
| Overall client readiness | 2 | 3.0 |

---

*OPENCLAW-PHASE-D-SCORECARD-001 | Version 1.3 | Created: 2026-05-20 | Status: ACTIVE*

*v1.4 changes (2026-05-22): Delivery 2 scored and entered (overall readiness: 4). Rolling averages updated to 2 deliveries.*

*v1.3 changes (2026-05-21): Four new dimensions added based on pilot client PM interview: Source specificity, Source provenance clarity, Industry coverage breadth, Full retrieval transparency. Delivery 1 scored and entered. Rolling averages updated.*

*v1.2 changes (2026-05-20): Cross-reference to OPENCLAW_PHASE_D_OPERATOR_REVIEW_PROCEDURE.md added to PURPOSE section. Clarified that scorecard rows are proposed by CoWork and operator-confirmed.*

*v1.1 changes (2026-05-20): Scored by, Client reviewed?, and Client usefulness confirmation columns added to scorecard table. Rolling averages maintenance rule added (manually maintained by operator per delivery).*
