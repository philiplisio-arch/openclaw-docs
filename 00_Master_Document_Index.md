# OPENCLAW — MASTER DOCUMENT INDEX

---
document_id: OPENCLAW-MDI-001
version: v5.0
last_updated: 2026-05-21
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
- **OPERATOR APPROVED** — explicitly approved by the operator for use or implementation; governing force depends on document class and location
- **ARCHIVED** — superseded; retained for history only

**Location key:**
- `[root]` — main project folder
- `governance/` — phase docs, design docs, standards
- `specs/` — locked system specs
- `advisory/` — advisory memos and operator replies
- `templates/` — blank templates
- `config/` — client configuration and VPS sync files
- `old/` — archived versions
- `phase_d/` — Phase D controlled pilot operational documents

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
| Client Config — test_client_002 | — | `config/client_config_test_client_002.yaml` | config/ | ACTIVE | Synthetic test client config; pilot_mode=true, brain_context=false, query_template_set=china_monitor_v1; deployed VPS 2026-05-20 |
| VPS Sync Protocol | OPENCLAW-SYNC-001 | `config/VPS_SYNC_PROTOCOL.md` | config/ | ACTIVE | Session-start PowerShell scp block; CoWork local read pattern |
| Phase D Feedback Register | — | `phase_d/OPENCLAW_PHASE_D_FEEDBACK_REGISTER.md` | phase_d/ | OPERATIONAL | Cumulative append-only log of all operator/client feedback; classifies feedback categories A–E per ADV-012 |
| Phase D Content Scorecard | — | `phase_d/OPENCLAW_PHASE_D_CONTENT_SCORECARD.md` | phase_d/ | OPERATIONAL | Per-delivery scoring across 10 dimensions; tracks rolling averages toward Phase D gate threshold |
| Phase D Operator Review Procedure | OPENCLAW-PHASE-D-ORP-001 | `phase_d/OPENCLAW_PHASE_D_OPERATOR_REVIEW_PROCEDURE.md` | phase_d/ | ACTIVE | Standard post-delivery review prompt, CoWork output format, feedback ID convention, severity scale, disposition rules, and change packet threshold |
| Change Packet 001 — Brain Lite Validation Path | OPENCLAW-D-CP-001 | `phase_d/OPENCLAW_PHASE_D_CP_001_brain_lite_validation_path.md` | phase_d/ | IMPLEMENTED | Brain Lite get_validator_metrics() namespace path fix; resolves T-10 regression; validation pending 2026-05-22 cron |
| Change Packet 002 — Content Specificity | OPENCLAW-D-CP-002 | `phase_d/OPENCLAW_PHASE_D_CP_002_content_specificity.md` | phase_d/ | IMPLEMENTED | ET/AL specificity requirements (dollar amounts, named entities, dates); addresses D-FB-001 F-02/F-03; validation pending |
| Change Packet 003 — LinkedIn Draft Format | OPENCLAW-D-CP-003 | `phase_d/OPENCLAW_PHASE_D_CP_003_linkedin_format.md` | phase_d/ | IMPLEMENTED | LinkedIn Draft instruction rewrite — specific, historically grounded, single-story; addresses D-FB-001 F-05 and T-07; validation pending |
| Change Packet 004 — Source Provenance Labelling | OPENCLAW-D-CP-004 | `phase_d/OPENCLAW_PHASE_D_CP_004_source_provenance.md` | phase_d/ | IMPLEMENTED | [CN]/[INTL]/[CN+INTL] provenance tags per ET/AL bullet; addresses D-FB-001 F-06; validation pending |

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
| Strategic Vision Memo | — | `advisory/OPENCLAW_Strategic_Vision_Memo_2026-05-15.md` | advisory/ | REFERENCE | Long-term product vision — AE exoskeleton, five-layer architecture, query layer, corpus/entity model; speculative discussion only |
| Strategic Recap Memo | OPENCLAW-RECAP-001 | `advisory/OPENCLAW_Strategic_Recap_Memo_2026-05-18.md` | advisory/ | REFERENCE | Phase-by-phase project history and forward roadmap; operator-reviewed 2026-05-18; reference only |
| Strategy Memo (external) | — | `advisory/Strategy Memo 6.8.26.txt` | advisory/ | REFERENCE | External strategy discussion document; reference only |

Next advisory memo: ADV-013

---

## TIER 8 — TEMPLATES

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Daily Status Template | OPENCLAW-TPL-001 | `templates/TPL_DAILY_STATUS_TEMPLATE.md` | templates/ | TEMPLATE | Blank template for producing daily status documents |
| Phase D Content Change Packet Template | — | `phase_d/OPENCLAW_PHASE_D_CHANGE_PACKET_TEMPLATE.md` | phase_d/ | TEMPLATE | Blank form for proposing content changes; requires recurrence evidence, single-layer scope, rollback plan, and operator approval before implementation |

---

## TIER 9 — OTHER REFERENCE

| Document | Document ID | Filename | Location | Status | Purpose |
|----------|-------------|----------|----------|--------|---------|
| Isolation Verification Script | — | `other_ref/verify_isolation.py` | other_ref/ | REFERENCE | Multi-client namespace isolation test harness; implements OPENCLAW-TEST-HARNESS-DESIGN v1.1; production copy lives at /root/ on VPS |

---

## TIER 10 — ARCHIVED

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

*OPENCLAW-MDI-001 | Version v5.0 | Last updated: 2026-05-21 | Status: ACTIVE*

*v5.0 changes (2026-05-21): Four Phase D Change Packets added to Tier 6 — CP-001 (Brain Lite validation path fix, OPENCLAW-D-CP-001), CP-002 (content specificity, OPENCLAW-D-CP-002), CP-003 (LinkedIn Draft format, OPENCLAW-D-CP-003), CP-004 (source provenance labelling, OPENCLAW-D-CP-004). All status: IMPLEMENTED; validation pending 2026-05-22 cron run. IMPLEMENTED added to status definitions. "IMPLEMENTED" status: change packet applied to VPS; awaiting validation runs.*

*v4.9 changes (2026-05-20): Root folder cleanup — three strategic memo files moved from [root] to advisory/ (REFERENCE status); verify_isolation.py moved from [root] to other_ref/. Tier 9 (Other Reference) added. Former Tier 9 (Archived) renumbered to Tier 10. Strategy Memo 6.8.26.txt noted as filename convention exception (spaces) — operator to rename if desired.*

*v4.8 changes (2026-05-20): Phase D Operator Review Procedure (OPENCLAW-PHASE-D-ORP-001) added to Tier 6. Feedback Register updated to v1.2; Scorecard updated to v1.2 (cross-references to procedure document added).*

*v4.7 changes (2026-05-20): phase_d/ added to location key. Phase D Feedback Register and Content Scorecard added to Tier 6 (OPERATIONAL). Phase D Content Change Packet Template added to Tier 8 (TEMPLATE).