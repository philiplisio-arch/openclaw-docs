# WS1 Lane-0 Discovery Scout — Design, Provider Evaluation, First Findings

---
document_id: OPENCLAW_WS1_DISCOVERY_LANE0_2026-06-28
version: v1.0
last_updated: 2026-06-28
status: ACTIVE (built, validated, gated OFF — not in the live cron)
builds_on: OPENCLAW_WS1_SELECTION_REDESIGN_SPEC_2026-06-23, OPENCLAW_RETRIEVAL_TOOLS_ASSESSMENT_2026-06-11
scope: An additive, non-authoritative discovery layer for WS1 (China Business Daily).
  The deterministic crawler/frontier and the verbatim-grounding trust foundation are
  UNCHANGED and remain the source of truth.
---

## 1. What this is (and is not)

Lane-0 is an **LLM/external discovery scout**: a provider-agnostic component that can
**PROPOSE** candidate articles the deterministic crawler did not surface. It is **not** a
new retrieval authority. Proposals are treated as **untrusted input**:

1. Deduped against the frontier AND the in-window crawler pool.
2. Hard-capped (per-query + per-run) so a misbehaving proposer cannot flood verification.
3. Tagged with provenance (`src_kind="llm"`, `discover_provider`).
4. Appended to the pool and run through the **same** `china_filter → clustering → evidence →
   verbatim-Chinese grounding verify` path as every crawler article.

A proposal with no fetchable Chinese grounding is dropped by `verify()` exactly like any
other article. **The scout can add candidates; it cannot inject facts, retrieve on its own
authority, bypass validation, or alter evidence.**

**OFF by default.** Enabled only with `CBIZ_DISCOVER=1` and a provider key present. Enabling
it in the live 07:10 cron is a separate change requiring explicit operator approval (P-02).

## 2. Implementation

- `cbiz_crawler/cbiz_discover.py` — providers behind one `DiscoveryProvider` interface;
  `discover(arts, queries)` orchestration (dedup, caps, provenance); `DISCOVER_QUERIES`.
- `cbiz_crawler/cbiz_daily.py` — gated hook in `main()` right after `load_articles()`;
  writes a `state/cbiz_daily/discovered.json` sidecar so the **proposal→verified survival
  rate** is measurable every run.
- Knobs (env): `CBIZ_DISCOVER`, `CBIZ_DISCOVER_PROVIDER`, `CBIZ_DISCOVER_CAP_PER_QUERY`,
  `CBIZ_DISCOVER_CAP_TOTAL`, plus per-provider config.

## 3. Provider evaluation

| Provider | Verdict | Why |
|---|---|---|
| **Gemini** (Google Search grounding) | **Rejected** | Confabulates article URLs in TEXT output (real URLs live only in `groundingMetadata.groundingChunks[].web.uri` as redirect links); grounding skews to English/global editions (yicaiglobal, caixinglobal) for Chinese business news. |
| **GDELT DOC 2.0** | **Rejected for this host** | Free, real URLs, Chinese-filterable — but this VPS's datacenter IP gets a **sticky, extended 429 ban**: a single request still returned 429 after a 5-minute and then a 2-hour silence once the burst limit was crossed. Documented limit is 1 req / 6 s; the ban escalates well past that. Fail-soft is built in. Revisit via a clean egress IP or a strict 1-query/day cadence. |
| **OpenAI web_search** (Responses API) | **Deferred** | Reliable, real URLs; needs an API key (not yet provisioned) and a small per-call spend. Provider is scaffolded in code. |
| **Tavily** | **CHOSEN** | Real, reachable URLs (5/5 HTTP 200 in validation), reliable from a datacenter IP, free tier (~1,000 searches/mo) covers ~5 queries/day. Two required tunings below. |

### Tavily tunings (both necessary)
- **`include_domains` pinned to mainland Chinese outlets.** Without it, a Chinese-language
  query still returns English/global editions (CNBC/Bloomberg/BBC) — the same bias that sank
  Gemini. Default list spans the crawler's seed outlets plus major Chinese business/finance
  domains the crawler does not seed.
- **Client-side freshness gate.** Tavily's `days=` filter is loose; broad queries pull in
  undated evergreen/section pages (homepages, year-in-review). We keep only candidates with a
  real publish date inside the window. Discovery is **high-precision; the crawler owns recall.**

## 4. First measurement (2026-06-28 dry-run, no delivery)

- Tavily proposed **10**, kept **10** (all fresh, dated, mainland Chinese-language; 0 frontier/pool dups).
- Overall brief trust check clean (10/10 grounded).
- **Proposal→verified survival: 0 of 10.** None of the discovered articles reached the brief.
  Two compounding reasons:
  1. **Query strategy.** Broad noun queries (e.g. `中国经济`) surface official commentary and
     soft features (a summer-harvest piece), not the specific company/market news that earns a
     slot. Discovery needs **event/company-oriented queries**, not broad topics.
  2. **Ledger suppression.** 18 of 20 ranked clusters were already-delivered (7-day no-repeat
     ledger), leaving a thin 2-story dry-run edition — a poor day to judge added recall.

**Read:** the mechanism is sound and safe (real CN URLs in, full verification, 0 noise leaked
to the brief). The *value* is unproven until the query strategy is fixed and survival is
measured across several days.

## 5. Next steps

1. **Query strategy** — replace broad nouns with event/company/sector-oriented queries; consider
   per-sector rotation. This is the single biggest lever on survival.
2. **Domain breadth** — extend `include_domains` toward quality outlets the crawler does *not*
   seed (where discovery adds the most), not just the existing seed set.
3. **Measure** — run dry-runs across 5+ days, track survival rate and net-new corroboration; only
   then decide promotion.
4. **Cron enable** — gated, separate operator approval (P-02). Until then discovery stays OFF in
   production; the deterministic brief is unaffected.
5. **GDELT/OpenAI** — revisit GDELT via clean egress if a free path is wanted; OpenAI web_search is
   the drop-in paid fallback if a key is provisioned.

## 6. Cost

- Tavily: free tier covers the daily cadence; **$0 to date**. Provider key reused in place
  (`/root/.secrets/tavily.key`), never created by the agent.
- Dry-run LLM spend (DeepSeek V4 Flash) is the normal per-run cost; discovery adds only a few
  extra extractions, all capped.
