# OPENCLAW — MASTER DOCUMENT INDEX

---
document_id: OPENCLAW-MDI-001
version: v4.3
last_updated: 2026-05-14
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
- **CONSULTANT APPROVED** — reviewed and approved by consultant; awaiting operator approval before governing
- **ARCHIVED** — superseded; retained for history only

**Location key:**
- `[root]` — main project folder
- `governance/` — phase docs, design docs, standards
- `specs/` — locked system specs
- `advisory/` — advisory memos and operator replies
- `templates/` — blank templates
- `config/` — client configuration and VPS sync files
- `old/` — archived versions

---

## TIER 1 — TOP-LEVEL GOVERNANCE

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Master Document Index | OPENCLAW-MDI-001 | `00_Master_Document_Index.md` | [root] | ACTIVE | This document — navigable index of all system documents |
| System Constitution | OPENCLAW-CONST-001 | `00_System_Constitution.md` | [root] | GOVERNING | Canonical pipeline, principles, document hierarchy |
| CoWork Operating Protocol | OPENCLAW-OPS-001 | `OPENCLAW_COWORK_OPERATING_PROTOCOL.md` | [root] | LOCKED | Claude CoWork role, phase lock, analysis contract, hard safety rules |
| Phase 7 Detailed Execution Plan | — | `OpenClaw_Phase7_Execution_Plan.docx` | [root] | GOVERNING | Canonical Phase 7 roadmap — phase gates, Brain Lite scope, VPS model, pilot prerequisites (approved 2026-05-07) |
| Phase 7 Gate Checklist | OPENCLAW-P7-GATE-001 | `06_PHASE_GATE_CHECKLIST.md` | [root] | ACTIVE | Phase A/B/C/D gate tracking — trust runs, VPS setup, Brain Lite confirmation |
| Filename & Version Control Standard | OPENCLAW-SYS-FILENAME-002 | `governance/OPENCLAW-SYS-FILENAME-002_2026-05-13.md` | governance/ | GOVERNING | Approved filename convention, version control process, archive rules |
| Document Governance Protocol | OPENCLAW-DOC-GOV-001 | `governance/OPENCLAW-DOC-GOV-001_2026-05-14.md` | governance/ | LOCKED | Advisory note vs. system document boundary; advisory notes are reference only; system changes require explicit operator instruction |

---

## TIER 2 — SYSTEM ARCHITECTURE

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Foundation Document | OPENCLAW-FOUND-001 | `01_Foundation_Doc.md` | [root] | ACTIVE | System architecture, strategy, tolerance model, guarantees |
| Architecture Map | OPENCLAW-ARCH-001 | `specs/08_Architecture_Map.md` | specs/ | ACTIVE | Pipeline diagram, layer responsibilities, key runtime files |
| Architecture Philosophy | OPENCLAW-PHIL-001 | `specs/07_OpenClaw_Structure_Defense.md` | specs/ | REFERENCE | Layering strategy and design rationale |

---

## TIER 3 — LAYER SPECIFICATIONS

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Agent Input Contract | OPENCLAW-AIC-001 | `specs/09_Agent_Input_Contract.md` | specs/ | LOCKED | Agent input rules, locked output format, citation schema |
| Control Layer Spec | OPENCLAW-CLS-001 | `specs/10_Control_Layer_Spec.md` | specs/ | LOCKED | Structural completeness evaluation and delivery decision rules |
| Validator Layer Spec | OPENCLAW-VAL-001 | `specs/11_Validator_Layer_Spec.md` | specs/ | LOCKED | Evidence integrity verification, PASS/WARN/FAIL classification |
| Scrubber Layer Spec | OPENCLAW-SCR-001 | `specs/12_Scrubber_Layer_Spec.md` | specs/ | LOCKED | Deterministic citation cleanup, invalid ID removal |

---

## TIER 4 — RETRIEVAL SYSTEM

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Retrieval Failure Handling | OPENCLAW-FH-001 | `specs/SYS_RETRIEVAL_FAILURE_HANDLING.md` | specs/ | ACTIVE | Cross-layer failure model; contains Unified Failure Matrix |
| Retrieval Query Planning Rules | OPENCLAW-RQP-001 | `specs/SYS_Retrieval_Query_Planning_Rules.md` | specs/ | ACTIVE | Query design rules, provider alignment, time window policy |
| Retrieval Query Templates | OPENCLAW-RQT-001 | `specs/SYS_Retrieval_Query_Templates.md` | specs/ | ACTIVE | Live query bundle (6 queries) used in production |
| Retrieval Orchestrator Execution Plan | OPENCLAW-OEP-001 | `specs/SYS_Retrieval_orchestrator_Execution_plan.md` | specs/ | ACTIVE | Full execution sequence Steps 1–14, retrieval through delivery |

---

## TIER 5 — PHASE 7 GOVERNANCE

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Advisory Roadmap | OPENCLAW-ADV-002 | `advisory/OPENCLAW-ADV-002_2026-05-08.md` | advisory/ | REFERENCE | Phase 7 execution roadmap — reference only per DOC-GOV-001 |
| Brain Lite Implementation Design | OPENCLAW-BRAIN-LITE-DESIGN | `governance/OPENCLAW-BRAIN-LITE-DESIGN_2026-05-09.md` | governance/ | ACTIVE | Architecture, triggering model, failure model, injection point, digest budget |
| Brain Lite Run Summary Schema | OPENCLAW-BRAIN-LITE-SCHEMA-v1 | `governance/OPENCLAW-BRAIN-LITE-SCHEMA-v1_2026-05-09.md` | governance/ | LOCKED | 14-field locked run_summary schema; no fields may be added without operator approval |
| CoWork Daily Report Template | OPENCLAW-COWORK-REPORT-TEMPLATE | `governance/OPENCLAW-COWORK-REPORT-TEMPLATE_2026-05-09.md` | governance/ | REFERENCE | CoWork report format reference — superseded by OPS-001 Section 4 Analysis Contract as governing format |
| Multi-Client Test Harness Design | OPENCLAW-TEST-HARNESS-DESIGN | `governance/OPENCLAW-TEST-HARNESS-DESIGN_2026-05-09.md` | governance/ | ACTIVE | Test harness design for multi-client namespace isolation validation |
| Client Config Loader Spec | OPENCLAW-SPEC-CONFIG-LOADER-001 | `specs/OPENCLAW-SPEC-CONFIG-LOADER-001.md` | specs/ | OPERATOR APPROVED | Step 7 loader design — config loader, artifact namespacing, synthetic second client, isolation verification; operator approved 2026-05-18 |
| Document Versions Index | — | `governance/Document_Versions_Index.md` | governance/ | ACTIVE | Version history tracker for all core operational documents |

---

## TIER 6 — OPERATIONAL DOCUMENTS

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Issues Log | OPENCLAW-ISSUES-001 | `03_Issues_Log.md` | [root] | OPERATIONAL | Active and recently resolved issues; numbered cumulatively |
| Daily Status | — | `04_DAILY_STATUS.md` | [root] | OPERATIONAL | Current position, system health, next step; **single source of truth for active phase** |
| Client Config — china_monitor_001 | — | `config/client_config_china_monitor_001.yaml` | config/ | ACTIVE | Client configuration for china_monitor_001; brain_context=true (activated 2026-05-15) |
| VPS Sync Protocol | OPENCLAW-SYNC-001 | `config/VPS_SYNC_PROTOCOL.md` | config/ | ACTIVE | Session-start PowerShell scp block; CoWork local read pattern |

---

## TIER 7 — ADVISORY MEMOS

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Advisory Memo 002 | OPENCLAW-ADV-002 | `advisory/OPENCLAW-ADV-002_2026-05-08.md` | advisory/ | REFERENCE | Phase 7 roadmap — reference only per DOC-GOV-001 |
| Advisory Memo 003 | OPENCLAW-ADV-003 | `advisory/OPENCLAW-ADV-003_2026-05-09.md` | advisory/ | REFERENCE | Brain Lite options analysis |
| Operator Reply to ADV-003 | — | `advisory/OPENCLAW-REPLY-ADV-003_2026-05-09.md` | advisory/ | REFERENCE | Operator response selecting Option A for Brain Lite |
| Advisory Memo 004 | OPENCLAW-ADV-004 | `advisory/OPENCLAW-ADV-004_2026-05-11.md` | advisory/ | REFERENCE | Daily Status correction — Phase B steps confirmed complete |
| Advisory Memo 009 | OPENCLAW-ADV-009 | `advisory/OPENCLAW-ADV-009_2026-05-11.md` | advisory/ | REFERENCE | File organization system — convention captured in OPENCLAW-SYS-FILENAME-002; reference only per DOC-GOV-001 |
| Advisory Memo 010 | OPENCLAW-ADV-010 | `advisory/OPENCLAW-ADV-010_2026-05-11.md` | advisory/ | REFERENCE | Documentation improvement proposals — reference only per DOC-GOV-001 |
| Advisory Memo 012 | OPENCLAW-ADV-012 | `advisory/OPENCLAW-ADV-012_2026-05-14.md` | advisory/ | ACTIVE | Phase D — Editorial Quality & Product Transformation; operator-approved 2026-05-14 |

Next advisory memo: ADV-013

---

## TIER 8 — TEMPLATES

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Daily Status Template | OPENCLAW-TPL-001 | `templates/TPL_DAILY_STATUS_TEMPLATE.md` | templates/ | TEMPLATE | Blank template for producing daily status documents |

---

## TIER 9 — ARCHIVED

| Document | Original ID | Location | Note |
|----------|-------------|----------|------|
| System Audit (2026-05-01) | — | old/ | Point-in-time audit; superseded |
| Phase 6 Execution Plan | OPENCLAW-EXEC-001 | old/ | Superseded by Phase 7 Execution Plan (2026-05-07) |
| Advisory Memo 011 | OPENCLAW-ADV-011 | old/ | Targeted doc cleanup — 4 items implemented 2026-05-13; moved to old/ 2026-05-14 |
| All prior dated versions | — | old/ | Superseded versions; retained for history only. See governance/Document_Versions_Index.md |

---

## FILE NAMING CONVENTION

Per OPENCLAW-SYS-FILENAME-002 (approved 2026-05-13):

- **Live docs:** No date in filename; one active version per function; version tracked in frontmatter
- **Archives (/old/):** `NN_Name_vX.X_YYYY-MM-DD.md` — immutable
- **Advisory docs:** `OPENCLAW-ADV-NNN_YYYY-MM-DD.md` — immutable
- **Governance docs:** `[ID]_YYYY-MM-DD.md`
- **Config/technical:** Stable names, no date
- **Forbidden:** spaces, parentheses, commas, multiple dots in filename body

---

## INDEX MAINTENANCE RULE

This index must be updated whenever:
- A new document is created
- A document's status changes
- A document is renamed, versioned, or moved
- A document is moved to `old/`

Updates require operator approval per Hard Safety Rule R-01.

---

*OPENCLAW-MDI-001 | Version v4.5 | Last updated: 2026-05-18 | Status: ACTIVE*

*v4.5 changes (2026-05-18): OPENCLAW-SPEC-CONFIG-LOADER-001 status updated from CONSULTANT APPROVED to OPERATOR APPROVED (approved 2026-05-18).*

*v4.4 changes (2026-05-15): Client Config entry updated — brain_context=true (activated 2026-05-15).*

*v4.3 changes (2026-05-14): Remediation plan executed — CONSULTANT APPROVED status added to legend; Control Layer Spec and Architecture Philosophy filenames updated to .md; ADV-002, ADV-009, ADV-010 status updated to REFERENCE; ADV-011 moved to old/ and added to Tier 9.*

*v4.2 changes (2026-05-14): OPENCLAW-DOC-GOV-001 added to Tier 1 (locked 2026-05-14); ADV-012 added to Tier 7 (operator approved 2026-05-14).*

*v4.1 changes (2026-05-13): OPENCLAW-SPEC-CONFIG-LOADER-001 added to Tier 5 (consultant approved 2026-05-13; awaiting operator approval).*

*v4.0 changes (2026-05-13): Full migration to OPENCLAW-SYS-FILENAME-002 filename standard. All filenames updated to remove dates, spaces, and parentheses. OPENCLAW_COWORK_OPERATING_PROTOCOL.md renamed from 05_OPERATING_PROTOCOL. Tier 1 now references filename standard. VPS Sync Protocol added to Tier 6. Document Versions Index added to Tier 5. File Organization Convention section replaced with File Naming Convention per new standard.*
