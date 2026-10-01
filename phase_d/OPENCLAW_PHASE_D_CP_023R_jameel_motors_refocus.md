# OPENCLAW — Phase D Change Packet CP-023R (DRAFT)
# ALJ Weekly Brief → Jameel Motors Refocus (supersedes CP-023 scope)

---
document_id: OPENCLAW-D-CP-023R
version: 0.1-DRAFT
created: 2026-06-11
classification: PHASE D CHANGE PACKET — CLIENT SCOPE / QUERY TEMPLATES / REPORT TEMPLATE (ALJ)
status: DRAFT — presented for operator review; nothing deploys before WS1 Phase D gate closure + per-item approval
---

## SECTION 0 — PRODUCT DEFINITION (operator direction, 2026-06-11)

The ALJ weekly brief's end client is **Jameel Motors** (Abdul Latif Jameel's mobility/distribution arm). Three purposes, in priority order:

- **A. Situational awareness** — what the Jameel Motors team needs to understand about relevant developments in China.
- **B. Brand tracking** — key Chinese auto brands, inside AND outside China (Jameel's partner brands first, their competitors second).
- **C. Media angles** — surface topics Jameel Motors executives can credibly speak to media about.

Purpose C is new and changes the advisory layer: it should split into business implications and media-opportunity angles.

## SECTION 1 — JAMEEL MOTORS FOOTPRINT (public sources, compiled 2026-06-11; operator to correct/extend)

| Brand (owner) | Territory | Status |
|---|---|---|
| Toyota / Lexus / Hino | Saudi Arabia (since 1955) + MENA/Asia markets | Heritage core |
| BYD | Türkiye | Active |
| GAC AION (JV) | UK | First deliveries ~Q1 2026 (AION V, AION UT) |
| GAC Motor | Poland | Signed 2025 |
| MG Motor (SAIC) | Morocco | Since 2023 |
| Geely Farizon (NE commercial vehicles) | Global collaboration, 11 countries (incl. UAE) | Active |
| Changan | South Africa | Signed (SUVs, sedans, pickups, NEVs) |
| JMC commercial vehicles | Morocco | From Spring 2026 |
| Omoda/Jaecoo (Chery) | Iraq | Active |
| Ford / Ford Trucks; multi-brand retail | Egypt (Auto Store), Türkiye (OTOShops) | Context only |

Markets footprint: Saudi, UK, Poland, UAE, Türkiye, Morocco, Egypt, Algeria, Iraq, Japan, China, Australia, Monaco, South Africa.

**Implication:** Jameel's Chinese partners (BYD, GAC, Geely/Farizon, Changan, Chery, SAIC/MG, JMC) ≈ China's top auto exporters. "Key Chinese brands" coverage and "partner coverage" largely coincide; competitor coverage (Tesla in China, NIO/XPeng/Li Auto, Leapmotor/Stellantis) is the supplement.

## SECTION 2 — PROPOSED CONFIG SCOPE (client_config_alj_china_auto_001.yaml topic_focus rewrite)

1. Jameel partner brands in China: BYD, GAC/AION, Geely (incl. Farizon), Changan, Chery (Omoda/Jaecoo), SAIC/MG, JMC — sales, strategy, products, leadership, financials
2. Partner brands outside China: launches, expansion, localization in Jameel territories (Gulf/Saudi, Türkiye, UK/Europe, Morocco/North Africa, South Africa, Iraq) and adjacent markets
3. China NEV market pulse: CAAM/CPCA weekly data, NEV penetration, price competition, battery/PHEV/charging technology shifts
4. China auto export corridors & trade policy: export volumes, shipping, tariffs (EU, Türkiye, Gulf localization requirements), overseas plants
5. Toyota/Lexus competitive position in China and vs Chinese brands globally
6. Distribution & dealer economics: agency models, aftersales, dealer profitability — China and export markets
7. Media-angle raw material: industry inflection points, firsts/records, controversy-adjacent topics where a distributor voice is credible

Geographic scope addition: `regions` gains europe, africa, turkiye (currently china + middle_east only).

## SECTION 3 — PROPOSED QUERY FAMILIES (alj_jameel_weekly_v2; replaces 7-query alj_china_auto_weekly_v1)

Baidu (zh) unless marked; ~16 queries. _excl = -site:baike.baidu.com -site:bilibili.com -site:zhihu.com -site:tieba.baidu.com

**JF1 — Partner brands in China (3):**
- 比亚迪 销量 战略 新车 本周
- 广汽埃安 吉利 长安 销量 新能源 本周
- 奇瑞 上汽名爵 江铃 出口 销量 本周

**JF2 — Partner brands global (3, Brave en + Baidu zh):**
- [en] BYD OR GAC OR Chery OR Changan OR Geely Europe Turkey Middle East Africa launch expansion
- [en] Chinese EV brands UK Poland South Africa sales launch
- 中国车企 海外 工厂 本地化 中东 欧洲 非洲 本周

**JF3 — China NEV market pulse (2):**
- 新能源汽车 乘联会 中汽协 渗透率 销量 数据 本周
- 电池 插混 充电 技术 价格战 车企 本周

**JF4 — Export corridors & trade policy (3):**
- 中国 汽车 出口 数据 海湾 中东 本周
- [en] China car exports tariffs EU Turkey Gulf localization policy
- 中国 新能源汽车 出口 关税 欧盟 土耳其 政策

**JF5 — Toyota/Lexus × China (2):**
- 丰田 雷克萨斯 中国 销量 电动化 战略 本周
- [en] Toyota Lexus China strategy electric hybrid competition BYD

**JF6 — Dealer/distribution economics (1):**
- 汽车 经销商 渠道 代理制 售后 盈利 本周

**JF7 — Competitor watch (2):**
- 特斯拉 蔚来 小鹏 理想 零跑 中国 销量 动态 本周
- [en] Tesla NIO XPeng Li Auto Leapmotor China news

**Requires:** enabling Brave for ALJ (config `brave_enabled: false` → true; `source_filter.chinese_only` relaxed for JF2/JF4/JF5/JF7 en-queries). Purpose B explicitly covers brands OUTSIDE China — not reachable via Baidu-only. Lane 3 config change, operator approval.

## SECTION 4 — REPORT TEMPLATE CHANGES (alj report template)

- EXECUTIVE TAKE: unchanged mechanics; relevance test = names a Jameel brand/territory/corridor or a market shift that affects them.
- ADVISORY LAYER splits into two tagged bullet types:
  - `[IMPLICATION]` — what Jameel Motors should consider operationally.
  - `[MEDIA ANGLE]` — a topic a Jameel executive could speak to media about, with the hook stated (e.g., "Chinese EV expansion into Europe — Jameel operates the UK GAC launch; credible voice on what European consumers actually ask for").
- Source appendix "ALJ relevance note" → "Jameel relevance: [A/B/C] + brand/territory".

## SECTION 5 — VALIDATION PLAN (mirrors CP-022A method)

1. Held-mode dry run(s) of alj_jameel_weekly_v2 in isolated namespace (retrieval stages only) — same comparison table: kept sources, partner-brand hit rate, territory coverage, publisher concentration, operator usefulness score.
2. Sunday 2026-06-14 13:00 cron runs OLD queries held — serves as baseline + repetition check vs June 9 test briefs.
3. Full pipeline held run with new report template → operator reviews brief quality incl. media angles.
4. Live resumption per ADV-017: WS1 gate closed + separate operator authorization + controlled first delivery.

## SECTION 6 — APPROVALS REQUESTED (sequenced)

1. Section 1 footprint table — confirm/correct brand list (can proceed on public-source basis per operator 2026-06-11).
2. Section 2 scope + Section 3 query families — approve for held-mode dry run (Lane 3, held only, no client exposure).
3. Brave enablement for ALJ — approve as part of dry run.
4. Section 4 report template changes — approve spec; implementation after dry-run evidence.

---
*OPENCLAW-D-CP-023R | v0.1-DRAFT | 2026-06-11 | Sources: jameelmotors.com (our-story, Farizon/JMC/Changan announcements), alj.com, yicaiglobal.com CEO interview, Arab News (GAC UK), bodyshopmag.com (GAC Poland), omodajaecooiraq.com*
