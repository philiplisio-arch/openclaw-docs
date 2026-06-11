# OpenClaw Retrieval-Tools Assessment
Date: 2026-06-11 | Author: Claude (operator-requested) | Status: v1.0 for operator review
Evidence basis: vendor docs/pricing verified by web research 2026-06-11; hands-on tests run from this VPS same day; failure data from live OpenClaw runs (2026-06-08 → 2026-06-11).

---

## 1. Executive recommendation

**Top 5 tools to test immediately**
1. **Jina Reader** (full-text extraction fallback) — VALIDATED TODAY on this VPS: extracted clean full text + publication date from a Sohu article our Playwright fetcher classified as boilerplate-only, and from a Baijiahao page (Baidu's own anti-bot, one of the hardest Chinese targets). Free tier, no key, one-line integration.
2. **GDELT DOC 2.0 API** (free cross-language news corroboration) — VALIDATED reachable from this VPS; supports `sourcelang:zho`; free; strict 1-req/5s rate limit (fine for cron, bad for bursts).
3. **SerpAPI Baidu engine** (resilient Baidu discovery) — structured Baidu SERP JSON without maintaining our own scraper against Baidu's WAF; $25–75/mo trial tier.
4. **Google Programmable Search (CSE)** — googleapis.com confirmed reachable from this VPS (64ms); 100 free queries/day; international corroboration breadth alongside Brave.
5. **Firecrawl** (paid extraction escalation) — markdown-clean scraping with stealth mode (5 credits/page) for bot-protected sites; free 500–1,000 credits/mo to trial.

**Top 3 most likely to improve source quality:** Jina Reader (full text = better grounding & alignment), GDELT (independent corroboration signal per claim), a deterministic domain-tier table (not a tool purchase — build it; see §5 Layer 4).

**Top 3 most likely to improve Chinese-source retrieval:** Jina Reader (today's tests beat our fetcher on 2/2 hard Chinese pages), SerpAPI/SearchApi Baidu+Sogou engines (engine redundancy), Newrank/Qingbo (WeChat official-account data — operator-procured commercial route; the only sustainable WeChat path).

**Avoid or defer:** Bing Search API (RETIRED Aug 2025; Azure "Grounding with Bing" replacement is ~$35/1k, returns no raw results — unusable for citation-grade work); Diffbot ($299/mo entry, solves entity extraction we don't need); Browserbase (we already run Playwright locally; hosted browsers add cost + data egress for no capability gain); direct WeChat/Sogou-weixin scraping (adversarial anti-bot, account bans, governance risk); NewsAPI (thin Chinese coverage, 1-month history); MediaCloud (research-grade aggregates, no full text).

---

## 2. Current OpenClaw retrieval gaps (evidence from our own runs)

| Gap | Evidence | Client impact |
|---|---|---|
| **Full-text failure rate** | ALJ enriched run today: of 176 sources, 91 fetched, 41 failed, ~44 chrome-only junk. Jina succeeded on 2/2 pages we failed. | Briefs grounded on snippets → shallow bullets, weaker citation alignment. |
| **Single-engine China discovery** | ALJ is Baidu-only (16 queries). Baidu serves spam farms (today's `3g.*.kakuyun.vip` cluster) and weak date metadata (timestamp inference required; freshness gate already patched once 2026-06-08). | Misses anything Baidu ranks poorly; spam dilutes the 20–30 source cap. |
| **No corroboration layer** | A claim cited to one Tier-4/5 source cannot be cross-checked automatically; tier discipline lives only in the prompt. | Source-authority errors reach delivered briefs unflagged. |
| **No WeChat/Weibo coverage** | Chinese auto industry discourse (OEM announcements, KOL pressure campaigns) increasingly lives in official accounts, not the open web Baidu indexes. | Blind spot for exactly the PR-intelligence signal clients pay for. |
| **Prompt-only quality rules don't hold** | Today's A/B: agent ignored CITATION ECONOMY rule under full-text volume (6-source citation trains). | Quality rules must be enforced mechanically post-hoc, not requested. |
| **Provider safety refusals** | History of sed-rewriting source text to dodge refusals (removed 33f43a3) — symptom of sending raw geopolitical text to a safety-tuned model with no fallback provider. | Run failures on legitimate news weeks (Iran, sanctions, military topics). |

Which matter most for client-grade PR intelligence: **full-text failure rate** (directly caps brief depth — the exact complaint CP-026 answers) and **no corroboration layer** (citation reliability is the product's spine; Option B measures alignment but nothing measures source trustworthiness).

---

## 3. Tool-by-tool assessment matrix

Depth = full-text/detail gain; Breadth = discovery gain; Quality = evidence/citation gain. ✓✓ strong, ✓ some, — none.

| Tool | Category | Depth | Breadth | Quality | China fit | Full text | Integration | Cost | Security risk | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|
| Baidu direct (current) | CN discovery | — | ✓✓ | — | Native | No | Done | Free (fragile) | Low | **Core (keep)** |
| Brave Search API (current) | Intl discovery | — | ✓✓ | — | Weak | No | Done | $5/1k, $5 free/mo | Low | **Core (keep, re-enable for corroboration)** |
| Playwright fetcher (current) | Extraction | ✓✓ | — | ✓ | Good | Yes (~52% today) | Done | VPS only | None | **Core (keep as first attempt)** |
| **Jina Reader** | Extraction | ✓✓ | — | ✓✓ | **Tested: excellent** | Yes + metadata | Trivial (HTTP GET) | Free tier; ~$20/mo paid; 100 RPM free | Med: URLs+content transit Jina (US) | **Core — adopt as fallback** |
| **GDELT DOC 2.0** | News corroboration | — | ✓✓ | ✓✓ | 65-lang incl. zh, machine-translated | No (links only) | Easy (REST, no key) | Free | Low (queries visible) | **Core — corroboration layer** |
| **SerpAPI** | SERP API (Baidu/Sogou/Google +80) | — | ✓✓ | ✓ | Good (Baidu engine) | No | Easy (REST) | $25/mo 1k → $75/mo 5k | Med: query stream to vendor | **Secondary — paid trial** |
| Google Programmable Search | Intl discovery | — | ✓✓ | ✓ | Weak (CN sites de-indexed) | No | Easy; reachable from VPS | 100/day free; $5/1k to 10k/day | Low–Med | **Secondary** |
| **Firecrawl** | Extraction/crawl | ✓✓ | ✓ | ✓ | Moderate (stealth helps) | Yes, markdown | Easy (REST/self-host) | Free 500cr → $16–99/mo; stealth 5cr/page | Med | **Secondary — escalation tier** |
| Tavily | AI search+extract | ✓ | ✓ | ✓ | **Unverified** for zh — must benchmark | Partial | Easy (REST/MCP) | Free 1k cr/mo → $30+/mo | Med | **Experimental** |
| Exa | Semantic search | ✓ | ✓ | ✓ | English-leaning; zh unverified | Yes (contents incl.) | Easy | Free 1k/mo → $5–15/1k | Med | **Experimental** |
| Apify (Baidu/Weibo actors) | Scraper marketplace | ✓ | ✓ | — | Actor-dependent | Actor-dependent | Medium (per-actor QA) | $5 free/mo → $29+/mo | Med–High (3rd-party actor code) | **Experimental** |
| Event Registry | News aggregation | — | ✓✓ | ✓ | 300k+ sources, some zh | No | Easy | Expensive (€hundreds/mo) | Med | **Defer (cost)** |
| RSS (MIIT/MOFCOM/CAAM/outlets) | Regulatory monitoring | ✓ | ✓ | ✓✓ | Native official sources | Links→fetch | Easy (cron + feedparser) | Free | None | **Secondary — build** |
| Newrank 新榜 / Qingbo 清博 | WeChat/Weibo monitoring | ✓✓ | ✓✓ | ✓ | Native (the only legal WeChat path) | Yes (article text+stats) | Hard (CN procurement, zh contracts, likely CN entity/payment) | ¥ thousands/yr, opaque | Med: client topics exposed to CN vendor | **Operator-only — procurement decision** |
| Sogou-weixin scraping (DIY) | WeChat | ✓ | ✓ | — | Adversarial | Fragile | Hard, breaks constantly | Proxy costs | **High: bans, ToS, uncontrolled behavior** | **Reject** |
| NewsAPI | News API | — | ✓ | — | Thin zh coverage | No | Easy | $0–449/mo | Low | **Reject** |
| Bing API / Azure Grounding | Intl discovery | — | ✓ | — | n/a | No raw results at all | Heavy (Azure AI Foundry project) | ~$35/1k | Med | **Reject** |
| Diffbot | Entity extraction | ✓ | — | ✓ | Moderate | Yes | Easy | $299/mo entry | Med | **Reject (cost vs need)** |
| Browserbase | Hosted browsers | ✓ | — | — | Unknown CN egress | Yes | Medium | ~$50+/mo | Med–High | **Reject (redundant w/ local Playwright)** |
| MediaCloud | Media research | — | ✓ | ✓ | Some zh | No | Medium | Free | Low | **Reject (no full text)** |
| MCP servers (Tavily/Firecrawl/Brave/Exa) | Agent tooling | — | — | — | n/a | n/a | n/a for cron | Bundled | **High in cron** (agentic, non-deterministic) | **Operator-side only** |

---

## 4. Detailed notes on recommended tools

### 4.1 Jina Reader — adopt (Core)
- **A/B:** `GET https://r.jina.ai/<url>` returns markdown article text + title + published time. Use case: fallback in `content_fetcher.py` when Playwright yields `chrome_only`/`error`.
- **C:** Depth + quality (publication dates fix exactly the date-attribution problem patched in citation_sub today).
- **D (China):** Tested today: full text from `news.sohu.com` (16KB, our fetcher got boilerplate-only) and `baijiahao.baidu.com` (4.9KB clean). 2/2 on pages we failed.
- **E/F:** Full text yes; structured enough (title/URL/date/markdown body) to map onto our `full_text`/`timestamp` fields directly.
- **G:** Improves evidence grounding; does not itself verify claims.
- **H:** Trivial — one HTTP call; fits `_fetch_one()` fallback branch. Cron-safe, deterministic, logs cleanly into existing `[FETCH]` trace.
- **I/J/K:** Keyless free use (rate-limited); free API key = 10M tokens; paid ~$20/mo. Free key: 100 RPM / 100K TPM — enough for ~50 fallback fetches/run.
- **L (security):** URLs and retrieved content transit Jina's (US) infra. We send only public article URLs already present in the retrieval package — no client identity, no credentials, no local file access. Acceptable; document in governance.
- **M:** Jina AI, established vendor, actively maintained.
- **N:** Per-IP throttling possible at volume; occasional CAPTCHAs on hardest sites; latency higher than direct fetch (~3–8s).
- **O:** Core.
- **P (tests):** run the 41 failed + 44 chrome-only URLs from today's ALJ run through it; measure recovery %, text quality, latency; verify no truncation vs MAX_TEXT_CHARS.

### 4.2 GDELT DOC 2.0 — adopt (Core, corroboration)
- **A/B:** Free global news index, 65 languages machine-translated, 15-min updates. Use case: per-claim corroboration probe ("is this development reported by >1 independent domain?") and weekly sweep for Jameel-footprint topics in non-Chinese press.
- **C:** Breadth + quality (corroboration count is a cheap confidence score).
- **D:** Monitors Chinese-language media (`sourcelang:zho`), returns links/domains/dates — useful as discovery and corroboration, not as text source.
- **E/F/G:** No full text (links only → feed into L3 extraction). JSON output. Strong citation usefulness: independent-domain counts and date confirmation.
- **H:** Easy: keyless REST. Tested from this VPS — works.
- **I/J/K:** Free, no account. HARD limit 1 request/5 seconds (observed today: violating it returns plain-text error and brief throttling). Cron must serialize with sleeps.
- **L:** Queries visible to GDELT; public-interest research infra; low risk.
- **M:** Long-running academic project; stable for a decade; single-maintainer API quirks.
- **N:** Machine-translation artifacts; coverage skews to indexed web news (not WeChat); no SLA.
- **O:** Core (corroboration layer).
- **P:** for the last 3 delivered briefs, query each Section-1/2 claim's topic; measure % of claims corroborable, zh recall vs our Baidu set, latency at 1 req/5s.

### 4.3 SerpAPI (Baidu engine) — paid trial (Secondary)
- **A/B:** Commercial SERP API, 80+ engines incl. Baidu (web + news) and Sogou. Use case: redundancy/replacement for our hand-rolled `baidu_executor` when Baidu's WAF rotates, plus Baidu News vertical we don't currently query.
- **C:** Breadth + reliability (their proxies/parsers absorb the anti-bot arms race).
- **D:** Purpose-built Baidu support; structured JSON with positions, snippets, dates.
- **E:** No full text (SERP only) → L3.
- **F/G:** Clean structured output; only discovery-level evidence.
- **H:** Easy REST; drop-in parallel to `brave_executor.py` pattern (API key via env, consistent with d297a93).
- **I/J/K:** Account + key. $25/mo (1k searches) trial; $75/mo (5k). Only successful searches billed. Our scale: ALJ 16 queries + WS1 ~10/week ≈ trivial volume.
- **L:** Our query stream (client topics) goes to SerpAPI (US). Same exposure class as Brave today. No local access.
- **M:** Most established SERP vendor; stable for years.
- **N:** Cost at scale; SERP parsing can lag Baidu layout changes (their problem, but outages happen).
- **O:** Secondary — adopt if Baidu direct breaks more than once a quarter, or to add Baidu News + Sogou verticals.
- **P:** run our 16 ALJ queries through SerpAPI Baidu and diff against `baidu_executor` results: overlap %, unique authoritative finds, date quality.

### 4.4 Google Programmable Search — trial (Secondary)
- **B:** International corroboration breadth next to Brave (different index). 100 free queries/day covers both clients' weekly needs entirely.
- **D:** Weak for mainland Chinese content; intended for Section-4/INTL corroboration only.
- **H:** Reachable from this VPS (verified, 64ms). REST + key + CSE ID.
- **J/K:** Free 100/day; $5/1k beyond, 10k/day hard cap.
- **N:** Index restricted to configured CSE scope; result quality depends on CSE setup; Google account/billing required.
- **O:** Secondary. **P:** same-queries diff vs Brave on a Sunday ALJ run; count unique authoritative INTL sources.

### 4.5 Firecrawl — escalation tier (Secondary)
- **B:** Markdown-out scraping API with stealth mode for bot-protected sites; also search+crawl. Use case: third rung of extraction ladder (Playwright → Jina → Firecrawl stealth) for high-value URLs that defeat both.
- **D:** Moderate China fit — stealth/proxies help on CN portals; not tested today (needs key).
- **H/I/J:** Easy REST; free 500–1,000 credits/mo to trial; Hobby $16–19/mo; stealth = 5 credits/page so reserve for Tier-1/2 sources only. Self-host option exists but lacks the anti-bot features that are the whole point.
- **L/M:** Content transits vendor (US); well-maintained, very popular (most-starred web-research tooling).
- **O:** Secondary. **P:** feed it whatever URLs Jina fails on from the 4.1 test; measure marginal recovery per credit.

### 4.6 RSS regulatory layer — build (Secondary, no vendor)
MIIT/MOFCOM/NDRC/SAMR announcement feeds, CAAM/中汽协 stats, plus 2–4 quality auto outlets. `feedparser` + cron, output normalized into the retrieval package as Tier-1 sources. Free, zero third-party exposure, directly raises source-authority mix. Test: 2-week shadow run; count Tier-1 items surfaced that Baidu queries missed.

### 4.7 Newrank/Qingbo (WeChat) — operator-only procurement decision
The only sustainable, legal route to WeChat official-account content (Qingbo claims 620k accounts, 24h refresh, article text + engagement stats). Everything DIY (Sogou-weixin scraping, client automation) is adversarial, ban-prone, and a governance risk — rejected. Procurement realities: Chinese-language contracts, likely CN payment/entity, pricing opaque (expect ¥5k–50k/yr depending on scope). Client-sensitive topics would be visible to a CN vendor — needs explicit operator/client comfort. Recommendation: operator decides whether WeChat coverage justifies procurement; technically we'd integrate their REST API like any executor.

### 4.8 MCP servers — operator-side only
Tavily/Firecrawl/Brave/Exa all ship MCP servers. Useful inside Claude Code for ad-hoc operator research; **not recommended inside the cron pipeline**: MCP adds an agentic, non-deterministic layer where OpenClaw needs auditable, repeatable REST calls with logged inputs/outputs. Our governance requirement ("no uncontrolled agent behavior") is better served by the same vendors' plain APIs. No "ClawHub" skill registry with vetted retrieval skills was found in research worth adopting over direct APIs.

---

## 5. Proposed target retrieval architecture

Maps onto the existing pipeline (`query_builder → executors → normalize/dedupe/filter → content_fetcher → package_builder → agent → validator/citation_sub`); each addition is a new executor or a fallback branch, all behind env switches per house pattern.

- **Layer 1 — China-first discovery:** `baidu_executor` (keep) + SerpAPI Baidu News vertical (trial) + RSS regulatory feeds (build). Future: Qingbo WeChat executor if procured.
- **Layer 2 — International/offshore corroboration:** `brave_executor` (re-enable for ALJ as corroboration-only, not narrative) + Google CSE (trial) + GDELT sweep.
- **Layer 3 — Full-text retrieval ladder:** Playwright (current, free, first) → Jina Reader fallback on `chrome_only`/`error` (adopt now) → Firecrawl stealth for residual high-value misses (paid, capped). Every rung logs `fetch_status` + provider into the existing trace files — fully auditable.
- **Layer 4 — Source-quality scoring (build, not buy):** deterministic domain-tier YAML (Tier 1–5 mapping replacing prompt-only tiers), spam-domain blocklist (seed with today's `kakuyun.vip`/`newok.cc`/`lffmgs.cc` cluster), GDELT corroboration count per claim topic, syndication/dup detection across domains. Output: per-source `tier`, `corroboration_n`, `confidence` fields in the retrieval package.
- **Layer 5 — Evidence packaging:** existing `build_agent_input_slim` + the Layer-4 fields, so the agent sees tier/confidence per source instead of being asked to infer authority.
- **Layer 6 — Citation & claim-support audit:** existing Option B alignment gauge (promote to blocking per plan) + mechanical citation-economy enforcement in scrubber (today's A/B showed the prompt rule doesn't hold) + agent_source_map resolver (live).

---

## 6. Pilot test plan

**Benchmark queries (12)** — run identically through each candidate, offline namespaces, no delivery:
1. 比亚迪 土耳其 工厂 (BYD Türkiye plant — ALJ core)
2. 广汽埃安 英国 出口 (GAC AION UK — ALJ)
3. 奇瑞 中东 经销商 (Chery/Omoda Iraq-GCC distribution — ALJ)
4. 中国汽车出口 关税 欧盟 (China auto export EU tariffs — ALJ INTL)
5. 长安汽车 南非 (Changan South Africa — ALJ)
6. 丰田 中国 市场份额 电动化 (Toyota China position — ALJ)
7. 中国车企 IPO 港股 (China auto IPO — WS1 finance)
8. 外资企业 中国 监管风险 数据安全 (MNC regulatory risk — WS1)
9. 中美 贸易 汽车 芯片 (US-China trade/auto-chips — WS1)
10. 中东主权基金 中国投资 (ME SWF China investment — WS1)
11. "BYD Turkey factory" (English mirror of #1 — cross-language comparison)
12. "China EV exports Gulf" (English — INTL corroboration)

**Per-tool metrics:** relevant results in top 10; authoritative (Tier 1–2) count; Chinese-source recall vs Baidu-direct baseline; full-text success rate (extraction tools, on the result URLs); duplicate/syndication rate; citation risk (does the tool return real URLs + real dates — spot-check 5 per tool); latency p50; cost per useful result; integration effort (hours, estimated after writing one executor).

**Harness:** one `retrieval_bench.py` writing per-tool JSONL to `openclaw_traceability/retrieval_bench/{date}/` — same audit pattern as ADV-016. Existing namespaced offline runs prove this is safe to run any day.

**Extraction-specific test (highest value, zero query cost):** replay today's 85 failed/chrome-only ALJ URLs through Jina (free) and Firecrawl trial; the recovery rate directly predicts CP-026 quality gain.

---

## 7. Final recommendation — adoption roadmap

| Step | What | Lane | Cost | Needs |
|---|---|---|---|---|
| Now | Jina Reader fallback in `content_fetcher.py` behind `OPENCLAW_FETCH_FALLBACK=jina`; replay today's 85 failed URLs as acceptance test | Lane 3 | Free | Operator approval of the patch |
| Now | GDELT corroboration probe script (read-only, no pipeline change); evaluate on last 3 briefs | Lane 3 (additive) | Free | None beyond approval |
| Now | Spam-domain blocklist + domain-tier YAML (Layer 4 seed) | Lane 3 | Free | Operator approval |
| Week 2 | Google CSE trial key; Sunday diff vs Brave | Lane 3 | Free tier | Google account |
| Week 2 | SerpAPI $25 trial: Baidu engine diff + Baidu News vertical | Lane 3 | $25 one month | Operator approves spend |
| Week 3 | Firecrawl free-credit trial on residual extraction misses | Lane 3 | Free credits | Account |
| Security review before any adoption | Data-egress note per vendor (what leaves the VPS: public URLs + queries only; never package contents, configs, env, client identity) | Lane 2 | — | Operator sign-off |
| Cron integration | Only after each tool passes its §6 benchmark AND the CP-026/Phase D gates settle — one change at a time per house rule | Lane 3 | — | Per-item approval |
| Operator-only | Newrank/Qingbo WeChat procurement decision | Lane 2 / commercial | ¥5k–50k/yr est. | Operator/client decision |
| Reject | Bing/Azure Grounding, Diffbot, Browserbase, NewsAPI, MediaCloud, DIY WeChat scraping, MCP-in-cron | — | — | — |

**Honest labels:** SerpAPI/CSE/GDELT improve *discovery breadth*, not evidence quality by themselves. Jina/Firecrawl improve *evidence depth*. Only Layer 4 (tier table + corroboration counts) and Layer 6 (alignment gauge, already live) improve *citation reliability*. Tavily/Exa are agent-convenience layers whose Chinese recall is unproven — benchmark before believing any claim.

---

## Appendix: hands-on test log (2026-06-11, this VPS)
- `r.jina.ai` on `news.sohu.com/a/1032790826` (our fetcher: chrome_only) → 16,471 bytes clean markdown + published-time metadata. PASS.
- `r.jina.ai` on `baijiahao.baidu.com/s?id=1867381469…` → 4,858 bytes clean article text. PASS.
- GDELT DOC API → reachable; burst requests rejected with 1-req/5s notice; needs serialized cron usage. PASS with constraint.
- `googleapis.com/customsearch/v1` → HTTP 400 in 64ms (API alive, bad key as expected) → CSE feasible from VPS. PASS.
- Current-stack baseline (ALJ enriched run run_20260611T091642Z): content_fetcher 91 fetched / 41 failed / ~44 chrome-only of 176. This is the number the extraction ladder must beat.

## Sources (key references)
- Bing retirement: https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement ; cost analysis: https://ppc.land/microsoft-ends-bing-search-apis-on-august-11-alternative-costs-40-483-more/
- Brave API pricing: https://brave.com/search/api/ ; https://api-dashboard.search.brave.com/documentation/pricing
- Tavily pricing: https://www.tavily.com/pricing ; https://docs.tavily.com/documentation/api-credits
- Exa pricing (2026-03 update): https://exa.ai/pricing ; https://exa.ai/docs/changelog/pricing-update
- SerpAPI Baidu: https://serpapi.com/baidu-search-api ; pricing: https://serpapi.com/pricing
- Firecrawl: https://www.firecrawl.dev/pricing
- Jina Reader: https://jina.ai/reader/
- Diffbot: https://www.diffbot.com/pricing/
- GDELT DOC 2.0: https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/
- WeChat monitoring survey: https://yage.ai/share/wechat-official-account-monitoring-en-20260422.html
- Qingbo WeChat API: https://github.com/gsdata-qingbo/wechatAPI ; Newrank: https://chinachannel.co/wechat-tools-platforms/newrank/
- MCP server rankings: https://agentrank-ai.com/blog/best-mcp-servers-web-scraping-research/
