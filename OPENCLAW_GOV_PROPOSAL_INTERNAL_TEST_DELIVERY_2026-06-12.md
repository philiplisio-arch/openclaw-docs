# GOVERNANCE PROPOSAL — Internal Test Delivery Posture (Phase D)

---
document_id: OPENCLAW_GOV_PROPOSAL_INTERNAL_TEST_DELIVERY_2026-06-12
date: 2026-06-12
author: Claude Fable 5 (assessment + drafting), from operator memo "OpenClaw Internal Testing Delivery Posture"
lane: 2 (governance / delivery-gate semantics) + Lane 3 implementation rider
status: PROPOSAL — on branch, not adopted; requires operator approval
---

## What this adopts

The operator memo's core distinction, verbatim as the governing rule:

> During the current Phase D internal testing period, OpenClaw outputs may be delivered automatically to internal operator-review destinations even when warnings, alignment issues, enrichment defects, or editorial imperfections are present. These outputs must be clearly labeled as internal test outputs and must not be treated as client-ready unless they satisfy the applicable clean-delivery gate. Internal review delivery is not equivalent to external client delivery.

Two delivery categories become explicit:

| Category | Status | Gate behavior |
|---|---|---|
| **Internal Review Delivery** | ACTIVE (all current channels) | Gates classify and label; they do not block. Every run delivers to the operator's review destination with an `INTERNAL TEST — <STATE>` label. |
| **External Client Delivery** | NOT ACTIVE (no channel exists) | Full Phase D clean-delivery standard, per-delivery operator approval, unchanged. |

## Factual basis (verified 2026-06-12, code + config)

- WS1 (`china_monitor_001`) delivers to a Lark doc reached via the local relay; readership is the operator.
- ALJ (`alj_china_auto_001`) config states: *"pilot client — no live delivery credential exists yet."* The 2026-06-11 "first real ALJ delivery" was an operator-approved manual send to the ALJ Lark doc, not to a Jameel-side recipient.
- **Adoption condition (operator attestation required):** no person other than the operator has read access to either Lark destination. If any destination is ever shared externally, it immediately becomes an External Client Delivery channel and reverts to the strict gate.

## Assessment and amendments (Claude)

The memo is sound: with no external reader, fail-closed blocking only slows the feedback loop that improves the system, and yesterday proved it — the WS2 zero-citation brief was blocked into the archive where the operator never saw it, and the CP-026 enriched outputs never reached review delivery at all. Classification-not-suppression is the right posture **provided the following five amendments ride with it**:

1. **Destination allowlist, not labels, is the safety boundary.** A label is text; it cannot stop a leak. Each client config gains an explicit `delivery_mode: internal_review | external_client` key. `internal_review` is the only mode that bypasses blocking, and it is only valid for destinations covered by the attestation above. `external_client` (none exist today) keeps every current block plus per-delivery operator approval. Flipping a client to `external_client` is itself a Lane 2 change.
2. **The Phase D streak definition must be amended in the same change** — current text requires "five consecutive clean *external deliveries with client confirmation*," which is incoherent when no client exists. Amended definition: the streak counts **the scheduled production-path runs** (WS1 daily cron; ALJ Sunday cron once counted), assessed against the unchanged six-item clean standard, with **operator confirmation substituting for client confirmation** during the internal period. Internal test runs in experiment namespaces (cp026_*, capreplay_*, etc.) never count for or against the streak.
3. **Nothing silent.** A delivery that would previously have been blocked must say so in its label and carry the failure summary (e.g. `INTERNAL TEST — BLOCKED-GRADE: zero cited bullets survived scrubbing`). All validation artifacts, traceability archives, and counters continue exactly as today; the posture changes delivery, not evidence.
4. **Content pipeline unchanged.** The scrubber still scrubs (invalid ids removed, uncited bullets removed, citation cap enforced); internal review sees what a client *would* see, plus the label. Raw output remains in the archive for comparison.
5. **Streak protection by construction.** Because gates still compute everything, a labeled-dirty production run simply fails item 6 and the streak rule as it does today. Faster internal flow cannot launder a dirty run into the streak.

## Label taxonomy (delivery header line 1)

`INTERNAL TEST — CLEAN` · `INTERNAL TEST — ALIGNMENT WARNING (misaligned=N)` · `INTERNAL TEST — BLOCKED-GRADE: <reason>` · `INTERNAL TEST — EXPERIMENTAL ENRICHMENT (CP-026)` · `INTERNAL TEST — NOT CLIENT-READY: <reason>`

Labels are derived mechanically from the run's validation result; agents and prompts cannot influence them.

## Lane 3 implementation rider (after approval)

1. `client_config_*.yaml`: add `delivery_mode: internal_review` (both clients). Loader exports `OPENCLAW_DELIVERY_MODE`.
2. `run_light_to_lark.sh`: under `internal_review` — scrubber/validator failure paths and `pilot_mode` skip deliver the scrubbed output with the appropriate label instead of suppressing; label line prepended to `FINAL`. Under any other mode, behavior is byte-identical to today (default if key missing: current blocking behavior — fail-safe).
3. CP-026/experiment drivers: optional `--push-internal` so enriched legs reach the review doc labeled `EXPERIMENTAL ENRICHMENT`.
4. Validation: replay matrix — (a) clean run → label CLEAN, body unchanged; (b) yesterday's WS2 zero-citation run → delivers labeled BLOCKED-GRADE; (c) `delivery_mode` absent → byte-identical legacy behavior; (d) pilot_mode + internal_review → labeled delivery; pilot_mode + external_client → still blocked.
5. Rollback: remove `delivery_mode` keys (single-line revert per config) → system returns to current blocking behavior; runtime `.bak` for the script.

## Documentation changes carried on this branch

- `06_PHASE_GATE_CHECKLIST.md` (v1.11-PROPOSED): Internal vs External delivery section; amended streak wording per amendment 2.
- This proposal document.
- On adoption (not on branch): Daily Status entry, CoWork protocol cross-reference, Master Document Index row. `00_System_Constitution.md` is **not** touched — this changes operating procedure, not authority or roles.

## Decision requested

- **Adopt** → merge branch, stamp checklist v1.11 ACTIVE, execute Lane 3 rider with replay validation, deliver attestation line recorded in Daily Status.
- **Adopt with changes** → note them; branch updated before merge.
- **Reject** → branch closed unmerged; current fail-closed posture stands.
