# OpenClaw — As-Built State (Current-State Reconciliation)

---
document_id: OPENCLAW_AS_BUILT_STATE_2026-06-16
date: 2026-06-16
status: AUTHORITATIVE for current architecture/products/posture (descriptive, not forward plan)
purpose: Reconcile the governing docs (Foundation v6.2, Constitution, dashboards — all pre-pivot)
  with what the system ACTUALLY is after the 2026-06-08..16 architectural pivot. Forward execution
  plan is DEFERRED to after the vision discussion.
---

## 1. What changed (one paragraph)
Between early and mid June 2026 the project pivoted from a Baidu/Brave-retrieval "China Monitor /
PR intelligence" pilot into two concrete intelligence products built on a new **curated-crawl +
evidence-first** architecture. The central trust failure the CEO Dashboard (June 6) flagged as the
critical risk — *valid citation ID but the source does not support the claim* — is now **solved** by
the evidence-first trust model.

## 2. Products (as built)
- **WS1 — China Business Daily** (was "China Monitor"). Daily ranked digest of the **top ~15 China
  business stories** for foreign CEOs, Chinese sources only, facts-not-advice. Sourced from a curated
  19-outlet business-press crawler; ranked by cross-source corroboration; written by DeepSeek with the
  evidence-first trust gate; delivered labeled to the WS1 Lark doc. Daily 07:10 cron. The old
  Baidu Executive-Take/LinkedIn WS1 (06:30 cron) is **retired**.
- **WS2 — ALJ Jameel Motors China Auto Weekly**. Runs on the original retrieval pipeline (Baidu +
  enrichment), now with: full-text enrichment, mechanical citation cap, Chinese-source enforcement,
  per-client Pro model (gemini-2.5-pro), advisory content removed, enriched deterministic appendix,
  clickable dated citations. Held/pilot; labeled internal delivery.
- **WS2B — Source-Packet Intelligence** (designed, plan v1.2; not yet built). Operator-curated premium
  source packets → evidence extraction → two-pass synthesis. The higher-ceiling commercial play.

## 3. Architecture (as built) — note: TWO pipelines exist
- **Evidence-first pipeline (WS1, the new core):** continuous crawler (curated outlet universe) →
  full-text fetch (3-rung ladder: trafilatura → browser-headers → Jina) → **verbatim-grounded evidence
  extraction** (DeepSeek, each record a guaranteed substring of the source) → cluster + authority/
  corroboration ranking → China-relevance filter → synthesis from evidence only → **number-grounded
  verification** → labeled Lark delivery. Host-side; per-stage models; no gateway dependency.
- **Legacy retrieval pipeline (WS2/ALJ):** Baidu/Brave → orchestrator (normalize/dedup/filter/fetch)
  → gateway agent (Gemini primary, **DeepSeek→Kimi failover** wired 06-15) → resolver → scrubber
  (+citation cap) → validator (+citation_alignment) → citation_sub → labeled Lark.

## 4. Trust model — and the key finding
Two divergent verification systems are currently running:
- **WS2 uses the original chain (~100%, enhanced):** resolver → scrubber+cap → validator →
  citation_alignment → citation_sub. Mature; strong on citation *existence*, weaker on claim *grounding*.
- **WS1 uses a new evidence-first gate (~0% shared code):** verbatim-span grounding at extraction +
  number-based grounding at verify. One session old; fundamentally stronger on claim-source grounding
  (solves the June 6 issue).
**Recommendation (for the execution plan):** standardize on **evidence-first** as THE trust system and
migrate WS2 onto it; retire the original once converged. Do not keep two permanently.

## 5. Delivery posture (as built)
**Internal Test Delivery** (adopted 2026-06-12): no external client recipient exists; all delivery
destinations are operator-only Lark docs (allowlisted). Gates **classify and label** (`INTERNAL TEST —
CLEAN / ALIGNMENT WARNING / SOURCE-VERIFIED / …`) rather than block. Strict external gate reserved for
a future `external_client` mode. **Phase D gate-streak framework is RETIRED** — it measured consecutive
clean *external* deliveries toward client-readiness for the old WS1, which no longer maps under this
posture and the pivot.

## 6. Models / providers (as built)
Per-stage: DeepSeek-chat (WS1 clustering + writing; evidence extraction), Gemini-2.5-pro (WS2/ALJ
writing), Gemini-2.5-flash (legacy gateway primary) with **DeepSeek-flash → Kimi failover**. Note:
DeepSeek-v4-flash/v4-pro and Kimi-k2.5 are *reasoning* models that return empty on long inputs — use
`deepseek-chat` for long-context structured/long-output tasks.

## 7. Discovery: build-vs-buy (settled)
Search-API discovery rediscovers ~1% of a monitoring feed; one-shot direct crawl ~20% (cadence-limited).
Verdict: **hybrid** — self-crawl the open high-authority tier (cheap, defensible), and/or consume a
curated/licensed feed; the system is the refinery, not the drill. A week-long continuous-crawl coverage
test is running.

## 8. What this doc does NOT cover
The **forward execution plan and roadmap** are deliberately deferred to after the vision discussion
(operator direction 2026-06-16). This document is descriptive (as-built) only.
