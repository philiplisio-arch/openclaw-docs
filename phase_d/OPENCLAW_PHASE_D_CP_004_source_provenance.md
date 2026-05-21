---
document_id: OPENCLAW-D-CP-004
version: 1.0
created: 2026-05-21
classification: PHASE D CHANGE PACKET — AGENT PROMPT
---

# OPENCLAW — Phase D Change Packet 004
## Agent Prompt — Source Provenance Labelling (Chinese vs. International)

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-004 |
| Date raised | 2026-05-21 |
| Raised by | Pilot client PM interview (2026-05-21) |
| Client ID | china_monitor_001 |
| Feedback items addressed | D-FB-001 (F-06) |
| Feedback recurrence threshold met? | Yes — structural absence confirmed on Delivery 1; core product differentiator |
| Implementation layer | Agent prompt / output format (build_agent_input_slim.py) |
| Status | IMPLEMENTED — validation pending next cron run |

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

The delivered brief does not distinguish between insights sourced from
Chinese-language media and insights sourced from international media. The
client explicitly identified this as essential — the product's core
differentiation is China-accessible intelligence that clients cannot get
from reading Western press themselves. Without provenance labelling, that
differentiator is invisible.

**Evidence:**

Delivery 1 (2026-05-21):
- ET Bullet 1 cites CNBC and usnews.com — both Western/international
- ET Bullet 2 cites kuaixun.eastmoney.com — Chinese-language source
- No labelling distinguishes these in the delivered output
- Client cannot tell, at a glance, which bullets represent China-side
  intelligence vs. international coverage

Client interview: "It's very important to understand which are the insights
that we're pulling from China and which are the insights from international
media." This was the final and strongest closing point of the interview —
described as a core reason the product is valuable.

Scorecard score: Source provenance clarity = 2.

**Why this matters for client-grade output:**

A PR firm advising clients on China-related matters needs to know whether
a development is being reported from within China or by international
observers. A Chinese-language source citing a domestic policy initiative
carries different weight and different implications than the same story
covered by Reuters. Without this distinction, the brief cannot be used
to make that judgment.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `/root/openclaw_phase5/orchestrator/build_agent_input_slim.py`

**Current behaviour:**

Bullets are labelled with source provider and date in the delivered output
(e.g., "CNBC, May 21"). No distinction between Chinese-language and
international-media sources is marked in the output format.

**Proposed behaviour:**

Add a provenance tagging instruction to the output_format block:

```
SOURCE PROVENANCE LABELLING:
For every bullet in EXECUTIVE TAKE and ADVISORY LAYER, append a
provenance tag immediately after the citation, on the same line:

  [CN] — if ALL cited sources for that bullet are Chinese-language
         or Chinese-domestic media (Baidu-retrieved, .cn domain,
         Chinese-language publication)
  [INTL] — if ALL cited sources for that bullet are international/
            Western media (English-language, non-CN domain)
  [CN+INTL] — if the bullet draws on both Chinese and international
               sources

The tag appears after the citation substitution, in square brackets.

EXAMPLE OUTPUT FORMAT:
- US-China summit yielded $X billion in agricultural commitments. (CNBC,
  May 21; usnews.com, May 21) [INTL]
- China's domestic private economy stimulus package targets SME lending.
  (Sina Finance, May 21) [CN]
- Middle East energy disruption is influencing China's import strategy.
  (CCTV, May 21; Reuters, May 21) [CN+INTL]

Apply this tag to every bullet. Do not omit the tag on any bullet.
```

**Rationale:**

Provenance is knowable at citation time — the agent already has the
source list with provider metadata. This instruction makes provenance
explicit in the output without requiring any pipeline change. It is
a purely additive formatting instruction. The validator and scrubber
do not need to be modified — the tag is plain text appended after the
citation substitution block.

**Important constraint:** The provenance determination is based on the
source provider metadata in the retrieval package. The agent must not
infer provenance from the content of the article — only from the
source's domain and retrieval provider (Brave = generally international;
Baidu = generally Chinese-language). If provenance is unclear, use [INTL]
as the conservative default.

**Change scope:** One instruction block added to output_format. No changes
to ET/AL content instructions, scrubber, validator, resolver, or retrieval.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** MEDIUM

**Risk description:**

The provenance tag is plain text appended to existing bullet format.
Primary risks:
(a) Agent may mis-classify a source (e.g., labelling a Chinese-language
    source as [INTL] due to English title). Mitigation: instruction
    specifies domain and retrieval provider as the classification basis,
    not article content.
(b) Tag format may be inconsistently applied across runs (LLM
    stochasticity). Mitigation: explicit format example with three
    tag values reduces ambiguity.
(c) The tag is delivered as plain text — the scrubber and validator
    do not parse it, so a malformed tag passes through. Monitored
    manually during Phase D review.

No citation enforcement risk — the tag is post-citation text and does
not interact with result_id parsing, scrubbing, or validation.

**Rollback plan:**

Before any modification:
```
cp /root/openclaw_phase5/orchestrator/build_agent_input_slim.py \
   /root/openclaw_phase5/orchestrator/build_agent_input_slim.py.bak_20260521_pre_cp004
```
Note: if CP-002 or CP-003 were implemented first, back up from the
most recent state.

Rollback: restore from backup.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. Every ET and AL bullet in the next run carries a [CN], [INTL], or
   [CN+INTL] tag
2. Tags are consistent with the known source providers for that run
   (verify against retrieval_package.json)
3. No tag is missing or malformed
4. Citation discipline unchanged: ids_removed = 0; validator GREEN
5. Source provenance clarity score ≥ 3 on next two scored deliveries

**Number of runs required to validate:** 3

**How to confirm resolved:**

Source provenance clarity ≥ 3 across two consecutive scored deliveries.
Tags verified against retrieval_package.json on first validation run.
D-FB-001 F-06 marked Implemented.

**How to confirm no regression:**

ids_removed = 0. Validator GREEN. ET/AL bullet content and citation
structure unchanged — only the tag text is new.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [ ] Change is confined to one pipeline layer (agent prompt — output format)
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

**Feedback Register update:** D-FB-001 F-06 marked Implemented after
Run 1; Validated after Run 3.

---

*OPENCLAW-D-CP-004 | Version 1.0 | Created: 2026-05-21 | Status: PROPOSED*
