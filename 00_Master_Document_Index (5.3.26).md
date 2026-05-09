# OPENCLAW — MASTER DOCUMENT INDEX

---
document_id: OPENCLAW-MDI-001
version: 5.8.26a
last_updated: 2026-05-08
status: ACTIVE
---

## PURPOSE

Single navigable index of all OpenClaw system documents. Defines status, classification, and purpose for each document. Only documents listed as ACTIVE or LOCKED are governing. All others are reference, template, or archived.

**Status definitions:**
- **GOVERNING** — defines system behavior; authoritative
- **LOCKED** — governing and frozen; changes require explicit operator approval
- **ACTIVE** — governing and maintained; updated as system evolves
- **OPERATIONAL** — tracks current state; updated each session
- **TEMPLATE** — blank form for recurring documents
- **REFERENCE** — informational; not governing
- **ARCHIVED** — superseded; retained for history only

---

## TIER 1 — TOP-LEVEL GOVERNANCE

| Document | ID | Status | Purpose |
|----------|----|--------|---------|
| System Constitution | OPENCLAW-CONST-001 | GOVERNING | Canonical pipeline, principles, document hierarchy |
| CoWork Operating Protocol | OPENCLAW-OPS-001 | LOCKED | Claude CoWork role, phase lock, analysis contract, hard safety rules |
| Phase 7 Detailed Execution Plan | — | GOVERNING | Canonical Phase 7 roadmap — phase gates, Brain Lite scope, VPS model, pilot prerequisites (approved 2026-05-07) |
| Phase Exit Criteria | OPENCLAW-PEC-001 | ACTIVE | Phase gate definitions and exit criteria for all phases |

---

## TIER 2 — SYSTEM ARCHITECTURE

| Document | ID | Status | Purpose |
|----------|----|--------|---------|
| Foundation Document | OPENCLAW-FOUND-001 | ACTIVE | System architecture, strategy, tolerance model, guarantees |
| Phase 6 Blueprint | OPENCLAW-BP-001 | LOCKED | Phase structure, dependency order, core principles (architectural reference) |
| Architecture Philosophy | OPENCLAW-PHIL-001 | REFERENCE | Layering strategy and design rationale |
| Architecture Map | OPENCLAW-ARCH-001 | ACTIVE | Pipeline diagram, layer responsibilities, key runtime files |

---

## TIER 3 — LAYER SPECIFICATIONS

| Document | ID | Status | Purpose |
|----------|----|--------|---------|
| Agent Input Contract | OPENCLAW-AIC-001 | LOCKED | Agent input rules, locked output format, citation schema |
| Control Layer Spec | OPENCLAW-CLS-001 | LOCKED | Structural completeness evaluation and delivery decision rules |
| Validator Layer Spec | OPENCLAW-VAL-001 | LOCKED | Evidence integrity verification, PASS/WARN/FAIL classification |
| Scrubber Layer Spec | OPENCLAW-SCR-001 | LOCKED | Deterministic citation cleanup, invalid ID removal |

---

## TIER 4 — RETRIEVAL SYSTEM

| Document | ID | Status | Purpose |
|----------|----|--------|---------|
| Retrieval Failure Handling | OPENCLAW-FH-001 | ACTIVE | Cross-layer failure model; contains Unified Failure Matrix |
| Retrieval Query Planning Rules | OPENCLAW-RQP-001 | ACTIVE | Query design rules, provider alignment, time window policy |
| Retrieval Query Templates | OPENCLAW-RQT-001 | ACTIVE | Live query bundle (6 queries) used in production |
| Retrieval Orchestrator Execution Plan | OPENCLAW-OEP-001 | ACTIVE | Full execution sequence Steps 1–14, retrieval through delivery |

---

## TIER 5 — OPERATIONAL DOCUMENTS

| Document | ID | Status | Purpose |
|----------|----|--------|---------|
| Advisory Roadmap | OPENCLAW-ADV-002 | ACTIVE | Operator-approved Phase 7 execution roadmap — 10-step sequential plan for solo operator (2026-05-08) |
| Phase 7 Gate Checklist | OPENCLAW-P7-GATE-001 | ACTIVE | Phase A/B/C gate tracking — trust run count, VPS setup, Brain Lite confirmation (pending creation) |
| Issues Log | OPENCLAW-ISSUES-001 | ACTIVE | Active and recently resolved issues; numbered cumulatively |
| Daily Status | — | OPERATIONAL | Current position, system health, next step; **single source of truth for active phase** |
| Session Handover | — | OPERATIONAL | Session continuity document; produced at end of each session |

---

## TIER 6 — TEMPLATES

| Document | ID | Status | Purpose |
|----------|----|--------|---------|
| Daily Status Template | OPENCLAW-TPL-001 | TEMPLATE | Blank template for producing daily status documents |

---

## TIER 7 — ARCHIVED

| Document | Original ID | Status | Note |
|----------|-------------|--------|------|
| System Audit (2026-05-01) | — | ARCHIVED | Point-in-time audit; superseded by 2026-05-03 audit |
| Phase 6 Execution Plan | OPENCLAW-EXEC-001 | ARCHIVED | Superseded by Phase 7 Execution Plan (approved 2026-05-07) |
| All documents in `/old/` | — | ARCHIVED | Superseded versions; retained for history |

---

## INDEX MAINTENANCE RULE

This index must be updated whenever:
- A new document is created
- A document's status changes (e.g., ACTIVE → ARCHIVED)
- A document is renamed or versioned
- A document is moved to `/old/`

Updates require operator approval per Hard Safety Rule R-01.

---

*OPENCLAW-MDI-001 | Version 5.8.26a | Created: 2026-05-03 | Last updated: 2026-05-08 | Status: ACTIVE*

*5.8.26a changes: Phase 7 Execution Plan added to Tier 1; OPENCLAW-ADV-002 and OPENCLAW-P7-GATE-001 added to Tier 5; Phase 6 Execution Plan moved to Tier 7 Archived; Phase Exit Criteria description updated.*
