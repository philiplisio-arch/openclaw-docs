# OPENCLAW — DIAGNOSTIC REPORT — JUNE 10 BLOCKED RUN

---
document_id: OPENCLAW_DIAG_JUNE10_BLOCK_2026-06-10
version: v1.0
date: 2026-06-10
author: Claude Fable 5
status: DIAGNOSIS COMPLETE — report only; no fix applied (Lane 3, P-10)
authorization: Operator approved diagnose-only investigation 2026-06-10 (Master Plan item 0.2)
---

## Bottom line

The June 10 WS1 run was blocked because the AI agent ignored its (correct) instructions and produced an **ALJ-format brief for the WS1 client**. It did this because the agent gateway keeps **one shared, permanent conversation across all clients and all runs** — and the five ALJ test runs on June 9 morning had just filled that conversation with ALJ briefs. The agent followed the pattern of its recent history instead of the prompt. The safety gates caught it and nothing was delivered.

This same mechanism is the most plausible root cause of **Issue #66 (citation misbinding)** — the agent carries thousands of remembered sources from past runs that can bleed into new briefs.

A second, separate finding: **three unreviewed ALJ test briefs were pushed to the live ALJ Feishu document on June 9 morning** (09:45, 09:48, 10:39 Shanghai) during namespacing-fix testing, because `pilot_mode` was false at the time. Delivery succeeded (HTTP 200) to document `IAvBdHg6CoyCR0xlE0dcnYWyn0a`.

## Evidence chain (run_20260609T223001Z, WS1, 2026-06-10 06:31 Shanghai)

1. **Retrieval and prompt were correct.** 159 filter decisions, 25 sources passed. The agent prompt (`agent_input_slim_china_monitor_001.txt`, 57,653 bytes) exactly matches the byte count logged inside the container (`prompt_bytes=57653`), contains the correct WS1 template (EXECUTIVE TAKE + ADVISORY LAYER), and contains zero ALJ references. Contamination did NOT come from the pipeline.
2. **Agent output was ALJ-format.** The pre-gate output (preserved in legacy `final_output.txt`, 4,380 bytes, same timestamp) is an 8-section ALJ brief ("Relevance to ALJ", "ACTION NOTES FOR ALJ", Chinese Source Appendix) with no ADVISORY LAYER section.
3. **Gates fired correctly.** Completeness check RE_2 (`ADVISORY LAYER` header) failed; scrubber found zero cited EXECUTIVE TAKE bullets; delivery blocked; 194-byte block notice archived. P-01/P-02 honored.
4. **The cited source was not in the run's package.** The single cited article (yuanchuang.10jqka.com.cn, "出海卡位战") has zero matches in WS1's June 10 filtered package — but matches sources throughout ALJ's June 9 retrieval artifacts. The URL in the output (`/20260608/c676527581.shtml`) matches neither exactly: it appears to be a memory-mutated variant of the real June 9 ALJ source URL (`/20260606/c677263211.shtml`). Same misbinding signature as Issue #66.
5. **The shared session.** In the gateway container, `agents/china_pr_enrichment/sessions/sessions.json` keys everything to `agent:china_pr_enrichment:main` → a single session file (`c16d9aa3….jsonl`, **6.3 MB, 577 messages**, mixing 38 ALJ-brief markers and 511 WS1 markers). The orchestrator passes a unique `--session-id` per run, but the gateway records it without isolating — every run for every client appends to the same conversation. All clients also share the single hardcoded agent `china_pr_enrichment` (run_phase5_offline.sh).
6. **Timeline fits exactly.** WS1 June 9 06:31 run (before the ALJ batch): clean, delivered, GREEN 10/10. Five ALJ runs 09:41–10:39 June 9 (namespacing tests): appended ALJ turns. WS1 June 10 06:31 (first WS1 run after the batch): ALJ-format output, blocked.

## Implications

- **Every WS1 run that follows ALJ runs is at risk of this failure** until sessions are isolated. Next ALJ cron is Sunday; next WS1 cron is daily.
- Even when the format survives, the shared history degrades quality silently: remembered facts/sources from previous runs can be woven in and bound to the wrong citation — Issue #66's exact signature. This elevates the urgency of fixing it beyond "occasional blocked run."
- The June 9 ALJ deliveries mean the live client document currently contains three unreviewed test briefs (one of them a thin single-source brief). The `pilot_mode: true` fix applied today prevents recurrence; the existing blocks in the client doc are an operator-communication decision.

## Proposed fix (NOT applied — requires Lane 3 approval)

**Give the agent a fresh conversation every run.** One change in `run_phase5_offline.sh` agent invocation: reset/clear the `china_pr_enrichment` session store before each run (or use the gateway's flag for a new session, if available — to be confirmed at implementation). The agent is supposed to be stateless: everything it needs arrives in the prompt; Brain Lite context is injected deliberately by the pipeline. Nothing relies on session memory.

- Affected file: `/root/openclaw_phase5/orchestrator/run_phase5_offline.sh` (agent invocation block only)
- Rollback: revert the one block; session file is recreated automatically
- Validation: after next cron run — output format correct; session file small/fresh; validator result unchanged or better
- Risk of change: LOW. Risk of not changing: MED-HIGH (recurring cross-client contamination + ongoing misbinding pressure)
- Side benefit: should be tested as a likely mitigation for Issue #66

## Approval needed

1. Lane 3 approval to implement per-run session isolation as above.
2. Operator awareness/decision on the three June 9 test briefs sitting in the live ALJ Feishu document (remove / leave / notify client contact).

*Cross-references: Issue #66, Issue #56 (exit=1 — unrelated, still open), ADV-016 (raw pre-gate output archiving would have made this diagnosis instant), Master Plan items 0.2, 1.3.*
