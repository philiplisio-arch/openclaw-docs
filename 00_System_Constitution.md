# OPENCLAW — SYSTEM CONSTITUTION

---
document_id: OPENCLAW-CONST-001
version: 5.3.26a
last_updated: 2026-05-03
status: GOVERNING — highest authority document in the corpus
---

## PURPOSE

This document is the single onboarding and reference point for the OpenClaw system. It defines the canonical pipeline, document authority hierarchy, and non-negotiable system principles. In any conflict between documents, this document and the Daily Status govern.

---

## ACTIVE PHASE

**→ The Daily Status document is the single source of truth for the current active phase.**

All other documents must reflect the Daily Status on matters of phase. In any conflict, Daily Status governs.

---

## CANONICAL PIPELINE

```
Trigger (cron / webhook)
→ Retrieval Layer       [Brave + Baidu]
→ Orchestrator          [normalize, dedup, filter, package]
→ Agent (LLM)           [signal generation, locked citation selection]
→ Scrubber              [deterministic citation cleanup]
→ Control Layer         [structural completeness check]
→ Validator             [evidence integrity check — PASS / WARN / FAIL]
→ Delivery Gate         [sole and final delivery authority]
→ Lark
```

Claude CoWork operates **outside and after** this pipeline. It reads artifacts and produces analysis. It does not execute, modify, or influence any pipeline step.

---

## NON-NEGOTIABLE SYSTEM PRINCIPLES

These principles may not be waived, overridden, or reinterpreted by any document, session, or instruction.

| # | Principle |
|---|-----------|
| P-01 | No unverified output reaches the client |
| P-02 | No silent failure — every failure is explicit, structured, and logged |
| P-03 | No fabricated citations — all delivered result_ids map to retained retrieval results |
| P-04 | Retrieval is complete before reasoning begins |
| P-05 | The pipeline is deterministic — non-deterministic layers operate outside it |
| P-06 | No phase may advance without explicit operator approval |
| P-07 | No document may be updated without explicit operator approval |
| P-08 | The Delivery Gate is the sole and final authority on whether output is delivered |
| P-09 | result_id matching is the primary validation mechanism — publisher/URL checks are secondary |
| P-10 | Observe and explain before adjusting — no change without a confirmed loss point |

---

## DOCUMENT AUTHORITY HIERARCHY

When documents conflict, authority is resolved in this order:

| Rank | Document | Governs |
|------|----------|---------|
| 1 | This document (OPENCLAW-CONST-001) | System principles and pipeline |
| 2 | Daily Status | Active phase (single source of truth) |
| 3 | CoWork Operating Protocol (OPENCLAW-OPS-001) | Claude CoWork governance and phase lock |
| 4 | Phase Exit Criteria (OPENCLAW-PEC-001) | Phase gate definitions |
| 5 | Layer Specs (09–12, SYS docs) | Technical behavior per layer |
| 6 | Execution Plan | Active work and methodology |
| 7 | Reference docs (Blueprint, Philosophy, Architecture Map) | Reference only — not governing |

---

## CANONICAL FAILURE MODEL

The **Unified Failure Matrix** in `SYS_RETRIEVAL_FAILURE_HANDLING` is the canonical reference for all cross-layer failure scenarios. All layer specs defer to it. In any ambiguity about failure behavior, the matrix governs.

---

## CLAUDE COWORK CONSTRAINTS

Claude CoWork is authorized to perform exactly three categories of action:

| Category | Permitted |
|----------|-----------|
| Interpret | Read artifacts, analyze outputs, identify anomalies |
| Recommend | Propose next steps within current phase scope |
| Document | Draft updates for operator review and approval |

No other category of action is authorized. Claude CoWork does not execute, modify, or influence any pipeline component.

---

## MASTER DOCUMENT INDEX

See `00_Master_Document_Index.md` for the full index of all active, locked, template, reference, and archived documents.

---

*OPENCLAW-CONST-001 | Version 5.3.26a | Created: 2026-05-03 | Status: GOVERNING*
