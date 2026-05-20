---
document_id: OPENCLAW-PHASE-D-ORP-001
version: 1.0
created: 2026-05-20
last_updated: 2026-05-20
status: ACTIVE
classification: OPERATIONAL — PHASE D OPERATOR REVIEW PROCEDURE
---

# OPENCLAW — Phase D Operator Review Procedure

## PURPOSE

This document defines the required operator review workflow for Phase D
controlled pilot deliveries. Its purpose is to make feedback capture
consistent, auditable, and easy for the operator to complete.

The operator may provide feedback in natural language. CoWork is responsible
for converting that feedback into proposed Feedback Register entries, a
proposed Content Scorecard row, and a recommended disposition for each item.

No feedback entry, scorecard row, or change recommendation becomes official
until approved by the operator.

---

## REVIEW TRIGGER

This procedure applies after each Phase D delivery reviewed by the operator.
Operator review is required on every delivery for the first two weeks or ten
deliveries, per the Phase D operating model.

---

## COWORK RESPONSIBILITY

After each reviewed delivery, CoWork must:

1. Present the standard Phase D Delivery Review Prompt to the operator.
2. Accept the operator's plain-language responses.
3. Produce proposed Feedback Register entries (in register format, with
   assigned Feedback IDs).
4. Produce a proposed Content Scorecard row.
5. Recommend a disposition for each feedback item.
6. Confirm that no implementation action has been taken.
7. Request operator approval before entries become official.

---

## OPERATOR RESPONSIBILITY

The operator reviews the delivered output and answers the CoWork prompt in
natural language. The operator may approve, reject, revise, or defer CoWork's
proposed entries. No entry is official until the operator explicitly approves.

---

## STANDARD PHASE D DELIVERY REVIEW PROMPT

CoWork must present the following prompt after each reviewed delivery:

---

**PHASE D DELIVERY REVIEW**

Delivery details:
- Date:
- Run timestamp:
- Client ID:
- Validator status:
- Delivery status:

Please review the delivery and answer the following:

**1. Was this delivery acceptable to show to the pilot client?**
- Yes
- Yes with reservations
- No

**2. Were there any delivery-blocking issues?**
Examples: fabricated citation, broken formatting, wrong client, wrong topic,
missing required section, obvious false claim, unsupported major claim,
delivery to wrong channel.

**3. What were the strongest parts of the brief?**
Please list 1–3 strengths.

**4. What were the weakest parts of the brief?**
Please list 1–3 weaknesses.

**5. Did any section feel weak, unclear, generic, unsupported, stale, or
off-target?**
Sections to consider:
- Executive Take
- Advisory Layer
- Regional Signals
- LinkedIn Draft
- Sources / citations
- Formatting / readability
- Validated Sources Appendix (if active)

**6. For each issue noticed, please provide:**
- The issue in plain English
- The section where it appeared
- A short example or quote from the output, if available
- Why it matters to client-grade output

**7. How should each issue be treated?**
- Log only
- Watch for recurrence
- Candidate for future change packet
- Delivery-blocking escalation
- Client preference

**8. Overall client-readiness score:**
- 1 = unacceptable
- 2 = poor
- 3 = adequate
- 4 = good
- 5 = excellent

**9. Did the brief feel useful to the intended client?**
- Yes
- Partially
- No
- Not enough information

---

## COWORK OUTPUT FORMAT AFTER EACH REVIEW

After the operator answers the prompt, CoWork must produce the following
structured output:

---

**PHASE D REVIEW OUTPUT**

**1. Delivery Acceptability**
- Acceptable / Acceptable with reservations / Not acceptable
- Reason (if not fully acceptable)

**2. Proposed Feedback Register Entries**
- Table entries in register format
- Each item assigned a Feedback ID (D-FB-NNN, sequential)
- Each item assigned category, severity, status, and disposition

**3. Proposed Content Scorecard Row**
- Scores by dimension
- Scored by: Operator (CoWork-assisted)
- Client reviewed?: Yes / No / Pending
- Client usefulness confirmation: (operator's answer to Q9)
- Top 3 strengths
- Top 3 weaknesses (cross-referenced to Feedback IDs where applicable)
- Delivery-blocking issues (cross-referenced to Feedback IDs)
- Recommended action

**4. Pattern Watch**
- Items to watch across future runs
- Similar prior Feedback IDs, if any

**5. Change Packet Recommendation**
- No packet yet / Packet candidate / Immediate packet recommended
- Rationale

**6. Operator Approval Request**
> "Approve these entries for the official Phase D record? Any corrections
> before logging?"

**7. Compliance Confirmation**
> ✓ No implementation action taken.
> ✓ No pipeline change proposed.
> ✓ No retrieval, scrubber, validator, or delivery-gate change proposed
>   outside an approved Change Packet.

---

## FEEDBACK ID FORMAT

Feedback items must be assigned sequential IDs in the following format:

```
D-FB-001
D-FB-002
D-FB-003
```

Where:
- `D` = Phase D
- `FB` = Feedback
- `001` = sequential item number

Rules:
1. IDs are sequential and are never reused.
2. Rejected or deferred items retain their original IDs.
3. Related items may be grouped under a Content Change Packet.
4. Content Change Packets must cite the Feedback IDs they address.
5. If one operator comment contains two unrelated issues, create two
   Feedback IDs.

---

## SEVERITY SCALE

| Level | Meaning |
|-------|---------|
| 1 | Minor — polish issue; does not materially affect usefulness; no immediate change required |
| 2 | Moderate — noticeable weakness; worth logging and watching for recurrence |
| 3 | Material — important product-quality issue; likely Change Packet candidate if repeated |
| 4 | Delivery-blocking — delivery should not count as clean; immediate escalation required |

Severity 4 examples: fabricated citation, wrong client, broken output,
missing required section, unsupported major claim, wrong delivery channel,
severe factual error.

---

## FEEDBACK DISPOSITION VALUES

| Disposition | When to use |
|-------------|-------------|
| Log only | Minor, one-off observation; no action required |
| Watch | Issue may matter if repeated; not yet a confirmed pattern |
| Accepted | Issue is valid and should remain active in the register |
| Rejected | Comment is not accepted as a system or product issue |
| Batched | Item grouped into a Content Change Packet |
| Deferred | Issue is valid but outside current Phase D scope |
| Delivery-blocking escalation | Delivery should not count as clean or be shown externally |
| Closed | Issue resolved, validated, or explicitly abandoned |

---

## CHANGE PACKET THRESHOLD

| Pattern | Action |
|---------|--------|
| One-off minor issue (Severity 1) | Log only |
| One-off moderate issue (Severity 2) | Watch |
| Repeated issue across 2–3 deliveries | Accept and monitor as pattern |
| Recurring issue across 3–5 reviewed deliveries | Eligible for Content Change Packet |
| Delivery-blocking issue (Severity 4) | Immediate escalation; may trigger immediate change packet or delivery hold |
| Client preference (Category E) | Log and assess whether it should alter client config, output template, or future defaults |

---

## APPROVAL RULE

CoWork may propose register entries and scorecard rows but may not make them
official without explicit operator approval. All proposed entries are held in
a proposed state until the operator approves, revises, or rejects them.

---

*OPENCLAW-PHASE-D-ORP-001 | Version 1.0 | Created: 2026-05-20 | Status: ACTIVE*
