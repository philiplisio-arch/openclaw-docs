---
document_id: COWORK-REVIEW-REPORT-20260608
version: v1.0
created: 2026-06-09
prepared_by: Claude CoWork
status: COMPLETE — AWAITING OPERATOR REVIEW
---

# OpenClaw — CoWork Review Report
## Session: 2026-06-08

---

## VPS SYNC STATUS NOTE

This review was completed without the D13, D14, and D15 scrubbed output files or their retrieval packages. The current vps_sync contains the confirmation run package (run_20260608T024200Z, mapping_size=4) and the run summaries through 2026-06-03 (D14). D15's run summary and all three delivery outputs are not in the local sync.

The traceability archive (ADV-016 partial) began with D18 (per cron log). D13–D15 predate the archive. Full Layer 4 spot-checks for D13–D15 require the operator to scp the following files from the VPS before certification can be completed:

- `/root/openclaw_phase5/data/` — the D13/D14/D15 final_output_scrubbed_china_monitor_001.txt files will not still be present (overwritten by subsequent runs), but the run_summary files for 20260604 (D15) should be retrievable
- The most practical path: pull the Brain Lite run summaries for all three dates and, if available, the phase5 agent logs from the per-run sidecars in `/root/openclaw_logs/`

This limitation is flagged at the top because it directly affects the Section 2 recommendation.

---

## 1. SYSTEM HEALTH SUMMARY

The system is recovering from its most severe failure sequence since Phase A: D18 and D19 both collapsed to 1-source output due to a `filter_results.py` bug that treated Baidu results with missing timestamps as stale. The bug was diagnosed and patched on 2026-06-08. A confirmation run validated the fix (mapping_size returned to 2 vs. 1). However, mapping_size=2 is well below the normal range of 14–15, reflecting underlying Baidu pool quality issues (index and wiki pages dominating) rather than a filter logic failure. The fix is sound; the root cause of thin Baidu pool quality is CP-022 (query expansion).

The domain exclusion expanded to seven domains. A validation question remains on whether the exclusion loads correctly — CCTV domains appeared as stale_url_date rather than domain_exclusion in D19 drop analysis. The 2026-06-09 06:30 cron run is the first live validation of the Issue #66 fix and the domain exclusion load. Gate streak remains held at 3/10 pending D13/D14/D15 five-layer review.

Cron log confirms D18 and D19 both delivered to Lark (final_decision=delivered) but were not sent externally. The traceability archive is partially operational from D18 onward: final_output and validation_result are being archived per run; the raw Brave/Baidu results and filter decision log are not yet archived (partial ADV-016 pre-deployment observed in log).

---

## 2. FIVE-LAYER D13/D14/D15 REVIEW

**⚠ OPERATOR DECISION REQUIRED — Recommendation: Option 3 (Continue Hold)**

### Available evidence

D13, D14, and D15 scrubbed output files are not in the current VPS sync and cannot be assessed at snippet/claim level. The review below uses: daily status topic descriptions, run summaries (D13/D14 confirmed; D15 not synced), and cron log metrics.

### Per-delivery assessment

**D13 — 2026-06-02**

| Layer | Assessment |
|-------|------------|
| 1. System | PASS — delivered, validator GREEN 16/16/0, 0 warnings, 0 failures. Cron log confirms final_decision=delivered. |
| 2. Citations | PASS — 16 citations, 16 matched, 0 removed. Zero fabricated result_ids. Structurally clean. |
| 3. Source quality | CANNOT FULLY ASSESS — retrieval package not in sync. Brave=39/Baidu=45, mapping_size not directly confirmed from log but validator_sources_indexed=12, suggesting 12 distinct sources reached the agent. Medium concern: the "EC declares relationship not sustainable" claim is high-stakes diplomatic language. No domain exclusion was active on D13 (deployed 2026-06-06), so TV shell pages and aggregators could have been in the package. |
| 4. Claim-source support | CANNOT ASSESS — scrubbed output and retrieval package not available. High-risk claims: (a) EC declares EU-China relationship "not sustainable" — precise diplomatic phrasing at ministerial level; (b) Nvidia AI chip shipment halt — regulatory action with named company; (c) Huawei 5-year semiconductor plan — corporate strategic announcement; (d) $30B export discussion figure. The "not sustainable" phrasing is the same diplomatic claim that appeared (uncited) in D17's confirmed misbinding. |
| 5. Client usefulness | LIKELY PASS — topic mix (US-China trade, EU-China, China PMI) is well-scoped for a China business intelligence client. Topics are concrete and timely. |

**D14 — 2026-06-03**

| Layer | Assessment |
|-------|------------|
| 1. System | PASS — delivered, validator GREEN 12/12/0 (13 citations, all matched, 0 removed). mapping_size=8. |
| 2. Citations | PASS — 13 citations, 13 matched, 0 removed. Structurally clean. |
| 3. Source quality | MODERATE CONCERN — mapping_size=8 is below the normal range. Baidu=54 returned but only 8 distinct sources reached the agent. Source quality of the 8 sources is unknown without the retrieval package. No domain exclusion active on D14. |
| 4. Claim-source support | HIGH CONCERN — D14 contains a claim about "Yvette Cooper China visit." This is the exact same claim (UK Foreign Minister visiting China) that appeared in D17 ET Bullet 2, where it was the confirmed citation misbinding: zero evidence for the claim appeared in any of D17's 12 retrieval package snippets, yet the agent cited an h5.article.smbae.cn aggregator page about US-China tariffs. D14 has mapping_size=8 vs D17's full package; a legitimate Reuters or BBC source for the Cooper visit could plausibly have been in D14's package (the visit was real news). However, this cannot be confirmed without the D14 retrieval package. The risk that D14 had the same misbinding pattern — absorbing the Cooper fact from one source and binding it to an adjacent citation — cannot be excluded without inspection. A second high-risk claim: "Israel/Lebanon/Gulf capital" involves geopolitical/financial assertions. |
| 5. Client usefulness | UNCERTAIN — US-China trade and Cooper visit are relevant; the Israel/Lebanon/Gulf capital topic requires a China nexus to be in-scope for the WS1 brief. Middle East content drift (T-05) is a known monitoring item. |

**D15 — 2026-06-04**

| Layer | Assessment |
|-------|------------|
| 1. System | PASS — delivered, validator GREEN 13/13/0. mapping_size=12. |
| 2. Citations | PASS — 13 citations, 13 matched, 0 removed. Structurally clean. |
| 3. Source quality | MODERATE CONCERN — unknown without retrieval package. No domain exclusion active on D15. Brave=44/Baidu=54, mapping_size=12 (healthy). Likely included a mix of sources; Baidu TV pages may have been present. |
| 4. Claim-source support | MODERATE CONCERN — High-risk claims: (a) "Soochow/Donghai brokerage consolidation ($1.7B)" — named companies, specific dollar figure, major transaction; (b) "China tech transfer curbs" — regulatory action requiring official source; (c) "Strait of Hormuz / China tech AI rally" — geopolitical + market claim. The financial consolidation figure ($1.7B) and named companies require strong source support — Chinese business press (Caixin, 21st Century Business Herald, Securities Times) would be appropriate sources. Whether the retrieved sources supported these specific claims cannot be confirmed. |
| 5. Client usefulness | LIKELY PASS — brokerage consolidation is a concrete China business development; PMI is standard monitoring; tech transfer curbs are high-relevance for PR clients. |

### Recommendation

**Option 3: Continue Hold.** The five-layer review cannot be completed to the ADV-017 standard without the D14 retrieval package (to assess the Yvette Cooper citation) and the D13 delivery content (to assess the "EC not sustainable" claim origin). Specifically:

- The D14 Yvette Cooper claim is the same claim confirmed as a misbinding in D17 three days later. The risk that D14 had the same misbinding is material and cannot be dismissed without source inspection.
- The D13 "EC not sustainable" diplomatic phrasing is similarly high-risk.

If the operator can confirm via scp that D14's retrieved sources include a legitimate news article naming Yvette Cooper's China visit, and D13's sources include a legitimate EU or news source for the "not sustainable" phrasing, then Option 1 (certify) becomes supportable for those two deliveries. D15 has lower risk claims and is more likely to certify.

**Minimum requirement to certify:**
1. Operator SCP: pull the per-run sidecar logs from `/root/openclaw_logs/` for the D13, D14, D15 runs (timestamped ~22:31 UTC on June 2, 3, and 4). These may contain resolver mapping details.
2. Claude Code: read the Brain Lite run_summary for 20260604 (D15) — not yet in sync.
3. Most importantly: if the operator has the original Lark deliveries for D13/D14/D15, a manual spot-check of the Yvette Cooper citation in D14 against whatever source was cited would resolve the key uncertainty.

---

## 3. D18/D19 PATCH ASSESSMENT

### Issue #66 fix — logical soundness

**Assessment: Logically sound.** The two-part fix is correct:

1. `if dt is None or dt < CUTOFF` → `if dt is not None and dt < CUTOFF` — This is the right inversion. The original condition dropped results when the timestamp was absent (treating None as "infinitely old"). The fix keeps results when the timestamp is absent or when it's within the freshness window. The logic is clean and the intent is correct.

2. Full-year Chinese date form `(20\d{2})年...日` added to `parse_date_from_title` — this aligns parse_date_from_title with parse_date_from_summary, which already had this pattern. Consistent across both parsing paths.

**Edge case to watch:** The fix means that Baidu results with NO parseable date are now kept unconditionally. These results will pass into the retrieval package regardless of age. If Baidu returns old content with no date field (e.g. evergreen wiki pages, undated index pages), those will now persist in the pool. The 2026-06-09 cron run should be monitored for results kept with filter_reason `keep:no_date` or similar — if these are dominating the pool, a follow-up to require positive date confirmation (or flag as quality warning) may be needed.

This is distinct from the intent of the fix, which is correct. It's a monitoring flag for one edge case.

### Confirmation run mapping_size=2 — does the explanation hold?

**Assessment: Plausible and consistent with available evidence.** The confirmation run retrieval package (run_20260608T024200Z) shows 4 results after filtering. The daily status explains 23/24 Baidu results dropped as valid quality decisions (index pages, wiki, stale CCTV clips). The retrieved package supports this:

- res_4d61ddb7eab4 (CNBC) — legitimate, Brave-sourced
- res_550415439aa8 (m.article.iyxgq.cn) — Baidu mobile aggregator. Content is MOFCOM press conference about US-China trade consultations — substantive, official-source content wrapped in aggregator URL
- res_85c60f9e14a3 (wap.article.ujhgq.cn) — Baidu mobile aggregator. Content is MOFCOM press conference about China-EU trade dialogues — similarly substantive
- res_e8c045d3255d (kuaixun.cngold.org) — Gelonghui financial news flash, attributing to央视/CCTV, reporting France-UK-Germany-Ukraine meeting

The explanation holds: the surviving Baidu results are content-bearing, even if accessed through aggregator URLs. The 23 dropped results being index/wiki/stale CCTV clips is consistent with the filter fix working correctly. mapping_size=2 reflects that the manual confirmation run used a limited query set (`manual_test` trigger type), not the full cron query bundle (6 queries).

**Note on res_e8c045d3255d:** This source produces the "France/UK/Germany/Ukraine leaders meeting" bullet in the confirmation run output. That claim has no China relevance. It passed into the brief because the eu_r1 query returned European-region results including non-China items. This is CP-022 territory (query formulation), not a filter failure. But it illustrates that even with the fix working, query scope is still producing off-target content.

### Over-inclusion risk from the fix

**Assessment: Low in the short term; monitor over time.** The fix retains results with no parseable date. In the confirmation run, both Baidu mobile aggregator results (res_550415439aa8, res_85c60f9e14a3) have explicit dates (2026-06-05) and are correctly retained via `keep:recent_url_date`. The risk of over-including genuinely stale content is contingent on Baidu returning undated results — which may occur but was not the primary failure mode observed. Monitor the 2026-06-09 cron run for any results with `keep:no_date` filter reason.

---

## 4. DOMAIN EXCLUSION LOADING — VALIDATION QUESTION

### Possible explanations for CCTV appearing as stale_url_date

The most likely explanation is **filter ordering**: `filter_results.py` evaluates the date freshness condition before the domain exclusion condition. CCTV TV page results (`tv.cctv.com`, `tv.cctv.cn`) are video content pages whose URL dates are old or absent. If the date filter runs first and assigns `filter_reason: stale_url_date`, the domain exclusion check may never be reached — so the result is dropped for the right reason but tagged with the wrong label. The domain exclusion would correctly exclude them if they had fresh dates (which they never do for TV shell pages).

Secondary possibilities: (a) `OPENCLAW_DOMAIN_EXCLUSION` env var not being correctly passed to filter_results.py subprocess; (b) domain exclusion list is loaded but the substring match is case-sensitive or uses wrong field; (c) D19 ran before the 2026-06-06 Layer 1 deployment propagated to the live filter (D19 is 2026-06-08 — the deployment was 2026-06-06, so timing is not the issue).

The filter ordering hypothesis is the most operationally benign: the domains are being excluded (correctly), just with the wrong label. The D17 concern — that low-quality sources are reaching the agent — would be addressed whether the label is stale_url_date or domain_exclusion. However, the filter reason label matters for traceability (ADV-016 filter decision log) and for understanding system behavior.

### How to read the 2026-06-09 cron run

1. **Check for CCTV results in the filter drop log.** If CCTV results appear, their filter_reason should show `domain_exclusion`. If they show `stale_url_date` again, the filter ordering issue is confirmed (not a config loading failure).
2. **Check for the four new domains** (baike.baidu.com, bilibili.com, chinawto.mofcom.gov.cn, zhsme.org.cn). If any of these appear, they should show `domain_exclusion`. If they show `stale_url_date` or `keep:recent_url_date`, the config loading or substring matching is suspect.
3. **mapping_size.** Should be materially higher than 2. Target is 10–15 for a normal WS1 cron run. If mapping_size is still low (below 5), the pool quality issue is structural and CP-022 is more urgent.
4. **No CCTV results at all** is also a valid outcome — domain exclusion working correctly would drop them at filter time and they would not appear in the retrieval package passed to the agent.

### Action required before cron run

**No pre-emptive action required.** The filter code was deployed and syntax-checked. The domain exclusion config is in place. Observation of the 2026-06-09 cron run is the right call. If the run reveals an ordering issue, Claude Code can patch the filter evaluation sequence in a follow-up session with low risk (it's a behavioral change to filter_results.py, not a schema or config change).

---

## 5. ADV-014 L2 + ADV-016 DEPLOYMENT READINESS

### ADV-014 Layer 2

**Assessment: Spec is complete and implementation-ready. Recommend waiting for 2026-06-09 cron validation before deploying.**

The ADV-014 advisory contains the full Python implementation spec, including the `passes_quality_floor()` function body, the `SHELL_KEYWORDS` list (with the '《' false-positive correctly removed), the `_nws_len()` helper, and the warn-only mode behavior. The config side (snippet_min_chars: 80) is noted as already in place in client_config_china_monitor_001.yaml.

The only implementation gap Claude Code must address: confirm that `load_client_config.py` exports `OPENCLAW_SNIPPET_MIN_CHARS` to the environment from the `snippet_min_chars` YAML key. This is described in the advisory but not confirmed deployed.

**Sequencing concern:** ADV-014 L2 modifies `filter_results.py`. Issue #66 also modified `filter_results.py`. Deploying ADV-014 L2 before the 2026-06-09 cron confirms the Issue #66 fix is stable would make it harder to attribute any filter behavior anomalies to the right change. Recommended: observe 2026-06-09 cron, then deploy ADV-014 L2.

**No conflict with other pending changes.** Warn-only mode means ADV-014 L2 does not drop any sources — it only logs quality flags. False positive risk at threshold 80 is confirmed LOW (no D17 package sources fell below 80).

### ADV-016 (Raw Retrieval Logging)

**Assessment: Spec is complete. Partial deployment already observed. Full deployment should be sequenced after Issue #66 validation.**

**Partial deployment observed:** The cron log shows `[TRACE]` lines beginning with the D18 run (2026-06-06T22:30 UTC): archive directory creation, `final_output` archiving, and `validation_result` archiving are already running. This partial implementation was not documented in the 2026-06-06 or 2026-06-08 session close notes. Claude Code appears to have partially deployed ADV-016 during one of the sessions.

What IS deployed (per log): archive directory creation, final_output archiving, validation_result archiving.
What is NOT yet deployed (per spec and log): raw Brave results, raw Baidu results, combined raw retrieval package, filter decision log.

**Implication:** The operator should confirm with Claude Code which files have been deployed and whether the partial implementation matches the ADV-016 spec. The most valuable missing pieces are the **filter decision log** (which would have confirmed the CCTV domain_exclusion/stale_url_date question definitively) and the **raw retrieval packages** (which would have allowed full Layer 4 review for future deliveries without a manual VPS pull).

**Sequencing:** The filter decision log output from ADV-016 is implemented in `filter_results.py`. Since ADV-014 L2 also touches `filter_results.py`, both changes should be deployed in the same session. Recommend: verify 2026-06-09 cron → single Claude Code session deploying both ADV-014 L2 and the remaining ADV-016 pieces to `filter_results.py` together.

**No conflicts with other pending changes.**

---

## 6. WORK QUEUE — SEQUENCING ASSESSMENT

**Assessment: Current sequencing is sound with one adjustment.**

The D18/D19 collapse and recovery does not change the fundamental sequencing. The Immediate tier (ADV-014 L2, ADV-016) remains correct. The streak-gated Tier 2 items (CP-021, CP-022A, CP-024) correctly wait for the streak resumption decision.

**Recommended adjustment:** Insert a hold point between the Immediate tier and deployment. The sequence should be:

1. Observe 2026-06-09 cron run (validate Issue #66 fix + domain exclusion load behavior)
2. Deploy ADV-014 L2 + remaining ADV-016 (filter_results.py and package_builder.py) in a single session
3. Operator review of D13/D14/D15 (streak resumption decision)
4. Then Tier 2: CP-021, CP-022A, CP-024

**Domain exclusion loading question as a Tier 2 blocker?** No. Even if the filter ordering issue is confirmed (CCTV correctly dropped but with the wrong label), this does not block CP-021 (output restructuring), CP-022A (query dry run), or CP-024 (source appendix). These operate on different pipeline layers. The label issue would be fixed in the same session as ADV-014 L2.

**Browser Phase 1 hard deadline:** Phase 1 must complete before CP-022 goes live. CP-022 is blocked on CP-022A gate + Phase 1 findings. Given the current hold (streak at 3/10), there is runway — CP-022 likely does not go live for at least 2–3 weeks. The remaining Phase 1 items (CCTV networkidle re-test, Reuters/Bloomberg stealth UA) are low-effort. The deadline is not in immediate jeopardy but should not be deferred indefinitely. Recommend scheduling Phase 1 completion in the next available session that is not occupied by Immediate-tier deployments.

---

## 7. OPEN ISSUES — RE-PRIORITISATION

| # | Title | Assessment |
|---|-------|------------|
| #47 | Intermediate retrieval artifacts not namespaced | No change to priority. Pre-production blocker, non-urgent while ALJ is manual-trigger-only. Operator decision required before second real client. |
| #54 | Broadcaster-level dedup gap | Slightly reduced urgency. CCTV TV pages (the primary dedup offender) are now excluded at filter level for WS1. The remaining exposure is news.cctv.com (article pages, which pass the exclusion list). Worth keeping open but not urgent relative to current trust repair work. |
| #56 | Orchestrator exit=1 on ALJ | No change. Not blocking. Investigate with `bash -x` on next ALJ manual run as planned. |
| #63 | ALJ freshness label inconsistency | **Move up slightly.** Issue #62 (which was blocking this) is now resolved. This should be rechecked on the next ALJ manual run. The inconsistency (same source labeled CONTEXT-7D inline and NEW-24H in appendix) is an agent-prompt behavior issue addressable in CP-020 prompt tightening. Should be on the checklist for the next ALJ session. |

No issues require immediate escalation ahead of the 2026-06-09 cron run.

---

## 8. QUESTIONS FOR THE OPERATOR

**Requiring a decision before next session:**

**Q1 — D14 Yvette Cooper verification (BLOCKING streak resumption)**
D14 contains a "Yvette Cooper China visit" claim. The exact same claim was the confirmed misbinding in D17. Without seeing D14's cited source for this claim, certification cannot proceed. Can the operator locate the original D14 Lark delivery and check which source was cited for the Yvette Cooper bullet? If the cited source explicitly names Yvette Cooper and her China trip, D14 is clean on Layer 4. If the cited source is a US-China tariff aggregator page (as in D17), D14 has the same failure.

**Q2 — ADV-016 partial deployment**
The cron log shows archive directory + final_output + validation_result being archived from D18 onward. This was not mentioned in the 2026-06-06 or 2026-06-08 session close notes. Operator should confirm with Claude Code: (a) is this the intended partial ADV-016 implementation, and (b) which specific files were modified? This affects the scope of the "remaining ADV-016" deployment.

**Q3 — Streak resumption timeline**
Once the D14 Yvette Cooper question is answered, the operator should designate a streak resumption date. The clean delivery count has been held since 2026-06-06. Tier 2 work (CP-021 etc.) is gated on this decision. A path should be agreed: e.g., "if D13/D14/D15 certified by 2026-06-10, resume count from 3/10 and begin CP-021 implementation."

**For information, no decision required:**

- Confirmation run output (current VPS sync) includes a "France/UK/Germany/Ukraine leaders meeting" bullet with no China relevance. This is expected off-target content from the eu_r1 query — not a quality concern for the confirmation run, but illustrates why CP-022 query refinement matters.
- res_e8c045d3255d (kuaixun.cngold.org) in the confirmation run is a Gelonghui financial news flash index page. It passed the freshness filter but is a low-authority source for geopolitical claims. This source type would be caught by ADV-014 L2 keyword gate (`更多>` may appear in flash index pages) but not by the char threshold (char count likely above 80).

---

## COMPLIANCE CONFIRMATION

> ✓ No architecture changes were made or proposed outside phase scope.
> ✓ No phase drift occurred during this session.
> ✓ No scope expansion was introduced.

---

*COWORK-REVIEW-REPORT-20260608 | v1.0 | 2026-06-09 | Prepared by Claude CoWork*
*In response to COWORK-REVIEW-REQUEST-20260608*
