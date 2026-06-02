---
document_id: OPENCLAW-D-CP-025
version: 1.0
date_raised: 2026-06-02
status: PROPOSED — PENDING OPERATOR APPROVAL
---

# OPENCLAW — Phase D Change Packet CP-025
## ALJ: tv.cctv.com / tv.cctv.cn Domain Exclusion from Filter Layer

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-025 |
| Date raised | 2026-06-02 |
| Raised by | CoWork (pilot run analysis) |
| Client ID | alj_china_auto_001 |
| Feedback items addressed | ALJ Pilot Run 2026-06-01 scorecard — source quality |
| Feedback recurrence threshold met? | Yes — confirmed in pilot run 1; also matches Browser Retrieval Phase 1 Days 2/3 findings |
| Implementation layer | Retrieval filter (filter_results.py) — ALJ client profile only |
| Status | APPROVED — operator approved 2026-06-02 |

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**
tv.cctv.com and tv.cctv.cn URLs are being retrieved and retained in the ALJ
retrieval pool. These are CCTV television programme listing pages — they contain
no article text, only video programme titles and broadcast schedules. Their
blurbs are TV show listings (e.g. "[第一时间]中东局势扰动全球市场 00:02:05"),
not article summaries. They are structurally unsuitable as intelligence sources.

In the 2026-06-01 pilot run, 4 of 9 retained sources were tv.cctv.com pages
(Sources 1, 6, 7, 8 in the appendix). A single CCTV TV page (res_fc8e20c42b21)
accounted for 8 of 11 citations — the entire brief effectively rested on one
television programme listing page.

**Evidence:**
- ALJ Pilot Run 2026-06-01: Sources 1, 6, 7, 8 = tv.cctv.com (4/9 retained sources)
- res_fc8e20c42b21 = 8 of 11 citations (73% source concentration, single TV page)
- Browser Retrieval Phase 1 Days 2/3 (2026-05-28): tv.cctv.com and tv.cctv.cn
  confirmed as "structurally unsuitable for text extraction" — HTTP 200 but
  thin (10 words); "TV-video shell pages, no article body in DOM"

**Why this matters for client-grade output:**
A source appendix entry for a CCTV TV programme listing page — with a blurb
consisting of programme titles and air times — cannot support credible
intelligence claims. The ALJ product spec (Section 9) requires that blurbs /
snippets be "useful and readable" and that source appendix entries support the
report's narrative. TV shell pages fail this gate. The Complete Chinese Source
Appendix is a non-negotiable product requirement; sources that cannot provide
substantive blurbs degrade the appendix and undermine client trust.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** filter_results.py (ALJ client profile only)

**Current behaviour:**
filter_results.py does not apply any domain-level exclusion. tv.cctv.com and
tv.cctv.cn URLs pass through filtering as valid Chinese-language sources with
HTTP 200 status and non-zero (but thin) content.

**Proposed behaviour:**
For the ALJ client profile (client_id=alj_china_auto_001 or
OPENCLAW_CLIENT_ID=alj_china_auto_001), add a domain exclusion list that
drops results from the following domains before the retained pool is built:

```
EXCLUDED_DOMAINS_ALJ = [
    "tv.cctv.com",
    "tv.cctv.cn",
]
```

Logic: if a result's URL hostname matches any entry in EXCLUDED_DOMAINS_ALJ
and OPENCLAW_CLIENT_ID == "alj_china_auto_001", set the result's filter status
to DROPPED with reason "domain_excluded_alj" and exclude from retained pool.

This exclusion applies only to the ALJ client profile. WS1 (china_monitor_001)
is unaffected.

Note: news.cctv.com is NOT excluded. news.cctv.com article pages have been
confirmed viable in Browser Retrieval Phase 1 (1/2 substantial; 1/2 JS_RENDER
pending networkidle re-test). Only the tv. subdomain is excluded.

**Rationale:**
TV programme listing pages (tv.cctv.com, tv.cctv.cn) have no article body
and cannot produce usable intelligence. Excluding them at the filter layer
removes the most structurally unsuitable source type without affecting CCTV
news article pages (news.cctv.com) or any other domain.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** LOW

**Risk description:**
- Scope is narrow: two subdomains, ALJ client only
- news.cctv.com is explicitly preserved — no CCTV article content is lost
- WS1 is completely unaffected
- If tv.cctv.com / tv.cctv.cn are the only results for a given query, the
  effect is a thinner retained pool — acceptable given these sources provide
  no usable content anyway
- No validator, scrubber, or delivery gate changes

**Rollback plan:**
Standard backup before implementation:
filter_results.py.bak_{date}_pre_cp025
Rollback: restore from backup; py_compile exit 0; confirm on next ALJ pilot run.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**
- No tv.cctv.com or tv.cctv.cn URLs appear in the retained source pool
  for the next ALJ pilot run
- WS1 retrieval pool is unchanged (spot-check: no "domain_excluded_alj"
  entries appear in WS1 filter log)
- ALJ retained pool contains at least as many sources as v1 run (i.e.
  exclusion does not collapse retrieval — at minimum 5 retained sources)
- news.cctv.com URLs (if retrieved) are not excluded

**Number of runs required to validate:** 1 ALJ pilot run

**How to confirm resolved:**
Source appendix of next ALJ pilot run contains no tv.cctv.com or tv.cctv.cn
entries.

**How to confirm no regression:**
WS1 D14+ validator continues GREEN; no change to WS1 filter log patterns.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change is confined to one pipeline layer (filter_results.py)
- [x] Rollback path exists and is documented above
- [x] Change is within Phase D scope

**Forbidden change check:**

- [ ] Does NOT alter retrieval behavior (query logic, provider config,
      freshness params) — NOTE: This CP modifies filter_results.py,
      which is a retrieval filter component. Precedent: CP-011 also
      modified filter_results.py (client-aware Baidu freshness) and
      was approved and implemented. This change is narrower in scope
      than CP-011 (domain exclusion vs. freshness window logic).
- [x] Does NOT weaken validator strictness
- [x] Does NOT weaken scrubber behavior
- [x] Does NOT bypass or modify the Delivery Gate decision
- [x] Does NOT affect client namespace isolation

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-06-02 |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | |
| Backup confirmed | |

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

*To be completed after next ALJ pilot run.*

| Run # | Date | Outcome vs. validation criteria |
|-------|------|----------------------------------|
| 1 | | |

**Overall outcome:** PENDING

---

*OPENCLAW-D-CP-025 | v1.0 | 2026-06-02 | APPROVED — operator approved 2026-06-02*
*Client: alj_china_auto_001 | filter_results.py — domain exclusion*
*Drafted by: Claude CoWork | No system changes until operator approval*
