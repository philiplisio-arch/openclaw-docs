# CP-026 A/B SCORING PACKET — RE-TEST UNDER MECHANICAL CITATION CAP (2026-06-12)

---
document_id: OPENCLAW_CP026_AB_SCORING_PACKET_2026-06-12
date: 2026-06-12
author: Claude Fable 5
status: PRESENTED FOR OPERATOR SCORING — held-mode test, nothing delivered externally
supersedes-context: OPENCLAW_CP026_AB_SCORING_PACKET_2026-06-11 (pre-cap test, HOLD decision)
---

## Bottom line

Yesterday's HOLD reason is gone. With the mechanical citation cap (b5d2e43) and the corrected alignment checker (012efe4) in the chain, full-text enrichment **no longer degrades citation alignment — it improves it**. The ALJ enriched leg scored **0 misaligned** (vs 2 on the same-day un-enriched run, vs 6 on yesterday's pre-cap enriched run) while producing slightly *more* cited claims, not fewer. The WS1 enriched leg also scored 0 misaligned but remains thinner than its baseline (6 cited bullets vs 8) — the brevity concern persists for WS1.

**Recommendation: adopt enrichment for ALJ; hold for WS1 pending a depth fix.** Editorial quality is yours to score from the briefs.

## Same-day comparison (all runs 2026-06-12, post-fix checker throughout)

| Run | Mode | Cited bullets | Aligned | Weak | Misaligned | Cap activity | Validator |
|---|---|---|---|---|---|---|---|
| ALJ enriched (cp026_alj) | full text, held | **30** | **25** | 3 | **0** | 8 groups capped, 12 ids dropped | GREEN 57/57 |
| ALJ un-enriched (WS2 rerun) | standard, held | 28 | 22 | 1 | 2 | 8 groups capped, 15 ids dropped | GREEN 48/48 |
| WS1 enriched (cp026_ws1) | full text, held | 6 | 3 (+3 unscorable) | 0 | **0** | 0 (compliant) | GREEN 6/6 |
| WS1 baseline (D23 delivered) | standard, live | 8 | 6 (corrected) | 0 | 0 (corrected) | 2 groups capped, 2 ids dropped | GREEN 10/10 |

Yesterday's pre-cap enriched legs, for contrast: ALJ 11/9/6 of 28; WS1 2/0/1 of 3.

## Reading

1. **The cap, not enrichment, was the missing control.** Yesterday's alignment collapse under full text was the agent burying claims in 6-source citation trains. With trains mechanically capped to the 2 best-aligned sources, full text gives the agent *better* evidence and alignment improves.
2. **ALJ benefits clearly:** more claims (30 vs 28), better alignment (0 vs 2 misaligned), richer evidence behind each citation. The enriched brief is the best-scoring ALJ output produced to date.
3. **WS1 still shrinks under enrichment** (6 vs 8 cited bullets; same pattern as yesterday). Full text appears to make the WS1 agent more conservative rather than deeper. If you score the enriched WS1 brief as editorially better despite fewer bullets, that changes the call; otherwise WS1 enrichment needs a depth-side iteration (e.g., minimum-claims floor in the template) before adoption.
4. **Caveat:** the ALJ enriched run hit one Gemini overload mid-run; the yield-fallback recovered the full brief (all sections intact). Worth watching, not blocking.

## Decision requested

- **Adopt enrichment for ALJ** (flip `OPENCLAW_ENRICHMENT` on for `alj_china_auto_001` runs): ALJ is held-mode/pilot anyway — every output still reaches you labeled for review before any future external use.
- **WS1**: hold enrichment off (recommended), or adopt-with-depth-iteration.
- Briefs for editorial scoring: `final_output_scrubbed_cp026_alj.txt` / `final_output_scrubbed_cp026_ws1.txt` (phase5/data) and the traceability archive `cp026_test/2026-06-12/`.

Streak note: these are experiment-namespace runs — they do not count for or against the Phase D streak (2/5 as of D23).
