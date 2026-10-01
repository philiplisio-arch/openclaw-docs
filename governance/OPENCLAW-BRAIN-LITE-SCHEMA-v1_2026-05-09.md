---
document_id: OPENCLAW-BRAIN-LITE-SCHEMA-v1
version: 1.0
date: 2026-05-09
status: APPROVED — 2026-05-09
source: Phase 7 Detailed Execution Plan (locked field set)
---

# OPENCLAW — Brain Lite Run Summary Schema

## Purpose

This document extracts the locked 14-field run_summary schema from
the Phase 7 Execution Plan into a standalone implementation artifact.
It does not change the schema. It makes the locked schema explicit
for implementation and testing in Phase C.

No additional fields may be added without formal operator approval.

---

## Locked 14-Field Schema

```json
{
  "run_date":               "YYYY-MM-DD",
  "run_time":               "HH:MM CST",
  "client_id":              "string — must match client_config client_id",
  "delivery_status":        "delivered | blocked",
  "topics_covered":         ["string", "..."],
  "sources_cited":          ["string", "..."],
  "conflicts_flagged":      ["string", "..."],
  "ids_seen":               0,
  "ids_kept":               0,
  "ids_removed":            0,
  "uncited_claims_removed": 0,
  "validator_status":       "GREEN | WARN | FAIL",
  "brave_results":          0,
  "baidu_results":          0
}
```

---

## Field Constraints

| Field | Type | Constraint |
|---|---|---|
| run_date | string | YYYY-MM-DD format |
| run_time | string | HH:MM CST format |
| client_id | string | must match client_config client_id |
| delivery_status | enum | delivered \| blocked |
| topics_covered | array | max 8 items; max 60 chars each |
| sources_cited | array | max 12 items |
| conflicts_flagged | array | max 5 items; max 120 chars each |
| ids_seen | integer | ≥ 0 |
| ids_kept | integer | ≥ 0; ≤ ids_seen |
| ids_removed | integer | ≥ 0; ids_kept + ids_removed = ids_seen |
| uncited_claims_removed | integer | ≥ 0 |
| validator_status | enum | GREEN \| WARN \| FAIL |
| brave_results | integer | ≥ 0 |
| baidu_results | integer | ≥ 0 |

**Confirmed definition (operator-confirmed 2026-05-11):**
`brave_results` and `baidu_results` record the pre-filter result
count from each provider — read directly from `brave_raw.json` and
`baidu_raw.json` (result_count field written by brave_executor.py:68
and baidu_executor.py:139 respectively). Post-filter counts were
considered but rejected: they would require modifying package_builder.py
with no meaningful analytical benefit for Brain Lite trend tracking.

---

## Validation Failure Behavior

If a generated run_summary.json fails schema validation:
- Write rejected summary to quarantine or error log
- Do not include in seven-day digest
- Log `[BRAIN_LITE] summary_schema_invalid`
- Continue pipeline without Brain Lite context if at run start

---

## Example — Populated run_summary (Run 2026-05-09)

```json
{
  "run_date":               "2026-05-09",
  "run_time":               "06:31 CST",
  "client_id":              "china_monitor_001",
  "delivery_status":        "delivered",
  "topics_covered":         [
                              "US-China trade negotiations",
                              "Chinese financial markets",
                              "China tech regulatory environment"
                            ],
  "sources_cited":          [
                              "Reuters", "Sina Finance",
                              "finance.sina.cn", "Bloomberg"
                            ],
  "conflicts_flagged":      [],
  "ids_seen":               26,
  "ids_kept":               26,
  "ids_removed":            0,
  "uncited_claims_removed": 0,
  "validator_status":       "GREEN",
  "brave_results":          14,
  "baidu_results":          12
}
```

---

*OPENCLAW-BRAIN-LITE-SCHEMA-v1 | 2026-05-09 | APPROVED*
*Extracted from Phase 7 Execution Plan — field set locked.*
*No implementation authorized until Phase C opens.*
*No system changes take effect without explicit operator approval.*
