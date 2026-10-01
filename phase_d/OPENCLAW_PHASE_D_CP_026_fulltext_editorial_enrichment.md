# OPENCLAW — Phase D Change Packet CP-026 (DRAFT)
# Full-Text Editorial Enrichment Test (held-mode A/B)

---
document_id: OPENCLAW-D-CP-026
version: 0.1-DRAFT
created: 2026-06-11
classification: PHASE D CHANGE PACKET — RETRIEVAL DEPTH / AGENT INPUT (ALL CLIENTS, HELD-MODE TEST)
status: DRAFT — operator approved drafting 2026-06-11; nothing deploys without per-item approval
origin: operator advice note 2026-06-11 ("Full-Text Retrieval and Editorial Enrichment")
---

## SECTION 0 — PROBLEM STATEMENT (evidence from the 2026-06-11 ALJ delivery)

Briefs read snippet-like even though browser retrieval (Playwright/Chromium,
`content_fetcher.py`) runs in every pipeline run. Measured on the 30 sources
the agent received in the delivered Jameel Motors brief (run_20260611T071837Z):

1. **Leading page chrome consumes the text budget.** Extraction starts at the
   top of the page; cookie banners / menus / sign-in chrome precede the
   article. Median 146 chars of junk, mean 289, before the first clean
   article sentence — inside a 1,000-char cap (`MAX_TEXT_CHARS`).
2. **5 of 30 sources were 100% chrome** — zero article body reached the agent.
3. **Even clean text is lede-only.** ~700–850 usable chars ≈ headline + first
   1–2 sentences (English; CJK fares better per char). No paragraph-5
   material: specific figures, quotes, context.
4. **The prompt never asks for depth.** System rules are all discipline
   (cite, don't fabricate, don't pad); there is no instruction to mine the
   source body for specifics. Constraint-heavy prompt + lede-only evidence →
   cautious generic synthesis.

Correction to the advice note's premise: full text is NOT restricted to a
verification role in code — the fetched text IS what the agent writes from.
Both trust and editorial layers consume the same truncation. The gap is
extraction quality + depth + instruction, not an approval restriction.
(The note's "D17 claim-source misbinding" could not be verified in records;
the misbinding class was root-caused 2026-06-11 — resolver positional bug,
fixed via agent_source_map — making the citation_alignment metric
trustworthy as this test's regression gauge.)

## SECTION 1 — PROPOSED CHANGE (three parts, tested together)

Operator direction 2026-06-11 (supersedes the tiered-cap design): **the goal
is the full text of each article in the composition of both WS1 and ALJ
briefs.** Implemented 2026-06-11 behind an opt-in switch (`OPENCLAW_ENRICHMENT`);
the default/cron path stays byte-identical until adoption is approved.

**1A. Extraction quality (content_fetcher.py).** Under enrichment, strip
leading page chrome before keeping text: drop everything before the first
"clean long sentence" (≥80 chars, no boilerplate tokens). Pages that are
all chrome are excluded from enrichment (`fetch_status=chrome_only`).
Cheap heuristic now; the Phase 7 readability fetcher remains the thorough
successor (still sandboxed, unchanged by this packet).

**1B. Full-article text (content_fetcher.py).** Under enrichment,
`MAX_TEXT_CHARS` rises 1,000 → 6,000 on cleaned text. 6,000 is a tripwire
ceiling against freak pages (multi-page PDFs, infinite feeds), not a
routine cap — most news articles fit whole. Tiered caps from the original
advice note are dropped in favor of full text for all retained sources;
source-quality control remains with the existing filter/tier rules.

**1C. Editorial-use instruction (build_agent_input_slim.py).** Under
enrichment, an EDITORIAL DEPTH RULE is appended to the system rules (both
WS1 and ALJ): draw figures, percentages, named individuals/companies,
quoted statements, and dates from source bodies into the narrative, under
the existing citation discipline. Depth from evidence, not padding.

**Prompt-size control:** under enrichment MAX_SOURCES drops 30 → 20 —
twenty articles read whole beats thirty read as headlines. Expected prompt
~70–110KB vs today's 48–55KB; agent latency and stability are explicit
test measurements.

**Deferred from the advice note:** separate `verification_text` /
`editorial_context` blocks per source. Two parallel texts double prompt
weight and blur which text supports a citation; one deeper cleaned body
achieves the editorial goal. Revisit only if misalignment rises in dry runs.

## SECTION 2 — TEST DESIGN (held-mode, isolated namespace, mirrors CP-022A)

- **Mode A (baseline):** current behavior. Baseline artifacts exist for both
  clients — the delivered 2026-06-11 Jameel brief (traceability,
  CANDIDATE_B_*) and the delivered 2026-06-11 WS1 cron brief.
- **Mode B (full-article):** 1A + 1B + 1C. Two held runs executed 2026-06-11
  (operator-approved): namespaces `cp026_alj` (alj_jameel_weekly_v2) and
  `cp026_ws1` (china_monitor_v1), offline orchestrator only (no delivery
  code path), gated manually through resolver/scrubber/validator.
- Mode C (5,000-char tier caps) from the advice note is obsolete — Mode B
  already reads full articles.

No delivery in any mode. pilot/held gates untouched. Switch-on for live
runs = separate approval (set OPENCLAW_ENRICHMENT=on in client loader env
or flip the default after operator scoring).

## SECTION 3 — GUARDRAILS

- No changes to validator, scrubber, resolver, delivery gate, or cron.
- citation_alignment (warn-only) is the misbinding regression metric;
  Mode B must not increase misaligned count vs Mode A on comparable content.
- Tier 4–5 sources get no enrichment; corroboration rules unchanged.
- Runtime: fetch cost unchanged (truncation is post-extraction); watch agent
  latency under the 540s orchestrator timeout.

## SECTION 4 — SUCCESS CRITERIA (Mode B vs Mode A)

1. Article-body specifics visible in output (figures/quotes/names per section — counted)
2. Stronger "why it matters" analysis (operator judgment)
3. Less generic advisory language (operator judgment)
4. Better sector/context explanation (operator judgment)
5. citation_alignment: misaligned not increased; aligned share not decreased
6. Scrubber: no increase in removed/unsupported claims
7. Runtime within timeout; agent stable on the larger prompt
8. Operator usefulness score improves vs baseline

## SECTION 5 — FILES IN SCOPE / ROLLBACK

- `openclaw_phase5/orchestrator/content_fetcher.py` (1A, 1B)
- `openclaw_phase5/orchestrator/build_agent_input_slim.py` (1C, MAX_SOURCES)
- Rollback: `.bak` per file + git; flat 1,000-char behavior restorable in one revert.

## SECTION 6 — SEQUENCING & APPROVALS REQUESTED

Queue behind CP-023R validation settling. Held-mode only; no client
exposure; Phase D gate unaffected.

1. Section 1 full-article design — APPROVED 2026-06-11 (operator: "i simply
   want the full text of each article ... in both"; "go ahead").
2. Mode B held dry runs — APPROVED & EXECUTED 2026-06-11.
3. Production adoption (enrichment on for live WS1 + ALJ runs) — PENDING
   operator scoring of the A/B comparison.

---
*OPENCLAW-D-CP-026 | v0.1-DRAFT | 2026-06-11 | Evidence: run_20260611T071837Z agent-input measurement (boilerplate share, 5/30 all-chrome); operator advice note 2026-06-11*
