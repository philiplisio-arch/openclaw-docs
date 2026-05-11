# OPENCLAW — MASTER DOCUMENT INDEX

---
document_id: OPENCLAW-MDI-001
version: 5.11.26
last_updated: 2026-05-11
status: ACTIVE
---

## PURPOSE

Single navigable index of all OpenClaw system documents. Defines status,
classification, purpose, filename, and location for each document. Only
documents listed as GOVERNING, LOCKED, or ACTIVE are authoritative.

**Status definitions:**
- **GOVERNING** — defines system behavior; authoritative
- **LOCKED** — governing and frozen; changes require explicit operator approval
- **ACTIVE** — governing and maintained; updated as system evolves
- **OPERATIONAL** — tracks current state; updated each session
- **TEMPLATE** — blank form for recurring documents
- **REFERENCE** — informational; not governing
- **ARCHIVED** — superseded; retained for history only

**Location key:**
- `[root]` — main project folder
- `governance/` — phase docs, design docs
- `specs/` — locked system specs
- `advisory/` — advisory memos and operator replies
- `templates/` — blank templates
- `config/` — client configuration files
- `old/` — archived versions

---

## TIER 1 — TOP-LEVEL GOVERNANCE

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Master Document Index | OPENCLAW-MDI-001 | `00_Master_Document_Index (5.3.26).md` | [root] | ACTIVE | This document — navigable index of all system documents |
| System Constitution | OPENCLAW-CONST-001 | `00_System_Constitution (5.3.26).md` | [root] | GOVERNING | Canonical pipeline, principles, document hierarchy |
| CoWork Operating Protocol | OPENCLAW-OPS-001 | `05_OPERATING_PROTOCOL (5.11.26).md` | [root] | LOCKED | Claude CoWork role, phase lock, analysis contract, hard safety rules |
| Phase 7 Detailed Execution Plan | — | `OpenClaw_Phase7_Execution_Plan.docx` | [root] | GOVERNING | Canonical Phase 7 roadmap — phase gates, Brain Lite scope, VPS model, pilot prerequisites (approved 2026-05-07) |
| Phase 7 Gate Checklist | OPENCLAW-P7-GATE-001 | `06_PHASE_GATE_CHECKLIST.md` | [root] | ACTIVE | Phase A/B/C/D gate tracking — trust runs, VPS setup, Brain Lite confirmation |
| Phase Exit Criteria | OPENCLAW-PEC-001 | `03_Phase_Exit_Criteria (5.6.26).md` | old/ | ACTIVE | Phase gate definitions and exit criteria for all phases |

---

## TIER 2 — SYSTEM ARCHITECTURE

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Foundation Document | OPENCLAW-FOUND-001 | `01_Foundation doc (5.5.26).md` | [root] | ACTIVE | System architecture, strategy, tolerance model, guarantees |
| Architecture Map | OPENCLAW-ARCH-001 | `08_Architecture_Map (5.3.26).md` | specs/ | ACTIVE | Pipeline diagram, layer responsibilities, key runtime files |
| Architecture Philosophy | OPENCLAW-PHIL-001 | `07_OpenClaw_Structure_Defense (5.3.26).txt` | specs/ | REFERENCE | Layering strategy and design rationale |
| Phase 6 Blueprint | OPENCLAW-BP-001 | `06_Phase 6 Blueprint (LOCKED 5.1.26).txt` | old/ | LOCKED | Phase structure, dependency order, core principles (architectural reference) |

---

## TIER 3 — LAYER SPECIFICATIONS

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Agent Input Contract | OPENCLAW-AIC-001 | `09_Agent_Input_Contract (LOCKED 5.5.26).md` | specs/ | LOCKED | Agent input rules, locked output format, citation schema |
| Control Layer Spec | OPENCLAW-CLS-001 | `10_Control_Layer_Spec (LOCKED 5.1.26).txt` | specs/ | LOCKED | Structural completeness evaluation and delivery decision rules |
| Validator Layer Spec | OPENCLAW-VAL-001 | `11_Validator_Layer_Spec (LOCKED 5.5.26).md` | specs/ | LOCKED | Evidence integrity verification, PASS/WARN/FAIL classification |
| Scrubber Layer Spec | OPENCLAW-SCR-001 | `12_Scrubber_Layer_Spec (LOCKED 5.1.26).md` | specs/ | LOCKED | Deterministic citation cleanup, invalid ID removal |

---

## TIER 4 — RETRIEVAL SYSTEM

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Retrieval Failure Handling | OPENCLAW-FH-001 | `SYS_RETRIEVAL_FAILURE_HANDLING (5.1.26).md` | specs/ | ACTIVE | Cross-layer failure model; contains Unified Failure Matrix |
| Retrieval Query Planning Rules | OPENCLAW-RQP-001 | `SYS_Retrieval_Query_Planning_Rules (5.1.26).md` | specs/ | ACTIVE | Query design rules, provider alignment, time window policy |
| Retrieval Query Templates | OPENCLAW-RQT-001 | `SYS_Retrieval_Query_Templates (5.1.26).md` | specs/ | ACTIVE | Live query bundle (6 queries) used in production |
| Retrieval Orchestrator Execution Plan | OPENCLAW-OEP-001 | `SYS_Retrieval_orchestrator_Execution_plan (5.1.26).md` | specs/ | ACTIVE | Full execution sequence Steps 1–14, retrieval through delivery |

---

## TIER 5 — PHASE 7 GOVERNANCE

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Advisory Roadmap | OPENCLAW-ADV-002 | `OPENCLAW-ADV-002 (5.8.26).md` | advisory/ | ACTIVE | Operator-approved Phase 7 execution roadmap — 10-step sequential plan (2026-05-08) |
| Brain Lite Implementation Design | OPENCLAW-BRAIN-LITE-DESIGN | `OPENCLAW-BRAIN-LITE-DESIGN (5.9.26).md` | governance/ | ACTIVE | Architecture, triggering model, failure model, injection point, digest budget |
| Brain Lite Run Summary Schema | OPENCLAW-BRAIN-LITE-SCHEMA-v1 | `OPENCLAW-BRAIN-LITE-SCHEMA-v1 (5.9.26).md` | governance/ | LOCKED | 14-field locked run_summary schema; no fields may be added without operator approval |
| CoWork Daily Report Template | OPENCLAW-COWORK-REPORT-TEMPLATE | `OPENCLAW-COWORK-REPORT-TEMPLATE (5.9.26).md` | governance/ | ACTIVE | 11-field CoWork daily report format |
| Multi-Client Test Harness Design | OPENCLAW-TEST-HARNESS-DESIGN | `OPENCLAW-TEST-HARNESS-DESIGN (5.9.26).md` | governance/ | ACTIVE | Test harness design for multi-client namespace isolation validation |

---

## TIER 6 — OPERATIONAL DOCUMENTS

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Issues Log | OPENCLAW-ISSUES-001 | `03_Issues Log (5.11.26).md` | [root] | OPERATIONAL | Active and recently resolved issues; numbered cumulatively |
| Daily Status | — | `04_DAILY_STATUS (5.11.26).md` | [root] | OPERATIONAL | Current position, system health, next step; **single source of truth for active phase** |
| Client Config — china_monitor_001 | — | `client_config_china_monitor_001.yaml` | config/ | ACTIVE | Client configuration for china_monitor_001; brain_context=false (dormant) |

---

## TIER 7 — ADVISORY MEMOS

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Advisory Memo 002 | OPENCLAW-ADV-002 | `OPENCLAW-ADV-002 (5.8.26).md` | advisory/ | ACTIVE | Phase 7 roadmap (see Tier 5) |
| Advisory Memo 003 | OPENCLAW-ADV-003 | `OPENCLAW-ADV-003 (5.9.26).md` | advisory/ | REFERENCE | Brain Lite options analysis |
| Operator Reply to ADV-003 | — | `OPENCLAW-REPLY-ADV-003 (5.9.26).md` | advisory/ | REFERENCE | Operator response selecting Option A for Brain Lite |
| Advisory Memo 004 | OPENCLAW-ADV-004 | `OPENCLAW-ADV-004 (5.11.26).md` | advisory/ | REFERENCE | Daily Status correction — Phase B steps confirmed complete |
| Advisory Memo 009 | OPENCLAW-ADV-009 | `OPENCLAW-ADV-009 (5.11.26).md` | advisory/ | ACTIVE | File organization system — approved convention (2026-05-11) |

---

## TIER 8 — TEMPLATES

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Daily Status Template | OPENCLAW-TPL-001 | `TPL_OPENCLAW PROJECT — DAILY STATUS TEMPLATE (5.3.26).md` | templates/ | TEMPLATE | Blank template for producing daily status documents |

---

## TIER 9 — ARCHIVED

| Document | Original ID | Location | Note |
|----------|-------------|----------|------|
| System Audit (2026-05-01) | — | old/ | Point-in-time audit; superseded |
| Phase 6 Execution Plan | OPENCLAW-EXEC-001 | old/ | Superseded by Phase 7 Execution Plan (2026-05-07) |
| All dated prior versions | — | old/ | Superseded versions; retained for history only |

---

## FILE ORGANIZATION CONVENTION

Per OPENCLAW-ADV-009 (approved 2026-05-11):

- **[root]:** Session-start operational docs and permanent anchors only (00_, 01_, 03_, 04_, 05_, 06_ prefixes)
- **governance/:** OPENCLAW- prefix; formal document IDs retained inside files
- **specs/:** Locked system specs; existing legacy names retained; new specs require OPENCLAW-SPEC naming
- **advisory/:** OPENCLAW-ADV-NNN sequential; next memo ADV-010
- **templates/:** TPL_ prefix
- **config/:** Client YAML configuration files
- **old/:** Append-only archive; nothing deleted

---

## INDEX MAINTENANCE RULE

This index must be updated whenever:
- A new document is created
- A document's status changes
- A document is renamed, versioned, or moved
- A document is moved to `old/`

Updates require operator approval per Hard Safety Rule R-01.

---

*OPENCLAW-MDI-001 | Version 5.11.26 | Last updated: 2026-05-11 | Status: ACTIVE*

*5.11.26 changes: Added filename/location columns to all tiers per ADV-009 condition 2;
added Brain Lite Design, Schema, CoWork Report Template, Test Harness Design to Tier 5;
added ADV-003, ADV-004, ADV-009, client_config, Gate Checklist to index;
updated Operating Protocol filename to 05_OPERATING_PROTOCOL;
updated Gate Checklist filename to 06_PHASE_GATE_CHECKLIST;
added Tier 8 Templates, Tier 9 Archived; added File Organization Convention section.*
