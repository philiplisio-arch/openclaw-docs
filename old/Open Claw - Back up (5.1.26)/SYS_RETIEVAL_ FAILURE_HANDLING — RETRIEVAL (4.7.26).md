# FAILURE HANDLING — RETRIEVAL ORCHESTRATION LAYER
OpenClaw Phase 5.1

---

## PURPOSE

Define how the system behaves when retrieval is incomplete, degraded, or conflicting.

Failure handling is owned by the ORCHESTRATOR.

The agent does NOT detect or manage failure — it only reacts to structured signals.

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

## FINAL PRINCIPLE

Failure handling is not an edge case.

It is a FIRST-CLASS SYSTEM LAYER.

A system that hides failure is untrustworthy.

A system that exposes failure is controllable.

---

END