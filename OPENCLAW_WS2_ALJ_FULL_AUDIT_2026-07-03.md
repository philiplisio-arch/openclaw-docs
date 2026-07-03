# OPENCLAW WS2 / ALJ JAMEEL MOTORS — FULL AUDIT

---
document_id: OPENCLAW_WS2_ALJ_FULL_AUDIT_2026-07-03
date: 2026-07-03
author: Claude Sonnet 4.6
status: AUDIT REPORT — read-only; no code or config modified
scope: alj_china_auto_001 and alj_china_auto_x01; all runtime, config, and output artifacts as of 2026-07-03
---

---

## 10. EXECUTIVE SUMMARY

**Where WS2 stands:** Structurally sound but not ready for external delivery. The pipeline runs daily, is consistently using the crawler-based sourcing model, and has passed citation validation on the majority of recent runs. The content itself is auto-sector-relevant, well-cited, and properly attributed. However, several critical gaps prevent external delivery: the source appendix does not meet its own stated spec, citation alignment is warn-only (not a blocking gate), Issue #66 (citation misbinding) is unresolved at the detector level, and the July 3 run was blocked entirely by a Gemini API error with no failover to a backup model.

**What is working:**
- Crawler sourcing fully operational; Baidu/Brave correctly bypassed
- 103-source retrieval packages with healthy family/tier diversity (10 families, 22% max concentration)
- Citation syntax valid: 24/24 and 27/27 on July 1 and 2 runs
- Citation alignment strong: 9/12 and 16/16 respectively; 0 misaligned on both
- pilot_mode correctly holds all output; internal-review labels applied
- Completeness gate blocking when agent output is empty (July 3 caught and labeled)
- Traceability archive running cleanly on all runs

**What is risky:**
- Model reliability: Gemini 2.5 Pro produced a provider error on July 3 (gateway fell to Flash, which returned an error); no DeepSeek/Kimi failover is wired for WS2 (WS1 has failover, WS2 does not)
- Source appendix: config requires a rich 9-field appendix (Chinese title, English title, publisher, date, URL, blurb, ALJ relevance note, used/not-used, related section); the pipeline only generates title|publisher|date|url via citation_sub.py — the richer fields are never populated
- citation_alignment is warn-only, not blocking — grounding is not mechanically enforced
- Issue #66 (citation misbinding, "valid ID but wrong source") — generator mechanism resolved, but detector not yet a gate
- config/cron mismatch: alj_china_auto_001 says `schedule: null` (manual) but IS wired into Sunday 13:00 cron

**Is WS2 client-grade today?** No. Internal operator review only.

**Next 1–2 actions:**
1. Wire a model failover (DeepSeek V4 Flash or Kimi k2.5) into the WS2 path so a Gemini outage does not produce zero output.
2. Decide whether to implement the full source appendix or declare the current citation_sub.py SOURCES block sufficient. This is a product decision, not a code problem.

---

## 1. CURRENT AS-BUILT STATE

### What trigger runs WS2?

WS2 runs via **two separate config instances**:

| Config | Client ID | Cron | Purpose |
|---|---|---|---|
| `alj_china_auto_x01` | daily experiment | `32 7 * * *` — every day at 07:32 CST | Feedback loop / iteration instrument |
| `alj_china_auto_001` | Sunday official | `0 13 * * 0` — Sundays 13:00 CST | Production candidate (manual-or-cron, see below) |

### Is WS2 manual, cron, or both?

**Both**, but with a config/cron mismatch (see Section 2). The x01 leg runs daily by cron. The 001 leg runs by cron every Sunday; its config says `schedule: null # Manual trigger only` which contradicts the live crontab entry.

### What exact command is used?

```bash
/bin/bash /root/run_light_to_lark.sh --client_id alj_china_auto_x01
/bin/bash /root/run_light_to_lark.sh --client_id alj_china_auto_001
```

Both append to `/root/openclaw_logs/light_to_lark.log`.

### What client config is loaded?

`/root/openclaw_docs/config/client_config_alj_china_auto_x01.yaml` and `client_config_alj_china_auto_001.yaml`. Both are near-identical; x01 adds `lark_append: true`. Key active settings:

| Field | Value (both configs) |
|---|---|
| `delivery_mode` | `internal_review` |
| `enrichment` | `true` |
| `pilot_mode` | `true` |
| `source_preferences.mode` | `crawler` |
| `source_filter.chinese_only` | `false` |
| `source_filter.source_language` | `zh_en` |
| `agent_model` | `google/gemini-2.5-pro` |
| `lookback_days` | `7` |
| `require_complete_source_appendix` | `true` |
| `brain_context` | `false` |
| `linkedin_draft` | `false` |

### What env vars are exported?

Loaded by `load_client_config.py` → `loader.env` → sourced into run script. Active exports include:
`OPENCLAW_CLIENT_ID`, `OPENCLAW_ARTIFACT_NAMESPACE`, `OPENCLAW_PILOT_MODE=true`, `OPENCLAW_DELIVERY_TYPE=internal_review`, `OPENCLAW_AGENT_MODEL=google/gemini-2.5-pro`, `OPENCLAW_REPORT_TEMPLATE=alj_china_auto_weekly_v1`, `OPENCLAW_QUERY_TEMPLATE=alj_jameel_weekly_v2`, `OPENCLAW_ENRICHMENT=true`.

### What model is actually used?

Config: `google/gemini-2.5-pro`. The run log confirms this is loaded, not passed as a flag:

```
[AGENT] model=google/gemini-2.5-pro (requested; set in openclaw.json, NOT passed as flag)
```

On the July 3 run, the gateway **fell back to gemini-2.5-flash** and that call returned an error:
```
[agent/embedded] isError=true model=gemini-2.5-flash provider=google error=An unknown error occurred
```

**No DeepSeek or Kimi failover is wired for WS2.** The gateway has a Gemini→DeepSeek-flash→Kimi failover for general use, but the per-client model override (`agent_model: google/gemini-2.5-pro`) appears to bypass that chain; when Pro fails, the gateway attempted Flash but that also failed, returning an empty agent output.

### Is OPENCLAW_SOURCE=crawler active?

**Yes.** Confirmed in every run log:
```
[SOURCE] building crawler retrieval package for alj_china_auto_x01
[SOURCE] crawler-injected retrieval package (web retrieval skipped)
```

### Are Brave/Baidu actually bypassed, or still invoked?

**Bypassed.** Brave and Baidu are NOT called. The config retains `priority_providers: [brave, baidu]` and `brave_enabled: true` as stale fields, but `source_preferences.mode: crawler` causes the retrieval path to go directly to `to_retrieval_package.py` from the crawler frontier. No web search is executed. These config fields are dead code in the current runtime.

### Is full-text enrichment actually active?

**Yes.** `enrichment: true` is loaded, and the pipeline fetches full article text. The July 3 phase5 log confirms 142 auto-relevant frontier rows passed through full-text fetching before the 103 retained.

### Is pilot_mode active?

**Yes, on both configs.** `pilot_mode: true`. All deliveries go to the internal Lark doc with labels. No output has reached an external client.

### Is delivery_mode internal_review active?

**Yes.** Both configs set `delivery_mode: internal_review`. The internal review posture (labels-not-blocks; delivery proceeds with CLEAN/BLOCKED/ALIGNMENT-WARNING labels) was adopted 2026-06-12 and is working as designed.

---

## 2. CONFIG / DOC / CODE CONSISTENCY

### Crawler vs Brave/Baidu

**Inconsistency — stale config fields (low risk).**

Both ALJ configs retain `priority_providers: [brave, baidu]` and `brave_enabled: true` under `source_preferences`. The `mode: crawler` field correctly overrides these in the runtime, and the run logs confirm Brave/Baidu are never called. However, the stale fields create confusion: a reader of the config without knowledge of the runtime would conclude Brave and Baidu are active.

**Recommendation:** remove `priority_providers` and `brave_enabled` from the crawler-mode configs, or add a comment marking them as inactive.

### Chinese-only vs zh_en

**Consistent.** Both configs set `chinese_only: false` and `source_language: zh_en`. The actual outputs contain primarily Chinese-language sources (Sections 1–3) with limited international content (Section 4). This matches the config intent.

**Partial concern:** The config allows `source_region: china_plus_international`, but in practice international sources are scarce. Section 4 in both July 1 and July 2 outputs contains only 1 bullet each (Volkswagen restructuring; Lamborghini PHEV launch) — both sourced from Chinese-language media reporting on international topics. Genuine non-Chinese source corroboration is absent. This is a sourcing/frontier issue, not a config mismatch.

### Weekly vs daily naming

**Inconsistency — labeling vs cadence mismatch.**

The product is named "ALJ China Auto **Weekly** Brief" and Week Ending dates are populated, but the x01 leg runs **daily**. The x01 config is documented as a "feedback-loop instrument; never a delivery candidate" — however, both run logs and Lark labels do not distinguish between experiment and candidate. An uninformed reader of the Lark doc cannot tell which editions are weekly-candidate vs daily-experiment.

**Recommendation:** add a DAILY EXPERIMENT label to x01 Lark entries so weekly-candidate (001) runs are visually distinct.

### Pilot/internal delivery vs external delivery

**Consistent.** Both configs are in `pilot_mode: true` and `delivery_mode: internal_review`. No external delivery has ever occurred. The internal Lark credentials are the ALJ Feishu doc (`/root/openclaw_secrets/lark_webhook_alj_china_auto_001`). Config note confirms "no live delivery credential exists yet" for an external client.

### Gemini model config vs actual invocation

**Partial inconsistency — provider fallback behavior unclear.**

Config specifies `google/gemini-2.5-pro`. Runtime confirms Pro is the requested model. The July 3 failure shows the gateway attempted a fallback to Gemini Flash, but that also errored. The gateway's Gemini→DeepSeek-flash→Kimi failover chain (deployed 2026-06-15 per memory record `gateway-model-failover`) does not appear to be engaged for the per-client `agent_model` override; only the gateway's default path uses the failover chain.

**This is the most operationally significant gap: WS2 has no effective model failover.** One Gemini outage = zero output.

### Stale unresolved issues that may already be fixed

| Issue | Issues Log Status | Evidence-Based Assessment |
|---|---|---|
| #54 Broadcaster dedup gap | OPEN | Still open; no dedup.py patch in log history; CCTV-slot duplication risk persists |
| #56 Orchestrator exit=1 | OPEN | Still occurs (per run patterns); July 3 log shows exit=0 actually, but blank output; root cause still unknown |
| #63 Freshness label inconsistency | OPEN | Stale fields in config still present; no CP-020 ALJ tightening deployed |
| #66 Citation misbinding | OPEN (downgraded) | Generator resolved; detector (citation_alignment) is warn-only; still open |
| #75 No-delivery alerting | OPEN (WS1, but affects WS2) | WS2 does append BLOCKED-GRADE labels to Lark; no dedicated ALERTS.log entry for ALJ blocked runs |

---

## 3. SOURCE PIPELINE AUDIT

**Based on July 3 phase5 run log and June 28 ALJ discovery dashboards.**

### Frontier statistics (July 3 x01 run)

| Metric | Value |
|---|---|
| Frontier total rows | 2,239 |
| Within 7-day window | 750 |
| Auto-relevant (tagged) | 142 |
| Stale/undated dropped (authority gate) | 8 |
| Delivered to retrieval package | 103 |
| Capped to agent input | 20 |

### Source families (June 28, alj_china_auto_001 — 127 sources)

| Family | Count | Notes |
|---|---|---|
| Dongchedi | 33 (26%) | Near-top concentration — ok (under 35%) |
| D1EV | 23 (18%) | Specialist EV outlet |
| Securities Times | 16 | Financial press |
| 36Kr | 14 | Tech/startup press |
| Yicai | 12 | Business press |
| Xinhua | 12 | Official state media |
| China Daily | 8 | Official bilingual |
| CAAM | 5 | Official association |
| CADA | 3 | Dealer association |
| Guangming | 1 | State media |

**Top concentration: 26% (Dongchedi) — within the 35% threshold.** Family diversity is acceptable.

### Authority tier mix (June 28, alj_china_auto_001)

| Tier | Count |
|---|---|
| T1 official/association | 8 |
| T2 state media | 13 |
| T3 financial/specialist | 84 |
| T4 platform | 14 |
| Untiered | 8 |

**T3 dominates (66%)** — expected for automotive specialist content. T1+T2 combined = 16.5%, which is reasonable for the topic area but low for policy/regulatory coverage (only 2 policy_official tags in June 28 dashboard). CAAM (5 sources) and CADA (3 sources) are present and supply official association coverage.

### Cross-cutting tag coverage (June 28)

| Tag | Count | Assessment |
|---|---|---|
| export_gcc | 15 | Moderate — GCC/tariff context present |
| toyota_lexus | 30 | Good — Toyota competitive coverage |
| nev_tech | 24 | Good — technology content strong |
| china_oem | 23 | Good — OEM brand coverage |
| dealer | 14 | Adequate |
| sales_data | 7 | Light — CPCA/CAAM sales figures sparse |
| policy_official | 2 | **Very low** — regulatory/policy coverage is the weakest dimension |

### Stale/undated source count

8 sources dropped by the authority freshness gate on July 3. This is a small number relative to 142 auto-relevant; the freshness gate is functioning correctly.

### Source-family concentration

Maximum 26% (Dongchedi) — within acceptable bounds. No single-source dominance. 10 distinct families in the retrieval package.

### Domain exclusion (low-authority domains)

The domain exclusion list is active (wikipedia.org, baike.baidu.com, wikiwand.com, fandom.com, made-in-china.com, alibaba.com, electriccarscheme.com, innovation-village.com). No exclusion violations have appeared in recent validated outputs.

### Jameel relevance

**Moderate but improving.** The July 1 and 2 outputs contain directly relevant content:
- Partner brand coverage: BMW, Chery (Omoda/Jaecoo), Volkswagen
- Dealer association coverage (CADA branches for BMW/Mercedes/Porsche)
- NEV technology coverage (EV standards, battery requirements)
- Regulatory coverage (L3/L4 AV standards)

**Gap:** Minimal coverage of Jameel-specific territories (GCC, Türkiye, Morocco, South Africa). Section 4 (International Context) contains at most 1 bullet per run, and those bullets are sourced from Chinese media reporting on European/international topics rather than from GCC-region sources.

### Toyota/Lexus relevance

Good — `toyota_lexus: 30` in June 28 dashboard. Toyota competitive intelligence is consistently present in the frontier. The July 1 output included coverage of Volkswagen restructuring (competitor context relevant to Toyota's position). Toyota was specifically mentioned in the topic_focus config.

### China NEV/export/GCC relevance

NEV coverage is strong (nev_tech: 24, china_oem: 23). Export/GCC coverage is present but light (export_gcc: 15). Policy coverage is very thin (policy_official: 2). This means the briefs are strong on technology and market dynamics but weak on trade-policy angles relevant to ALJ's export-market positioning.

---

## 4. VERIFICATION CHAIN AUDIT

### Layer-by-layer analysis

| Layer | File/Script | Input | Output | Client-namespaced | Deterministic | On failure |
|---|---|---|---|---|---|---|
| Crawler frontier | `cbiz_crawl.py` / `crawl.py` | RSS/HTML scrape | SQLite frontier | Shared (WS2 uses alj config tags) | Yes | Silent (no articles added that day) |
| Retrieval package builder | `to_retrieval_package.py` | Frontier SQLite | `retrieval_package_{ns}.json` | Yes | Yes | Silent if 0 sources |
| Agent input builder | `build_agent_input_slim.py` | Retrieval package | `agent_input_slim_{ns}.txt` | Yes | Yes (capped to 20) | Exit non-zero |
| Gateway agent | `openclaw agent` | Agent input slim | `final_output_{ns}.txt` | Yes | No (LLM stochastic) | Error → empty output → RE_1 completeness block |
| Resolver | `resolve_source_numbers.py` | Final output | Rewritten final output | Yes | Yes | Warns; logs drops |
| Scrubber | `scrub_result_ids.py` | Final output | `final_output_scrubbed_{ns}.txt` | Yes | Yes | exit=1 if SECTION 1 has 0 cited bullets |
| Validator | `validator.py` | Scrubbed output + retrieval | `validation_result_{ns}.json` | Yes | Yes | WARN (cite structure); FAIL if 0 citations |
| citation_alignment | Embedded in validator | Agent output snippets + sources | Part of validation_result.json | Yes | Semi (NLP overlap check) | warn_only (not blocking) |
| citation_sub.py | citation substitution + SOURCES | Scrubbed output | Lark payload with SOURCES | Yes | Yes | Exit non-zero |
| Lark delivery | `lark_doc_relay.py` | Lark payload | ALJ Feishu doc | Yes (per-client doc_id) | Yes | HTTP error → no delivery |

### Critical gaps in the verification chain

1. **citation_alignment is warn-only**: Claim-source alignment is checked (12/16 bullets were checked in July 1/2) but mismatches do not block delivery. A clean citation syntax (GREEN 24/24) can coexist with a factually misaligned brief. Issue #66 is the documented instance.

2. **Agent layer is non-deterministic and has no failover**: The model produces variable-length output. If Gemini errors (as on July 3), the completeness gate catches it, but the user gets zero content. No backup model exists for WS2.

3. **Source appendix field coverage**: `citation_sub.py` generates a `SOURCES` block with `title|publisher|date|url`. The config requires a 9-field appendix (Chinese title, English title, publisher, date, full URL, blurb/snippet, ALJ relevance note, used/not-used, related section/bullet). **The gap between config spec and delivered appendix has never been formally closed or waived.** The delivered appendix meets 4 of 9 required fields.

4. **No-delivery alerting for ALJ**: WS2 blocked runs are labeled in Lark (BLOCKED-GRADE label), but there is no entry in `ALERTS.log` for ALJ blocked runs. The July 3 block would not trigger an email or operator alert outside the Lark doc label.

---

## 5. WS1 COMPARISON

| Dimension | WS1 Status | WS2 Status | Gap |
|---|---|---|---|
| Publish-date window (not crawl-time) | SHIPPED 2026-06-24 (PUB_WINDOW_DAYS) | Uses `lookback_days: 7` on frontier fetch-time; not explicitly publish-date filtered | WS2 may surface crawled-later articles from earlier in the week |
| Source clustering / corroboration | SHIPPED — real distinct-outlet count, deterministic clustering | Not implemented — each bullet cites 1–2 sources; no corroboration measurement | WS2 has no multi-outlet corroboration check |
| Real corroboration score | SHIPPED — recount_outlets() | Not present | No |
| Recency-aware ranking | SHIPPED — recency decay in ranking | Not present for WS2 sourcing | No explicit recency ranking |
| Source-first / evidence-first writing | WS1 = verbatim span extraction, evidence-first synthesis | WS2 = full-text enrichment fed to agent; agent writes from full text, not extracted verbatim spans | WS2 does not use verbatim-span grounding |
| Number verification | SHIPPED — verify step checks numbers vs evidence | Not present for WS2 | No number-grounding gate |
| Qualitative claim grounding | Still OPEN (#76) | Also absent | Both open |
| Source appendix | SHIPPED — deterministic citation_sub.py SOURCES block | PARTIALLY SHIPPED — same citation_sub.py SOURCES, but config requires 9-field appendix, only 4 delivered | WS2 spec gap unfilled |
| No-delivery alerting | OPEN (#75) — Alerts.log not wired | Not wired for ALJ either | Both open |
| Operator review labels | SHIPPED — CLEAN/HELD-MODE/BLOCKED-GRADE | SHIPPED — same label system | Same |
| Model failover | WS1 uses DeepSeek V4 Flash — one provider | WS2 uses Gemini Pro — one provider, no failover | WS2 is more fragile |

**WS2 already has:** Citation syntax validation (GREEN/WARN/FAIL), citation_alignment in warn-only mode, scrubber (uncited bullet removal), pilot_mode gate, internal_review labels, deterministic SOURCES block, traceability archive, session isolation, full-text enrichment, domain exclusion, diversity caps.

**WS2 partially has:** citation_alignment (exists but warn-only), source appendix (4/9 fields vs spec).

**WS2 lacks:** Evidence-first grounding, verbatim-span extraction, corroboration measurement, recency-decay ranking, number-grounding verification, model failover, no-delivery alerting.

---

## 6. OPEN ISSUES REVIEW — WS2 IMPACT

### Issue #54 — Broadcaster-level dedup gap

**Issues Log status:** OPEN — operator decision required.
**WS2-specific impact:** Present. The ALJ frontier includes Xinhua and CCTV-adjacent sources. Near-duplicate stories across outlets/slots can inflate retrieval packages. In the June 28 dashboard Xinhua accounts for 12 sources. Dedup.py keys on URL only; broadcaster-level dedup is not applied.
**Actual code status:** No patch applied; dedup.py URL-key logic unchanged.
**Recommendation:** KEEP OPEN. The 35% concentration cap limits the worst case. Address as part of WS2 quality hardening before external delivery.

### Issue #56 — Orchestrator exit=1 on ALJ runs

**Issues Log status:** OPEN — not blocking; recovery path reliable.
**WS2-specific impact:** Present. Root cause (something in the orchestrator wrapper after agent completion exits non-zero) still unknown. The July 3 run log shows exit=0 and `output complete heuristic = false` together, which is a different failure mode (agent returned empty output, not an exit=1). The July 3 behavior was a model error (Gemini Flash returned error), not the original Issue #56.
**Recommendation:** KEEP OPEN for the original mystery exit=1. The July 3 block is a separate issue (model failover gap).

### Issue #63 — ALJ freshness label inconsistency

**Issues Log status:** OPEN — agent applying inconsistent labels; CP-020 prompt needs tightening.
**WS2-specific impact:** Present. The config notes this was blocked on Issue #62 (now resolved). The June 28 dashboard shows no freshness label entries in the issue tracker; no CP-020 tightening for ALJ has been deployed.
**Actual code status:** No ALJ-specific CP-020 prompt tightening applied. The `SOURCES` block is pipeline-generated (citation_sub.py); inline freshness labels if any are agent-generated. Since citation_sub.py now strips agent Section 8, any inline freshness labels in bullets are agent-controlled and potentially inconsistent.
**Recommendation:** KEEP OPEN. Evaluate once the source appendix spec is finalized.

### Issue #66 — Cross-source citation misbinding

**Issues Log status:** OPEN (downgraded) — generator mechanism removed 2026-06-10; detector in calibration.
**WS2-specific impact:** High. WS2 still uses the original trust model (citation syntax validation only). The evidence-first trust model was deployed only to WS1. WS2 citation_alignment is warn-only and the clean runs on July 1/2 (0 misaligned) are encouraging but do not guarantee grounding — citation alignment checks snippet overlap, not verbatim source grounding.
**Actual code status:** Option B (citation_alignment) is live, warn-only. July 1: 9/12 aligned, 3 insufficient anchors. July 2: 16/16 aligned. Clean streak for citation_alignment = 2 runs of an unspecified required streak before blocking promotion.
**Recommendation:** KEEP OPEN. Promote citation_alignment to blocking is the next milestone for WS2 trust posture.

### Issue #75 — Silent no-delivery on crash

**Issues Log status:** PARTIAL — WS1 category KeyError patched; dedicated ALERTS.log not wired.
**WS2-specific impact:** Medium. The July 3 WS2 block was labeled BLOCKED-GRADE in Lark (operator must read Lark to notice). There is no email alert, ALERTS.log entry, or system notification for ALJ blocked runs. A blocked Sunday 001 run would be invisible until the operator opens Lark.
**Recommendation:** KEEP OPEN. Add ALJ blocked-run entry to ALERTS.log as part of the minimum fix packet.

### Issue #76 — Qualitative claim grounding

**Issues Log status:** OPEN — numbers-only verification for WS1.
**WS2-specific impact:** WS2 has no number verification at all (WS1 at least has number-grounding at verify step). Qualitative claims in WS2 briefs are entirely unverified beyond citation_alignment snippet overlap.
**Recommendation:** KEEP OPEN. This is a NICE/later item for WS2 given other priorities.

---

## 7. LATEST OUTPUT REVIEW

### Run 1 — 2026-07-01 (x01 daily, run_20260630T233203Z)

| Dimension | Value |
|---|---|
| Validator status | GREEN PASS |
| Citation count | 27 citations checked, 27 matched, 0 failures |
| citation_alignment | 16/16 aligned, 0 weak, 0 misaligned, 0 insufficient anchors |
| Source appendix integrity | Not in traceability file (appended by citation_sub.py to Lark payload) |
| Unsupported/weak claims | None flagged by citation_alignment |
| Freshness label consistency | Not verified (labels if present are inline, agent-generated) |
| Source diversity | 10 families, tiers T1–T4 |
| Sections present | 1, 2, 3, 4 + LINKEDIN DRAFT (despite config `linkedin_draft: false`) |
| Content quality | High — specific facts, Chinese-language sources, regulations cited correctly |
| Client-readiness score | **5/10** — content strong; LinkedIn section policy violation; source appendix spec gap; no corroboration; citation alignment not blocking |
| Disposition | Eligible for continued internal review; NOT eligible for external delivery |

**Notes:** LinkedIn Draft appeared despite config `linkedin_draft: false`. This is agent non-compliance with the output format spec. Content is otherwise accurate and ALJ-relevant (EV safety standards, AV regulations, BMW China-specific model, Volkswagen restructuring).

### Run 2 — 2026-07-02 (x01 daily, run_20260701T233202Z)

| Dimension | Value |
|---|---|
| Validator status | GREEN PASS |
| Citation count | 24 citations checked, 24 matched, 0 failures |
| citation_alignment | 9/12 aligned, 0 weak, 0 misaligned, 3 insufficient anchors |
| Source appendix integrity | Not in traceability file |
| Freshness label consistency | Not verified |
| Source diversity | Same 10 families |
| Sections present | 1, 2, 3, 4 (no LinkedIn Draft this run) |
| Content quality | Good — specific models and dates, dealer association news, policy updates |
| Client-readiness score | **5/10** — same structural gaps; 3 insufficient citation anchors is a minor concern |
| Disposition | Eligible for continued internal review; NOT eligible for external delivery |

**Notes:** The 3 insufficient anchors (citation_alignment couldn't verify 3 bullets against source snippets) indicate the full-text of those sources may not have been retrieved or matched. Not a validator failure, but a trust caveat.

### Run 3 — 2026-07-03 (x01 daily, run_20260702T233203Z)

| Dimension | Value |
|---|---|
| Validator status | WARN (YELLOW) — 0 citations checked (0 in final output) |
| Citation count | 0 |
| citation_alignment | 0 bullets checked |
| Source appendix integrity | N/A — blocked before SOURCES generated |
| Root cause | Gemini 2.5 Pro API error → gateway fell back to Gemini Flash → Flash also errored → agent returned empty/truncated output → RE_1 completeness gate blocked |
| Delivery decision | `blocked_control_fail` → converted to labeled BLOCKED-GRADE delivery in Lark |
| Lark label | `INTERNAL TEST — BLOCKED-GRADE: scrubber gate failed (exit=1) — NOT CLIENT-READY \| EXPERIMENTAL ENRICHMENT (CP-026) \| HELD-MODE PILOT` |
| Client-readiness score | **0/10** — no content |
| Disposition | HELD; BLOCKED-GRADE labeled in Lark; no content delivered |

**Notes:** This is the second known instance of a Gemini-driven WS2 failure. The gateway failover (Gemini→DeepSeek-flash→Kimi, deployed 2026-06-15) does NOT appear to be engaged for the per-client `agent_model` override. The frontier and retrieval package were healthy (103 sources, 20 capped for agent input), confirming the failure is entirely at the agent/model layer.

---

## 8. RECOMMENDED MINIMUM FIX PACKET

The following is the smallest safe change packet to bring WS2 to WS1-level trust posture. No implementation is authorized by this audit.

### MUST before external delivery

| # | Item | Rationale |
|---|---|---|
| M-1 | Wire model failover for WS2 (DeepSeek V4 Flash or Kimi k2.5 as backup to Gemini 2.5 Pro) | July 3 block proves Gemini Pro is not reliable enough as a single model. One outage = zero delivery. |
| M-2 | Promote citation_alignment to blocking for WS2 after a clean streak | Currently warn-only. External delivery requires mechanical claim-source grounding enforcement, not just structural citation validation. Blocking at citation_alignment is the minimum acceptable gate before client exposure. Required streak: 5 clean runs (aligned ≥ 0.50 on all checked bullets). |
| M-3 | Define and close the source appendix spec gap | Config says 9-field appendix; pipeline delivers 4 fields. Either implement the full spec (blurb, ALJ relevance note, used/not-used, related section) or formally waive the 4 missing fields and update the config. A client-grade ALJ brief must have a verifiable source appendix. |
| M-4 | Resolve or formally waive Issue #66 (citation misbinding) | The detector (citation_alignment) must be blocking before external delivery. See M-2. |
| M-5 | Add ALJ blocked-run entry to ALERTS.log | Currently a Sunday 001 block is invisible until operator opens Lark. The operator must be alerted to any missed delivery. |
| M-6 | Fix cron/config mismatch for alj_china_auto_001 | Config says `schedule: null` (manual); crontab has a Sunday 13:00 entry. Update config to reflect reality or remove the cron entry if truly manual. |

### SHOULD before regular internal delivery

| # | Item | Rationale |
|---|---|---|
| S-1 | Remove stale Brave/Baidu fields from config | Dead config creates confusion; `priority_providers` and `brave_enabled` are never read in crawler mode. |
| S-2 | Add DAILY EXPERIMENT label to x01 Lark entries | Operator cannot distinguish experiment iterations from Sunday production candidate without labels. |
| S-3 | Fix LinkedIn Draft agent non-compliance | Config says `linkedin_draft: false`; July 1 output included LinkedIn Draft. Prompt needs explicit prohibition or the output section gate needs to strip it. |
| S-4 | Improve policy_official coverage | Currently 2 sources per run for policy/regulatory. Regulatory changes (L3/L4 standards, NEV policy) are exactly what ALJ clients need. Add MIIT/NDRC/MOFCOM as prioritized seeds with a policy tag. |
| S-5 | Add GCC/international source corroboration | Section 4 (international context) consistently has 1 bullet from Chinese-language reporting. Genuine GCC-region or English-language source coverage would materially improve ALJ relevance. |

### NICE for later

| # | Item | Rationale |
|---|---|---|
| N-1 | Deploy number-grounding verification for WS2 | WS1 has a number-verify step; WS2 has none. Quantitative claims (23 million NEV sales, 100,000 Volkswagen layoffs) are unverified. |
| N-2 | Implement corroboration scoring per story | WS1 uses recount_outlets(); WS2 has no multi-outlet corroboration. Single-source stories go unchallenged. |
| N-3 | Deploy publish-date window enforcement | WS2 uses crawl-time window; stale stories published before the crawl window may appear. |
| N-4 | Add broadcaster-level dedup (Issue #54) | Low impact at current Xinhua/CCTV volumes; worth adding before volume scales. |
| N-5 | Activate brain_context for alj_china_auto_001 | Config is `brain_context: false` with note "no run history exists yet." Sufficient history now exists; Brain Lite would give topic-differentiation across weeks. |
| N-6 | Resolve Issue #56 (orchestrator exit=1) | Not blocking, but unknown root cause is technical debt. |

---

## 9. ACCEPTANCE CRITERIA — WS2 CLEAN-RUN GATE

A WS2 clean run for internal delivery is defined as follows.

### Minimum green criteria (internal delivery)

| Criterion | Threshold |
|---|---|
| Validator status | GREEN PASS (≥1 citation checked, 0 failures) |
| citations_checked | ≥ 10 |
| sources_matched / citations_checked | 100% |
| uncited_claims_removed | 0 preferred; ≤ 2 tolerated |
| unsupported_groups | 0 |
| citation_alignment misaligned | 0 (warn-only; operator reviews) |
| citation_alignment insufficient_anchors | ≤ 3 tolerated |
| completeness gate | SECTION 1 has ≥ 1 cited bullet |
| Domain exclusions | No excluded domains in delivered output |
| pilot_mode label | Present and correct |

### Warnings tolerated for internal delivery

- `citation_alignment` warn-only is acceptable for internal delivery
- 3 insufficient anchors (citation_alignment) is tolerated
- A LinkedIn Draft appearing despite config (S-3) is a quality flag, not a blocker for internal delivery
- `orchestrator exit=1` (Issue #56) is tolerated (recovery path reliable)

### What blocks delivery

- `validator status = FAIL`
- `completeness gate` blocked (missing SECTION 1)
- Agent returned empty output (model error)
- Any citation that resolves to an excluded domain in the delivered Lark payload

### Source appendix — non-negotiable requirements before external delivery

1. Every source cited in the brief must appear in the SOURCES appendix
2. Each entry must include: publisher, publication date, full URL, and English title (current 4-field spec)
3. Before external delivery: blurb/snippet, ALJ relevance note, and used/not-used flag must be added (M-3 above)
4. No fabricated URLs (Issue #62 resolved; pipeline-generated SOURCES eliminates this risk)

### When citation_alignment can move from warn-only to blocking

After **5 consecutive clean runs** for the WS2 path where:
- All bullets checked have `aligned` ≥ 0.50 (or `insufficient_anchors` — not `misaligned`)
- Zero `misaligned` bullets on any run in the streak
- Operator has reviewed at least one full run under the blocking threshold to confirm false-positive rate is acceptable
- Streak must be on the same config (x01 daily or 001 Sunday — separate streaks)

---

## APPENDIX — KEY ARTIFACT PATHS

| Artifact | Path |
|---|---|
| Daily run log | `/root/openclaw_logs/phase5_run_YYYYMMDD_HHMMSS.log` |
| Light-to-lark log | `/root/openclaw_logs/light_to_lark.log` |
| Retrieval package | `/root/openclaw_phase5/data/retrieval_package_alj_china_auto_x01.json` |
| Agent input | `/root/openclaw_phase5/data/agent_input_slim_alj_china_auto_x01.txt` |
| Final output (pre-citation-sub) | `/root/openclaw_phase5/data/final_output_alj_china_auto_x01.txt` |
| Scrubbed output | `/root/openclaw_phase5/data/final_output_scrubbed_alj_china_auto_x01.txt` |
| Validation result | `/root/openclaw_phase5/data/validation_result_alj_china_auto_x01.json` |
| Traceability archive | `/root/openclaw_traceability/alj_china_auto_x01/YYYY-MM-DD/` |
| Discovery dashboard | `/root/openclaw_phase5/data/alj_discovery_dashboard_alj_china_auto_x01_YYYYMMDD.md` |
| ALJ 001 dashboard | `/root/openclaw_phase5/data/alj_discovery_dashboard_alj_china_auto_001_YYYYMMDD.md` |
| Client config (x01) | `/root/openclaw_docs/config/client_config_alj_china_auto_x01.yaml` |
| Client config (001) | `/root/openclaw_docs/config/client_config_alj_china_auto_001.yaml` |
| Lark webhook | `/root/openclaw_secrets/lark_webhook_alj_china_auto_001` |
