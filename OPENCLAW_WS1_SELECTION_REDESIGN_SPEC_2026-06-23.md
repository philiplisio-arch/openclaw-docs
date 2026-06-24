# WS1 Selection-Layer Redesign — China Business Daily

---
document_id: OPENCLAW_WS1_SELECTION_REDESIGN_SPEC_2026-06-23
date: 2026-06-23
status: IMPLEMENTED & LIVE 2026-06-24 (commits e85b855, 890321f) — §3.1–3.4 (dates, deterministic
  clustering, real corroboration, recency ranking) and the client-grade format shipped; §3.5
  (qualitative-claim verify) and §3.6 ALERTS.log no-delivery alerting remain OPEN (Issues #75–#76)
builds_on: OPENCLAW_WS1_REDESIGN_SPEC_2026-06-15 (product/concept unchanged)
scope: The selection + ranking + verification layer in cbiz_crawler/cbiz_daily.py.
  Crawler, fetch ladder, Lark delivery, and the verbatim-grounding trust FOUNDATION are
  sound and are NOT being rebuilt.
---

## 1. Why this exists (the gap between spec and build)

The approved 2026-06-15 spec already calls for the *right* design: importance = **measured**
cross-source corroboration **× recency**, with each story **synthesized from its whole cluster**.
The as-built pipeline silently deviated from that spec on three points, producing the failures
found in the 2026-06-23 deep assessment:

| Concern (operator) | Spec said | Build actually does | Result |
|---|---|---|---|
| Use the source material | synthesize from whole cluster | caps at 144 candidates, ~15 forced stories, **3 sources/story** | ~755 daily articles → ~19 cited |
| Factual | trust gates | verbatim grounding (good) **but verify checks numbers only**, pooled-set matching | qualitative claims unverified; coincidental number matches |
| Relevant, esp. dates | cluster size **× recency** | window = **crawl-time**, ranker is **date-blind**, no recency term | 35 stale items (3–12 days old) in today's window; 46% undated |
| (corroboration signal) | measured cluster size | **LLM free-text `outlet_count`** | "covered by 10 outlets" from an 8-outlet pool — fabricated |

**Conclusion: this is an execution fix, not a concept change.** We implement the selection layer
the original spec already specified, mechanically.

## 2. Design principles (reaffirmed)

- **Measured, not guessed.** Corroboration and recency are computed from data, never emitted by an LLM.
- **Mechanical enforcement over prompt requests.** Deterministic gates; the LLM writes prose and makes
  significance/tie-break judgments only.
- **Recency is first-class**, equal to corroboration in ranking.
- **Keep what works:** the crawler, the 3-rung fetch, and verbatim-Chinese grounding are untouched.

## 3. Component changes

### 3.1 Publish-date normalization (NEW, deterministic) — fixes Concern 3
- Derive a reliable `pub_date` for every article via, in order: (a) existing crawler `pub_date`;
  (b) date embedded in the URL path (Chinese outlets commonly encode it: `/2026/0623/`,
  `/20260622/`, `/2026-06-22/`); (c) `<meta>`/article date parsed during full-text fetch.
- **Window is publish-time, not crawl-time.** Admit an article only if its derived `pub_date`
  is within the window (default **48h**, configurable). The current `first_seen >= cut` admission
  path is removed as a primary gate.
- Articles with no derivable date go to an **"undated" bucket**: excluded from the ranked top,
  available only as supporting corroboration for an already-dated cluster.

### 3.2 Deterministic clustering + real corroboration — fixes the fabricated count
- Cluster in-window articles by near-duplicate similarity (title/entity tokens; SimHash or
  embeddings). Mechanical, so it scales to the full window with no LLM long-input limit.
- `outlet_count = COUNT(DISTINCT outlet)` among **actual** cluster members. The LLM's free-text
  `outlet_count` is **deleted**. "Covered by N outlets" becomes a fact or it isn't printed.
- Single-source clusters are labeled honestly (no corroboration claim) and down-weighted, not
  dressed up.

### 3.3 Authority-weighted, recency-aware ranking — fixes Concern 3 + restores the spec formula
- `score = authority_weight × corroboration(distinct outlets) × recency_decay(hours_since_pub)`
  - `authority_weight`: from the existing source tiers (Tier 1 official/state > Tier 2 press > Tier 3 verticals).
  - `recency_decay`: monotonic penalty on age (e.g. full weight ≤24h, decaying to near-zero by 72h).
- The LLM ranking step (if retained) receives **dates and the outlet list** and is restricted to
  significance tie-breaking; it no longer selects blind.

### 3.4 Raise the funnel caps — fixes Concern 1
- **Candidate pool:** remove the 144 cap as a hard ceiling; mechanical clustering consumes the full
  in-window set. (LLM is no longer the clustering bottleneck.)
- **Per-story sources:** lift the 3-source cap; cite up to the cluster's real distinct outlets,
  capped at ~6–8 for readability — so corroboration is *shown*, not just claimed.
- **Story count:** dynamic — every cluster above an importance threshold, targeting ~12–18.
  Header states the **actual** count ("THE TOP 13"), never a fixed "TOP 15" when it's 7.

### 3.5 Deeper trust gate — fixes Concern 2
- Keep the verbatim-Chinese grounding foundation (it works).
- Extend `verify()` to **qualitative claims**: every fact-bearing sentence must map to an evidence
  record's `fact_en`; unmapped sentences are dropped, not merely flagged.
- **Tighten number matching:** check a claim's figure against the **specific cited source's**
  evidence numbers, not the pooled set across all sources — kills coincidental matches.

### 3.6 Reliability
- WS1 writes failures to `ALERTS.log` (it currently does not); a no-delivery day must alert.
- Guard against the 2026-06-19 `category` KeyError class with schema defaults at cluster output.

## 4. Validation plan (before live)
- **Replay** the new selection layer over the last 7 days already in the frontier (offline; dry-run
  delivery) and report: stale-leak count (target **0**), median citations/story (target **≥2**),
  share of stories with real multi-outlet corroboration, and honest top-N count.
- Side-by-side 3 days old-vs-new for operator review before promotion to the live cron.

## 5. Cost note (approval gate)
The redesign adds: optional embedding calls for clustering (or a free local SimHash), and more
full-text fetches + evidence extractions because more sources are cited per story. Net LLM spend
per daily run rises roughly in proportion to citations/story (from ~19 to an estimated ~40–60
extractions). A precise per-run estimate will be provided before any live or replay run that spends
tokens. **No paid run without explicit approval.**

## 6. Sequencing
1. **Dates first** (3.1 + 3.3 recency) — the credibility risk.
2. **Volume** (3.2 + 3.4) — make corroboration real and use the corpus.
3. **Verification depth** (3.5) and reliability (3.6).

## 7. Explicitly NOT in scope
Crawler/seed universe, fetch ladder, Lark delivery, the product concept, and the verbatim-grounding
trust foundation. This spec changes how stories are *selected, ranked, corroborated, and dated* —
nothing upstream of the frontier or downstream of the writer.
