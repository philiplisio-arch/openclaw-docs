---
document_id: OPENCLAW-PHASE-D-CP-TEMPLATE
version: 1.1
created: 2026-05-20
classification: TEMPLATE — PHASE D CONTENT CHANGE PACKET
---

# OPENCLAW — Phase D Content Change Packet (Template)

*Copy this template for each new packet. Rename file to:*
*OPENCLAW_PHASE_D_CP_[NNN]_[short_description].md*

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-[NNN] |
| Date raised | YYYY-MM-DD |
| Raised by | Operator |
| Client ID | china_monitor_001 |
| Feedback items addressed | [Feedback IDs from Register] |
| Feedback recurrence threshold met? | Yes / No — confirmed across [N] reviewed deliveries |
| Implementation layer | [Select one: Agent prompt/output format / Presentation formatting / Source appendix formatting / Client config / Documentation only] |
| Status | PROPOSED / APPROVED / IMPLEMENTED / VALIDATED / CLOSED |

---

## SECTION 1 — PROBLEM PATTERN

*Describe the recurring issue across multiple runs. One packet addresses
one pattern. If feedback items span two unrelated patterns, raise two packets.*

Problem pattern:

Evidence from prior runs (reference run timestamps and Feedback IDs):

Why this matters for client-grade output:

---

## SECTION 2 — PROPOSED CHANGE

*State the specific change. Must be confined to a single pipeline layer.*

**Affected file / parameter:**

**Current behaviour:**
```
[exact current state — quote from file or output]
```

**Proposed behaviour:**
```
[exact proposed state]
```

**Rationale:**

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** LOW / MEDIUM / HIGH

**Risk description:**

**Rollback plan:**
*Rollback path must exist before implementation begins. Standard pattern:
.bak_{date}_{description} backup created before any file is modified.*

---

## SECTION 4 — VALIDATION METHOD

*Define how success will be measured across the next 3–5 runs after
implementation.*

Validation criteria (specific, observable, not subjective):

Number of runs required to validate:

How to confirm the feedback item is resolved:

How to confirm no regression was introduced:

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

Before this packet may proceed to operator approval, all items must be confirmed:

- [ ] Change is confined to one pipeline layer
- [ ] Rollback path exists and is documented above
- [ ] Change is within Phase D scope

**Forbidden change check — all must be confirmed NO:**

- [ ] Does NOT alter retrieval behavior (query logic, provider config, freshness params)
- [ ] Does NOT weaken validator strictness (thresholds, PASS/WARN/FAIL logic)
- [ ] Does NOT weaken scrubber behavior (citation removal, uncited bullet removal)
- [ ] Does NOT bypass or modify the Delivery Gate decision
- [ ] Does NOT affect client namespace isolation

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | YYYY-MM-DD |
| Implementation assigned to | Claude Code / VPS operator |
| Implementation confirmed date | YYYY-MM-DD |
| Backup confirmed | Yes / No — path: |

---

