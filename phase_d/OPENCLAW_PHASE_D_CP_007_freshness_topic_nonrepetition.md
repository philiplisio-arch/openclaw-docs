---
document_id: OPENCLAW-D-CP-007
version: 1.0
created: 2026-05-23
classification: PHASE D CHANGE PACKET — EDITORIAL / PROMPT
---

# OPENCLAW — Phase D Change Packet CP-007
# Agent Freshness Preference + Topic Non-Repetition Instructions

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-007 |
| Date raised | 2026-05-23 |
| Raised by | Operator (Delivery 3 review) |
| Client ID | china_monitor_001 |
| Feedback items addressed | D-FB-003 (topic repetition across consecutive deliveries), D-FB-004 Part A (agent-side freshness preference) |
| Recurrence threshold met? | Yes — same three topic clusters across all three Phase D deliveries (confirmed via run_summary topics_covered, 2026-05-21/22/23) |
| Implementation layer | Agent input script (build_agent_input_slim.py) — system_rules section only |
| Status | IMPLEMENTED — validation pending 2026-05-24 cron run |

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

All three Phase D deliveries (2026-05-21, 2026-05-22, 2026-05-23) covered
identical topic clusters: US-China post-summit outcomes, European trade
tensions with China, and Middle East crisis / global economic slowdown.
This is confirmed by run_summary topics_covered across all three runs.
Additionally, operator review of Delivery 3 identified articles older than
48 hours in the evidence pool.

**Root cause (dual):**

1. Retrieval layer: query templates consistently surface the same dominant
   story clusters when the news cycle is concentrated (US-China summit has
   dominated for 3+ days). This is a retrieval-layer root cause outside
   CoWork implementation scope. D-FB-004 Part B documents a parallel
   retrieval investigation track.

2. Agent layer: no instruction exists in the current system_rules to (a)
   prefer fresh sources over older ones, or (b) seek topical differentiation
   from prior deliveries. The agent writes about whatever the retrieval
   package contains, with no awareness of what it covered yesterday.

3. Brain Lite staleness: the digest was last rebuilt 2026-05-18 and does not
   include Phase D runs (2026-05-21, 2026-05-22, 2026-05-23). Even with a
   current digest, the agent has no instruction to use it for topic avoidance.

**Evidence:**

run_summary topics_covered (truncated at 60 chars):
- 2026-05-21: "US-China post-summit outcomes include agreements for Chinese"
- 2026-05-22: "US-China post-summit outcomes include Chinese plans to buy 2"
- 2026-05-23: "US-China post-summit outcomes include Chinese plans to buy 2"

All three runs: same Middle East crisis topic, same European trade topic.

**Why this matters:**

A daily intelligence brief that repeats the same three topic clusters across
consecutive days provides no incremental value. A client reviewing the brief
on day three receives no new intelligence. This is a core product quality
failure and the primary driver of low scores on Freshness clarity,
Advisory usefulness, and Industry coverage breadth in the Phase D scorecard.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `/root/openclaw_phase5/orchestrator/build_agent_input_slim.py`

**Affected section:** `system_rules` block — append two new rule blocks after
the existing ADVISORY LANGUAGE CALIBRATION block.

**Prerequisite (operator action before implementation):**
Brain Lite digest must be rebuilt to include Phase D runs before this CP is
deployed, so that the injected Brain Lite context contains current topic history.
Command (VPS root terminal):
```
python3 /root/openclaw_phase7/brain_lite/build_brain_digest.py --client_id china_monitor_001
```
Confirm digest file updated (check timestamp and size of
brain_digest_china_monitor_001.txt in /root/openclaw_phase7/brain_lite/).

---

**Current behaviour:**

system_rules contains the ADVISORY LANGUAGE CALIBRATION block (deployed
2026-05-13, T-04). No freshness preference or topic differentiation
instruction exists.

---

**Proposed behaviour — two additions to system_rules:**

**Addition 1 — FRESHNESS RULE** (append after ADVISORY LANGUAGE CALIBRATION block):

```
FRESHNESS RULE
Each source in the retrieval package has a timestamp field (publication date).
You must apply the following rules when selecting evidence:
- Prefer sources published within the last 48 hours.
- Where all sources covering a topic are older than 48 hours, you may use them,
  but do not frame the development as breaking or current. Use language such as
  "ongoing," "continuing," or "as of [date]."
- Do not lead an Executive Take bullet with a development sourced exclusively
  from articles older than 72 hours when fresher material exists on other topics.
- Never present a development as today's intelligence if its only sources are
  more than 72 hours old.
```

**Addition 2 — TOPIC DIFFERENTIATION RULE** (append after FRESHNESS RULE):

```
TOPIC DIFFERENTIATION RULE
A Brain Lite digest of prior run topics is injected into this input. Before
selecting topics for today's brief, review the topics_covered entries in the
Brain Lite context.

Apply the following rules:
- Do not repeat a topic that was the primary focus of the most recent delivery
  unless there is a material new development (a new decision, announcement,
  figure, or event — not a restatement of a known situation).
- Where the same major story continues but no material new development exists,
  downrank that topic in the Executive Take and elevate a different story
  cluster if the retrieval package supports it.
- If the retrieval package contains only the same story clusters as the prior
  run with no material new development on any of them, cover the freshest
  available angle and include a note in the LinkedIn Draft that this is a
  continuing story under active development.
- Do not manufacture differentiation by fabricating developments. Apply the
  LOW-SIGNAL RULE if retrieval is genuinely thin on new developments.
```

**Change scope:** Two text blocks appended to the system_rules string in
build_agent_input_slim.py. No logic changes, no schema changes, no other
files. py_compile should exit 0 on the modified file.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** LOW

The change modifies only the text content of the system_rules prompt block.
No processing logic, pipeline structure, citation handling, or scrubber/
validator behavior is affected. The risk is that the new instructions
interact unexpectedly with the agent's citation discipline — specifically,
the TOPIC DIFFERENTIATION RULE might cause the agent to downrank a topic
that has many valid citations in favor of a topic with fewer, resulting in
thinner citation coverage. This is acceptable: the scrubber handles thin
citation groups, and the validator confirms only what is delivered.

The freshness rule does not instruct the agent to reject sources — only to
prefer recent ones and to calibrate language when using older material.
This is not expected to cause citation failures.

**Rollback plan:**

Before any modification, Claude Code creates:
```
/root/openclaw_phase5/orchestrator/build_agent_input_slim.py.bak_20260523_cp007
```

Rollback: restore from backup. No downstream file changes. No restart required.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. py_compile exit 0 on modified build_agent_input_slim.py
2. First post-implementation cron run: validator GREEN, delivery confirmed
3. run_summary topics_covered shows at least one topic cluster distinct from
   the prior run's topics_covered (primary validation signal)
4. Delivered output: no Executive Take bullet framing a development older than
   72 hours as breaking news (operator check against source timestamps in
   retrieval_package)
5. T-04 compliance maintained: all AL bullets conditional/hedged (regression check)

**Runs required to validate:** 2 consecutive runs showing topic variation.
One clean run is insufficient — topic variation must be sustained to confirm
the instruction is functioning.

**Confound warning:** If the retrieval package continues to return only the
same dominant story clusters, topic variation may not appear even with this CP
active. In that case the failure is retrieval-side (D-FB-004 Part B) and this
CP should still be considered validated if the agent demonstrably deprioritises
the repeated cluster when fresher alternatives exist.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to one layer (agent input script — system_rules text only)
- [x] Rollback path documented
- [x] Within Phase D scope (editorial quality improvement — prompt calibration)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT alter retrieval behavior or freshness filter
- [x] Does NOT alter citation syntax or validation rules
- [x] Does NOT weaken scrubber behavior
- [x] Does NOT bypass or modify the Delivery Gate decision
- [x] Does NOT affect client namespace isolation
- [x] Does NOT introduce new output fields or schema changes

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-05-23 |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | 2026-05-23 |
| Backup confirmed | Yes — build_agent_input_slim.py.bak_20260523_cp007 (14,234 bytes) |

**Pre-implementation checklist:**
- [ ] Brain Lite digest rebuilt (build_brain_digest.py --client_id china_monitor_001)
- [ ] Digest file updated timestamp confirmed
- [ ] build_agent_input_slim.py.bak_20260523_cp007 created
- [ ] py_compile exit 0 confirmed on modified file

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Date | Timestamp | topics_covered distinct from prior run? | Validator | T-04 compliant? |
|-------|------|-----------|----------------------------------------|-----------|-----------------|
| 1 | | | | | |
| 2 | | | | | |

**Overall outcome:** PENDING

---

*OPENCLAW-D-CP-007 | Version 1.0 | Created: 2026-05-23 | Status: IMPLEMENTED — validation pending 2026-05-24 cron run*
*Implementation note (2026-05-23): FRESHNESS RULE and TOPIC DIFFERENTIATION RULE inserted after ADVISORY LANGUAGE CALIBRATION block at line 66 of build_agent_input_slim.py. +31 lines. py_compile exit 0. Brain Lite digest rebuilt same session (3,715 bytes, 2026-05-23 10:22). Retrieval audit (Step 3) confirmed 16/23 results older than 48h — CP-007 FRESHNESS RULE is necessary but retrieval-side fix also required (D-FB-004 Part B, operator decision).*
*Feedback items: D-FB-003, D-FB-004 Part A | Layer: build_agent_input_slim.py system_rules*
*Drafted by: Claude CoWork | Implementation: Claude Code / VPS operator*
