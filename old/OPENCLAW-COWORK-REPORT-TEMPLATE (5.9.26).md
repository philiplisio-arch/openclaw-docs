---
document_id: OPENCLAW-COWORK-REPORT-TEMPLATE
version: 1.0
date: 2026-05-09
status: APPROVED — 2026-05-09 (Step 4)
source: Phase 7 Execution Plan, Section 10.2
---

# OPENCLAW — CoWork Daily Post-Run Report Template

## Purpose

This template defines the fixed format for the automated daily post-run
report produced by CoWork after each cron delivery. Once approved, the
report is written to:

  /root/openclaw_cowork/reports/run_review_YYYYMMDD.md

All 11 fields are required. No field may be omitted — this is a
governance constraint per Section 10.2 of the Phase 7 Execution Plan.
Changes to the field set require a formal phase decision.

The internal format of each field (wording, layout, data presentation)
is adjustable by operator direction at any time without a formal phase
decision.

---

## Template Definition

```
# OPENCLAW — Daily Run Review
Run date:   YYYY-MM-DD
Run time:   HH:MM CST
Client:     [client_id]
Generated:  [timestamp]
---

## 1. SYSTEM STATE
[Factual summary: did the pipeline complete, what was the delivery
status, any failures or anomalies in execution. One short paragraph.]

---

## 2. CITATION HEALTH
ids_seen:       [N]
ids_kept:       [N]
ids_removed:    [N]
fabrication %:  [N%]

5-run trend (ids_removed): [D-4] → [D-3] → [D-2] → [D-1] → [today]

[One sentence on whether the trend is stable, improving, or degrading.]

---

## 3. UNCITED CLAIMS
uncited_claims_removed: [N]
Sections affected: [EXECUTIVE TAKE / ADVISORY LAYER / none]

[One sentence on impact, or "None — all bullets retained."]

---

## 4. SOURCE CONTRIBUTION
Brave results:   [N]
Baidu results:   [N]
Providers:       [brave OPERATIONAL | FAILED] / [baidu OPERATIONAL | FAILED]

[One sentence on provider health or any notable retrieval pattern.]

---

## 5. CONFLICT DETECTION
Conflicts flagged: [N]
Tiers present:     [⚠ factual / ↔ directional / ~ numeric / none]

[Brief description of any new conflict patterns, or "No conflicts
flagged this run."]

---

## 6. VALIDATOR STATUS
Status:           [GREEN | WARN | FAIL]
Citations checked: [N]
Citations matched: [N]
Warnings:          [N]
Failures:          [N]

[One sentence noting any WARN patterns, or "Clean pass — no warnings."]

---

## 7. DELIVERY STATUS
HTTP response:       [200 | error code]
Substitutions made:  [N]
Missing IDs:         [N]
Anomalies:           [description or "None"]

---

## 8. ACTIVE ISSUE IMPLICATIONS
[How this run's data bears on any open issues in the Issues Log, or
"No open issues. Run data consistent with resolved issue history."]

---

## 9. PROPOSED DOC UPDATES
[List of documents requiring updates and the proposed changes,
or "No document updates required this run."]

Full proposed content written to:
  /root/openclaw_cowork/proposed_doc_updates/YYYYMMDD_[doc_name].md

---

## 10. RECOMMENDED NEXT ACTION
1. [First action — within current phase scope]
2. [Second action — within current phase scope, or omit if only one]

---

## 11. PHASE ALIGNMENT CHECK
Active phase: [phase name]

[Explicit confirmation that this run, its outputs, and this analysis
are fully within the scope of the current active phase. Any scope drift
flagged here before proceeding.]

Phase alignment: [CONFIRMED — no scope drift detected. / DRIFT DETECTED:
description]
```

---

## Populated Example — Run 2026-05-09

The following shows the template populated with today's actual run data.

```
# OPENCLAW — Daily Run Review
Run date:   2026-05-09
Run time:   06:31 CST
Client:     china_monitor_001
Generated:  2026-05-09 (post-run)
---

## 1. SYSTEM STATE
Pipeline executed and delivered on schedule. Cron ran at 06:31 CST,
consistent with the 30 06 * * * schedule. Delivery completed
successfully. No execution failures or pipeline anomalies detected.
3 EXECUTIVE TAKE bullets and 5 ADVISORY LAYER bullets in delivered
output.

---

## 2. CITATION HEALTH
ids_seen:       26
ids_kept:       26
ids_removed:    0
fabrication %:  0%

5-run trend (ids_removed): 0 → 0 → 0 → 0 → 0

Stable at 0% fabrication across all five gate-period runs — consistent
with Phase 6.8 resolution.

---

## 3. UNCITED CLAIMS
uncited_claims_removed: 0
Sections affected: none

None — all bullets retained.

---

## 4. SOURCE CONTRIBUTION
Brave results:   [pending — requires brave_raw.json read]
Baidu results:   [pending — requires baidu_raw.json read]
Providers:       sources_indexed=18 confirmed via log

Highest sources_indexed count observed to date (18 vs 12 prior run);
10 distinct publishers in delivered output including 6 Chinese-language
sources.

---

## 5. CONFLICT DETECTION
Conflicts flagged: [pending — requires conflict_log.json read]
Tiers present:     [pending — requires conflict_log.json read]

To be confirmed from /root/openclaw_phase6/validation/conflict_log.json.

---

## 6. VALIDATOR STATUS
Status:            GREEN
Citations checked:  26
Citations matched:  26
Warnings:           0
Failures:           0

Clean pass — no warnings. 26/26 citations matched; no patterns of
concern.

---

## 7. DELIVERY STATUS
HTTP response:       200
Substitutions made:  26
Missing IDs:         0
Anomalies:           None

---

## 8. ACTIVE ISSUE IMPLICATIONS
No open issues. Run data consistent with resolved issue history.
ids_removed=0 confirms Issue #43 (fabrication) remains resolved.
Sina Finance and finance.sina.cn present in delivery confirms Issue
#44 (source surfacing) remains resolved. T-06 (scrubber_report.json
path) remains open — scrubber counters confirmed via cron log but
JSON file path unverified.

---

## 9. PROPOSED DOC UPDATES
Daily Status (04_DAILY_STATUS): update Run 4 trust gate entry and
current position. Full proposed content written to:
  /root/openclaw_cowork/proposed_doc_updates/20260509_daily_status.md

Gate Checklist (OPENCLAW-P7-GATE-001): update Run 4 to CONFIRMED.
Full proposed content written to:
  /root/openclaw_cowork/proposed_doc_updates/20260509_gate_checklist.md

---

## 10. RECOMMENDED NEXT ACTION
1. Monitor 2026-05-10 cron run — one further clean delivery closes
   the Phase A five-consecutive-run trust gate (4 of 5 confirmed).
2. Proceed to Step 3 — client_config.yaml schema approval.

---

## 11. PHASE ALIGNMENT CHECK
Active phase: Phase 7 Entry — Phase B (Infrastructure & Planning)

This run review reads pipeline artifacts and produces a structured
analysis. No retrieval, scrubber, validator, agent, or delivery gate
modifications proposed or implied. No architecture changes. No phase
advancement action taken.

Phase alignment: CONFIRMED — no scope drift detected.
```

---

## VPS Subdirectory Structure Required

Before automation is enabled, create the following subdirectories
under /root/openclaw_cowork/:

```bash
mkdir -p /root/openclaw_cowork/reports
mkdir -p /root/openclaw_cowork/proposed_doc_updates
mkdir -p /root/openclaw_cowork/proposed_patches
mkdir -p /root/openclaw_cowork/run_summaries   # Phase C — Brain Lite
```

Ownership: openclaw_cowork:openclaw_cowork
Permissions: 700 (each directory)

---

## Prerequisites Before Automation Goes Live

The following items from Section 10.3 of the Phase 7 Execution Plan
must be completed before CoWork automated report generation is enabled.
These are not blocking Step 4 approval but must be confirmed before
the automated report is treated as live:

1. Git pre-commit hook installed in /root/openclaw_docs/ and
   /root/openclaw_cowork/ requiring a commit message before files
   can be applied to production.

2. Written access control model reviewed and confirmed by operator.
   (VPS permission model set in Step 2B — formal sign-off pending.)

3. Credentials migration: SerpAPI key and Lark webhook moved out of
   readable script files. Not authorized as a Phase B runtime change —
   to be handled when Phase C opens or via separate operator decision.

---

*OPENCLAW-COWORK-REPORT-TEMPLATE v1.0 | 2026-05-09 | DRAFT*
*No system changes take effect without explicit operator approval.*
