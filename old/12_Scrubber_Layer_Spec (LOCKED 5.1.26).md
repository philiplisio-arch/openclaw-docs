━━━━━━━━━━━━━━━━━━━━━━

OPENCLAW — SCRUBBER LAYER SPEC (LOCKED)

---
document_id: OPENCLAW-SCR-001
version: phase6_v2 (updated 2026-05-08 — Phase 6.8)
status: LOCKED
━━━━━━━━━━━━━━━━━━━━━━

## PURPOSE

Define deterministic cleanup of agent output before validation.

Scrubber ensures only valid result_id references reach the Validator.

---

## POSITION IN PIPELINE

Trigger
→ Retrieval
→ Orchestrator
→ Agent
→ Resolver (resolve_source_numbers.py)
→ **Scrubber**
→ Validator
→ Delivery Gate
→ Lark

## RESOLVER PRECONDITION

The Scrubber must not run on raw agent_output.txt.

`resolve_source_numbers.py` must execute first and convert all `[source_numbers: N]` and `[based_on: N]` citations to `[result_ids: res_xxx]` and `[based_on: res_xxx]` format.

The Scrubber operates on the resolved output produced by the resolver — not on raw agent output. If the resolver has not run or has failed, the Scrubber must not proceed.

---

## INPUTS

1. Resolved agent output (produced by resolve_source_numbers.py from agent_output.txt)
2. retrieval_package.json

Note: The Scrubber does NOT receive raw agent_output.txt. It receives the resolver's output, which contains result_id format citations only.

---

## OUTPUTS

1. scrubbed_output.txt
2. scrubber_report.json (path to be confirmed — T-06 open; expected: /root/openclaw_phase5/data/)

---

## LOCKED CITATION SYNTAX (PHASE 6.3a)

As of Phase 6.3a, the agent produces output in locked citation format:

- Claims: `[result_ids: res_xxxxxxxx, res_yyyyyyyy]`
- Advisory: `[based_on: res_xxxxxxxx]`

The Scrubber must parse both formats. Within each citation group, it validates each result_id token against retrieval_package.json.

**Interaction with VALID_RESULT_IDS:**
Once VALID_RESULT_IDS injection is implemented in build_agent_input_slim.py, the agent will only select from the provided list. The Scrubber remains the system-side enforcement layer — if any invalid ID reaches the Scrubber despite injection, it will be removed. The Scrubber's role does not narrow when VALID_RESULT_IDS is in use; it serves as the final deterministic safety net.

---

## CORE FUNCTIONS

1. Parse citation groups in locked syntax ([result_ids: ...] and [based_on: ...])
2. Extract all result_id tokens from each citation group
3. Validate each result_id against retrieval_package.json
4. Remove invalid or fabricated IDs from citation groups
5. Rewrite citation groups using only valid IDs
6. Remove bullets with no valid citation remaining after ID removal (uncited claim removal)
7. Extract CONFLICTS section before citation scrubbing — conflicts block must not be processed as body text
8. Preserve prose structure where possible

---

## CITATION GROUP RULES

- Valid group: contains ≥1 valid result_id → retain
- Mixed group: remove invalid IDs, retain valid IDs
- Invalid group: contains 0 valid IDs → mark unsupported

---

## EDGE CASE HANDLING

1. Empty citation group
   → mark unsupported

2. Mixed valid/invalid IDs
   → strip invalid IDs, retain group

3. Duplicate IDs
   → deduplicate within group

4. Malformed syntax
   → attempt parse → if fail → mark unsupported

---

## CLASSIFICATION OUTPUT

scrubber_report.json must include:

- citation_groups_seen
- valid_groups
- unsupported_groups
- ids_seen
- ids_kept
- ids_removed
- uncited_claims_removed
- conflicts_extracted
- conflict_count

---

## FAILURE LOGIC

- IF unsupported_groups == citation_groups_seen
  → signal FAIL condition

- IF unsupported_groups > 0 AND < total
  → signal WARN condition

- IF unsupported_groups == 0
  → signal PASS condition

---

## LOGGING REQUIREMENTS

Each run must log:

- ids_seen
- ids_kept
- ids_removed
- unsupported_groups

---

## VERSIONING

scrubber_version: phase6_v2

---

## RELATION TO VALIDATOR

The Scrubber runs BEFORE the Validator.

Scrubber responsibility: structural cleanup of citation tokens.
Validator responsibility: evidence integrity of retained citations.

Scrubber does NOT:
- judge claim meaning
- perform evidence matching
- produce PASS / WARN / FAIL delivery decisions

Validator does NOT:
- rewrite output
- remove tokens
- perform cleanup

These layers must not overlap.

---

## RELATION TO UNIFIED FAILURE MODEL

For cross-layer failure scenarios involving the Scrubber (parse failure, all groups unsupported, partial ID removal), refer to the **Unified Failure Matrix** in `SYS_RETRIEVAL_FAILURE_HANDLING`. That document is the canonical failure reference for the full pipeline. The failure logic defined here is consistent with and subordinate to that matrix.

---

## RELATION TO AGENT INPUT CONTRACT

The Scrubber is the system-side enforcement of the Agent Input Contract.

The contract specifies what the agent must do.
The Scrubber enforces what the system will accept.

If the agent violates the contract:
→ Scrubber removes the violation
→ Validator confirms what remains
→ Delivery Gate acts on the result

---

## FINAL PRINCIPLE

Scrubber enforces structural truth of citations.

It does NOT judge meaning or claims.

━━━━━━━━━━━━━━━━━━━━━━
