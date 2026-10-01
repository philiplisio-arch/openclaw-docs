# OpenClaw — As-Built State (Current-State Reconciliation)

---
document_id: OPENCLAW_AS_BUILT_STATE_2026-06-18
date: 2026-06-18
status: AUTHORITATIVE for current architecture/products/posture (descriptive, not forward plan)
supersedes: OPENCLAW_AS_BUILT_STATE_2026-06-16
purpose: Reconcile the governing docs (Foundation v6.2, Constitution, dashboards — all pre-pivot)
  with what the system ACTUALLY is after the 2026-06-08..18 work. Forward execution plan lives in
  internal (local-only) strategy memos, not this doc.
---

## 1. What changed since 06-16 (one paragraph)
WS2 (ALJ Jameel Motors) was migrated off search-API retrieval onto the curated-crawl architecture, so
both live products now share the same sourcing model. The evidence-first trust gate was made
cross-language-correct (it had been false-flagging English briefs written over Chinese-only sources),
and a brittle completeness check that was silently blocking roughly half of WS2 runs was fixed. Source
breadth for WS2 was materially widened (official/association sources, specialist outlets, cross-cutting
tagging, an operator discovery dashboard). The central June-6 trust failure — *valid citation ID but the
source does not support the claim* — remains solved.

## 2. Products (as built)
- **WS1 — China Business Daily.** Daily ranked digest of the top ~15 China business stories for foreign
  CEOs, Chinese sources only, facts-not-advice. Curated ~19-outlet business-press crawl; ranked by
  cross-source corroboration; written by DeepSeek with the evidence-first gate; delivered labeled to the
  WS1 Lark doc (daily 07:10). Recent additions: source appendix, diversified candidate pool (round-robin
  per outlet), uncited-tail stripping.
- **WS2 — ALJ Jameel Motors China Auto Weekly.** Now sourced from the **curated scrape crawler**
  (`OPENCLAW_SOURCE=crawler`); Baidu/Brave retired from the ALJ path. Full-text enrichment, mechanical
  citation cap, Chinese-source enforcement, per-client model via config, clickable dated citations,
  source appendix. All three ALJ configs (daily, Sunday official, test) on crawler. Held/pilot; labeled
  internal delivery.
- **WS2B — Source-Packet Intelligence** (designed; not yet built). The higher-ceiling commercial play.

## 3. Architecture (as built) — convergence in progress
- **Sourcing (shared):** continuous curated-outlet crawler → frontier (SQLite, dedup ledger) →
  per-report retrieval package. Relevance filter (precision-tightened), cross-cutting **tagger**
  (Export/GCC, Toyota/Lexus, dealer, policy, sales-data + authority tier + source-family), and
  diversity-aware retention (per-family cap, priority tags protected).
- **WS1 pipeline:** crawler → full-text (trafilatura → browser-headers → Jina) → verbatim-grounded
  evidence extraction → cluster/rank → China filter → synthesis-from-evidence → number-grounded verify →
  labeled Lark.
- **WS2 pipeline:** crawler → retrieval-package adapter → phase5 orchestrator (normalize/dedup/filter/
  fetch/package) → gateway agent (model from config; Gemini primary with DeepSeek→Kimi failover) →
  resolver → scrubber (+cap) → validator (+citation_alignment) → labeled Lark.
- Both reports now run on curated-crawl sourcing; the trust/synthesis back-ends are still distinct but
  converging.

## 4. Trust model — status
- **WS2 gate (citation_alignment):** numbers + entities vs cited sources; now **cross-language-correct**
  (unmatchable English entity names against CJK-only evidence are excluded, not failed). Warn-only;
  promotion to *blocking* gated on a streak of clean runs.
- **WS1 gate:** verbatim-span grounding at extraction + number-based grounding at verify.
- Direction: converge on one evidence-first gate; promote to blocking after the agreed clean-run streak.

## 5. Delivery posture (as built)
**Internal Test Delivery** (adopted 2026-06-12): all destinations are operator-only Lark docs
(allowlisted). Gates classify and label (CLEAN / ALIGNMENT WARNING / SOURCE-VERIFIED / …) rather than
block. Strict external gate reserved for a future `external_client` mode. No external client recipient
exists.

## 6. Models / providers (as built)
Per-stage: DeepSeek-chat (WS1 clustering + writing; evidence extraction), per-client model for WS2/ALJ
set in client config (not a CLI flag — the prior `--model` flag was unsupported and caused crashes;
fixed). Gateway primary Gemini with DeepSeek-flash → Kimi failover. Reasoning models (deepseek-v4,
Kimi-k2.5) return empty on long inputs — use `deepseek-chat` for long-context tasks.

## 7. Discovery: tooling status (live-audited 2026-06-18)
Curated self-crawl of the high-authority tier is the spine. Official/association portals
(CAAM/CADA reachable and yielding; MIIT/NDRC/SAMR reachable, low auto-yield) added as seeds. Evaluated
and not adopted: a free global-news API (wrong corpus — non-Chinese), an aggregator feed (URLs not
cleanly fetchable), and headless rendering (installed and capable, but target specialists are
bot-protected — kept dormant). Verdict unchanged: the system is the refinery, not the drill.

## 8. What this doc does NOT cover
The forward execution plan, roadmap, and competitive analysis live in **internal local-only strategy
memos** (not in this public docs set). This document is descriptive (as-built) only.
