# WS1 Story Selection Advisory — China Business Daily

**Date:** 2026-06-24  
**Audience:** Claude Code main operator / WS1 maintainer  
**Related files:** `ChinaBiz_Crawler_Status.md`, published daily brief at `daily.thefootegroup.com`  
**Purpose:** Improve WS1 story ranking and editorial selection while preserving the current higher-trust sourcing model.

---

## Executive Summary

The current edition demonstrates a significant improvement in source quality and factual reliability. The report is drawing from a broad, credible source universe and the selected stories are generally defensible.

However, the report remains overly biased toward official-policy and consensus coverage. It is functioning more as a summary of what government and state-affiliated business media are saying than as an intelligence product identifying the developments most likely to matter to multinational executives.

The challenge is no longer source quality.

The challenge is story ranking.

The system is successfully finding important stories. It is not always selecting the most informative stories.

---

## Current Bias

The current ranking system appears to favor:

- Stories appearing across multiple outlets
- Official announcements
- Government policy releases
- Broad macroeconomic themes
- Highly corroborated reporting

This approach is safe.

The downside is that it systematically under-ranks emerging business developments that may have greater strategic importance.

As a result, the report often selects the most widely reported version of a story rather than the most informative version of a story.

---

## Example: Automotive Sector

The report correctly selected the automobile after-market policy package and related consumption measures.

This was a reasonable choice.

However, the crawler also surfaced several stronger business-intelligence angles:

- Intensifying price pressure on ICE vehicles
- Competition among provinces for NEV leadership
- Chinese autonomous-driving progress versus global competitors
- Expansion of charging and battery-swap infrastructure
- Chinese EV international expansion

These developments provide more insight into where the sector is moving.

The policy announcement explains what Beijing wants.

The industry stories explain what is actually happening.

The latter is often more valuable to corporate readers.

---

## What CEOs Actually Need

A CEO rarely needs a complete summary of today's policy announcements.

A CEO needs to know:

1. What changed?
2. Why does it matter?
3. Is this a one-day headline or part of a larger trend?
4. What should I watch next?

The report should increasingly optimize for these questions.

---

## Recommended Ranking Framework

When evaluating candidate stories, assign separate scores for:

### 1. Strategic Significance

Will this matter six months from now?

Examples:

- AI infrastructure investment
- Semiconductor supply chains
- Foreign investment trends
- Industrial policy shifts
- Regulatory changes

### 2. Business Impact

Could this influence:

- revenue
- investment decisions
- supply chains
- market access
- competition

within the next twelve months?

### 3. Novelty

Is this genuinely new information?

Many policy stories repeat themes already reported for months.

A new industrial development may carry greater informational value.

### 4. Executive Relevance

Would a multinational executive forward this article to a colleague?

If not, it is probably not Top 15 material.

### 5. Corroboration

Corroboration should remain important.

However, it should function as a confidence modifier rather than the primary ranking factor.

Current behavior appears to over-weight corroboration.

---

## Recommended Editorial Mix

For a Top 15 report:

- **30–40%** policy and regulatory developments
- **30–40%** business and industry developments
- **20–30%** technology, capital markets, and investment themes
- **10%** emerging signals and unusual developments

The current report is closer to:

- **60–70%** policy
- **20–30%** macro
- **10%** business developments

This creates a more predictable but less insightful product.

---

## Specific Missing Themes from the Current Source Universe

The crawler surfaced several themes that deserve more attention in future editions:

- AI infrastructure and data-center buildout
- Semiconductor and compute-market developments
- Foreign-investment sentiment and supply-chain positioning
- Industrial upgrading and advanced manufacturing
- Logistics and trade infrastructure
- Chinese firms expanding internationally
- Technology commercialization and deployment

These themes are often more useful to executives than another summary of an official policy release.

---

## Operator Guidance

Do not change the sourcing system.

Do not change the trust model.

Do not loosen verification standards.

Instead, improve the ranking model.

The source universe is now strong enough that the primary determinant of report quality will be editorial selection.

The next stage of WS1 should focus on identifying the stories that are most important, not merely the stories that are easiest to verify.

---

## Suggested Implementation Direction

Add or strengthen a story-selection layer that ranks each candidate story on:

- strategic significance
- business impact
- novelty
- executive relevance
- corroboration / confidence

Then force the final Top 15 to include a healthier mix of:

- official policy
- market/industry developments
- company and sector signals
- technology and capital-market themes
- unusual but important emerging signals

The goal is not to make the report more speculative.

The goal is to make it more useful while preserving the trust gains already achieved.
