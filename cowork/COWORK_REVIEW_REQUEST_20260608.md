---
document_id: COWORK-REVIEW-REQUEST-20260608
version: v1.0
created: 2026-06-08
requested_by: Operator (Philip)
prepared_by: Claude Code
status: ACTIVE — AWAITING COWORK EXECUTION
---

# OpenClaw — CoWork Review Request
## Session: 2026-06-08

---

## HOW TO START

**Before reading anything else, complete the two sync steps below.**

### Step 1 — Pull latest documents from GitHub

```powershell
cd "C:\Users\phil\Documents\OpenClaw project"
git pull
```

This pulls all documents updated by Claude Code this session, including this file.

### Step 2 — Pull latest VPS runtime artifacts

Run the full scp block from `config/VPS_SYNC_PROTOCOL.md`. If you are reading this file after a `git pull`, the full block is in that file. The short version:

Pull these files from the VPS into `config/vps_sync/`:
- `light_to_lark.log` — full pipeline cron log
- `validation_result_china_monitor_001.json` — latest WS1 validator result
- `final_output_scrubbed_china_monitor_001.txt` — latest WS1 delivered output
- `retrieval_package_china_monitor_001.json` — latest WS1 retrieval pool
- Most recent `run_summary_china_monitor_001_YYYYMMDD.json` — Brain Lite summary

Both steps are required. Do not proceed until both are complete.

---

## CURRENT PROJECT POSITION

- **Phase:** Phase 7 Entry — Phase D (Controlled Pilot) — ACTIVE
- **Gate streak:** 3 of 10 — HELD at 2026-06-06
- **System health:** RECOVERING — D18/D19 Baidu collapse patched 2026-06-08
- **WS1 (china_monitor_001):** In held mode. No deliveries count toward streak until operator reviews D13/D14/D15 and resumes count.
- **WS2 (alj_china_auto_001):** Live since 2026-06-04. Manual trigger only. Next run when fresh news cycle available.

### What happened last session (2026-06-08)

- **Issue #66 resolved** — `filter_results.py` had a Baidu timestamp bug: results with missing timestamps were treated as stale and dropped, causing D18 and D19 to collapse to 1-source output. Two-part fix applied: (1) `dt is None` now keeps the result instead of dropping it; (2) full-year Chinese date form added to `parse_date_from_title`. Confirmation run: mapping_size=2, GREEN 4/4/0.
- **lark_doc_relay.py clear-before-write deployed** — document is now cleared before each new delivery is appended.
- **Domain exclusion expanded** — `baike.baidu.com`, `bilibili.com`, `chinawto.mofcom.gov.cn`, `zhsme.org.cn` added to `client_config_china_monitor_001.yaml`.
- **Uncommitted config changes** remain in workspace (see git status): ALJ `pilot_mode: false` and WS1 domain exclusion / `snippet_min_chars: 80`. These need a commit.

### Validation note requiring follow-up

In D19 filter drops, `tv.cctv.com` and `tv.cctv.cn` appeared as `stale_url_date` — not `domain_exclusion`. These domains are in the exclusion list. This may mean `OPENCLAW_DOMAIN_EXCLUSION` is not being loaded from the config correctly. Confirm on 2026-06-09 cron run: CCTV drops should show `domain_exclusion` reason, and the four new domains should also show `domain_exclusion`.

---

## DOCUMENTS TO READ

Read in this order:

1. `04_DAILY_STATUS.md` — full project history, current position, delivery history, next steps
2. `03_Issues_Log.md` — all open issues with full detail
3. `governance/OPENCLAW-P7-GATE-001.md` — Phase D gate criteria and streak status
4. `config/vps_sync/light_to_lark.log` — live cron pipeline log (runtime artifact, after scp pull)
5. `config/vps_sync/validation_result_china_monitor_001.json` — latest WS1 validator result
6. `config/vps_sync/final_output_scrubbed_china_monitor_001.txt` — latest WS1 delivered output
7. `config/vps_sync/retrieval_package_china_monitor_001.json` — WS1 retrieval pool

As needed:
- `phase_d/OPENCLAW_PHASE_D_CP_021_source_first_output_restructuring.md`
- `phase_d/OPENCLAW_PHASE_D_CP_022A_query_family_dry_run.md`
- `phase_d/OPENCLAW_PHASE_D_CP_024_source_appendix_upgrade.md`
- `advisory/OPENCLAW-ADV-014*` — domain exclusion / snippet quality floor
- `advisory/OPENCLAW-ADV-015*` — claim-source alignment check spec
- `advisory/OPENCLAW-ADV-016*` — raw retrieval logging / traceability
- `advisory/OPENCLAW-ADV-017*` — five-layer product quality workflow

---

## REVIEW TASKS

### A. Five-Layer Delivery Review — D13, D14, D15

These three deliveries were sent externally and form the current gate streak of 3/10. They have not yet been reviewed under the five-layer trust standard introduced in ADV-017 (operator-approved 2026-06-06). The gate is held until this review is complete.

**Deliveries to review:**
- D13 — 2026-06-02 — 16/16 citations; topics: US-China trade ($30B, Nvidia chip halt), Europe-China "not sustainable" (Temu fine), China PMI above forecast
- D14 — 2026-06-03 — 12/12 citations; topics: US-China trade, Yvette Cooper China visit, Israel/Lebanon/Gulf capital
- D15 — 2026-06-04 — 13/13 citations; topics: Soochow/Donghai brokerage consolidation ($1.7B), China May PMI, Strait of Hormuz / China tech AI rally, China tech transfer curbs

For each delivery, assess all five layers:

| Layer | Criterion |
|-------|-----------|
| 1. System | Did the system run successfully? (validator status, delivery status, no pipeline failures) |
| 2. Citations | Are citations structurally valid? (ids_seen/kept/removed; zero fabrication) |
| 3. Source quality | Any low-authority aggregators, TV shell pages, navigation-menu snippets, or wiki/index pages carrying high-stakes claims? |
| 4. Claim-source support | Do the cited sources actually support the specific claims made? Spot-check ET bullets involving named officials, financial figures, regulatory actions, diplomatic claims, or quoted language. |
| 5. Client usefulness | Are topics concrete, diverse, and relevant to a China business intelligence client? Advisory framing appropriate? |

Delivery details are in `04_DAILY_STATUS.md` (Phase D delivery history). Source content is in `config/vps_sync/retrieval_package_china_monitor_001.json` (most recent run) and Brain Lite run summaries in `config/vps_sync/`.

**Conclude with a recommendation to the operator:**
- Option 1: Certify D13/D14/D15 — all pass the five-layer standard; continue from 3/10
- Option 2: Reset streak to 0 — one or more counted deliveries had a material claim-source failure
- Option 3: Continue hold — review incomplete or inconclusive; specific items need operator decision

---

### B. System Health — D18/D19 Collapse and Patch Assessment

D18 (2026-06-07) and D19 (2026-06-08) both collapsed to 1-source output (mapping_size=1, 2 citations). Root cause: `filter_results.py` bug treating Baidu results with missing timestamps as stale — all 55 Baidu results dropped. Fix applied 2026-06-08. Confirmation run: mapping_size=2, GREEN 4/4/0.

First live validation: 2026-06-09 06:30 Shanghai cron run.

**Assess:**
1. Is the patch description in Issue #66 (`04_DAILY_STATUS.md`) logically sound? Any edge cases the fix might miss?
2. Confirmation run showed mapping_size=2 (vs norm 14–15). The session notes explain 23/24 Baidu drops were valid quality decisions (index pages, wiki, stale CCTV clips). Does this explanation hold up given the retrieval package data?
3. Is there any risk of the fix over-including stale content now that `dt is None` keeps rather than drops?

---

### C. Domain Exclusion Loading — Validation Question

ADV-014 Layer 1 deployed 2026-06-06: `h5.article.smbae.cn`, `tv.cctv.com`, `tv.cctv.cn` added to domain exclusion in `client_config_china_monitor_001.yaml`. Four more domains added 2026-06-08: `baike.baidu.com`, `bilibili.com`, `chinawto.mofcom.gov.cn`, `zhsme.org.cn`.

In D19 filter drop analysis, `tv.cctv.com` and `tv.cctv.cn` results were categorised as `stale_url_date` — not `domain_exclusion`. These domains are in the exclusion list.

**Assess:**
1. What are the possible explanations? (Config not loading; `OPENCLAW_DOMAIN_EXCLUSION` env var not being exported; filter code checking the wrong field; timing of when the config was deployed vs when D19 ran?)
2. How should the 2026-06-09 cron run be read to confirm whether the exclusion is loading correctly?
3. Any action required before that cron run, or is observation sufficient?

---

### D. Pending Deployments — ADV-014 Layer 2 and ADV-016

Both were operator-approved 2026-06-06 and authorized for Claude Code implementation. Neither has been deployed.

**ADV-014 Layer 2** — Snippet quality floor in `filter_results.py`:
- Threshold: 80 non-whitespace characters
- Mode: warn-only (log the flag; do not drop)
- Keyword gate: results flagged only if snippet contains `热播榜`, `内容简介`, `推荐阅读`, or `更多>`
- Config side already in place: `snippet_min_chars: 80` in `client_config_china_monitor_001.yaml`
- Reference: `advisory/OPENCLAW-ADV-014*`

**ADV-016** — Raw retrieval logging / per-run traceability archive:
- Immutable per-run archive at `/root/openclaw_traceability/{client}/{date}/`
- 5 file types per run: retrieval package, filter drops log, validation result, scrubbed output, run summary
- Reference: `advisory/OPENCLAW-ADV-016*`

**Assess:**
1. Are the advisory specs clear enough for Claude Code to implement without further operator clarification?
2. Any sequencing concern — should either of these wait for the 2026-06-09 cron validation first?
3. Any conflict with other pending changes?

---

### E. Work Queue Sequencing

Current approved sequence from `04_DAILY_STATUS.md`:

| Tier | Items | Blocker |
|------|-------|---------|
| Immediate | ADV-014 Layer 2, ADV-016 | None — authorized |
| Tier 2 | CP-021 (source-first restructure), CP-022A (query dry run), CP-024 (source appendix upgrade) | Streak resumption decision |
| Tier 3 | CP-022 (WS1 query expansion, live) | CP-022A gate + Browser Phase 1 findings |
| Tier 4 | CP-023 (ALJ query expansion) | 1 baseline held ALJ cron run |
| Browser Phase 1 | CJK fix done; CCTV networkidle re-test; Reuters/Bloomberg stealth UA | Parallel track — hard deadline before CP-022 goes live |

**Assess:**
1. Is this sequencing still correct given the D18/D19 collapse and recovery?
2. Should anything move up in priority (e.g., does the domain exclusion loading question block Tier 2)?
3. Browser Phase 1 hard deadline: must complete before CP-022 (Tier 3). Is there enough runway?

---

### F. Open Issues

| # | Title | Current Status |
|---|-------|----------------|
| #47 | Intermediate retrieval artifacts not namespaced | Pre-production; operator decision required before second real client |
| #54 | Broadcaster-level dedup gap | Open; operator decision required on CP scope and timing |
| #56 | Orchestrator exit=1 on ALJ runs | Not blocking; root cause unknown |
| #63 | ALJ freshness label inconsistency | Was blocked on #62 (now resolved); needs recheck on next ALJ pilot run |

**Assess:**
1. Any of these under-prioritised given current system state?
2. Any action needed before next ALJ manual run?

---

## REPORT FORMAT

Please structure your report as follows:

1. **System health summary** (3–5 sentences, plain English)
2. **Five-layer D13/D14/D15 review** — per-delivery findings and final recommendation (certify / reset / hold)
3. **D18/D19 patch assessment** — sound or concerns
4. **Domain exclusion loading** — your assessment and what to watch on 2026-06-09 cron
5. **ADV-014 L2 + ADV-016 deployment readiness** — ready to deploy or clarification needed
6. **Work queue** — any sequencing changes recommended
7. **Open issues** — any re-prioritisation
8. **Questions for the operator** — flag any item requiring a decision before next session

Keep each section concise. Flag operator decisions clearly at the top of the relevant section.

---

## AFTER YOUR REVIEW

When your report is complete:
- Save it to `cowork/COWORK_REVIEW_REPORT_20260608.md` in this repository
- Commit and push so Claude Code and the operator can read it at next session start

---

*COWORK-REVIEW-REQUEST-20260608 | v1.0 | 2026-06-08 | Prepared by Claude Code*
