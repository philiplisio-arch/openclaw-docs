---
document_id: OPENCLAW-D-CP-002
version: 1.0
created: 2026-05-21
classification: PHASE D CHANGE PACKET — AGENT PROMPT
---

# OPENCLAW — Phase D Change Packet 002
## Agent Prompt — Content Specificity (Bullets + Advisory Layer)

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-002 |
| Date raised | 2026-05-21 |
| Raised by | Pilot client PM interview (2026-05-21) |
| Client ID | china_monitor_001 |
| Feedback items addressed | D-FB-001 (F-02, F-03) |
| Feedback recurrence threshold met? | Yes — confirmed on Delivery 1; structural pattern, not a one-off |
| Implementation layer | Agent prompt / output format (build_agent_input_slim.py) |
| Status | IMPLEMENTED — validation pending next cron run |

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

Executive Take and Advisory Layer bullets are too broad and generic to be
actionable. Bullets summarise themes rather than reporting specific
developments. Dollar amounts, dates, named entities, and concrete policy
details are absent. Advisory bullets rephrase the Executive Take in softer
language without adding materially actionable guidance.

**Evidence:**

Delivery 1 (2026-05-21):
- ET Bullet 1: "US-China post-summit outcomes include agreements for Chinese
  purchases of Boeing airplanes and increased imports of US agricultural
  products, despite a historical trend of China reducing reliance on US farm
  goods." — No dollar amount, no quantity, no named deal, no date of agreement.
- ET Bullet 2: "European trade ties are influenced by a broader global commerce
  context, while China concurrently focuses on domestic initiatives to promote
  private economic growth." — No specific initiative named, no policy detail,
  no concrete development.
- AL Bullet 1: "Companies engaged in US-China trade should consider monitoring
  the implementation of recently announced deals..." — Restates ET Bullet 1
  in advisory framing without adding decision-relevant information.
- AL Bullet 2: "Businesses with international operations may wish to observe
  the global economic slowdown..." — Generic global macro statement; not
  material to any specific company decision.

Client interview (2026-05-21): "They are very broad, generic, do not include
any specific items that may be of interest." Dollar amounts and dates called
out explicitly as the most important missing elements. Advisory layer described
as "far too generic to be useful, even though directionally correct." Bar for
usefulness: "material to a company's decision-making process."

Scorecard scores: Source specificity = 2; Advisory usefulness = 2.

**Why this matters for client-grade output:**

A PR firm advising companies on China-related decisions cannot use generic
thematic summaries. Actionable intelligence requires specific facts a company
can act on — a deal amount, a named regulatory change, a specific date. Without
this, the brief is a news digest, not an intelligence product.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `/root/openclaw_phase5/orchestrator/build_agent_input_slim.py`

**Current behaviour:**

Executive Take bullets summarise thematic developments at a high level.
Advisory Layer bullets rephrase ET content in conditional framing without
adding specific decision-relevant detail. Neither section is instructed to
prioritise concrete specifics over thematic framing.

**Proposed behaviour:**

Two additions to the agent prompt in `build_agent_input_slim.py`:

**Addition 1 — Executive Take specificity instruction (system_rules block):**
```
SPECIFICITY REQUIREMENT — EXECUTIVE TAKE:
Every Executive Take bullet must include at least one concrete, verifiable
detail drawn directly from the cited source: a dollar amount, a quantity,
a named entity (company, official, policy, regulation), or a specific date.
Thematic summaries without at least one specific anchoring detail are not
acceptable. If the cited source contains a specific figure or named entity,
it must appear in the bullet.

PERMITTED: "China agreed to increase purchases of US agricultural products
by $X billion over Y years, per the post-summit joint statement (DATE)."
NOT PERMITTED: "China agreed to increase imports of US agricultural products
despite a historical trend of reducing reliance on US farm goods."
```

**Addition 2 — Advisory Layer specificity instruction (output_format block):**
```
ADVISORY LAYER SPECIFICITY:
Each Advisory Layer bullet must add materially to the corresponding
Executive Take bullet — not rephrase it. The advisory must identify a
specific decision implication: a company type, an exposure, a supply chain
consideration, a regulatory risk, or a market opportunity tied directly to
the specific development cited. Generic "monitor this trend" framing is
not acceptable. The advisory must be specific enough to be material to a
company's decision-making process.

PERMITTED: "Companies importing US soybeans or poultry into China should
assess whether the announced purchase commitments affect their contracted
volumes, given China's historical pattern of announcing agricultural deals
that are subsequently revised."
NOT PERMITTED: "Companies engaged in US-China trade should consider
monitoring the implementation of recently announced deals."
```

**Rationale:**

The agent has access to specific details in the retrieval package
(dollar amounts, dates, named entities) but is not currently instructed
to surface them. These additions constrain the agent to ground each bullet
in at least one verifiable specific. The negative examples anchor the
instruction against the exact failure mode observed in Delivery 1.

**Change scope:** 2 instruction blocks added to existing prompt sections.
No changes to scrubber, validator, resolver, or retrieval.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** MEDIUM

**Risk description:**

Adding specificity requirements to the agent prompt may cause the agent to:
(a) reach for specifics that are not present in the retrieval package,
potentially introducing fabricated details — this is the primary risk;
(b) produce differently structured bullets that interact with citation
enforcement in unexpected ways.

Mitigation: the instruction explicitly requires specifics to be "drawn
directly from the cited source" and does not permit the agent to generate
figures not present in retrieved material. The validator and scrubber
remain unchanged and will continue to catch fabricated result_ids.
Fabrication rate monitoring (ids_removed) is the primary validation signal.

**Rollback plan:**

Before any modification:
```
cp /root/openclaw_phase5/orchestrator/build_agent_input_slim.py \
   /root/openclaw_phase5/orchestrator/build_agent_input_slim.py.bak_20260521_pre_cp002
```
Rollback: restore from backup. No downstream dependencies.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. Next run after implementation: at least one ET bullet contains a
   specific figure, named entity, or date drawn from the cited source
2. ids_removed = 0 (fabrication rate unchanged — specifics are not
   being invented)
3. Advisory usefulness score ≥ 3 on next two scored deliveries
4. Source specificity score ≥ 3 on next two scored deliveries
5. Validator GREEN PASS maintained

**Number of runs required to validate:** 3

**How to confirm resolved:**

Scorecard Source specificity ≥ 3 and Advisory usefulness ≥ 3 across
two consecutive scored deliveries. D-FB-001 F-02 and F-03 marked
Implemented.

**How to confirm no regression:**

ids_removed = 0 maintained across validation runs. Validator GREEN.
No new uncited claims introduced.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [ ] Change is confined to one pipeline layer (agent prompt)
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

**Feedback Register update:** D-FB-001 F-02 and F-03 marked Implemented
after Run 1; Validated after Run 3.

---

*OPENCLAW-D-CP-002 | Version 1.0 | Created: 2026-05-21 | Status: PROPOSED*
