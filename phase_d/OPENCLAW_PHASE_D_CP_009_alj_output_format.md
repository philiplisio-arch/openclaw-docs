---
document_id: OPENCLAW-D-CP-009
version: 1.0
created: 2026-05-23
classification: PHASE D CHANGE PACKET — AGENT INPUT / PROMPT
---

# OPENCLAW — Phase D Change Packet CP-009
# ALJ-Specific Agent Output Format — build_agent_input_slim.py

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-009 |
| Date raised | 2026-05-23 |
| Raised by | Operator (WS2 pre-run confirmation check) |
| Client ID | alj_china_auto_001 (does not affect china_monitor_001) |
| Feedback items addressed | N/A — new client capability |
| Recurrence threshold met? | N/A |
| Implementation layer | Agent input script (build_agent_input_slim.py) — conditional output_format and system_rules blocks |
| Status | APPROVED — implementation pending |

**Note:** This packet enables the ALJ-specific output format for WS2.
Without this change, running alj_china_auto_001 produces WS1-shaped output
(Executive Take + Advisory Layer + LinkedIn Draft) with all ALJ-specific
YAML fields silently ignored. No crash occurs, but the output violates the
product spec. This CP is required before the first ALJ pilot run.

---

## SECTION 1 — PROBLEM PATTERN

**Problem pattern:**

`build_agent_input_slim.py` hardcodes the WS1 output format and system rules.
The `OPENCLAW_REPORT_TEMPLATE` environment variable is emitted by the config
loader and exported by `run_light_to_lark.sh` (Issue #49 fix, 2026-05-23),
but no downstream code reads it. The pipeline has no mechanism to switch
output structure based on client template.

**Root cause:**

The config loader exports `OPENCLAW_REPORT_TEMPLATE=alj_china_auto_weekly_v1`
for the ALJ client. `build_agent_input_slim.py` does not read this variable.
The agent receives WS1 instructions regardless of which client is running.

**Evidence (Claude Code VPS audit, 2026-05-23):**

- `grep -n 'REPORT_TEMPLATE' /root/openclaw_phase5/orchestrator/build_agent_input_slim.py` → zero matches
- No template files exist anywhere in the pipeline
- `OPENCLAW_REPORT_TEMPLATE` appears only in loader (emitted) and shell (exported) — never consumed
- ALJ-specific YAML fields (output_sections, require_complete_source_appendix, source_filter, context_days) have zero consumers in any pipeline script

**Why this matters:**

The ALJ product spec mandates 8 specific output sections including a mandatory
Complete Chinese Source Appendix. Running WS2 without this change produces a
brief with WS1 structure — missing the appendix, missing 5 of 8 sections, and
including a LinkedIn Draft the client does not want. The output would be
unscorable against the ALJ scorecard and unsuitable for any internal or external review.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `/root/openclaw_phase5/orchestrator/build_agent_input_slim.py`

**Change description:**

Read `OPENCLAW_REPORT_TEMPLATE` from the environment at the top of the script.
If the value is `alj_china_auto_weekly_v1`, replace the `system_rules` and
`output_format` strings with ALJ-specific versions before building the agent
input. All other logic (Brain Lite injection, retrieval package formatting,
file I/O) remains unchanged.

**Implementation approach:**

Add at the top of the script (after existing imports):
```python
import os
REPORT_TEMPLATE = os.environ.get("OPENCLAW_REPORT_TEMPLATE", "china_monitor_v1")
```

Before the agent input is assembled, add:
```python
if REPORT_TEMPLATE == "alj_china_auto_weekly_v1":
    system_rules = ALJ_SYSTEM_RULES
    output_format = ALJ_OUTPUT_FORMAT
# else: existing system_rules and output_format are unchanged
```

`ALJ_SYSTEM_RULES` and `ALJ_OUTPUT_FORMAT` are defined as string constants
earlier in the file (before they are referenced).

**WS1 preservation:** The default path (`china_monitor_v1`) is completely
unchanged. No existing string, variable, or logic is modified — the conditional
only executes when `OPENCLAW_REPORT_TEMPLATE == "alj_china_auto_weekly_v1"`.

---

### ALJ_SYSTEM_RULES (full text for implementation)

```
ALJ CHINA AUTO BRIEF — SYSTEM RULES

SOURCE DISCIPLINE
You are writing for Abdul Latif Jameel / Jameel Motors. All intelligence
must be grounded in Chinese or China-market sources from the retrieval
package. Do not invent, supplement, or infer from international sources.
Do not fabricate sources. Every factual claim must be supported by a
retrieved result.

SOURCE AUTHORITY TIERS
Tier 1 (highest): Official / regulatory — MIIT, MOFCOM, NDRC, SAMR, Customs
Tier 2: Industry bodies / market data — CAAM, CPCA, auto dealer associations
Tier 3: Chinese automotive and business media — Gasgoo, Yicai auto, 36Kr
  Auto, LatePost Auto, Dongchedi, Yiche, Sina Auto, Securities Times auto,
  Caixin auto
Tier 4: OEM / company sources — Toyota China, FAW Toyota, GAC Toyota, BYD,
  SAIC/MG, GAC, Geely, Changan/Deepal, Chery/Omoda/Jaecoo, Farizon, CATL
Tier 5 (lowest): Platform contributor pages, reposted or aggregated content
Tier 5 sources must not support strong claims unless corroborated by a
higher-authority source in the same retrieval package.

CITATION RULE
Every factual claim in Sections 1–7 must cite [source_numbers: N] using
numbers from the retrieval package. Do not cite source numbers that are
not present in the retrieval package. Uncited claims will be removed before
delivery. Where multiple sources support a claim, cite all relevant numbers:
[source_numbers: N, M].

ALJ RELEVANCE DISCIPLINE
Every bullet in Sections 1–6 must be relevant to ALJ's business context:
distribution strategy, OEM relationships, NEV positioning, Saudi/GCC
competitive position, or dealer economics. Do not include general China
auto news that has no plausible implication for ALJ. If a retrieved source
has no ALJ relevance, do not use it in narrative sections (it may still
appear in the source appendix as a retained-but-unused source).

ADVISORY LANGUAGE CALIBRATION
Avoid imperative constructions in Action Notes (Section 7). Write
recommendations as: "Consider...", "It may be worth...", "Monitor...",
"Review whether..." — not as directives. Do not use alarm-grade language
("critical", "urgent", "crisis") unless directly supported by retrieved
official sources using that language.

COMPLETE CHINESE SOURCE APPENDIX RULE
Section 8 is mandatory. It must list every source in the retrieval package
that was retained for consideration, whether or not it appears in Sections
1–7. Rules:
- Title, publisher, date, and URL must come from retrieval package metadata.
  Do not reconstruct or invent any of these fields.
- The ALJ relevance note is the only field you write from judgment.
- Do not omit URLs. Full URL from retrieval package required for every entry.
  Do not substitute publisher/date labels for URLs.
- If a source has no Chinese title available, leave that field blank.
  Do not invent a Chinese title.
- Mark "Used in Report: Yes" only if the source was cited in Sections 1–7.

LOW-SIGNAL RULE
If the retrieval package is thin on a given section topic, write a shorter
section with fewer claims rather than padding with weak or uncited material.
You may write: "Limited retrieval this week on [topic]." Do not fabricate
developments to fill sections.
```

---

### ALJ_OUTPUT_FORMAT (full text for implementation)

```
OUTPUT FORMAT — ALJ CHINA AUTO WEEKLY BRIEF

Produce exactly the following sections in order. Do not add or remove
sections. Do not include a LinkedIn Draft section.

---
ALJ CHINA AUTO WEEKLY BRIEF
Week Ending: [DATE]
Client: Abdul Latif Jameel / Jameel Motors
Source Basis: Chinese / China-market sources via Baidu
---

SECTION 1 — EXECUTIVE TAKE
Three to five bullet points on the China auto-market signals that matter
most to ALJ this week. Each bullet must answer:
  - What happened?
  - Why does it matter to ALJ?
  - What is the practical implication?
Ground every bullet in retrieved Chinese sources. Cite [source_numbers: N]
inline at the end of each claim.

---

SECTION 2 — OEM / PARTNER WATCH
Developments involving companies relevant to ALJ:
Toyota / Lexus in China, FAW Toyota, GAC Toyota, BYD, SAIC / MG, GAC,
Geely, Changan / Deepal, Chery / Omoda / Jaecoo, Farizon, Hino (where
relevant), Ford Trucks (where relevant).
Focus: sales movements, pricing changes, product announcements, China
strategy shifts, and developments affecting ALJ's OEM relationships.
Cite [source_numbers: N] inline for each claim.
Write "No significant OEM / partner developments retrieved this week" if
the retrieval package contains nothing usable for this section.

---

SECTION 3 — NEV / HYBRID / BATTERY TREND
Weekly developments in BEV, PHEV, HEV, battery technology, charging
infrastructure, smart driving / ADAS, software-defined vehicles, and
NEV pricing or subsidy shifts.
Focus: developments affecting ALJ's product mix decisions, aftersales
readiness, or customer conversations about electrification.
Cite [source_numbers: N] inline.
Write "Limited NEV / battery retrieval this week" if thin.

---

SECTION 4 — EXPORT & GULF RELEVANCE
Weekly developments in Chinese OEM export strategy, Saudi Arabia / GCC
implications, MENA and Africa distribution signals, and Chinese competitor
activity in ALJ's core markets.
Focus: competitive threats to ALJ's distribution position.
Cite [source_numbers: N] inline.
Write "Limited export / Gulf retrieval this week" if thin.

---

SECTION 5 — DEALER / DISTRIBUTOR IMPLICATIONS
Weekly signals on pricing pressure, discounting, inventory risk, warranty
and parts availability, NEV aftersales economics, residual values, and
battery service readiness.
Focus: China dealer-channel dynamics that may preview conditions ALJ faces
in its own distribution network.
Cite [source_numbers: N] inline.
Write "Limited dealer / distributor retrieval this week" if thin.

---

SECTION 6 — COMMUNICATIONS / REPUTATION ANGLE
What ALJ may need to explain or prepare for in conversations with OEM
partners, customers, regulators, media, or internal leadership.
Focus: reputational, messaging, or relationship-management implications
of this week's China auto developments.
Cite [source_numbers: N] inline.
Write "No significant communications / reputation angle this week" if thin.

---

SECTION 7 — ACTION NOTES FOR ALJ
One to three specific, grounded recommendations for ALJ this week.
Each must be tied to a development from the retrieved sources.
Use advisory framing: "Consider...", "Monitor...", "Review whether..."
Do not include generic recommendations that are not grounded in this
week's retrieved material.

---

SECTION 8 — COMPLETE CHINESE SOURCE APPENDIX
List every source retained for this report, whether or not it was cited
in Sections 1–7. This section is mandatory. Do not omit it.

Format each entry exactly as:

[N] Chinese Title: [original Chinese title, or leave blank if unavailable]
    English Title: [translated or descriptive English title]
    Publisher: [source name from retrieval package]
    Date: [publication date from retrieval package]
    URL: [full URL from retrieval package — do not abbreviate or substitute]
    Blurb: [retrieved snippet or summary from retrieval package]
    Relevance to ALJ: [one sentence explaining why this source matters to ALJ]
    Used in Report: Yes / No
    Related Section: [Section number and name if used, or N/A]
```

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** MEDIUM

The change modifies `build_agent_input_slim.py` — the same file as CP-007.
The risk to WS1 (china_monitor_001) is minimal: the conditional executes
only when `OPENCLAW_REPORT_TEMPLATE == "alj_china_auto_weekly_v1"`. WS1's
`OPENCLAW_REPORT_TEMPLATE` is `china_monitor_v1` — it never enters the
conditional. The WS1 `system_rules` and `output_format` strings are not
touched.

The risk to WS2 (ALJ) is that the ALJ system_rules or output_format text
contains a formatting error that confuses the agent. This is mitigated by:
the first ALJ run being pilot_mode=true (held for operator review); and the
existing scrubber and validator running on the output regardless of template.

**Rollback plan:**

Before any modification, Claude Code creates:
```
/root/openclaw_phase5/orchestrator/build_agent_input_slim.py.bak_20260523_cp009
```

Rollback: restore from backup. WS2 returns to WS1-shaped output (same as
current behavior — no crash, just wrong format). WS1 is unaffected in
either direction.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria:**

1. py_compile exit 0 on modified build_agent_input_slim.py
2. WS1 regression: china_monitor_001 next cron run produces normal 8-bullet
   output with no structural change (Executive Take + Advisory Layer + LinkedIn
   Draft as before)
3. WS2 first pilot run: output contains all 8 sections including Section 8
   (COMPLETE CHINESE SOURCE APPENDIX) with at least one source entry
4. Section 8: every entry contains publisher, date, and URL from retrieval
   package — no invented or missing URLs
5. No LinkedIn Draft section in ALJ output
6. Validator runs on ALJ output and produces a result (pass or fail — not abort)
7. pilot_mode=true confirmed — no external delivery

**Runs required to validate:** 1 ALJ pilot run + 1 WS1 regression confirmation
(next scheduled cron).

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to one layer (agent input script — conditional format strings)
- [x] Rollback path documented
- [x] Within Phase D scope (new client product format — WS2 capability)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT alter WS1 (china_monitor_001) behavior — conditional path only
- [x] Does NOT alter retrieval behavior
- [x] Does NOT alter citation syntax or validation rules
- [x] Does NOT weaken scrubber behavior
- [x] Does NOT bypass or modify the Delivery Gate decision
- [x] Does NOT affect client namespace isolation
- [x] Does NOT introduce new output fields or schema changes to WS1

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-05-23 |
| Implementation assigned to | Claude Code |
| Implementation confirmed date | |
| Backup confirmed | |

**Pre-implementation checklist:**
- [ ] build_agent_input_slim.py.bak_20260523_cp009 created
- [ ] REPORT_TEMPLATE env read confirmed (grep for OPENCLAW_REPORT_TEMPLATE)
- [ ] py_compile exit 0 on modified file
- [ ] WS1 smoke test: load china_monitor_001 loader.env, confirm OPENCLAW_REPORT_TEMPLATE=china_monitor_v1 (does NOT trigger conditional)

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Client | Date | Sections 1–8 present? | Source appendix entries | Validator | Delivery confirmed? |
|-------|--------|------|----------------------|------------------------|-----------|---------------------|
| 1 | alj_china_auto_001 | | | | | |
| 2 | china_monitor_001 | | N/A (regression check) | N/A | | |

**Overall outcome:** PENDING

---

*OPENCLAW-D-CP-009 | Version 1.0 | Created: 2026-05-23 | Status: APPROVED — implementation pending*
*Client scope: alj_china_auto_001 output format; china_monitor_001 unaffected*
*Drafted by: Claude CoWork | Implementation: Claude Code / VPS operator*
*Pre-run blocker confirmed: Claude Code VPS audit 2026-05-23 — OPENCLAW_REPORT_TEMPLATE has zero consumers in pipeline*
