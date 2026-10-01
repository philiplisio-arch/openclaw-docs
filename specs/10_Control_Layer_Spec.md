# OPENCLAW — CONTROL LAYER SPEC

---
document_id: OPENCLAW-CLS-001
version: v1.0
status: LOCKED
---

## PURPOSE

Define how the system evaluates execution success vs output validity
and determines whether output should proceed to the Validator.

This layer sits BETWEEN:

→ Scrubber output (scrubbed_output.txt)
→ Validator

Note: In the full Phase 6 pipeline, the Control Layer evaluates structural completeness of scrubbed_output.txt before passing it to the Validator. The Validator then performs evidence integrity checks. Both results feed the Delivery Gate.

---

## CORE PRINCIPLE

Execution success ≠ Output validity

The system must evaluate output independently of process exit code.

---

## INPUTS TO CONTROL LAYER

1. orchestrator_exit_code
2. output_files:

   * scrubbed_output.txt (primary — Scrubber output, used as of Phase 6)
   * agent_output.txt (secondary reference)
3. structural_checks:

   * required sections present
   * non-empty content
   * valid formatting

---

## STRUCTURAL COMPLETENESS RULE

Output is considered structurally complete if:

✔ EXECUTIVE TAKE exists
✔ ADVISORY LAYER exists
✔ content length exceeds minimum threshold
✔ no truncation detected

---

## DECISION MATRIX

### Case 1 — exit_code = 0 AND output complete

→ status: SUCCESS
→ action: pass structural PASS to Delivery Gate

---

### Case 2 — exit_code ≠ 0 AND output complete

→ status: RECOVERABLE
→ action: pass structural PASS (with warning) to Delivery Gate

Log:

* [WARN] recovered from non-zero exit

---

### Case 3 — exit_code = 0 AND output incomplete

→ status: FAILURE
→ action: DO NOT deliver

---

### Case 4 — exit_code ≠ 0 AND output incomplete

→ status: FAILURE
→ action: DO NOT deliver

---

## DELIVERY RULE

The Control Layer passes a structural PASS to the Delivery Gate ONLY if:

→ structural completeness = true

The Delivery Gate is the sole and final authority on whether output is delivered.
The Control Layer produces a structural result — it does not deliver directly.
Exit code alone must NEVER block delivery.

---

## LOGGING REQUIREMENTS

Each run must log:

* orchestrator exit code
* structural completeness result
* recovery decision
* delivery result (HTTP code)

---

## FAILURE VISIBILITY RULE

If output is not delivered:

→ reason must be logged explicitly

No silent suppression allowed.

---

## RELATION TO UNIFIED FAILURE MODEL

For cross-layer failure scenarios involving the Control Layer (structural incompleteness, blocked delivery), refer to the **Unified Failure Matrix** in `SYS_RETRIEVAL_FAILURE_HANDLING`. That document is the canonical failure reference for the full pipeline. The decision matrix defined here is consistent with and subordinate to that matrix.

---

## RELATION TO PHASE 6

This layer becomes input to:

→ Validator Layer (6.1)
→ Delivery Gate (6.2)

Validator will extend this logic, not replace it.

---

## FINAL PRINCIPLE

The system delivers structurally complete output only.
Truth validation is handled exclusively by the Validator Layer.

---

END
