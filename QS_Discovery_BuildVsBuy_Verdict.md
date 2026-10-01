# QS Discovery — Build vs Buy Verdict (2026-06-15)

## The two experiments
| Discovery method | Rediscovery of QSData's 105 articles |
|---|---|
| Search APIs (Baidu, our current stack) | **1%** (2/105) |
| Direct outlet crawl, single snapshot | **20%** (22/105) |
| A monitoring product (QSData) | 100% (the ground truth) |

## What the numbers mean
- **Search is a dead end for discovery.** Topic-search surfaces evergreen/ranked pages, not the fresh news flow. 1% settles it.
- **Direct crawl proves the articles ARE reachable** from the outlets' own pages — 20× better than search. But 20% is a **one-shot snapshot taken days after publication**: most articles had already rolled off the section fronts, and most Chinese outlets expose no usable sitemap. The limiting factor is **cadence, not capability** — a crawler run *daily* (or hourly) against these ~30 sections would catch articles inside their fresh window, pushing coverage far higher. 20% is a conservative floor, not the ceiling.
- The hosts that scored 100% (news.cn 4/4, auto.ce.cn 4/4, m.ce.cn, cv.ce.cn) are where a listing/sitemap still held the week's articles — proof the mechanism works where freshness or archive depth cooperates.

## Verdict: HYBRID
1. **Now (cheapest value):** consume a monitoring-style export (QSData, or licensed feed) for discovery. We have **proven the entire back half end-to-end** — fetch 99%, evidence extraction 94% faithful (DeepSeek-flash), synthesis next. A URL list in, a premium brief out.
2. **Medium-term (reduce dependence):** build a **continuous daily crawler** over the open high-authority tier (the ~30 outlets seen here). This test shows the articles are reachable; the build is real (scheduler, per-outlet section adapters, freshness-window capture, dedup/clustering) but tractable. Run the daily-over-a-week test before committing to size the true coverage.
3. **Never:** don't self-fight the closed social tier (WeChat/Weibo) — license if its coverage is needed.

## One-line summary
Our pipeline is the refinery, not the drill. Whoever supplies a good URL list — exported feed today, our own continuous crawler later — we turn it into client-grade intelligence. Discovery is a buy-now / build-later decision; the refinery is already built and proven.
