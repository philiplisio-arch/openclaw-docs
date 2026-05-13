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
→ wrapper evaluation (exit + heuristic + recovery)  
→ enrichment extraction  
→ relay → Lark  

━━━━━━━━━━━━━━━━━━━━━━

# 🔷 PHASE 6 — TRUST & VALIDATION LAYER

OBJECTIVE:

Move system from:

• High output capability  
→ High trust, client-grade intelligence system  

---

## Phase 6 Structure (LOCKED)

6.1 — Validator Layer → COMPLETE  
6.2 — Validation-Aware Delivery Gate → CURRENT  
6.3 — Evidence Traceability System → NEXT  
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
- Validation_result.json generated every run
- PASS / WARN / FAIL classification working
- Publisher matching implemented
- Fabricated citation detection verified
- Chinese alias support (basic) implemented

---

### Behavior

Validator checks:

- Citation presence
- Publisher match vs retrieval_package
- No fabricated sources
- Basic claim-to-source alignment

---

### Validation Results Confirmed

PASS:
- Real run → citations matched → GREEN

WARN:
- Missing citations → YELLOW

FAIL:
- Fake publisher test → RED

---

### System Impact

- Output now evidence-aware
- Fabricated sourcing prevented
- Trust layer introduced

---

### Known Limitation

- Publisher normalization incomplete (multi-language)
- Alias coverage limited
- Domain vs publisher mismatch possible

---

### Status

→ Phase 6.1 COMPLETE  
→ Exit criteria satisfied  

━━━━━━━━━━━━━━━━━━━━━━

## Phase 6.2 — Validation-Aware Delivery Gate (CURRENT)

### Objective

Integrate Validator with Control Layer to determine final delivery behavior.

---

### Target Logic (LOCKED)

Control PASS + Validator PASS  
→ deliver

Control PASS + Validator WARN  
→ deliver (with warning)

Control PASS + Validator FAIL  
→ BLOCK delivery

Control FAIL  
→ BLOCK delivery

---

### Implementation Scope

Modify:

/root/run_light_to_lark.sh

To include:

- Read validation_result.json
- Extract validator status
- Apply delivery decision logic
- Log decision path

---

### Required Logging

Each run must show:

- Control result (complete / incomplete)
- Validator result (PASS / WARN / FAIL)
- Final decision:
  - delivered
  - delivered_with_warning
  - blocked

---

### Success Criteria

- FAIL blocks Lark delivery
- PASS/WARN allows delivery
- Logs clearly show decision path
- No silent delivery
- No unvalidated output reaches Lark

---

### Current Status

→ READY FOR IMPLEMENTATION  
→ First execution task for next session  

━━━━━━━━━━━━━━━━━━━━━━

## Phase 6.3 — Evidence Traceability System (NEXT)

### Objective

Make every output claim traceable to:

- retrieval_package result_id
- query_id
- provider
- source URL

---

### Planned Capabilities

- Claim → source mapping
- Evidence indexing
- Debug trace reconstruction
- Operator audit capability

---

### Status

→ BLOCKED until 6.2 complete  

━━━━━━━━━━━━━━━━━━━━━━

## CURRENT SYSTEM STATE

System is now:

✔ Deterministic  
✔ Observable  
✔ Recoverable  
✔ Retrieval-bound  
✔ Evidence-validated (V1)  

But NOT yet:

✖ Delivery-gated by validation  
✖ Fully traceable  
✖ Fully normalized across languages  

---

## NEXT STEP (CRITICAL)

→ Implement Delivery Gate logic in run_light_to_lark.sh using validation_result.json

---

## FINAL PRINCIPLE

The system must deliver only when:

→ structurally valid  
AND  
→ evidentially grounded  

---

END