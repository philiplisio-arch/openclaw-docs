# OPENCLAW — EXECUTION PLAN (ACTIVE)

━━━━━━━━━━━━━━━━━━━━━━

## Phase Overview

Phase 4 — Control & Stability → COMPLETE  
Phase 5 — Retrieval Orchestration → COMPLETE  
Phase 5.6 — Execution Stabilization → COMPLETE  

Phase 6 — Trust & Validation Layer → IN PROGRESS

━━━━━━━━━━━━━━━━━━━━━━

## Phase 5.6 — Execution Stabilization (COMPLETED)

### Achievements

- Fixed exit code capture bug in wrapper
- Eliminated silent output suppression
- Introduced structural completeness heuristic
- Implemented recovery logic for valid outputs
- Added delivery-level logging (HTTP + response)

---

### Key Principle Introduced

> Exit code alone is not a sufficient indicator of execution success

---

### System Behavior Now

- Non-zero exits can be conditionally recovered
- Valid outputs are no longer discarded
- Lark delivery is verified per run
- Full pipeline is observable end-to-end

---

### Execution Flow

cron → run_light_to_lark.sh  
→ orchestrator (run_phase5_offline.sh)  
→ retrieval pipeline  
→ agent execution  
→ control layer (structural validation)  
→ validator layer (evidence validation)  
→ delivery decision  
→ relay → Lark  

━━━━━━━━━━━━━━━━━━━━━━

# 🔷 PHASE 6 — TRUST & VALIDATION LAYER

OBJECTIVE:

Move system from:

• High output capability  
→ High trust, client-grade intelligence system  

---

## Core Principles (LOCKED)

- Trust > Speed  
- Observability > Elegance  
- Deterministic validation > Probabilistic judgment  
- No silent failure  
- No unverified output reaches client  

---

## Phase 6 Structure (LOCKED)

6.1 — Validator Layer → COMPLETE  
6.2 — Validation-Aware Delivery Gate → COMPLETE  
6.3 — Evidence Traceability System → CURRENT  
6.4 — Retrieval Quality Stabilization  

6.5 — Conflict Handling Upgrade  
6.6 — Low-Signal Handling Refinement  
6.7 — Output Consistency Hardening  

6.8 — Model Architecture Optimization  
6.9 — Source Expansion  
6.10 — Channel Expansion  

---

## Dependency Order (CRITICAL)

Hard Gates:

6.1 → 6.2 → 6.3 → 6.4  

Soft Layer:

6.5 → 6.6 → 6.7  

Expansion Layer:

6.8 → 6.9 → 6.10  

---

━━━━━━━━━━━━━━━━━━━━━━

## Phase 6.1 — Validator Layer (COMPLETED)

### Achievements

- Validator implemented as independent layer
- validation_result.json generated every run
- PASS / WARN / FAIL classification working
- Publisher matching implemented (V1)
- Fabricated citation detection verified

---

### Behavior

Validator checks:

- Source existence
- Publisher match
- URL presence
- No fabricated citations
- Basic claim-to-source alignment

---

### Validation Results Confirmed

PASS:
- Real run → citations matched → GREEN

WARN:
- Minor metadata mismatch → YELLOW

FAIL:
- Fabricated source → RED (delivery blocked)

---

### System Impact

- Output now evidence-aware
- Fabricated sourcing prevented
- Trust layer enforced

---

### Status

→ Phase 6.1 COMPLETE  
→ Exit criteria satisfied  

━━━━━━━━━━━━━━━━━━━━━━

## Phase 6.2 — Validation-Aware Delivery Gate (COMPLETED)

### Objective

Integrate Control Layer + Validator Layer into final delivery decision.

---

### Final Logic (ENFORCED)

Control PASS + Validator PASS  
→ deliver  

Control PASS + Validator WARN  
→ deliver (with warning)  

Control PASS + Validator FAIL  
→ BLOCK delivery  

Control FAIL  
→ BLOCK delivery  

---

### Implementation

- run_light_to_lark.sh reads:
  /root/openclaw_phase6/validation/validation_result.json

- Applies deterministic delivery decision

---

### Logging (REQUIRED)

Each run logs:

- Control result (complete / incomplete)
- Validator result (PASS / WARN / FAIL)
- Final decision:
  - delivered
  - delivered_with_warning
  - blocked

---

### System Impact

- No unvalidated output reaches Lark
- Delivery now deterministic
- Failure is visible and enforced

---

### Status

→ Phase 6.2 COMPLETE  

━━━━━━━━━━━━━━━━━━━━━━

## Phase 6.3 — Evidence Traceability System (CURRENT)

### Objective

Make every output claim traceable to:

- result_id
- retrieval_package
- query_id
- provider
- source metadata (post-mapping)

---

### Architectural Shift

From:

→ freeform citations (publisher/date)

To:

→ deterministic references (result_id)

---

### Current Implementation

✔ retrieval_package includes result_id  
✔ agent outputs (result_id: xxx) format  
✔ validator checks result_id validity  
✔ invalid outputs blocked  

---

### Critical Failure (CONFIRMED)

❌ Agent produces invalid result_id references

Observed:

- Mix of valid + fabricated IDs
- Partial match against retrieval_package
- Validator FAIL → delivery blocked

---

### Root Cause

- Agent remains probabilistic
- Prompt constraints insufficient
- No hard binding to valid ID set

---

### Key Insight

> Prompt-based citation control is fundamentally unreliable

Therefore:

→ Only deterministic validation + enforcement can guarantee correctness

---

## Phase 6.3a — result_id Validation Stabilization (CURRENT TASK)

### Objective

Diagnose and eliminate invalid result_id generation

---

### Required Actions

1. Extract all result_id from agent output  
2. Extract all valid result_id from retrieval_package  
3. Compare sets  
4. Identify mismatch patterns:

   - hallucinated IDs  
   - formatting errors  
   - truncation / corruption  

---

### Success Criteria

- 100% result_id match rate  
- Zero fabricated IDs  
- Validator PASS on real runs  
- Delivery unblocked  

---

### Constraints

DO NOT:

- modify retrieval layer  
- modify orchestrator  
- weaken validator  
- expand system scope  

---

### Status

→ IN PROGRESS  
→ BLOCKING Phase 6 completion  

━━━━━━━━━━━━━━━━━━━━━━

## Phase 6.4 — Retrieval Quality Stabilization (BLOCKED)

### Objective

Improve:

- Baidu contribution
- source diversity
- signal depth

---

### Status

→ BLOCKED until Phase 6.3 stable  

---

━━━━━━━━━━━━━━━━━━━━━━

## CURRENT SYSTEM STATE

System is now:

✔ Deterministic  
✔ Observable  
✔ Recoverable  
✔ Retrieval-bound  
✔ Validator-enforced  
✔ Delivery-gated  

But NOT yet:

✖ Deterministic evidence traceability  
✖ Agent citation reliability  
✖ Fully stable multi-source retrieval  

---

## NEXT STEP (CRITICAL)

→ Diagnose result_id mismatch pattern  

(No ambiguity — this is the ONLY task)

---

## FINAL PRINCIPLE

The system must deliver only when:

→ structurally valid  
AND  
→ evidentially grounded  

NOT:

→ plausible  
→ well-written  
→ or “likely correct”  

---

END