# Session Skills Backlog — Learnings from the 2026-06-28 Discovery/Feedback Session

---
document_id: OPENCLAW_SKILLS_BACKLOG_2026-06-28
version: v1.0
last_updated: 2026-06-28
status: REFERENCE
scope: Candidate reusable Claude Code skills distilled from this session. Each entry =
  a recurring, non-obvious procedure that cost real time to (re)derive. Not yet built;
  this is the backlog and rationale. Build order is a recommendation, not a commitment.
---

## Why these exist

This session re-derived several procedures from scratch — how to call Tavily for Chinese
news, why GDELT blocks this host, how to pull and triage Steve feedback, how to run a WS1
dry-run without touching live. Each is a candidate skill so the next session starts warm
instead of cold.

---

## P0 — highest leverage

### 1. `ws1-dry-run` — run a WS1 brief end-to-end with zero live blast radius
**When:** validating any WS1 change (code, style rule, discovery) before it can reach Lark,
the public site, or GitHub.
**Core facts:** set `CBIZ_DRY_RUN=1` (skips Lark `deliver()` + `publish_to_docs()`); brief is
still written to `state/cbiz_daily/brief_<ts>.md` for review; `CBIZ_NO_DOCS=1` belt-and-braces;
`CBIZ_DISCOVER=1` to exercise the scout. Outputs land in `state/cbiz_daily/` (brief, decisions,
`discovered.json`). Venv: `/root/openclaw_ws2b/venv/bin/python3`.
**Gotchas:** the 7-day delivered-ledger hard-suppresses already-shipped stories *before* evidence
fetch, so a dry-run can look artificially thin (one run was 2 stories, 18/20 suppressed) — judge
thinness against the ledger, not the pipeline. Never deploy a dry-run brief that is thinner than
the day's live edition.

### 2. `ws1-brief-review-gate` — review a brief before any live delivery
**When:** before promoting any dry-run brief or enabling a change in cron.
**Core facts:** READ the full brief; check trust/grounding (every factual bullet ends with a
complete `[Publisher, Date](url)` citation); check editorial-rule compliance against
`cbiz_style.md` (MARKET-SCOPE, MARKET-TIMING, SUMMARY-DEPTH, ATTRIB-DEDUP, ENGLISH-ONLY,
NAMES, BREADTH); check outlet-count honesty (no wire reprint double-counted). Fix-and-redo
until clean; never auto-send a sub-optimal edition.
**Gotchas:** watch for `### ###` double-hash headers (LLM emits `###`, template also prepends
`###` — pre-existing formatting fragility); body "covered by N outlets" prose can under-count
vs the mechanical Sources count (the mechanical count is authoritative).

### 3. `ws1-steve-feedback-triage` — pull and action reader feedback
**When:** operator says "review Steve feedback" or periodically.
**Core facts:** feedback is SQLite on the live BigScoots host at
`/home/thefoote/daily.thefootegroup.com/data/feedback.sqlite`; pull via
`scp -P 2222 -i /root/.ssh/footegroup_deploy thefoote@meg.securedserverspace.com:<path> <local>`.
Columns: id, ts, type, edition, rating, message, email, ua, ip_hash. Map each item to one of:
(a) **code** fix (`cbiz_daily.py` / `build_site.py`), (b) **editorial rule** (append one `- ` bullet
to `cbiz_style.md` under "Editorial rules" — append-only, ALL-CAPS tag, ships next run, no code
change), or (c) already covered by an existing rule / the nightly `ws1_optimizer.py` auto-rule.
**Gotchas:** the optimizer auto-appends rules nightly — check existing rules before adding a
duplicate. Editorial rules are cumulative policy; never rewrite, only append.

---

## P1 — clear value, narrower scope

### 4. `ws1-discovery-ops` — operate and extend the Lane-0 scout
**When:** tuning discovery, swapping providers, or measuring survival.
**Core facts:** providers live behind `DiscoveryProvider` in `cbiz_discover.py`; select with
`CBIZ_DISCOVER_PROVIDER` (mock|tavily|gdelt|gemini|openai); caps via
`CBIZ_DISCOVER_CAP_PER_QUERY` / `_CAP_TOTAL`; queries in `DISCOVER_QUERIES`. The
**proposal→verified survival rate** is the key metric — read it from
`state/cbiz_daily/discovered.json` after each run. Scout is non-authoritative: PROPOSES only,
runs through the same verify path, OFF by default.
**Gotchas:** broad noun queries (`中国经济`) yield soft/official filler → 0 survival; use
event/company/sector queries. Enabling discovery in the 07:10 cron is a P-02 change needing
operator approval.

### 5. `tavily-cn-retrieval` — Tavily for Chinese-language news
**When:** any task needing fresh, real, reachable mainland Chinese news URLs.
**Core facts:** `POST https://api.tavily.com/search`, auth `Authorization: Bearer tvly-...`
(key at `/root/.secrets/tavily.key`); body `{query, search_depth, topic:"news", days, max_results}`.
Free tier ~1,000 searches/mo. **Two mandatory tunings:** `include_domains` pinned to mainland CN
outlets (else it returns CNBC/Bloomberg English editions), and a **client-side freshness gate**
(Tavily's `days=` is loose; drop undated/evergreen results). Discovery is high-precision; let the
crawler own recall.
**Gotchas:** reliable from datacenter IPs (unlike GDELT). Reuse the existing key in place; never
create one.

### 6. `gdelt-rate-limit-survival` — the GDELT datacenter-IP trap
**When:** anyone considers GDELT DOC 2.0 for retrieval.
**Core facts:** free, real URLs, Chinese-filterable (`sourcelang:chinese`), but the documented
1-req/6s limit **escalates to a sticky, extended IP ban** on datacenter IPs — a single request
still 429s hours after the burst that tripped it. Keywords under ~3 chars are rejected ("too
short"). If used at all: ≥6.5s gap, fail-soft, one retry, and a strict ≤1 query/day cadence, or
route through a clean egress IP.
**Gotchas:** background retries from a different cwd need `sys.path.insert` for the module to import.

---

## P2 — generic, cross-project

### 7. `credential-reuse-in-place` — use existing secrets without creating any
**When:** a task needs an API key/token.
**Core facts:** read existing keys from `/root/.secrets/*` or the relevant auth profile; never
create, rotate, or echo a credential value (P-03/R-07). Never echo `git remote -v` for repos
whose remote carries an embedded PAT (e.g. openclaw_docs).
**Gotchas:** classifier blocks on credential creation are expected — respect them, ask the
operator to provision instead.

---

## Recommended build order

P0 first (`ws1-dry-run`, `ws1-brief-review-gate`, `ws1-steve-feedback-triage`) — they gate every
WS1 change and are invoked most often. Then P1 (`ws1-discovery-ops`, `tavily-cn-retrieval`,
`gdelt-rate-limit-survival`) as discovery work continues. `credential-reuse-in-place` is a thin
cross-project guardrail that can fold into existing operating-protocol skills rather than stand alone.
