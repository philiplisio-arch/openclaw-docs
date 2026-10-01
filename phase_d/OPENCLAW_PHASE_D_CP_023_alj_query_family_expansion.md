---
document_id: OPENCLAW-D-CP-023
version: 1.0
created: 2026-05-28
classification: PHASE D CHANGE PACKET — QUERY TEMPLATES / RETRIEVAL (ALJ)
---

# OPENCLAW — Phase D Change Packet CP-023
# ALJ Query Family Expansion

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-023 |
| Date raised | 2026-05-28 |
| Raised by | CoWork — signal-widening plan 2026-05-28 |
| Client ID | alj_china_auto_001 |
| Feedback items addressed | Signal-widening advisory ADV-013 Section IV |
| Tier | 4 — ALJ Query Family Expansion |
| Implementation layer | Query templates (alj_china_auto_weekly_v1 or successor) |
| Status | APPROVED — blocked on ALJ pre-live blockers + baseline held run |

---

## SECTION 1 — RATIONALE

The current ALJ query bundle is a general China auto query set. The
signal-widening plan calls for structuring ALJ retrieval into eight
named families targeting the specific source types most commercially
relevant to ALJ: official/regulatory, industry association/market data,
Chinese auto sector media, business/financial press, company/competitor
watch, China-to-Middle-East/Saudi bridge, policy/regulation, and
battery/charging/supply chain.

**Timing:** CP-023 may begin after:
  1. ALJ pre-live blockers are resolved (CP-015/016/017 + Lark doc_id)
  2. At least one baseline held-mode ALJ run is successfully produced
     with the current query set

CP-023 does NOT require ALJ external live delivery first. It may validate
entirely in held mode before ALJ goes live externally, subject to operator
review capacity.

The Baidu-only constraint (CP-006) applies throughout. All eight query
families are Baidu-only for ALJ.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** alj_china_auto_weekly_v1 query template (or successor)

**Eight proposed query families:**

Family 1 — Official / Regulatory Auto
  site:miit.gov.cn 新能源汽车 政策
  site:miit.gov.cn 智能网联汽车
  site:ndrc.gov.cn 汽车 消费
  site:samr.gov.cn 汽车 价格 监管
  site:mofcom.gov.cn 汽车 出口
  site:customs.gov.cn 汽车 出口 新能源
  site:gov.cn 新能源汽车 产业 政策
  site:gov.cn 汽车 以旧换新

Family 2 — Industry Association / Market Data
  中汽协 汽车 销量 新能源 出口
  乘联会 零售 批发 新能源汽车
  汽车 经销商 库存 指数
  新能源汽车 渗透率 月度
  中国 汽车 出口 数据
  乘用车 市场 分析

Family 3 — Chinese Auto Sector Media
  盖世汽车 新能源汽车 出海
  盖世汽车 价格战 汽车
  汽车之家 经销商 库存 新能源
  36氪 汽车 智能驾驶
  晚点 Auto 新能源 竞争
  电动汽车 价格战 比亚迪 吉利

Family 4 — Chinese Business / Financial Press (Auto)
  第一财经 汽车 新能源 价格战
  财新 汽车 出口 新能源
  证券时报 比亚迪 吉利 上汽 长城
  财联社 汽车 智能驾驶

Family 5 — Company / Competitor Watch
  比亚迪 中东 沙特 出口
  吉利 中东 出口
  奇瑞 沙特 汽车
  长城汽车 海外 经销商
  上汽 出海 中东
  丰田 中国 新能源 战略
  日产 中国 经销商
  现代 中国 新能源
  宁德时代 中东 储能 电池
  中国 汽车 经销商 合作 沙特

Family 6 — China-to-Middle-East / Saudi Bridge
  中国 汽车 沙特
  中国 新能源汽车 沙特
  中国 汽车 中东 出口
  比亚迪 沙特
  吉利 沙特
  奇瑞 沙特
  长城汽车 沙特
  上汽 沙特
  中国 电动车 中东 市场
  中国 车企 海外 本地化 中东
  沙特 汽车 中国 投资
  中沙 汽车 合作
  中东 新能源汽车 中国 品牌

Family 7 — Policy / Regulation Watch
  新能源汽车 补贴 政策
  智能驾驶 法规
  汽车 排放 标准 中国
  出口 管制 汽车 零部件

Family 8 — Battery / Charging / Supply Chain
  宁德时代 电池 出口
  动力电池 供应链
  中国 充电 基础设施
  新能源汽车 供应链 中东

**Change scope:** ALJ query template file only. No agent prompt (CP-021
handles output restructuring separately), no scrubber, no validator, no
delivery behavior changes.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** MEDIUM

Significant expansion of ALJ retrieval scope. The Baidu-only constraint
limits geographic access risk. Key unknowns: whether Baidu returns strong
results across all eight families; whether the 7-day freshness window
(CP-011) produces sufficient results across expanded query breadth.

Mitigation: Held-mode validation before any live ALJ delivery under the
expanded queries. Operator reviews source mix and counts before live.

**Rollback plan:**

Claude Code creates backup before modification:
```
[alj_query_template_file].bak_YYYYMMDD_cp023
```
Rollback: restore from backup. No other files affected.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria (against ALJ minimum source standard from ADV-013):**

| Criterion | Target |
|-----------|--------|
| Visible sources in SOURCES appendix | 8–12 |
| Chinese auto-sector sources (sector press) | 4+ |
| Official / association / market-data sources | 2+ where available |
| Company or competitor sources | 2+ |
| China-to-Middle-East / Saudi signal | 1+ where available |
| No single publisher dominant | No publisher >35% unless labeled |
| Source category labels present | Yes (CP-020 prerequisite) |
| Freshness labels present | Yes (CP-020 prerequisite) |
| Operator source-usefulness score | ≥4 on both held-mode runs |

**Runs required:** 2 held-mode runs; operator reviews; then live.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to ALJ query templates
- [x] Rollback path documented
- [x] Blocked on ALJ pre-live blockers and baseline held run
- [x] Within Phase D scope (ALJ retrieval quality improvement)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT affect WS1 retrieval (separate template)
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
| Blocked on | ALJ pre-live blockers (CP-015/016/017); 1 baseline held ALJ run |
| External live delivery NOT required before held-mode testing | Confirmed |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | |
| Backup confirmed | |

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Date | Mode | App sources | Sector sources | Official/Assoc | Company | Saudi signal | Operator score | Notes |
|-------|------|------|------------|---------------|----------------|---------|--------------|----------------|-------|
| baseline | | held | | | | | | | pre-CP-023 |
| 1 | | held | | | | | | | |
| 2 | | held | | | | | | | |

**Overall outcome:** PENDING — blocked on ALJ pre-live blockers

---

*OPENCLAW-D-CP-023 | Version 1.0 | Created: 2026-05-28 | Status: APPROVED — blocked on ALJ pre-live blockers*
*Raised by: CoWork — signal-widening plan approval 2026-05-28*
*Operator approved: 2026-05-28*
