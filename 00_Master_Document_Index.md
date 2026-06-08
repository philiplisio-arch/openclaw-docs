# OPENCLAW — MASTER DOCUMENT INDEX

---
document_id: OPENCLAW-MDI-001
version: v5.4
last_updated: 2026-06-08
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
| Claude Code Operating Protocol | OPENCLAW-CC-OPS-001 | `OPENCLAW_CLAUDE_CODE_OPERATING_PROTOCOL.md` | [root] | LOCKED | Claude Code role as primary VPS operating desk; authorized actions; document update protocol; session-close checklist; hard safety rules |
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
| VPS Sync Protocol | OPENCLAW-SYNC-001 | `config/VPS_SYNC_PROTOCOL.md` | config/ | ACTIVE | Session-start PowerShell scp block; review source matrix (GitHub vs SCP); CoWork local read pattern |
| Phase D Feedback Register | — | `phase_d/OPENCLAW_PHASE_D_FEEDBACK_REGISTER.md` | phase_d/ | OPERATIONAL | Cumulative append-only log of all operator/client feedback; classifies feedback categories A–E per ADV-012 |
| Phase D Content Scorecard | — | `phase_d/OPENCLAW_PHASE_D_CONTENT_SCORECARD.md` | phase_d/ | OPERATIONAL | Per-delivery scoring across 10 dimensions; tracks rolling averages toward Phase D gate threshold |
| Phase D Operator Review Procedure | OPENCLAW-PHASE-D-ORP-001 | `phase_d/OPENCLAW_PHASE_D_OPERATOR_REVIEW_PROCEDURE.md` | phase_d/ | ACTIVE | Standard post-delivery review prompt, CoWork output format, feedback ID convention, severity scale, disposition rules, and change packet threshold |
| Change Packet 001 — Brain Lite Validation Path | OPENCLAW-D-CP-001 | `phase_d/OPENCLAW_PHASE_D_CP_001_brain_lite_validation_path.md` | phase_d/ | IMPLEMENTED | Brain Lite get_validator_metrics() namespace path fix; resolves T-10 regression; validation pending 2026-05-22 cron |
| Change Packet 002 — Content Specificity | OPENCLAW-D-CP-002 | `phase_d/OPENCLAW_PHASE_D_CP_002_content_specificity.md` | phase_d/ | IMPLEMENTED | ET/AL specificity requirements (dollar amounts, named entities, dates); addresses D-FB-001 F-02/F-03; validation pending |
| Change Packet 003 — LinkedIn Draft Format | OPENCLAW-D-CP-003 | `phase_d/OPENCLAW_PHASE_D_CP_003_linkedin_format.md` | phase_d/ | IMPLEMENTED | LinkedIn Draft instruction rewrite — specific, historically grounded, single-story; addresses D-FB-001 F-05 and T-07; validation pending |
| Change Packet 004 — Source Provenance Labelling | OPENCLAW-D-CP-004 | `phase_d/OPENCLAW_PHASE_D_CP_004_source_provenance.md` | phase_d/ | CONFIRMED | [CN]/[INTL]/[CN+INTL] provenance tags per ET/AL bullet; confirmed working D2 onward |
| Change Packet 005 — Brain Lite Validator Status | OPENCLAW-D-CP-005 | `phase_d/OPENCLAW_PHASE_D_CP_005_brain_lite_validator_status.md` | phase_d/ | CONFIRMED | Brain Lite validator_status field; T-10 fully resolved; confirmed D3 and D4 |
| Change Packet 006 — Baidu-Only ALJ Client | OPENCLAW-D-CP-006 | `phase_d/OPENCLAW_PHASE_D_CP_006_baidu_only_alj_client.md` | phase_d/ | IMPLEMENTED | Baidu-only retrieval for alj_china_auto_001; 3-file change; validates on first ALJ pilot run |
| Change Packet 007 — Freshness + Topic Differentiation | OPENCLAW-D-CP-007 | `phase_d/OPENCLAW_PHASE_D_CP_007_freshness_topic_nonrepetition.md` | phase_d/ | PARTIAL | FRESHNESS RULE + TOPIC DIFFERENTIATION RULE in system_rules; agent-side only; same macro clusters persist (D-FB-004 Part B pending) |
| Change Packet 008 — Validated Sources Appendix | OPENCLAW-D-CP-008 | `phase_d/OPENCLAW_PHASE_D_CP_008_validated_sources_appendix.md` | phase_d/ | CONFIRMED | SOURCES section in citation_sub.py; publisher\|date\|url; confirmed D4 (7 entries with URLs) |
| Change Packet 009 — ALJ Output Format | OPENCLAW-D-CP-009 | `phase_d/OPENCLAW_PHASE_D_CP_009_alj_output_format.md` | phase_d/ | CONFIRMED | ALJ-specific 8-section output format + Complete Chinese Source Appendix; deployed 2026-05-24; ALJ pilot validates |
| Change Packet 010 — Unified SOURCES Footer | OPENCLAW-D-CP-010 | `phase_d/OPENCLAW_PHASE_D_CP_010_unified_sources_footer.md` | phase_d/ | IMPLEMENTED | title\|publisher\|date\|url in SOURCES; agent geographic footer suppressed; confirms 2026-05-25 cron |
| Change Packet 011 — Client-Aware Baidu Freshness | OPENCLAW-D-CP-011 | `phase_d/OPENCLAW_PHASE_D_CP_011_alj_baidu_freshness.md` | phase_d/ | CONFIRMED | ALJ=168h, WS1=48h; filter_results.py; deployed 2026-05-24; smoke test confirms WS1 unchanged |
| Change Packet 012 — Template-Aware Shell Heuristics | OPENCLAW-D-CP-012 | `phase_d/OPENCLAW_PHASE_D_CP_012_template_aware_shell.md` | phase_d/ | CONFIRMED | run_light_to_lark.sh case block; completeness heuristic/gate/awk/title parameterized; ALJ pilot validates |
| Change Packet 013 — Scrubber Template-ization | OPENCLAW-D-CP-013 | `phase_d/OPENCLAW_PHASE_D_CP_013_scrubber_template_aware.md` | phase_d/ | CONFIRMED | scrub_result_ids.py SECTION 1–8 headers + REQUIRED_CITED_SECTION; 3 amendments; ALJ replay: ids_kept=15/15, exit 0 |
| Change Packet 014 — Scrubber Failure Logging | OPENCLAW-D-CP-014 | `phase_d/OPENCLAW_PHASE_D_CP_014_scrubber_logging.md` | phase_d/ | CONFIRMED | Scrubber stdout tee to RUN_LOG; pipefail guard; PIPESTATUS; ALJ pilot confirms real reason visible |
| Change Packet 015 — SIGNAL Block Template-ization | OPENCLAW-D-CP-015 | (not yet drafted) | phase_d/ | PENDING | Skip/template-ize WS1 SIGNAL block (US/EU/ME) for ALJ; Issue #55; needed before ALJ live delivery |
| Change Packet 016 — Lark Per-Client Routing | OPENCLAW-D-CP-016 | (not yet saved) | phase_d/ | DRAFT | Shell-side document_id plumbing; OPENCLAW_CREDENTIALS_REF becomes load-bearing; awaiting ALJ Lark doc_id |
| Change Packet 017 — LAST_HASH_FILE Namespace | OPENCLAW-D-CP-017 | (not yet drafted) | phase_d/ | PENDING | Namespace last_delivery_hash.txt per client; one-line fix; Issue #57; bundle with CP-016 |
| Change Packet 018 — Brain Lite Digest Auto-Rebuild | OPENCLAW-D-CP-018 | `phase_d/OPENCLAW_PHASE_D_CP_018_digest_auto_rebuild.md` | phase_d/ | IMPLEMENTED | Auto-rebuild digest after each successful run; lines 371–381 run_light_to_lark.sh; bash -n exit 0; validation pending D9 |
| Change Packet 019 — Geographic Footer Suppression | OPENCLAW-D-CP-019 | `phase_d/OPENCLAW_PHASE_D_CP_019_geographic_footer_suppression.md` | phase_d/ | IMPLEMENTED | SOURCES SECTION RULE replaced lines 193–210 build_agent_input_slim.py; py_compile exit 0; validation pending D9; Issue #58 |
| Change Packet 020 — Source Taxonomy + Freshness Labels | OPENCLAW-D-CP-020 | `phase_d/OPENCLAW_PHASE_D_CP_020_source_taxonomy_freshness_labels.md` | phase_d/ | APPROVED | Shared source-label schema (CN-OFFICIAL/CN-STATE/CN-BUSINESS etc.) and freshness labels (NEW-24H/FOLLOW-UP-48H etc.); WS1 live; ALJ held/pre-live only; Tier 1 |
| Change Packet 021 — Source-First Output Restructuring | OPENCLAW-D-CP-021 | `phase_d/OPENCLAW_PHASE_D_CP_021_source_first_output_restructuring.md` | phase_d/ | APPROVED | Replace ET/AL/LinkedIn with 6-section source-first format; LinkedIn suppressed; gate streak restarts on first live delivery; 2 held-mode runs required; Tier 2 |
| Change Packet 022A — Query Family Held-Mode Dry Run | OPENCLAW-D-CP-022A | `phase_d/OPENCLAW_PHASE_D_CP_022A_query_family_dry_run.md` | phase_d/ | APPROVED | WS1 expanded query families tested in held mode only; gates CP-022 live; Tier 2B |
| Change Packet 022 — WS1 Query Family Expansion | OPENCLAW-D-CP-022 | `phase_d/OPENCLAW_PHASE_D_CP_022_ws1_query_family_expansion.md` | phase_d/ | APPROVED | Seven named WS1 query families live deployment; blocked on CP-022A + Browser Phase 1 findings; Tier 3 |
| Change Packet 023 — ALJ Query Family Expansion | OPENCLAW-D-CP-023 | `phase_d/OPENCLAW_PHASE_D_CP_023_alj_query_family_expansion.md` | phase_d/ | APPROVED | Eight ALJ query families; blocked on ALJ pre-live blockers + 1 baseline held run; Tier 4 |
| Change Packet 024 — Source Appendix Upgrade | OPENCLAW-D-CP-024 | `phase_d/OPENCLAW_PHASE_D_CP_024_source_appendix_upgrade.md` | phase_d/ | APPROVED | Adds source_category + freshness_label to SOURCES appendix; deterministic labeling; blocked on CP-020; Tier 2C |

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
| Advisory Memo 013 — Signal-Widening Strategy | OPENCLAW-ADV-013 | `advisory/Strategy Memo 6.8.26.txt` | advisory/ | REFERENCE | Best-in-class strategy for widening China-based signal in ALJ monitoring and core China report; prepared 2026-05-24; approved direction 2026-05-28 |
| Advisory Memo 013 Consultant Review | OPENCLAW-ADV-013-REVIEW | `advisory/OPENCLAW-ADV-013-REVIEW_2026-05-28.md` | advisory/ | REFERENCE | Consultant review of operator response; 8 targeted revisions recommended; incorporated into final response |
| Advisory Memo 013 Operator Response (Revised) | OPENCLAW-ADV-013-RESPONSE | `advisory/OPENCLAW-ADV-013-RESPONSE_2026-05-28.md` | advisory/ | OPERATOR APPROVED | Approved operator response to signal-widening advisory; tiered plan CP-020 through CP-024 + CP-022A; four decisions resolved; operator approved 2026-05-28 |
| Advisory Memo 014 — Source Authority Filter | OPENCLAW-ADV-014 | `advisory/OPENCLAW-ADV-014_2026-06-06.md` | advisory/ | OPERATOR APPROVED | Domain exclusion list + snippet quality floor; Layer 1 deployed; Layer 2 approved (threshold 80, warn-only, keyword gate); addresses D-FB-007/D-FB-008 |
| Advisory Memo 015 — Semantic Validation Gap | OPENCLAW-ADV-015 | `advisory/OPENCLAW-ADV-015_2026-06-06.md` | advisory/ | OPERATOR APPROVED | Validator GREEN ≠ semantic grounding; Option D spot-check added to review procedure; Option B spec pending; fabrication rate language corrected |
| Advisory Memo 016 — Raw Retrieval Logging | OPENCLAW-ADV-016 | `advisory/OPENCLAW-ADV-016_2026-06-06.md` | advisory/ | OPERATOR APPROVED | Per-run immutable traceability archive in /root/openclaw_traceability/; 7 file types per run; Claude Code implementation authorized |
| Advisory Memo 017 — Five-Layer Operating Model | OPENCLAW-ADV-017 | `advisory/OPENCLAW-ADV-017_2026-06-06.md` | advisory/ | OPERATOR APPROVED | CEO-controlled product quality workflow; five layers: System Run, Citation, Source Quality, Claim Support, Client Usefulness; operator-approved reference basis for governing document updates; gate streak HELD at 3/10 |

Next advisory memo: ADV-018

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

*OPENCLAW-MDI-001 | Version v5.4 | Last updated: 2026-06-08 | Status: ACTIVE*

*v5.4 changes (2026-06-08): OPENCLAW-CC-OPS-001 (Claude Code Operating Protocol) added to Tier 1 — LOCKED. CoWork Operating Protocol updated to v2.9 (role designation and document control updates). VPS Sync Protocol updated to v1.8 (review source matrix added). All changes implement the operating model shift approved by operator 2026-06-08.*

*v5.3 changes (2026-05-28): CP-018 through CP-024 + CP-022A added to Tier 6 (all APPROVED; CP-020/021/022A/022/023/024 are signal-widening plan; CP-018/019 are in-flight stabilization). ADV-013 / ADV-013-REVIEW / ADV-013-RESPONSE added to Tier 7. Next advisory counter updated to ADV-014.*

*v5.2 changes (2026-05-24): CP-011 through CP-017 added to Tier 6. CP-006 added (Baidu-only ALJ). ALJ client config and spec docs added.*

*v5.1 changes (2026-05-24): CP-005 through CP-010 added to Tier 6. CP-004 status updated to CONFIRMED. CONFIRMED added to status definitions: change packet validated across one or more cron runs. CP-010 file does not yet exist on disk — to be created.*

*v5.0 changes (2026-05-21): Four Phase D Change Packets added to Tier 6 — CP-001 (Brain Lite validation path fix, OPENCLAW-D-CP-001), CP-002 (content specificity, OPENCLAW-D-CP-002), CP-003 (LinkedIn Draft format, OPENCLAW-D-CP-003), CP-004 (source provenance labelling, OPENCLAW-D-CP-004). All status: IMPLEMENTED; validation pending 2026-05-22 cron run. IMPLEMENTED added to status definitions. "IMPLEMENTED" status: change packet applied to VPS; awaiting validation runs.*

*v4.9 changes (2026-05-20): Root folder cleanup — three strategic memo files moved from [root] to advisory/ (REFERENCE status); verify_isolation.py moved from [root] to other_ref/. Tier 9 (Other Reference) added. Former Tier 9 (Archived) renumbered to Tier 10. Strategy Memo 6.8.26.txt noted as filename convention exception (spaces) — operator to rename if desired.*

*v4.8 changes (2026-05-20): Phase D Operator Review Procedure (OPENCLAW-PHASE-D-ORP-001) added to Tier 6. Feedback Register updated to v1.2; Scorecard updated to v1.2 (cross-references to procedure document added).*

*v4.7 changes (2026-05-20): phase_d/ added to location key. Phase D Feedback Register and Content Scorecard added to Tier 6 (OPERATIONAL). Phase D Content Change Packet Template added to Tier 8 (TEMPLATE). client_config_test_client_002.yaml added to Tier 6 (ACTIVE). CoWork Operating Protocol now at v2.6 (updated 2026-05-20, phase lock Phase D).*

*v4.6 changes (2026-05-19): OPERATOR APPROVED added to formal status definitions. Frontmatter corrected to v4.6/2026-05-19 (previously mismatched vs footer at v4.5/2026-05-18).*

*v4.5 changes (2026-05-18): OPENCLAW-SPEC-CONFIG-LOADER-001 status updated from CONSULTANT APPROVED to OPERATOR APPROVED (approved 2026-05-18).*

*v4.4 changes (2026-05-15): Client Config entry updated — brain_context=true (activated 2026-05-15).*

*v4.3 changes (2026-05-14): Remediation plan executed — CONSULTANT APPROVED status added to legend; Control Layer Spec and Architecture Philosophy filenames updated to .md; ADV-002, ADV-009, ADV-010 status updated to REFERENCE; ADV-011 moved to old/ and added to Tier 9.*

*v4.2 changes (2026-05-14): OPENCLAW-DOC-GOV-001 added to Tier 1 (locked 2026-05-14); ADV-012 added to Tier 7 (operator approved 2026-05-14).*

*v4.1 changes (2026-05-13): OPENCLAW-SPEC-CONFIG-LOADER-001 added to Tier 5 (consultant approved 2026-05-13; awaiting operator approval).*

*v4.0 changes (2026-05-13): Full migration to OPENCLAW-SYS-FILENAME-002 filename standard. All filenames updated to remove dates, spaces, and parentheses. OPENCLAW_COWORK_OPERATING_PROTOCOL.md renamed from 05_OPERATING_PROTOCOL. Tier 1 now references filename standard. VPS Sync Protocol added to Tier 6. Document Versions Index added to Tier 5. File Organization Convention section replaced with File Naming Convention per new standard.*
