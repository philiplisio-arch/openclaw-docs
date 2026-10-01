---
document_id: OPENCLAW-D-CP-003
version: 1.0
created: 2026-05-21
classification: PHASE D CHANGE PACKET — AGENT PROMPT
---

# OPENCLAW — Phase D Change Packet 003
## Agent Prompt — LinkedIn Draft Format

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-003 |
| Date raised | 2026-05-21 |
| Raised by | Pilot client PM interview (2026-05-21) |
| Client ID | china_monitor_001 |
| Feedback items addressed | D-FB-001 (F-05) |
| Feedback recurrence threshold met? | Yes — T-07 (LinkedIn non-refresh) was previously logged; client interview confirms structural format failure |
| Implementation layer | Agent prompt / output format (build_agent_input_slim.py) |
| Status | IMPLEMENTED — validation pending next cron run |

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

The LinkedIn Draft section produces generic thematic syntheses that do not
reflect the specific sourced content of the day's brief. It reads as a
templated summary of broad trends rather than a sharp, specific post grounded
in the run's actual cited developments. Client described it as "pure noise."

Additionally, T-07 (logged 2026-05-11) observed the LinkedIn Draft producing
word-for-word identical output across consecutive runs with meaningfully
different brief content — confirming the agent treats the LinkedIn section
as a formulaic output rather than a daily-refreshed product.

**Evidence:**

Delivery 1 (2026-05-21) LinkedIn Draft:
"The recent US-China summit has yielded specific agreements on agricultural
and aviation trade, yet US-China economic ties remain complex with a history
of shifting trade patterns. Globally, the ongoing Middle East conflict
continues to exert pressure on economic growth and fuel markets, prompting
major economies to collaboratively address energy stability. These interwoven
geopolitical and economic trends underscore the need for businesses to
maintain vigilance and adapt strategies to evolving market conditions and
international collaborations."

Problems: (1) No specific figure cited (no dollar amount, no quantity);
(2) Middle East content appears in LinkedIn despite no Middle East bullet
being delivered; (3) Generic closing sentence adds no value; (4) No
historical context — "these agreements have a history" is exactly the insight
a PR firm needs but it is absent.

Client interview: "It would be more interesting to say what was announced —
the agricultural agreement between US and China with specifics — and focus in
on this one piece of information. It may want to draw back to previous
announcements and what they actually resulted in in terms of finalized deals
and actual sales, because these things have a history of just being empty
promises."

Scorecard score: LinkedIn usefulness = 2.

**Why this matters for client-grade output:**

LinkedIn is a direct client deliverable — the PR firm can use it to post
on behalf of clients. A generic, non-specific draft has zero deployment
value. A specific, historically-grounded draft saves the client time and
positions them as informed and credible.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `/root/openclaw_phase5/orchestrator/build_agent_input_slim.py`

**Current behaviour:**

LinkedIn Draft instruction produces a 2–3 sentence thematic synthesis
spanning all topics covered in the run. Output is not grounded in the
specific cited developments of the day.

**Proposed behaviour:**

Replace the LinkedIn Draft section instruction in the output_format block:

```
LINKEDIN DRAFT:
Write ONE LinkedIn post (maximum 4 sentences) focused on a single specific
development from today's Executive Take — the one most likely to be material
to a business audience. Requirements:

1. SPECIFIC: Include at least one concrete detail from the cited source
   (dollar amount, named entity, quantity, or specific policy). Do not
   write a thematic summary.

2. HISTORICALLY GROUNDED: If the development is an agreement, announcement,
   or commitment between governments or major institutions, add one sentence
   acknowledging the historical pattern — whether similar past announcements
   have produced the stated outcomes. Draw only on what is stated or implied
   in the cited sources; do not fabricate historical claims.

3. BUSINESS-RELEVANT FRAMING: Close with one sentence on what this means
   for companies — specific enough to be material to a decision, not a
   generic call to "monitor" or "adapt."

4. ONLY cite developments that appear in today's delivered Executive Take
   bullets. Do not introduce topics from the retrieval package that were
   not in the delivered output.

PERMITTED: "China and the US announced $X billion in agricultural purchase
commitments following this week's summit — a meaningful figure, though
similar commitments in [YEAR] resulted in less than Y% fulfillment within
the agreed timeframe. For agribusiness and logistics companies with China
exposure, the implementation timeline and enforcement mechanism are the
variables worth watching."

NOT PERMITTED: Generic synthesis spanning multiple themes with no specific
figure and a closing sentence about "maintaining vigilance."
```

**Rationale:**

The current instruction does not constrain the LinkedIn section to specific
sourced content or historical grounding. The proposed instruction forces
the agent to (1) select one story, (2) include a verifiable specific, (3)
add historical context drawn from cited sources, and (4) deliver a
business-relevant closing. The explicit NOT PERMITTED example anchors
against the observed failure mode.

**Change scope:** LinkedIn Draft instruction block replaced in output_format.
No changes to ET/AL instructions, scrubber, validator, resolver, or retrieval.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** LOW

**Risk description:**

The LinkedIn section is post-delivery content — it does not affect citation
enforcement, scrubbing, validation, or delivery gate decisions. Risk is
confined to output quality: the agent may occasionally struggle to identify
a suitable single story if the retrieval package is thin (as in Delivery 1).
In that case, the agent should default to the strongest available ET bullet.

No fabrication risk above baseline — the instruction requires specifics to
be drawn from cited sources. The validator remains unchanged.

**Rollback plan:**

Before any modification:
```
cp /root/openclaw_phase5/orchestrator/build_agent_input_slim.py \
   /root/openclaw_phase5/orchestrator/build_agent_input_slim.py.bak_20260521_pre_cp003
```
Note: if CP-002 is implemented first, the backup already exists as
`bak_20260521_pre_cp002`. In that case create:
`bak_20260521_pre_cp003` from the post-CP-002 state.

Rollback: restore from backup.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. LinkedIn Draft on next run references a specific figure or named entity
   from the day's cited sources
2. LinkedIn Draft is grounded in one story — not a multi-theme synthesis
3. Historical context sentence present if the story is an announcement/
   agreement
4. LinkedIn Draft content matches the run's delivered ET bullets —
   no topics appear that were not in the delivered output
5. LinkedIn usefulness score ≥ 3 on next two scored deliveries

**Number of runs required to validate:** 3

**How to confirm resolved:**

LinkedIn usefulness ≥ 3 across two consecutive scored deliveries.
D-FB-001 F-05 marked Implemented.

**How to confirm no regression:**

ET/AL content unchanged in structure and citation behavior. ids_removed = 0.
Validator GREEN.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [ ] Change is confined to one pipeline layer (agent prompt — LinkedIn section only)
- [ ] Rollback path exists and is documented above
- [ ] Change is within Phase D scope

**Forbidden change check — all confirmed NO:**

- [ ] Does NOT alter retrieval behavior
- [ ] Does NOT weaken validator strictness
- [ ] Does NOT weaken scrubber behavior
- [ ] Does NOT bypass or modify the Delivery Gate decision
- [ ] Does NOT affect client namespace isolation

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | |
| Approval date | |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | 2026-05-21 |
| Backup confirmed | Yes — build_agent_input_slim.py.bak_20260521_pre_cp002_003_004 |

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Date | Timestamp | Outcome vs. validation criteria |
|-------|------|-----------|----------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

**Overall outcome:** —

**Feedback Register update:** D-FB-001 F-05 marked Implemented after
Run 1; Validated after Run 3. T-07 marked CLOSED after Run 3 if
LinkedIn content confirmed day-specific across consecutive runs.

---

*OPENCLAW-D-CP-003 | Version 1.0 | Created: 2026-05-21 | Status: PROPOSED*
