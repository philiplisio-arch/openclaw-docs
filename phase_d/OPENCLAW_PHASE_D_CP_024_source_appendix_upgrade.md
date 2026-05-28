---
document_id: OPENCLAW-D-CP-024
version: 1.0
created: 2026-05-28
classification: PHASE D CHANGE PACKET — OUTPUT FORMAT / citation_sub.py
---

# OPENCLAW — Phase D Change Packet CP-024
# Source Appendix Upgrade

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-024 |
| Date raised | 2026-05-28 |
| Raised by | CoWork — signal-widening plan 2026-05-28 |
| Client ID | china_monitor_001 (WS1); alj_china_auto_001 (in scope) |
| Feedback items addressed | D-FB-005 (no source URLs); signal-widening advisory ADV-013 |
| Tier | 2C — Source Appendix Upgrade |
| Implementation layer | citation_sub.py / output format |
| Status | APPROVED — blocked on CP-020 deployment |

---

## SECTION 1 — RATIONALE

The current SOURCES appendix (CP-010 base) records title | publisher |
date | URL for each retained source. This gives the reader a citation
trail but no source classification metadata.

CP-024 upgrades the appendix to add source category label and freshness
label fields, producing a richer, more transparent source record.

The SOURCES appendix is becoming a trust artifact — the deterministic
evidence base for the product. Its classification fields must be assigned
reliably. The primary constraint of this CP is the **deterministic labeling
rule**: labels in the appendix must be derived from metadata where possible,
not freely inferred by the agent.

**Dependency:** CP-024 requires CP-020 to be deployed first. The label
vocabulary (source category labels and freshness labels) must be defined
before the appendix can apply them.

**Applies to both WS1 and ALJ.** The appendix format is shared.
ALJ appendix labels validate in held/pre-live mode consistent with
CP-020 ALJ constraints.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `citation_sub.py`

**Full per-source record (upgraded from CP-010):**

```
title | publisher | date | URL | source_category | freshness_label
```

**Deterministic labeling constraint:**

Source category and freshness labels in the SOURCES appendix MUST be
assigned deterministically where possible:
  - source_category: derived from publisher name, domain, and/or
    client-config source mappings. Examples:
      xinhuanet.com → CN-STATE
      people.com.cn → CN-STATE
      cctv.com → CN-STATE
      mofcom.gov.cn → CN-OFFICIAL
      ndrc.gov.cn → CN-OFFICIAL
      reuters.com → INTL-WIRE
      bloomberg.com → INTL-WIRE
      caixin.com → CN-BUSINESS
      yicai.com → CN-BUSINESS
      gasgoo.com → CN-SECTOR
      autohome.com.cn → CN-SECTOR
      [not classifiable] → UNKNOWN
  - freshness_label: derived from published_date vs run_date.
      0–1 days → NEW-24H
      2 days → FOLLOW-UP-48H
      3–7 days → CONTEXT-7D
      >7 days → BACKGROUND
      [no date available] → UNKNOWN

Agent-proposed labels are acceptable in signal bullets (SECTION 1 of the
CP-021 output structure) during early testing. However, the SOURCES appendix
must use metadata-derived labels wherever metadata is available.

**Appendix header upgrade:**

Add a one-line source mix summary before the source list:
  Sources: [N] total | [N] Chinese | [N] official/state | [N] international
  | [N] sector

**Change scope:** citation_sub.py — additions to the SOURCES appendix
builder block. No agent prompt changes (beyond defining label vocabulary
in CP-020). No scrubber, validator, or delivery gate changes.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** LOW

Additive fields on an existing appendix structure. The deterministic
label logic is a lookup table, not a reasoning task. The fallback to
UNKNOWN means a missing domain mapping produces a visible but harmless
unknown entry rather than a misclassification.

The appendix is post-delivery formatting — it does not affect citation
integrity, the validator, or the delivery gate decision.

**Rollback plan:**

Claude Code creates backup before modification:
```
citation_sub.py.bak_YYYYMMDD_cp024
```
Rollback: restore from backup. One file. No other changes.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. py_compile exit 0 on modified citation_sub.py
2. First post-deployment run: SOURCES appendix entries contain
   source_category and freshness_label fields
3. At least 3 entries have non-UNKNOWN source_category (confirms
   domain mapping logic working)
4. Freshness labels match published_date arithmetic (spot-check 2 entries)
5. Source mix summary line present in appendix header
6. No degradation in citation integrity (validator GREEN)
7. Operator confirms label quality acceptable

**Runs required:** 1 held-mode run reviewed by operator; then live.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to citation_sub.py (output formatting)
- [x] Rollback path documented
- [x] Blocked on CP-020 (label vocabulary must be defined first)
- [x] Within Phase D scope (source appendix / output quality improvement)

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
| Blocked on | CP-020 deployment |
| Deterministic labeling constraint | CONFIRMED — metadata-derived preferred; UNKNOWN fallback |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | |
| Backup confirmed | |

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Client | Date | Labels present? | Non-UNKNOWN entries | Freshness match? | Mix summary? | Validator | Notes |
|-------|--------|------|-----------------|---------------------|------------------|--------------|-----------|-------|
| 1 | WS1 | | | | | | | |
| 1 | ALJ | | | | | | | held mode |

**Overall outcome:** PENDING — blocked on CP-020

---

*OPENCLAW-D-CP-024 | Version 1.0 | Created: 2026-05-28 | Status: APPROVED — blocked on CP-020*
*Raised by: CoWork — signal-widening plan approval 2026-05-28*
*Operator approved: 2026-05-28*
