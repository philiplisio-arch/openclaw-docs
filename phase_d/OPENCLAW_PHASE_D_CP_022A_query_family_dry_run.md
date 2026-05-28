---
document_id: OPENCLAW-D-CP-022A
version: 1.0
created: 2026-05-28
classification: PHASE D CHANGE PACKET — QUERY TEMPLATES / RETRIEVAL (HELD MODE ONLY)
---

# OPENCLAW — Phase D Change Packet CP-022A
# WS1 Expanded Query Family Held-Mode Dry Run

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-022A |
| Date raised | 2026-05-28 |
| Raised by | CoWork — signal-widening plan 2026-05-28 |
| Client ID | china_monitor_001 (WS1) |
| Feedback items addressed | D-FB-003 (topic repetition); D-FB-004 (old articles / thin signal); signal-widening advisory ADV-013 |
| Tier | 2B — Early Retrieval Dry Run |
| Implementation layer | Query templates / retrieval (held mode only — no live delivery) |
| Status | APPROVED — implementation pending |

---

## SECTION 1 — RATIONALE

Weak signal is the current core product bottleneck. The fastest safe path
to better signal is to test richer query families in held mode as early as
possible — during Tier 2 (while CP-021 format changes are validating) —
rather than waiting until Tier 3 to discover whether expanded query families
actually improve source richness.

CP-022A is a held-mode-only dry run. Its purpose is to produce two comparison
data sets: the current WS1 source baseline vs the expanded query family
output. The operator reviews both and confirms whether source richness
materially improves before CP-022 is deployed live.

**No live delivery effect.** The pipeline must run in held mode (pilot_mode
or equivalent) throughout this test. If held mode cannot be enforced for
WS1, this CP must not be deployed until a safe held mode is available.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** Query template file for china_monitor_v1 (or new version)

**Proposed expanded query families:**

Family 1 — Official / Regulatory
  site:gov.cn 中国 经济 政策
  site:ndrc.gov.cn 民营经济 消费 投资
  site:mofcom.gov.cn 外贸 外资 贸易
  site:miit.gov.cn 工业 数字经济 人工智能
  site:samr.gov.cn 监管 平台经济
  site:csrc.gov.cn 上市公司 资本市场
  site:pbc.gov.cn 金融 政策
  site:customs.gov.cn 进出口 数据
  site:mfa.gov.cn 中美 经贸

Family 2 — State Media / Official Narrative
  site:xinhuanet.com 中国 经济 政策
  site:cctv.com 中国 经济 贸易
  site:people.com.cn 民营经济 政策

Family 3 — Chinese Business / Financial Press
  第一财经 中国 经济 外资
  财新 中国 经济 政策
  证券时报 A股 外资 中国
  财联社 人工智能 半导体 中国
  新浪财经 中国 市场 政策
  东方财富 中国 产业 投资
  21世纪经济报道 中国 企业 出海

Family 4 — Sector-Specific Rotation
  中国 人工智能 政策 企业
  中国 半导体 出口 管制 产业
  中国 新能源汽车 出口
  中国 消费 零售 数据
  中国 房地产 政策 融资
  中国 供应链 制造业 出口
  中国 能源 电力 投资
  中国 医药 监管 创新

Family 5 — Company / Corporate Signal
  中国 企业 出海 投资
  外资 企业 中国 投资
  跨国公司 中国 战略

Family 6 — International Corroboration
  China economy Reuters Bloomberg
  China business policy
  China trade exports foreign investors
  China technology regulation

Family 7 — Geopolitical / Trade Signal
  中美 经贸 出口 管制 关税
  中欧 贸易 经济
  China US trade tariffs sanctions

**Change scope:** Query template file only. No agent prompt, no scrubber,
no validator, no delivery behavior changes. Must run in held mode only.

**Baseline comparison requirement:** Before deploying expanded queries,
Claude Code or operator captures the current WS1 source baseline metrics
from the most recent clean run (retained source count, Chinese-source count,
business press count, official source count, sector source count) for
direct comparison.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** LOW-MEDIUM (held mode only)

In held mode, there is no live delivery and no external recipient. The risk
is that expanded queries produce unexpectedly high noise, duplicate
inflation, or runtime instability on the VPS.

Mitigation: Held mode only. Two runs before any live assessment.
If either run shows runtime instability (timeout, retrieval error, extreme
duplicate inflation), the query template is rolled back before any
consideration of live deployment.

**Rollback plan:**

Claude Code creates backup before modification:
```
[query_template_file].bak_YYYYMMDD_cp022A
```
Rollback: restore from backup. No other files affected.

---

## SECTION 4 — VALIDATION METHOD

**Comparison metrics (both held-mode runs, vs current baseline):**

| Metric | Baseline (current) | Run 1 | Run 2 |
|--------|-------------------|-------|-------|
| Retained sources after filtering | | | |
| Visible sources in appendix | | | |
| Chinese-source count | | | |
| Chinese business / financial press count | | | |
| Official / state-source count | | | |
| Sector-source count | | | |
| Duplicate / amplification rate | | | |
| Source concentration (dominant publisher %) | | | |
| Runtime: any errors or timeouts? | | | |
| Operator source-usefulness score (1–5) | | | |

**CP-022 live deployment gate:** CP-022 may proceed to live deployment only
after the operator confirms across both CP-022A runs:
  - Materially more Chinese-source items than baseline
  - No single publisher >35% of visible source list
  - No unacceptable noise, duplication, or runtime instability
  - Operator source-usefulness score ≥4

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to query templates (held mode only)
- [x] No live delivery effect
- [x] Rollback path documented
- [x] Within Phase D scope (retrieval quality improvement — held mode research)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT alter agent prompt
- [x] Does NOT alter scrubber behavior
- [x] Does NOT weaken validator strictness
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
| Mode constraint | HELD MODE ONLY throughout |
| Implementation confirmed date | |
| Backup confirmed | |

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Date | Mode | Retained sources | CN sources | Biz press | Official | Duplication rate | Operator score | Notes |
|-------|------|------|-----------------|-----------|-----------|----------|-----------------|----------------|-------|
| baseline | | | | | | | | | current WS1 |
| 1 | | held | | | | | | | |
| 2 | | held | | | | | | | |

**CP-022 gate decision:** PENDING — operator review of both runs required

---

*OPENCLAW-D-CP-022A | Version 1.0 | Created: 2026-05-28 | Status: APPROVED — implementation pending*
*Raised by: CoWork — signal-widening plan approval 2026-05-28*
*Operator approved: 2026-05-28 | Held mode only — no live delivery*
