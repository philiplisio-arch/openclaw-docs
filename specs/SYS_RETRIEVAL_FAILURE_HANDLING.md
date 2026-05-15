# FAILURE HANDLING — FULL PIPELINE
OpenClaw — covers Retrieval + Phase 6 Validation Chain

---
document_id: OPENCLAW-FH-001
version: v5.0
status: ACTIVE
---

---

## PURPOSE

Define how the system behaves when any layer fails: retrieval, scrubber, validator, or delivery gate.

For retrieval failures, handling is owned by the ORCHESTRATOR. The agent reacts to structured signals, not raw failure states.

For Phase 6 validation chain failures (Scrubber, Validator), handling is defined in the respective layer specs and governed by the Delivery Gate decision matrix.

---

## CORE PRINCIPLE

Failure must be:

- explicit
- structured
- machine-readable
- visible before agent execution

Never hidden  
Never inferred by the agent  
Never silently compensated for  

---

## FAILURE TYPES (LOCKED)

### 1. EMPTY RETRIEVAL

Definition:
- Both Brave and Baidu executed
- No usable results after filtering/dedup

Detection:
- results = []
- brave_status = empty
- baidu_status = empty

Required output:
- overall_status = empty

System behavior:
- agent runs in low-signal mode
- no forced narrative
- no synthetic insights
- fallback messaging allowed

---

### 2. PARTIAL RETRIEVAL

Definition:
- One provider succeeds
- One provider fails or returns no usable results

Detection:
- brave_status != baidu_status
- at least one = ok
- at least one = empty|failed|timeout

Required output:
- overall_status = partial

System behavior:
- retain valid results
- mark degraded coverage
- no compensation by invention
- no assumption of completeness

---

### 3. PROVIDER FAILURE

Definition:
- provider fails operationally

Types:
- timeout
- API error
- parse error

Detection:
- provider_status = failed|timeout

Required output:
- recorded in errors[]
- reflected in retrieval_status

System behavior:
- system continues if at least one provider succeeds
- otherwise escalates to full failure

---

### 4. FULL RETRIEVAL FAILURE

Definition:
- both providers fail operationally

Detection:
- brave_status = failed|timeout
- baidu_status = failed|timeout
- results = []

Required output:
- overall_status = failed

System behavior:
- agent must NOT generate normal analysis
- output must reflect failure state OR abort (implementation choice)
- no evidence-based claims allowed

---

### 5. CONFLICTED RETRIEVAL

Definition:
- multiple retained results contain contradictory facts

Examples:
- different numeric values
- different dates
- different causal interpretations

Detection:
- orchestrator identifies conflict during normalization
- conflicts[] populated

Required output:
- conflict_flag = true
- overall_status = ok_with_conflicts

System behavior:
- conflicting items retained
- NOT silently merged
- NOT overwritten
- passed to agent explicitly

---

### 6. DEGRADED QUALITY (SOFT FAILURE)

Definition:
- results exist but are weak, sparse, or low-confidence

Examples:
- too few results
- only one weak source
- missing timestamps
- missing URLs (edge cases)

Detection:
- orchestrator applies quality thresholds

Required output:
- overall_status = ok OR partial
- notes[] includes degradation flag

System behavior:
- agent reduces certainty
- avoids over-synthesis
- avoids strong pattern claims

---

## ERROR STRUCTURE (LOCKED)

All failures must be recorded in:

errors[]

Each error must include:
- layer (retrieval_source | orchestrator)
- source (Brave | Baidu | system)
- type (timeout | parse_error | empty_result | validation_error | other)
- message (human-readable)

---

## ORCHESTRATOR RESPONSIBILITY (CRITICAL)

The orchestrator MUST:

1. Detect all failure types
2. Assign correct status enums
3. Populate errors[]
4. Populate conflicts[]
5. Set conflict_flag
6. Set overall_status correctly
7. Ensure agent receives structured signal BEFORE execution

The orchestrator must NOT:
- hide failures
- smooth failures
- pass raw inconsistent data without labeling it

---

## AGENT RESPONSIBILITY (DERIVED)

The agent MUST:

- read retrieval_status BEFORE reasoning
- adapt behavior to overall_status
- respect conflict_flag
- avoid hallucination under degraded conditions
- avoid treating partial/empty as complete

The agent must NOT:
- detect failure independently
- override orchestrator signals
- compensate for missing data

---

## NON-NEGOTIABLE RULES

1. No silent failure
2. No silent conflict resolution
3. No fallback to invented narrative
4. No mixing failed and successful retrieval without labeling
5. No passing raw retrieval anomalies to agent without normalization

---

## SYSTEM GUARANTEE

At agent execution time:

The system MUST guarantee:

- retrieval state is fully known
- failure state is explicitly labeled
- evidence pool is bounded and validated

Only then may the agent run.

---

## PHASE 6 VALIDATION CHAIN FAILURES

### Resolver Failure

Definition: resolve_source_numbers.py cannot map source numbers to result_ids,
produces no output, or exits with error.

System behavior:
- Treat as structural failure
- Do NOT pass resolver output to Scrubber
- Block delivery
- Log: resolver_error with reason

### Scrubber Failure

Definition: Scrubber cannot parse citation groups in resolved output.

System behavior:
- Treat as structural failure
- Do NOT pass malformed output to Validator
- Block delivery
- Log: scrubber_error with reason

Note: scrubber_report.json is not produced (T-06, resolved 2026-05-11).
Scrubber failure is indicated by non-zero exit or absence of scrubbed_output.txt.
Scrubber metrics are emitted to stdout and captured in the cron log.

### Validator Failure (FAIL classification)

Definition: Validator returns FAIL after reviewing scrubbed_output.txt.

System behavior:
- Delivery Gate blocks delivery
- Log: validator_failed + reason (fabricated_citation / missing_source / etc.)
- No output reaches Lark

### Validator Warning (WARN classification)

Definition: Validator returns WARN (minor issues, no fabricated citations).

System behavior:
- Delivery Gate allows delivery with warning
- Log: validator_warned + reason

### Validator Runtime Error

Definition: Validator crashes or cannot produce validation_result.json.

System behavior:
- Treat same as FAIL
- Block delivery
- No silent pass

### Delivery Gate Failure

Definition: Lark push fails after validator PASS/WARN.

System behavior:
- Log: delivery_failed + HTTP response
- Retry logic (if implemented) before marking as failed
- Do NOT retry if validator returned FAIL

---

## UNIFIED FAILURE MATRIX

Cross-layer reference: Layer → Failure Type → System Behavior → Delivery Outcome.

| Layer | Failure Type | System Behavior | Delivery Outcome |
|-------|-------------|-----------------|------------------|
| Retrieval | Empty (both providers) | Agent runs in low-signal mode; no forced narrative | Deliver (low-signal output) |
| Retrieval | Partial (one provider down) | Agent uses surviving evidence; degraded coverage flagged | Deliver with partial coverage |
| Retrieval | Provider timeout / API error | Continue if other provider succeeded; escalate if both fail | Deliver or block (see Full Failure) |
| Retrieval | Full failure (both providers) | Agent must not generate normal analysis; output reflects failure | Block |
| Retrieval | Conflicted results | Conflicts passed to agent explicitly; not silently merged | Deliver (agent surfaces uncertainty) |
| Orchestrator | Package build failure | Cannot produce structured input for agent | Block |
| Resolver | Cannot map source numbers to result_ids / exits with error | Treat as structural failure; do not pass to Scrubber | Block |
| Scrubber | Cannot parse citation groups in resolved output | Treat as structural failure; do not pass to Validator | Block |
| Scrubber | Some IDs invalid (partial) | Invalid IDs removed; valid groups preserved | WARN → Deliver |
| Scrubber | All citation groups unsupported | Zero valid IDs across all groups | FAIL → Block |
| Control Layer | Output structurally incomplete | Missing required sections or truncated content | Block |
| Control Layer | Output structurally complete | Passes to validator | Continue |
| Validator | PASS | All cited result_ids verified against retrieval_package | Deliver |
| Validator | WARN | Minor issues (alias match, date fallback); no fabricated citations | Deliver with warning |
| Validator | FAIL | Fabricated or missing citations detected | Block |
| Validator | Runtime error | Cannot produce validation_result.json | Block (treated as FAIL) |
| Delivery Gate | Lark push failure post-PASS/WARN | Log HTTP response; retry if implemented | Mark failed; do not retry after FAIL |

---

## FINAL PRINCIPLE

Failure handling is not an edge case.

It is a FIRST-CLASS SYSTEM LAYER.

A system that hides failure is untrustworthy.

A system that exposes failure is controllable.

---

END