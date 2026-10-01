---
document_id: OPENCLAW-D-CP-019
version: 1.0
created: 2026-05-28
classification: PHASE D CHANGE PACKET — EDITORIAL / PROMPT
---

# OPENCLAW — Phase D Change Packet CP-019
# Strengthen Geographic Footer Suppression (SOURCES SECTION RULE)

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-019 |
| Date raised | 2026-05-28 |
| Raised by | CoWork (D8 final_output analysis) |
| Client ID | china_monitor_001 |
| Feedback items addressed | Issue #58 (CP-010 geographic footer suppression ineffective) |
| Feedback recurrence threshold met? | Yes — agent geographic footer present in D8 final_output_scrubbed; CP-010 was expected to suppress from D5 onward (4 runs without suppression confirmed) |
| Implementation layer | Agent input script (build_agent_input_slim.py) — SOURCES SECTION RULE only |
| Status | DEPLOYED AND VALIDATED — v2 footer absence confirmed on D13 2026-06-02; Issue #58 closed (stamped 2026-06-10 reconciliation) |

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

CP-010 (deployed 2026-05-24) added a SOURCES SECTION RULE to
`build_agent_input_slim.py` instructing the agent not to produce a
geographic footer (United States / Europe / Middle East sections with
source titles). CP-010 expected the agent to suppress this footer so that
the citation_sub.py-generated SOURCES section (title|publisher|date|url)
would be the only sources appendix in the delivered output.

D8 (2026-05-28) final_output_scrubbed_china_monitor_001.txt shows the
agent geographic footer still present in the scrubbed output, confirming
the suppression instruction is not working. The agent continues to
produce the geographic footer despite the CP-010 rule.

**Root cause:**

The CP-010 SOURCES SECTION RULE as written is insufficiently directive.
The agent is treating the instruction as advisory rather than as a hard
prohibition. The rule needs to be rewritten as an explicit, positively
framed prohibition with a concrete example of what NOT to produce.

**Evidence:**

D8 final_output_scrubbed_china_monitor_001.txt footer (observed
2026-05-28):
```
United States
- China industrial profits jump 24.7% in April... (CNBC)
- European companies double down... (CNBC)

Europe
- EU Firms Warm to China... (Bloomberg)
- China stalls Airbus approvals... (Reuters)

Middle East
- TotalEnergies extends... (Reuters)
- Brokerages' forecasts... (Reuters)
```

This is the agent-generated format. CP-010 was expected to suppress it
from D5 (2026-05-25) onward. Confirmed present through D8 (4 runs).

**Why this matters:**

The delivered Lark output contains both the agent geographic footer AND
the citation_sub.py SOURCES section — the footer is noise that duplicates
source information in a less structured format. The unified SOURCES section
(title|publisher|date|url) is the product-quality format; the agent
footer degrades it.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `/root/openclaw_phase5/orchestrator/build_agent_input_slim.py`

**Affected section:** SOURCES SECTION RULE (added by CP-010).

**Current behaviour (CP-010 rule — approximate, exact text on VPS):**

The CP-010 SOURCES SECTION RULE instructs the agent to produce a SOURCES
section in a specified format. It likely contains positive instructions
but insufficient prohibition language against the geographic footer.

**Proposed replacement for the SOURCES SECTION RULE:**

```
SOURCES SECTION RULE
Do NOT include a geographic sources section at the end of your output.
Do NOT group sources by region (e.g. "United States", "Europe", "Middle East"
followed by bullet-listed article titles). This geographic footer format is
explicitly prohibited.

A structured SOURCES appendix will be appended automatically by the
pipeline after your output is processed. You do not need to produce any
source listing. Your output must end with the LINKEDIN DRAFT section and
nothing after it.

Example of PROHIBITED output (do not produce this):
  United States
  - Article title (Publisher)
  Europe
  - Article title (Publisher)

Your output ends at the close of the LINKEDIN DRAFT section. No source
listing, no geographic grouping, no footer of any kind.
```

**Change scope:** Replace the SOURCES SECTION RULE text block in
`build_agent_input_slim.py`. No logic changes. No other files modified.
py_compile must exit 0.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** LOW

Modifying the SOURCES SECTION RULE text does not affect citation
discipline, validation logic, or scrubber behavior. The risk is that
removing the positive instruction about the SOURCES format (if CP-010
included one) causes the agent to produce unexpected content after the
LinkedIn Draft. The proposed text is explicit about where output ends
("ends at the close of the LINKEDIN DRAFT section") to mitigate this.

**Rollback plan:**

Before modification, Claude Code creates:
```
/root/openclaw_phase5/orchestrator/build_agent_input_slim.py.bak_20260528_cp019
```
Rollback: restore from backup. No other files affected.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. py_compile exit 0 on modified build_agent_input_slim.py
2. First post-implementation cron run: final_output_scrubbed file does NOT
   contain "United States", "Europe", "Middle East" geographic section headers
   after the LINKEDIN DRAFT section
3. Delivery confirmed GREEN; T-04 compliant
4. citation_sub.py SOURCES section (title|publisher|date|url) present in
   delivered Lark output (operator check against Lark delivery)

**Runs required to validate:** 1 run confirming geographic footer absent;
1 additional run confirming it does not recur.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [ ] Change confined to one layer (build_agent_input_slim.py — SOURCES SECTION RULE text only)
- [ ] Rollback path documented
- [ ] Within Phase D scope (editorial quality improvement — prompt calibration)

**Forbidden change check — all must be confirmed NO:**

- [ ] Does NOT alter retrieval behavior
- [ ] Does NOT weaken validator strictness
- [ ] Does NOT weaken scrubber behavior
- [ ] Does NOT bypass or modify the Delivery Gate decision
- [ ] Does NOT affect client namespace isolation
- [ ] Does NOT introduce schema changes

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-05-28 |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | 2026-05-28 |
| Backup confirmed | /root/openclaw_phase5/orchestrator/build_agent_input_slim.py.bak_20260528_cp019 (23888 bytes) |

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Date | Geographic footer absent? | SOURCES section in Lark? | Validator | T-04 compliant? |
|-------|------|--------------------------|--------------------------|-----------|-----------------|
| 1 | | | | | |
| 2 | | | | | |

**Implementation notes (Claude Code 2026-05-28):**
- Two SOURCES SECTION RULE blocks exist in build_agent_input_slim.py: one in
  ALJ_SYSTEM_RULES (lines 75–76, ALJ Section 8 footer rule) and one in the
  regular system_rules (lines 193–195, the WS1/non-ALJ block). The replacement
  text references "LINKEDIN DRAFT section" which is only present in the non-ALJ
  output flow (ALJ explicitly omits LinkedIn Draft), so the regular system_rules
  block was the correct target. The ALJ block was left untouched.
- Flag: ALJ SOURCES SECTION RULE at lines 75–76 will need review when CP-021
  restructures the ALJ output format. Not an issue for current WS1 pilot.
- WS1 rule replaced at lines 193–210 (3 lines → 18 lines).

**Overall outcome:** IMPLEMENTED — validation pending D9 cron run (Issue #58)

---

*OPENCLAW-D-CP-019 | Version 1.0 | Created: 2026-05-28 | Status: IMPLEMENTED*
*Raised by: Claude CoWork — D8 final_output analysis 2026-05-28*
*Operator approved: 2026-05-28 | Implemented: 2026-05-28 | Issue addressed: #58*
