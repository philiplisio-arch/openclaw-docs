# OpenClaw — Handover / Transition Note (2026-06-17)

For starting a fresh conversation. Read this + `OPENCLAW_AS_BUILT_STATE_2026-06-16.md` first.
Durable memory: `/root/.claude/projects/-root/memory/` (esp. `ws2b-build.md`, `MEMORY.md`).

## 1. Where we are (one paragraph)
The project pivoted (early–mid June) from a Baidu/Brave "China Monitor / PR intelligence" pilot into
two products on a new **curated-crawl + evidence-first** architecture. The central trust failure
(June 6: "valid citation but source doesn't support the claim") is **solved** for WS1 via evidence-first
grounding. Governance docs were reconciled 2026-06-16; the forward execution plan is **deliberately
deferred to a VISION DISCUSSION** (the next strategic step), after which we set the plan.

## 2. Products & status
- **WS1 — China Business Daily** (LIVE, daily 07:10). Top-~15 China business stories for foreign CEOs,
  Chinese sources only, facts-not-advice, ranked by cross-source corroboration, evidence-first trust,
  delivered labeled to the WS1 Lark doc. Pipeline: `/root/openclaw_ws2b/cbiz_crawler/cbiz_daily.py`.
  Crawler (19 outlets) every 3h, frontier ~1,500 articles. Old Baidu WS1 retired.
- **WS2 — ALJ Jameel Motors** (held/pilot, labeled). Legacy retrieval pipeline + this month's
  enhancements (citation cap, CN-source enforcement, gemini-2.5-pro writing, advisory removed,
  enriched appendix, clickable cites). Sunday 13:00 cron + daily experiment leg.
- **WS2B — Source-Packet Intelligence** (designed, plan v1.2, NOT built). Higher-ceiling commercial play.

## 3. Architecture — TWO pipelines (the key strategic fact)
- **Evidence-first (WS1, the better core):** crawl → 3-rung fetch (trafilatura→browser→Jina) →
  verbatim-grounded evidence extraction → cluster + corroboration ranking → China-relevance filter →
  synthesize from evidence only → number-grounded verify → labeled Lark. Host-side, per-stage models.
- **Legacy retrieval (WS2/ALJ):** Baidu/Brave → orchestrator → gateway agent (Gemini, **DeepSeek→Kimi
  failover** wired) → resolver → scrubber+cap → validator+alignment → citation_sub → labeled Lark.
- **Trust systems split:** WS2 uses ~100% of the original verification; WS1 uses ~0% (its own
  evidence-first gate). **Recommendation: standardize on evidence-first, migrate WS2 onto it, retire the
  original.** This is a flagship execution-plan item — decide in the vision session.

## 4. OPEN DECISIONS for the VISION SESSION (do these before the execution plan)
1. **Converge the two trust systems onto evidence-first?** (recommended yes) — migrate WS2.
2. **Priority: WS1 (China Business Daily) vs WS2B (packets)?** Both need work; which is the headline.
3. **External-client timeline** — currently Internal Test posture (no external client; labels not blocks).
4. **WS2B build go/no-go** (it's designed, not built).

## 5. Pending WS1 hardening (from the 2026-06-16 brief-review memo — agreed valid, NOT yet done)
1. **"THE TOP 15" shows only ~7 items** — china-filter + evidence-empty skips cut it; rank more
   candidates so ~15 survive, make the header honest.
2. **Claim-level trust table** — the trust line says "N partial" but not which; add claim/source/status/reason.
3. **Source appendix + URLs** for China Business Daily & Deep Dive (per-figure traceability).
4. **Macro-source authority weighting.**
(These are WS1 *improvements*; fold into the post-vision execution plan or action on request.)

## 6. What's running (all token-free except the WS1/WS2 LLM synthesis)
Crons: WS1 biz crawler 3h + WS1 China Business Daily daily 07:10; auto crawler 3h (week coverage test);
ALJ Sunday 13:00 + ALJ daily experiment 07:32. Services: Lark relay (:8787, replace-mode now paginates
the clear — fixed a doc-pollution bug 06-16), OpenClaw gateway (Gemini→DeepSeek→Kimi failover).

## 7. Technical gotchas (so they're not rediscovered)
- DeepSeek-v4-flash/v4-pro and Kimi-k2.5 are **reasoning models** → return EMPTY on long inputs. Use
  **`deepseek-chat`** for long-context structured/long-output tasks.
- Chinese sites need GB18030 decode (mojibake otherwise) and the 3-rung fetch ladder (36Kr/cnstock are JS).
- Lark "replace" must paginate the clear (fixed) or docs accumulate stale content.
- Crawlers: SQLite needs `busy_timeout` to avoid lock crashes when runs overlap.
- Reasoning models exhaust tokens → `finish_reason: length`, empty content.

## 8. Posture / governance
Internal Test Delivery (labels not blocks; operator-only Lark docs). Phase D gate-streak **RETIRED**.
Docs reconciled (as-built doc authoritative; Foundation/CEO-Dashboard/Phase-Gate carry superseded banners).

## 9. How to resume
Read this + as-built doc + `ws2b-build.md` memory. The immediate next step is the **vision discussion**;
after it, write the execution plan. WS1 product fixes (§5) and the trust-system convergence (§3) are the
main known work. Nothing is broken; system is healthy as of 2026-06-17.
