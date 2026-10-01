---
document_id: OPENCLAW-ADV-013-REVIEW
date: 2026-05-28
classification: PHASE D ADVISORY — CONSULTANT REVIEW
status: REFERENCE
---

# OPENCLAW — CONSULTANT REVIEW MEMO
**Subject:** Review of Operator Response to Signal-Widening Advisory
**Date:** 2026-05-28
**Prepared for:** OpenClaw Project Operator
**In review of:** Operator Response Memo — OPENCLAW-ADV-013-RESPONSE (initial draft)
**Status:** REFERENCE — revisions incorporated into final response; operator approved

---

## EXECUTIVE SUMMARY

The revised Operator Response Memo is substantially improved and is largely
ready for approval as the planning document governing the signal-widening
workstream.

**Consultant position:** APPROVE WITH TARGETED REVISIONS.

**Revisions recommended:**

1. Add CP-022A — an early held-mode query-family dry run before live CP-022 deployment.
2. Include ALJ in the shared CP-020 label schema, but validate ALJ labels only
   in held/pre-live mode.
3. Suppress LinkedIn from the default WS1 output under CP-021.
4. Restart the Phase D clean-delivery gate streak on the first live CP-021
   source-first delivery.
5. Add deterministic-labeling constraints to CP-024.
6. Expand CP-022 validation criteria so "better signal" is measured concretely.
7. Allow ALJ CP-023 query-family expansion to begin after ALJ pre-live blockers
   are cleared and one baseline held ALJ run exists, rather than requiring ALJ
   external live delivery first.
8. Clarify that CP-018/019 are in-flight stabilization/cleanup items, while
   ALJ CP-015/016/017 are true pre-live blockers.

---

## OVERALL ASSESSMENT

Grade: A / A-

The plan is strong enough to approve. The strongest improvement in the revised
memo is Section III (browser retrieval integration), which correctly identifies
the key structural question — can the VPS reliably fetch Chinese official,
sector, and business-press sources from its geographic position? — and correctly
keeps Phase 2 browser enrichment out of scope until Phase 1 findings are
reviewed.

---

## FINDING 1 — ADD CP-022A HELD-MODE QUERY-FAMILY DRY RUN

Because weak signal is the current core product problem, the plan should
introduce a non-live query-family dry run before formal CP-022 deployment.

CP-022A runs the proposed expanded WS1 query families in held mode only,
comparing the source mix against the current baseline. CP-022 may proceed
to live deployment only if the operator confirms materially improved source
richness without unacceptable noise or runtime instability.

Rationale: The safest acceleration is not to deploy query expansion live
sooner. It is to test richer retrieval in held mode sooner — during Tier 2,
while format changes are validating.

---

## FINDING 2 — CP-020 SHOULD INCLUDE ALJ SCHEMA BUT VALIDATE PRE-LIVE

WS1 and ALJ should not develop separate source-label vocabularies. Include
ALJ in the CP-020 shared schema. However, ALJ labels should validate only
in held/pre-live mode until ALJ routing and pre-live blockers are cleared.

---

## FINDING 3 — LINKEDIN SHOULD BE SUPPRESSED FROM DEFAULT OUTPUT

The product is moving toward a source-first China signal digest. LinkedIn is
a different product shape. Suppress from the default WS1 Lark output under
CP-021. LinkedIn may return only as an optional downstream artifact generated
from a selected source-based signal item.

---

## FINDING 4 — GATE STREAK SHOULD RESTART AFTER CP-021

CP-021 changes the user-facing product experience and the evaluation standard.
A clean run under the old format does not prove the new source-first format is
client-ready. Gate streak restarts on first live CP-021 delivery.

---

## FINDING 5 — CP-024 NEEDS DETERMINISTIC-LABELING CONSTRAINTS

The SOURCES appendix is a trust artifact. Appendix labels should be assigned
deterministically from publisher, domain, published date, and retrieved date
where possible. If deterministic classification is not available, the label
should be UNKNOWN — not aggressively inferred by the agent.

---

## FINDING 6 — CP-022 VALIDATION CRITERIA SHOULD BE CONCRETE

Minimum criteria before CP-022 live deployment:
- 15+ retained sources after filtering/dedup
- 8+ visible appendix sources
- 4+ Chinese-source items
- 2+ Chinese business/financial press items
- 1+ official or state-source item where relevant
- no single publisher >35% of visible source list
- duplicate/amplification count visible
- freshness labels on all major signal items
- source category labels on all appendix items
- operator source-usefulness score ≥4 across 2 held-mode runs

---

## FINDING 7 — ALJ CP-023 SHOULD NOT REQUIRE EXTERNAL LIVE DELIVERY FIRST

CP-023 may begin after ALJ pre-live blockers are resolved and at least one
baseline held-mode ALJ run is successfully produced. It does not need to wait
for ALJ external live delivery.

---

## FINDING 8 — DISTINGUISH TRUE BLOCKERS FROM HOUSEKEEPING ITEMS IN TIER 0

CP-015/016/017 are ALJ pre-live blockers. CP-018/019 are in-flight
stabilization/cleanup items. CP-018/019 are not conceptual blockers to
CP-020 design work if implementation slips for minor reasons.

---

## RECOMMENDED OPERATOR DECISIONS

1. Approve tier sequencing with: CP-022A added; Tier 0 distinction; ALJ
   CP-023 held-mode testing after blockers and baseline run (not live delivery).
2. Include ALJ in CP-020 taxonomy schema; validate ALJ pre-live only.
3. Suppress LinkedIn from default WS1 output.
4. Restart gate streak on first live CP-021 delivery.

---

*OPENCLAW-ADV-013-REVIEW | 2026-05-28 | REFERENCE — superseded by
OPENCLAW-ADV-013-RESPONSE (revised) which incorporates these findings*
