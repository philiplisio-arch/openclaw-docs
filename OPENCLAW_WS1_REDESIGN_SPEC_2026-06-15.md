# WS1 Redesign — China Business Daily (for foreign CEOs)

---
document_id: OPENCLAW_WS1_REDESIGN_SPEC_2026-06-15
date: 2026-06-15
status: APPROVED — build begun 2026-06-15 (operator直接 go)
supersedes: old WS1 "China Monitoring Brief" (Executive Take + LinkedIn Draft)
---

## Product
A **daily** ranked digest of the **top 10-15 business news events in China right now**, for a
foreign CEO keeping up to date. Chinese sources only. Facts, not advice. Each story corroborated
across authoritative outlets, with numbers, attribution, and dated citations. Plus a **deep dive
on the day's top 2-3 stories** (depth scaled to importance).

## The core idea — importance = cross-source corroboration
Rank stories by how many independent, authority-weighted Chinese outlets cover the same story the
same day (the QSData "相似文章数" signal, weaponized). What Xinhua + Caixin + Yicai + Securities
Times all run today *is* the news. Importance is measured, not guessed — and it is defensible:
"the stories China's own authoritative press is collectively prioritizing."

## Source universe (Chinese only, tiered — see cbiz_crawler/seeds.yaml)
- **Tier 1 official/regulatory:** NBS, PBOC, MOF, NDRC, MIIT, MOFCOM, SAMR, Customs, State Council, CSRC.
- **Tier 1 state agencies:** Xinhua (news.cn), People's Daily (people.com.cn), CCTV, China Daily, CNR.
- **Tier 2 business/financial press:** Caixin, Yicai, Securities Times, China Securities Journal,
  Shanghai Securities News (cnstock), Economic Observer, 21st Century Business Herald, National
  Business Daily, Cailian (cls.cn).
- **Tier 3 verticals:** 36Kr, Jiemian, LatePost.
- **Hard exclude:** Baijiahao/self-media, k.sina contributors, content farms, unverified Weibo/WeChat.
- Topic span: macro/economy, policy & regulation, finance & markets, trade & supply chain,
  technology, major company news, property, energy.

## Pipeline (reuses the crawler + WS2B refinery)
1. **Crawl** the universe continuously (business/finance/economy section pages) — engine exists.
2. **Extract + dedup** full text (99% fetch, GB18030-safe).
3. **Cluster** articles into stories (embedding near-dup grouping). Score = authority-weighted
   cluster size × recency. [NEW build]
4. **Rank** → top 10-15 today; flag top 2-3 for deep dive.
5. **Synthesize each story from its whole cluster** (corroborated facts, not single-source).
6. **Write** with Pro model + trust discipline + formal formatting.
7. **Verify** (deterministic gates) + deliver.

## Document structure
- Header: "China Business Daily — [date]".
- **THE TOP 15** (ranked). Each entry:
  - **Bold headline** (the development).
  - 2-3 sentences: what happened + **the key number**, "according to [outlets]", dated clickable citations.
  - Corroboration tag: "covered by N outlets incl. Xinhua, Caixin".
  - Category tag: Macro / Policy / Markets / Tech / Trade / Company / Property / Energy.
  - NO significance/advice line (operator direction: facts only).
- **DEEP DIVE** (top 2-3): 1-2 paragraphs each — the fuller picture from the cluster, key figures,
  what is confirmed vs reported, conflicts between sources surfaced. Still facts, no advice.
- **ALSO NOTED** (next ~5): one line each.

## What we apply (this session's lessons)
Curated authority over search; mechanical enforcement over prompt requests (CN-source gate,
citation gate, number+attribution gate); dated+attributed citations at academic standard; Pro
model for writing / cheap for extraction; formal formatting (bold, spacing); report-don't-advise;
corroboration-ranking as the importance signal.

## Build phases
- **P1 (begun):** source universe defined + business crawler running (discovery accumulates daily).
- **P2:** clustering + authority-weighted ranking → daily top-15 list.
- **P3:** synthesis (top 15 + deep dives) via Pro + trust/format discipline + gates.
- **P4:** daily delivery + operator review loop.

## Cadence: DAILY. Top 15 + deep dive on top 2-3 (depth by relevance). No significance framing.
