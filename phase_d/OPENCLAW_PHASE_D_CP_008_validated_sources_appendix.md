---
document_id: OPENCLAW-D-CP-008
version: 1.0
created: 2026-05-23
classification: PHASE D CHANGE PACKET — FORMAT / PRODUCT
---

# OPENCLAW — Phase D Change Packet CP-008
# Validated Sources Appendix — URL Section in Delivered Brief

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-008 |
| Date raised | 2026-05-23 |
| Raised by | Operator (Delivery 3 review) |
| Client ID | china_monitor_001 |
| Feedback items addressed | D-FB-005 (no source URLs provided to reader across all three Phase D deliveries) |
| Recurrence threshold met? | Yes — absent across all three Phase D deliveries (2026-05-21, 2026-05-22, 2026-05-23) |
| Implementation layer | Citation substitution script (citation_sub.py) — append SOURCES section after body substitution |
| Status | IMPLEMENTED — validation pending 2026-05-24 cron run |

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

The delivered brief substitutes result_ids with publisher/date in the body
text (citation_sub.py), but provides no URLs. The client has received three
consecutive deliveries in which every factual claim is attributed to a
publisher and date but cannot be traced to a primary source by the reader.

**Root cause:**

citation_sub.py performs result_id → publisher/date substitution and stops.
The retrieval_package contains all URL, publisher, date, and title fields
required to build a sources appendix. These fields are already read by
citation_sub.py during substitution. They are not surfaced in the output.

Field availability confirmed (CP-006 Appendix, 2026-05-22 Claude Code audit):
- title: "title" — exact match
- publisher: "publisher" — present
- publication date: "timestamp" — YYYY-MM-DD format
- url: "url" — exact match (also at trace.raw_url as fallback)
- result_id: "result_id" — exact match; stable per result
- summary: "summary" — present; contains raw HTML markup (must be stripped)

**Why this matters:**

Source accessibility is a core requirement of a "trusted intelligence"
product. A client paying for PR-grade China intelligence must be able to
verify claims. Without URLs, the brief functions as a summary service, not
an intelligence service. This is the highest-impact product gap in Phase D
and a blocker to client trust and the Phase D gate closure.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `/root/openclaw_phase6/citation_sub.py`
*(Note: spec originally listed /root/openclaw_phase6/validation/citation_sub.py — path was incorrect. Actual file confirmed by Claude Code at /root/openclaw_phase6/citation_sub.py. No validation/ subdirectory contains this file.)*

**Change description:**

After the existing result_id → publisher/date body substitution is complete,
extract all result_ids that were cited in the final output body, look each
up in the retrieval_package, and append a formatted SOURCES section to
the delivered output.

---

**Current behaviour:**

citation_sub.py:
1. Reads final_output_scrubbed_{namespace}.txt (contains result_ids)
2. Reads retrieval_package_{namespace}.json (contains source metadata)
3. Substitutes every (result_id: res_xxx) → (Publisher, Date)
4. Writes substituted output to the Lark delivery path
5. Stops.

No SOURCES section is appended. URL field is never surfaced.

---

**Proposed behaviour:**

citation_sub.py (additional steps after existing substitution):

5. Collect the ordered set of unique result_ids that appeared in the
   substituted body (in order of first appearance).
6. For each result_id in that set, look up the corresponding entry in
   retrieval_package["results"]:
   - publisher: results[i]["publisher"]
   - date: results[i]["timestamp"] (YYYY-MM-DD)
   - url: results[i]["url"] (fallback: results[i]["trace"]["raw_url"])
   - title: results[i]["title"] (strip HTML tags and entities)
7. Build a SOURCES section in the following format:

```
---
SOURCES
1. Publisher | Date | URL
2. Publisher | Date | URL
...
```

   Sources are numbered in order of first appearance in the body.
   Duplicate result_ids (same ID cited multiple times) appear once.
   If a result_id cannot be found in retrieval_package (should not
   occur after scrubber validation), skip it with a log warning.

8. Append the SOURCES section to the end of the substituted output.
9. Write the complete output (body + SOURCES) to the Lark delivery path.

**HTML stripping rule (per CP-006 Appendix):**
The `summary` field and occasionally `title` may contain HTML markup
(<strong>, &hellip;, etc.). The title field must be stripped of HTML
tags and entities before rendering in the SOURCES section. Use a simple
regex or html.unescape() + tag-strip pass. Do not use the summary field
in the SOURCES section — publisher + date + URL is sufficient.

**Change scope:** Additions to citation_sub.py only. No other files modified.
No schema changes. No changes to scrubber, validator, or delivery gate.
py_compile exit 0 expected on modified file.

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** MEDIUM

citation_sub.py is in the delivery path. A bug in the SOURCES section
generation code would produce a malformed delivered output. Mitigations:

1. The SOURCES section is appended after the body — a failure in the
   appendix logic cannot corrupt the already-substituted body text.
2. If the SOURCES section cannot be built (empty result set, JSON read
   failure), citation_sub.py should log a warning and proceed without
   appending the section — delivery is not blocked.
3. Rollback restores the pre-change backup immediately.

**Recommended implementation approach:**

Wrap the SOURCES section logic in a try/except block. On any exception:
- log("sources_appendix_error: [message]")
- proceed without appending the section
- do not raise or abort

This ensures the SOURCES logic is never delivery-blocking.

**Rollback plan:**

Before any modification, Claude Code creates:
```
/root/openclaw_phase6/validation/citation_sub.py.bak_20260523_cp008
```

Rollback: restore from backup. Delivered output returns to publisher/date
substitution only, no SOURCES section. No other files affected.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. py_compile exit 0 on modified citation_sub.py
2. First post-implementation delivery: SOURCES section present in
   final delivered Lark output
3. SOURCES section contains one entry per unique cited result_id
4. Each entry contains: publisher, date (YYYY-MM-DD), URL
5. No HTML tags or entities present in SOURCES entries
6. Validator result unchanged (GREEN PASS — SOURCES section does not
   contain citation syntax; validator should not be affected)
7. Delivery confirmed (final_decision=delivered) — SOURCES section
   does not block delivery gate

**Manual check (operator):**
Open the delivered Lark message. Confirm SOURCES section appears at
the bottom. Click two or three URLs — confirm they resolve to the
expected publisher pages.

**Runs required to validate:** 1 confirmation run + operator URL spot-check.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to one layer (citation_sub.py — output formatting only)
- [x] Rollback path documented
- [x] Within Phase D scope (product format improvement — source transparency)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT alter retrieval behavior
- [x] Does NOT alter citation syntax in the body
- [x] Does NOT alter validation logic or strictness
- [x] Does NOT alter scrubber behavior
- [x] Does NOT bypass or modify the Delivery Gate decision
- [x] Does NOT affect client namespace isolation
- [x] Does NOT alter Brain Lite or any upstream script

**Delivery-safety note:**
The try/except wrapper on the SOURCES logic ensures this change cannot
block delivery. In the worst case (bug in appendix generation), the
output is delivered without the SOURCES section — same as current
behavior. No regression to delivery rate is possible from this change.

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-05-23 |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | 2026-05-23 |
| Backup confirmed | Yes — citation_sub.py.bak_20260523_cp008 (3,173 bytes, 101 lines) |

**Pre-implementation checklist:**
- [ ] citation_sub.py.bak_20260523_cp008 created
- [ ] py_compile exit 0 confirmed on modified file
- [ ] HTML stripping confirmed in test (check title field of a known result_id)
- [ ] try/except wrapper confirmed in place around SOURCES logic

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Date | Timestamp | SOURCES section present? | URL count | Validator | Delivery confirmed? |
|-------|------|-----------|--------------------------|-----------|-----------|---------------------|
| 1 | | | | | | |
| 2 | | | | | | |

**Operator URL spot-check:**
| URL checked | Resolves? | Publisher matches? |
|-------------|-----------|-------------------|
| | | |
| | | |

**Overall outcome:** PENDING

---

*OPENCLAW-D-CP-008 | Version 1.0 | Created: 2026-05-23 | Status: IMPLEMENTED — validation pending 2026-05-24 cron run*
*Feedback item: D-FB-005 | Layer: citation_sub.py (output append only)*
*Field availability confirmed: CP-006 Appendix, 2026-05-22*
*Drafted by: Claude CoWork | Implementation: Claude Code / VPS operator*
*Implementation note (2026-05-23): Path corrected — actual file at /root/openclaw_phase6/citation_sub.py (no validation/ subdirectory). +28 lines added. try/except wrapper confirmed in place. result_ids extracted from original_body pre-substitution. Regex res_\w+ used (matches existing substitute() pattern). Order preserved via list(dict.fromkeys(...)). py_compile exit 0.*
