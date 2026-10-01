# GOVERNANCE PROPOSAL — PHASE D GATE: 10 → 5 CONSECUTIVE CLEAN DELIVERIES

---
document_id: OPENCLAW_GOV_PROPOSAL_PHASE_D_STREAK_5
date: 2026-06-11
author: Claude Fable 5 (drafted at operator direction)
lane: 2 (gate threshold change — governance tier)
status: ADOPTED — operator-approved 2026-06-11; merged to main; gate checklist v1.9
---

## What changes

Phase D gate requirement: **ten** consecutive clean external deliveries → **five** consecutive clean external deliveries. The five-layer clean-delivery standard, per-delivery operator confirmation, and reset-on-failure semantics are unchanged. Current streak (1 confirmed, D22 2026-06-11) carries over → reads **1/5**.

## Added condition (recommended, new)

A counted delivery must also show **citation_alignment misaligned = 0** in its validation result. This instrumentation (ADV-015 Option B, live 2026-06-10) did not exist when ADV-017 set the ten-delivery bar; it directly measures the failure mode (wrong-source citation) that caused the trust hold. With it, five deliveries carry more evidence than ten deliveries did under the June 6 standard.

## Rationale

1. The ten-delivery bar was set 2026-06-06, before: per-run traceability archive (full), session isolation (root-cause fix for the contamination that produced the misbinding), and the citation-alignment checker. Each confirmed delivery now carries materially more verification.
2. The gate's purpose is trust repair through verified deliveries, not calendar penance. Five fully-instrumented, operator-confirmed deliveries demonstrate the repaired system; the marginal evidence of deliveries 6–10 is low if 1–5 are clean under the new instrumentation.
3. Operator review load (~20 min/day) is a real constraint; concentrating it on five high-evidence reviews is a better trade.

## Risk and mitigations

- **Risk:** shorter proving window before the gate unlocks CP-021, CP-022, and the ALJ resumption path; the new safeguards have one clean validation day as of this proposal.
- **Mitigations:** (a) the misaligned=0 condition above; (b) any blocked run or any flagged layer still resets the streak per existing ADV-017 rules; (c) ALJ resumption keeps its own separate operator authorization and controlled first delivery (unchanged); (d) CP-022 live still requires its 5 pre-live fixes + operator go (unchanged).

## Proposed diff (06_PHASE_GATE_CHECKLIST.md)

- Requirement line: "Ten consecutive clean external deliveries" → "Five consecutive clean external deliveries (reduced from ten 2026-06-11, operator decision; see OPENCLAW_GOV_PROPOSAL_PHASE_D_STREAK_5)".
- Clean-delivery definition: add item 6 — "citation_alignment misaligned = 0 in the delivery's validation result (ADV-015 Option B)".
- Streak line: "1 of 10" → "1 of 5".
- Earliest possible gate closure at daily cadence: 2026-06-15 (D26), assuming D23–D26 all confirm clean.

## Adoption

On operator approval: merge this branch to main, apply the checklist edit (v1.9), record the decision in Daily Status and ADV-017's incorporation trail. Until then, main continues to read 1/10.
