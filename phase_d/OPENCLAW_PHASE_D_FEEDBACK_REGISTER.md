---
document_id: OPENCLAW-PHASE-D-FEEDBACK-001
version: 1.4
created: 2026-05-20
last_updated: 2026-05-22
status: ACTIVE
classification: OPERATIONAL — PHASE D FEEDBACK REGISTER
---

# OPENCLAW — Phase D Feedback Register

## PURPOSE

Central repository for operator and client feedback on delivered output
during Phase D controlled pilot. Every feedback item must be logged here
before action is taken. Entries are cumulative and append-only.

The operator review workflow — including the standard delivery review prompt,
CoWork output format, and change packet threshold — is defined in:
`OPENCLAW_PHASE_D_OPERATOR_REVIEW_PROCEDURE.md`

---

## FEEDBACK ID FORMAT

Feedback items are assigned sequential IDs in the format `D-FB-NNN` (e.g.,
D-FB-001, D-FB-002). IDs are assigned in order of logging and never reused.

---

## FEEDBACK CLASSIFICATION

| Code | Category |
|------|----------|
| A | Delivery-blocking |
| B | Editorial / prompt improvement |
| C | Source-quality / authority |
| D | Format / user experience |
| E | Client preference |

## SEVERITY SCALE

| Level | Meaning |
|-------|---------|
| 1 | Minor — noticeable but does not materially affect usefulness |
| 2 | Moderate — affects quality; change packet warranted after recurrence |
| 3 | Material — meaningfully degrades client-grade output |
| 4 | Delivery-blocking — must be resolved before next delivery |

## BATCHING RULE

One-off feedback should not generate a Content Change Packet unless the
operator explicitly marks it delivery-blocking (Severity 4). Non-blocking
feedback (Severity 1–3) should be batched after recurring pattern
confirmation across 3–5 reviewed deliveries.

## STATUS VALUES

New → Accepted / Rejected → Batched → Implemented → Validated / Reopened → Closed / Deferred

---

## REGISTER

| Feedback ID | Date | Run ID | Client ID | Section | Severity | Comment | Example from output | Why it matters | Classification | Proposed fix type | Client confirmed? | Disposition rationale | Status | Validation rule | Owner | Notes |
|------------|------|--------|-----------|---------|----------|---------|---------------------|----------------|----------------|-------------------|-------------------|-----------------------|--------|-----------------|-------|-------|
| D-FB-001 | 2026-05-21 | run_20260520T223002Z | china_monitor_001 | Full output | 3 | Thin retrieval package — mapping_size=7 (vs norm 14–15); 12 source numbers out of range; 4 citation groups unsupported; 4 bullets removed by scrubber | Delivered 2 ET + 2 AL bullets; expected 3 ET + 5 AL | Phase D Delivery 1 arrived materially shorter than standard; client received degraded brief on first pilot delivery | A | Diagnostic — read retrieval_package_china_monitor_001.json; investigate package assembly from raw results | Pending | Material quality event on first Phase D delivery; investigation required before pattern assessment | Monitoring — did not recur Delivery 2 or 3 | mapping_size ≥ 12; source_numbers_dropped = 0 | Operator | Did not recur on 2026-05-22 Delivery 2 (full 8-bullet brief, 25/25 citations) or 2026-05-23 Delivery 3 (19/19 citations). Two consecutive clean runs — candidate for closure pending operator decision. |
| D-FB-002 | 2026-05-22 | run_20260521T223002Z | china_monitor_001 | Logging | 2 | light_to_lark.log gap — 2026-05-22 run absent from log; pipeline completion confirmed by artifacts only | Log has 1525 lines ending with 2026-05-21 run; no 2026-05-22 entries present | Post-run analysis depends on log for resolver and scrubber metrics; gap creates partial observability loss | A | VPS investigation — check /root/openclaw_logs/ for rotated log file; update scp sync if rotation confirmed | Confirmed — not reproduced | Snapshot timing artefact — scp pulled mid-run; run present at lines 1526–1559; no log rotation | Closed | Run confirmed in log via Claude Code VPS audit | Operator | Issue #51 RESOLVED. Mitigation: run scp after 06:35 to avoid mid-run pull. No logrotate configured — file grows indefinitely; setup recommended. |
| D-FB-003 | 2026-05-23 | run_20260522T223001Z | china_monitor_001 | Full output | 3 | Topic repetition across all three Phase D deliveries — same three story clusters (US-China summit, EU-China trade, Middle East/global macro) across 2026-05-21, 2026-05-22, 2026-05-23 | run_summary topics_covered character-for-character identical across D2 and D3; D1 also same clusters | A daily brief repeating identical topics provides no incremental intelligence; core product value proposition fails | B | CP-007 — add TOPIC DIFFERENTIATION RULE to system_rules in build_agent_input_slim.py; rebuild Brain Lite digest as prerequisite. Root cause also has retrieval-side component (D-FB-004). | No | Recurrence confirmed across 3 deliveries (run_summary topics_covered); threshold met | Accepted — Batched (CP-007) | topics_covered in run_summary shows at least one cluster distinct from prior run's topics_covered across 2 consecutive runs | CoWork | Root cause is dual: (1) retrieval queries surface same dominant story clusters; (2) no agent instruction to seek differentiation. CP-007 addresses agent-side. D-FB-004 Part B addresses retrieval-side. Brain Lite digest must be rebuilt before CP-007 validates. |
| D-FB-004 | 2026-05-23 | run_20260522T223001Z | china_monitor_001 | Full output | 3 | Old articles — content in delivered brief sourced from articles published before 2026-05-22; today's brief should contain nothing older than the prior business day | Operator confirmed articles older than 48 hours present in Delivery 3 evidence pool | A daily intelligence brief presenting week-old developments as current intelligence fails its freshness promise and undermines client trust | C | Split implementation: Part A (in scope) — CP-007 adds FRESHNESS RULE to system_rules (agent preference for recent sources, language calibration when using older material). Part B (out of scope for CoWork) — operator + Claude Code retrieval investigation: inspect retrieval_package publication dates; tighten Baidu freshness filter if old articles confirmed in package. | No | Operator-confirmed on Delivery 3 | Accepted — Part A batched (CP-007); Part B parallel track (operator/Claude Code) | Part A: no Executive Take bullet frames a development >72 hours old as breaking news (operator spot-check against retrieval_package timestamps). Part B: retrieval_package timestamp audit shows no sources >48 hours in package. | Operator / CoWork | Root cause has two layers. Agent instruction (Part A) is a mitigation when retrieval returns older material. Retrieval filter tightening (Part B) is the structural fix. Both are needed. Part B requires VPS SSH access and retrieval layer inspection — out of CoWork implementation scope. |
| D-FB-005 | 2026-05-23 | run_20260522T223001Z | china_monitor_001 | Full output | 3 | No source URLs provided to reader — delivered brief attributes claims to publisher/date but provides no links; client cannot verify any claim | All three Phase D deliveries (D1, D2, D3) contain zero URLs; reader has no path to primary sources | Source accessibility is a foundational requirement of a trusted intelligence product; without URLs the brief cannot be independently verified | D | CP-008 — append SOURCES section (publisher, date, URL per cited result_id) to citation_sub.py output; all required fields confirmed present in retrieval_package (CP-006 Appendix, 2026-05-22 audit) | No | Absent across all three Phase D deliveries; three-delivery pattern confirmed | Accepted — Batched (CP-008) | SOURCES section present in delivered Lark output; all entries contain publisher + date + URL; operator URL spot-check confirms links resolve; validator result unchanged | CoWork | All retrieval_package fields required for implementation already confirmed (title, publisher, timestamp, url, result_id). HTML stripping required on title field (per CP-006 Appendix). try/except wrapper required to ensure SOURCES logic is never delivery-blocking. |
| D-FB-008 | 2026-06-06 | run_20260605T223002Z | china_monitor_001 | ET Bullet 2 / AL Bullets 2 | 4 | Cross-source citation misbinding (confirmed) — ET Bullet 2 ("European Commission has declared its trade and investment relationship with China 'not sustainable'... British foreign minister Yvette Cooper is traveling to China") and AL Bullet 2 cite res_0a5837f3bb9f (h5.article.smbae.cn) as sole source. That source's snippet is entirely about US-China tariffs and Commerce Ministry statements. Zero mention of EC, "not sustainable," Yvette Cooper, or UK in any of the 12 retrieval package snippets. Agent generated the claim from training knowledge and attached the nearest available result_id. Validator passed because it checks result_id syntax only, not claim-source alignment. | ET Bullet 2 in D17 delivered output — EC "not sustainable" + Yvette Cooper claim cited to h5.article.smbae.cn (snippet: US-China tariff Commerce Ministry statement); AL Bullet 2 same source cited for EU/UK regulatory risk framing | Fabricated claim with fabricated citation delivered to client. Fabrication rate logged as 0% is based on validator GREEN; validator cannot detect semantic misalignment. Client credibility risk if EC/Yvette Cooper facts are disputed or the linked source is checked. | A | Two separate change packets required: (1) ADV-014 — source authority filter at filter_results.py (domain exclusion + publisher quality gate); (2) ADV-015 — semantic validation layer to detect claim-source misalignment. Neither is a prompt fix — orchestrator spec prohibits prompt-based filtering. | No | Confirmed via retrieval package audit 2026-06-06 — all 12 source snippets searched; zero evidence for EC/Yvette Cooper claim | Accepted — severity 4; D17 retracted from gate streak (operator decision 2026-06-06); WS1 held-mode; ADV-014 and ADV-015 in progress | Streak does not advance until held-mode test runs approved by operator post ADV-014/ADV-015 controls | CoWork | Precise term: cross-source citation misbinding (per consultant 2026-06-06). Facts (EC statement, Yvette Cooper visit) are likely real-world events — failure is false grounding, not fabricated fact. Pipeline cannot distinguish. See Issue #66, ADV-014, ADV-015. |
| D-FB-007 | 2026-06-06 | run_20260605T223002Z | china_monitor_001 | Source composition | 2 | Brave:Baidu package split 3:9 on D17; all 3 Brave sources (CNBC, NYT, moderndiplomacy.eu) uncited by agent; delivered output 100% Chinese-sourced. Brave pool thin at package stage — ~40 raw Brave results filtered to 3 before agent sees them. Agent also passed over Brave sources for topics with direct Chinese-media coverage. | SOURCES appendix shows 8 Chinese sources only; CNBC (China retail access to US stocks), NYT (China economic fortress), moderndiplomacy.eu (China tech stocks) all present in retrieval package but uncited | A client-grade international intelligence product drawing exclusively from Chinese state/financial media on every citation undermines credibility and limits perspective diversity | C | Monitoring — CP-022A (WS1 query family dry run) is the diagnostic; will assess whether expanded query families surface a more balanced Brave pool. No immediate change packet warranted — single occurrence; topics this run were China-domestic-facing. | No | Single occurrence; topics this run naturally skewed toward Chinese primary sources; not confirmed as recurring pattern | Monitoring — batch if recurs across 3+ deliveries | Brave sources ≥ 2 cited in delivered SOURCES appendix on any run where Brave pool ≥ 5 sources in retrieval package | CoWork | First observation via retrieval_package sync (added to standard scp block 2026-06-06). Two-layer cause: (1) filtering reduces Brave ~40 raw → 3 package entries; (2) agent preferentially cites Chinese primary sources. CP-022A gates the retrieval-side fix. |

---

## OPEN ITEM COUNTS

| Category | New | Accepted | Batched | Implemented | Validated | Deferred | Total Open |
|----------|-----|----------|---------|-------------|-----------|----------|------------|
| A — Delivery-blocking | 2 | 0 | 0 | 0 | 0 | 1 | 2 |
| B — Editorial / prompt | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| C — Source-quality | 1 | 1 | 0 | 0 | 0 | 0 | 2 |
| D — Format / UX | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| E — Client preference | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **3** | **1** | **2** | **0** | **0** | **1** | **6** |

---

*OPENCLAW-PHASE-D-FEEDBACK-001 | Version 1.8 | Created: 2026-05-20 | Status: ACTIVE*

*v1.8 changes (2026-06-06): D-FB-008 updated — terminology corrected from "confirmed fabrication" to "cross-source citation misbinding" (consultant 2026-06-06); status updated from New to Accepted; D17 gate streak retraction noted (operator decision); WS1 held-mode posture recorded.*

*v1.7 changes (2026-06-06): D-FB-008 added — cross-source citation misbinding; EC/Yvette Cooper claim zero source evidence in retrieval package; validator passed on syntax only; Category A Severity 4. Open item counts updated.*

*v1.6 changes (2026-06-06): D-FB-007 added — D17 source composition; Brave:Baidu package split 3:9; all Brave sources uncited; 100% Chinese-source output; Category C Severity 2; Monitoring. Open item counts updated.*

*v1.5 changes (2026-05-23): D-FB-001 updated — did not recur Delivery 3; two consecutive clean runs; candidate for closure. D-FB-003 added — topic repetition across all three Phase D deliveries; Category B Severity 3; batched to CP-007. D-FB-004 added — old articles / freshness; Category C Severity 3; Part A batched to CP-007; Part B parallel retrieval investigation track. D-FB-005 added — no source URLs; Category D Severity 3; batched to CP-008. Open item counts updated.*

*v1.4 changes (2026-05-22): D-FB-001 status updated — did not recur Delivery 2; moved to Monitoring. D-FB-002 added — light_to_lark.log gap (2026-05-22); Category A Severity 2; Issue #51 logged. Open item counts updated.*

*v1.3 changes (2026-05-21): D-FB-001 added — Phase D Delivery 1 (2026-05-21); thin retrieval package; mapping_size=7; 4 bullets removed; Category A Severity 3. Open item counts updated.*

*v1.2 changes (2026-05-20): Cross-reference to OPENCLAW_PHASE_D_OPERATOR_REVIEW_PROCEDURE.md added to PURPOSE section.*

*v1.1 changes (2026-05-20): Feedback ID format added. Severity scale (1–4) defined. Batching rule added. Client confirmed? and Disposition rationale columns added to register table.*
