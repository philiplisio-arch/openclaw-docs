---
document_id: OPENCLAW-D-CP-020
version: 1.0
created: 2026-05-28
classification: PHASE D CHANGE PACKET — AGENT PROMPT / OUTPUT FORMAT
---

# OPENCLAW — Phase D Change Packet CP-020
# Source Taxonomy + Freshness Labels

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-020 |
| Date raised | 2026-05-28 |
| Raised by | CoWork — signal-widening plan 2026-05-28 |
| Client ID | china_monitor_001 (WS1 live); alj_china_auto_001 (held/pre-live only) |
| Feedback items addressed | D-FB-006 (signal quality); signal-widening advisory ADV-013 |
| Tier | 1 — Shared Labeling Foundation |
| Implementation layer | Agent prompt / build_agent_input_slim.py |
| Status | DEPLOYED 2026-06-02; ACCEPTED 2026-06-03 (status stamped 2026-06-10 reconciliation; Daily Status governs) |

---

## SECTION 1 — RATIONALE

The current product has [CN]/[INTL]/[CN+INTL] provenance labels per bullet
(CP-004) but no per-source classification system. Sources in the SOURCES
appendix carry no taxonomy or freshness metadata. The reader cannot
distinguish official policy signal from state-media amplification, sector
press from business press, or genuinely fresh news from repeated context.

This is the foundational labeling layer for the signal-widening plan. All
downstream CPs (CP-021 output restructuring, CP-024 appendix upgrade) depend
on a shared, defined label vocabulary.

A shared schema must apply across WS1 and ALJ so both products use the same
source taxonomy. ALJ labels are validated in held/pre-live mode only until
ALJ pre-live blockers are resolved.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `build_agent_input_slim.py` (agent prompt instructions)

**Label schema to define:**

Source category labels (applied per source in SOURCES appendix and per
signal item):

| Label | Meaning |
|-------|---------|
| CN-OFFICIAL | Chinese government ministry or agency |
| CN-REGULATORY | Chinese regulatory body (SAMR, CSRC, PBOC etc.) |
| CN-STATE | Chinese state media (Xinhua, CCTV, People's Daily, Global Times) |
| CN-BUSINESS | Chinese business / financial press (Yicai, Caixin, 证券时报 etc.) |
| CN-SECTOR | Chinese sector-specific trade or industry press |
| CN-COMPANY | Chinese company announcement, exchange filing, or release |
| CN-ASSOCIATION | Chinese industry association data or statement |
| INTL-WIRE | International wire service (Reuters, AP, Bloomberg) |
| INTL-BUSINESS | International business press (FT, WSJ, Nikkei Asia, SCMP) |
| PLATFORM | Social platform or aggregator (Weibo, WeChat, Sina etc.) |
| UNKNOWN | Source type not determinable from available metadata |

Freshness labels (applied per signal item and per source entry):

| Label | Meaning |
|-------|---------|
| NEW-24H | First reported within the last 24 hours |
| FOLLOW-UP-48H | Recent continuation of a developing story |
| CONTEXT-7D | Relevant context from the past week |
| BACKGROUND | Older material; useful context but not fresh news |

Signal role labels (optional on first pass — confirm with operator
whether to include in CP-020 or defer to CP-021):

| Label | Meaning |
|-------|---------|
| POLICY SIGNAL | Official or regulatory activity |
| MARKET SIGNAL | Pricing, sales, investment, capital markets |
| INDUSTRY SIGNAL | Sector-specific operational or commercial development |
| COMPANY SIGNAL | Corporate announcement, earnings, strategy, partnership |
| NARRATIVE SIGNAL | State-media or repeated official framing |
| RISK SIGNAL | Sanctions, compliance, geopolitical, reputational |

**WS1 application:** Labels applied to signal items and SOURCES appendix
from first live delivery after deployment.

**ALJ application:** Same schema and prompt instructions included. ALJ labels
appear only in ALJ held/pre-live runs. ALJ labels do not go live until ALJ
pre-live blockers (CP-015/016/017) are resolved.

**Change scope:** Additions to the output format instruction block in
build_agent_input_slim.py. Single file. No retrieval, validation, scrubber,
or delivery gate changes.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** LOW

Labels are additive instructions in the agent prompt. The agent may classify
inconsistently on early runs — particularly PLATFORM vs CN-BUSINESS, or
CN-STATE vs CN-OFFICIAL — but misclassification has no pipeline impact.
Labels are editorial metadata, not validation criteria.

**Rollback plan:**

Claude Code creates backup before modification:
```
build_agent_input_slim.py.bak_YYYYMMDD_cp020
```
Rollback: restore from backup. One file. No other changes.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. py_compile exit 0 on modified build_agent_input_slim.py
2. First post-deployment WS1 run: source category labels and freshness labels
   appear on signal items and in SOURCES appendix entries
3. Operator reviews label accuracy — spot-check at least 3 source entries
   against known publisher/domain
4. No degradation in citation integrity (validator GREEN, T-04 compliant)

**Runs required:** 1 held-mode run reviewed by operator; then live.

**ALJ validation:** Labels present in next ALJ held-mode run after CP-020
deployment; operator reviews before any ALJ live delivery.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to one layer (agent prompt)
- [x] Rollback path documented
- [x] Within Phase D scope (output format / editorial quality improvement)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT alter retrieval behavior
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
| Implementation assigned to | Claude Code |
| Implementation confirmed date | |
| Backup confirmed | |

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Client | Date | Labels present? | Operator accuracy review | Validator | Notes |
|-------|--------|------|-----------------|--------------------------|-----------|-------|
| 1 | WS1 | | | | | |
| 1 | ALJ | | | | | held mode only |

**Overall outcome:** PENDING

---

*OPENCLAW-D-CP-020 | Version 1.0 | Created: 2026-05-28 | Status: APPROVED — implementation pending*
*Raised by: CoWork — signal-widening plan approval 2026-05-28*
*Operator approved: 2026-05-28*
