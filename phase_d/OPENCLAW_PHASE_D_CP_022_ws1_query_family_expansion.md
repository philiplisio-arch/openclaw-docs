---
document_id: OPENCLAW-D-CP-022
version: 1.0
created: 2026-05-28
classification: PHASE D CHANGE PACKET — QUERY TEMPLATES / RETRIEVAL
---

# OPENCLAW — Phase D Change Packet CP-022
# WS1 Core China Query Family Expansion (Live)

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-022 |
| Date raised | 2026-05-28 |
| Raised by | CoWork — signal-widening plan 2026-05-28 |
| Client ID | china_monitor_001 (WS1) |
| Feedback items addressed | D-FB-003/004/005/006; signal-widening advisory ADV-013 |
| Tier | 3 — WS1 Retrieval Expansion (Live) |
| Implementation layer | Query templates |
| Status | APPROVED — blocked on CP-022A validation |

---

## SECTION 1 — RATIONALE

CP-022 is the live deployment of the query families first tested in held
mode under CP-022A. It may not proceed until:
  1. CP-022A has completed two held-mode validation runs
  2. The operator confirms materially improved source richness without
     unacceptable noise, duplication, or runtime instability
  3. Browser Retrieval Phase 1 findings report has been produced (CoWork)
     and the operator has made the Phase 2 go/no-go decision

The current WS1 query bundle is a single general query set. Structuring
queries into named families by source class is expected to produce:
  - More official/regulatory signal
  - More Chinese business/financial press coverage
  - More sector-specific material
  - Better international corroboration
  - Reduced dependence on broad-topic results that cycle through the
    same macro themes (US-China / Europe / Middle East)

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** Query template file for china_monitor_v1 (or successor)

**Query families:** As tested and confirmed in CP-022A (seven families:
official/regulatory, state-media/narrative, Chinese business/financial press,
sector-specific rotation, company/corporate signal, international
corroboration, geopolitical/trade signal). Exact query strings confirmed
during CP-022A — use the CP-022A validated set, not a new untested bundle.

**Change scope:** Query template file only. If the template format requires
changes to load_client_config.py or the orchestrator to support named
query families, those changes must be scoped as part of this CP and reviewed
separately before implementation.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** MEDIUM

Retrieval composition changes. The source mix could shift materially from
current norms. Thin package, increased deduplication load, or retrieval
timeout risk if query count grows significantly.

Mitigation: CP-022A validation is the primary risk control. The live
deployment uses exactly the query set validated in held mode.

**Rollback plan:**

Claude Code creates backup before modification:
```
[query_template_file].bak_YYYYMMDD_cp022
```
Rollback: restore from backup. If live delivery degrades materially
on first CP-022 run, roll back the same session.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria (must be met across 2 consecutive live runs):**

| Criterion | Target |
|-----------|--------|
| Retained sources after filtering | 15+ where available |
| Visible sources in SOURCES appendix | 8+ |
| Chinese-source items | 4+ |
| Chinese business / financial press | 2+ |
| Official or state-source | 1+ where relevant |
| Single publisher share | No publisher >35% unless labeled as amplification |
| Duplicate / amplification labeling | Present in SECTION 4 output |
| Freshness labels on all major signal items | Yes |
| Source category labels on all appendix items | Yes |
| Operator source-usefulness score | ≥4 on both runs |
| Validator | GREEN |
| T-04 compliance | COMPLIANT |

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to query templates
- [x] Rollback path documented
- [x] Blocked on CP-022A held-mode gate — will not deploy live until gate passes
- [x] Within Phase D scope (retrieval quality improvement)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT alter agent prompt (beyond what CP-021 already changes)
- [x] Does NOT weaken validator strictness
- [x] Does NOT weaken scrubber behavior
- [x] Does NOT bypass or modify the Delivery Gate decision
- [x] Does NOT affect client namespace isolation
- [x] Does NOT introduce Brain Lite schema changes

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-05-28 |
| Blocked on | CP-022A validation (2 held-mode runs); Browser Phase 1 findings |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | |
| Backup confirmed | |

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Date | Mode | Retained | CN sources | Biz press | Official | Publisher cap met? | Operator score | Validator | Notes |
|-------|------|------|----------|-----------|-----------|----------|--------------------|----------------|-----------|-------|
| 1 | | live | | | | | | | | |
| 2 | | live | | | | | | | | |

**Overall outcome:** PENDING — blocked on CP-022A

---

*OPENCLAW-D-CP-022 | Version 1.0 | Created: 2026-05-28 | Status: APPROVED — blocked on CP-022A validation*
*Raised by: CoWork — signal-widening plan approval 2026-05-28*
*Operator approved: 2026-05-28*
