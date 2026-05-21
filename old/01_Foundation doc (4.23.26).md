# OPENCLAW — FOUNDATION DOCUMENT

## System Purpose
OpenClaw is a China-focused PR intelligence system that produces a daily monitoring brief for multinational audiences.

Primary output:
- Lark-delivered “China Monitoring Brief”
- Structured into:
  - EXECUTIVE TAKE
  - ADVISORY LAYER
  - Regional sections (US / Europe / Middle East)

---

## Core Architecture

Trigger → Retrieval → Orchestrator → Agent → Relay → Lark

Strict boundaries:
- Retrieval happens outside the agent
- Agent consumes structured input only
- No direct API → prompt injection
- Control layer governs execution and delivery

---

## System Principles

### 1. Deterministic Pipeline
Each stage must produce observable outputs and logs.

### 2. Separation of Concerns
- Retrieval = data gathering
- Agent = reasoning and synthesis
- Wrapper = control + delivery

---

### 3. Control Layer Principle (UPDATED)

The system must distinguish between:
- execution failure
- output validity

Non-zero process exit codes do NOT automatically imply invalid output.

The control layer must:
1. Evaluate structural output completeness
2. Allow recovery when output is valid
3. Prevent suppression of usable results

---

### 4. Observability First
Every run must expose:
- what executed
- what succeeded/failed
- what was delivered

---

## Output Requirements

Agent must produce:
- EXECUTIVE TAKE (2–3 bullets)
- ADVISORY LAYER (3–5 bullets)
- Region sections
- Evidence-based sourcing

---

## Current Status

Phase 4: COMPLETE (Control & Stability)  
Phase 5.6: COMPLETE (Execution Stabilization)

System is now:
- stable
- observable
- recoverable
- delivering verified outputs to Lark