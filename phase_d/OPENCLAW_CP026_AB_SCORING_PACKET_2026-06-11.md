# CP-026 Full-Text Enrichment — A/B Scoring Packet
Date: 2026-06-11 | Status: READY FOR OPERATOR SCORING | Mode: held test, nothing delivered

## What is being compared
Baseline = today's delivered briefs (snippet-only retrieval, 1,000-char cap, 30 sources).
Enriched = same pipeline with `OPENCLAW_ENRICHMENT=on` (full text up to 6,000 chars, chrome-strip, 20 sources, editorial depth rule).

## Metrics

| Leg | Run | Validator | Claims matched | Alignment (aligned/weak/misaligned of checked) | Full-text |
|---|---|---|---|---|---|
| ALJ baseline (DELIVERED) | run_20260611T071837Z | GREEN PASS | 60/60 | 21 / 4 / 2 of 28 | none |
| ALJ enriched | run_20260611T091642Z | GREEN PASS | 72/72 | 11 / 9 / 6 of 28 (+2 insufficient) | 91 of 176 fetched |
| WS1 baseline (DELIVERED, cron) | run_20260610T223002Z | GREEN PASS | 9/9 | 5 / 0 / 0 of 7 | none |
| WS1 enriched | run_20260611T123807Z | GREEN PASS | 6/6 | 2 / 0 / 1 of 3 | 11 of 13 attempted (15 sources) |

## Files for side-by-side reading
- ALJ baseline: `/root/openclaw_traceability/alj_china_auto_001/2026-06-11/CANDIDATE_B_DELIVERY_PREVIEW.txt`
- ALJ enriched: `/root/openclaw_traceability/cp026_test/2026-06-11/DELIVERY_PREVIEW_cp026_alj_20260611_run_20260611T091642Z.txt`
- WS1 baseline: `/root/openclaw_traceability/china_monitor_001/2026-06-11/final_output_china_monitor_001_20260611_run_20260610T223002Z.txt`
- WS1 enriched: `/root/openclaw_traceability/cp026_test/2026-06-11/DELIVERY_PREVIEW_cp026_ws1_20260611_run_20260611T123807Z.txt`

## Findings (system observations — editorial quality is the operator's call)

1. **Citation alignment degrades under enrichment, both clients.** ALJ misaligned 2 → 6 (weak 4 → 9); WS1 misaligned 0 → 1. Warn-only gauge, so GREEN was unaffected, but this is the metric CP-023R taught us to trust.
2. **The agent ignored the new CITATION ECONOMY rule.** ALJ enriched bullets carry up to 6 citations including duplicates ("Baijiahao; Baijiahao"). Verified: the run DID use the current template (CITATION ECONOMY + NON-REPETITION both present in the archived agent input). Rule-by-prompt is not holding under full-text volume; if economy matters, it likely needs mechanical enforcement (truncate to 2 strongest in scrubber/citation_sub).
3. **WS1 enriched brief got shorter, not deeper:** 6 claims vs baseline 9, and only 3 bullets carried checkable citations. Depth instruction changed the shape of the output, not obviously its substance.
4. **First ALJ enriched attempt was killed by the old 540s ceiling** mid-agent; ceiling now 1800s (committed 33f43a3). Healthy enriched runs take ~7–8 min wall clock.
5. Enriched prompts are large (ALJ 131KB, WS1 122KB) — cost and latency scale with this.

## Decision requested from operator
- Score A vs B for editorial quality per client (depth, readability, client-grade voice).
- Given the alignment regression, recommended options:
  a) HOLD enrichment off; iterate prompt/mechanical citation enforcement; re-test. (recommended)
  b) Adopt for one client only after fix.
  c) Adopt as-is (not recommended — alignment regression contradicts the Phase D gate condition misaligned=0).
