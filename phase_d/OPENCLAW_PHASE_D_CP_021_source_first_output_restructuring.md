---
document_id: OPENCLAW-D-CP-021
version: 1.0
created: 2026-05-28
classification: PHASE D CHANGE PACKET — AGENT PROMPT / OUTPUT FORMAT
---

# OPENCLAW — Phase D Change Packet CP-021
# Source-First Output Restructuring (WS1)

---

## PACKET HEADER

| Field | Value |
|-------|-------|
| Packet ID | OPENCLAW-D-CP-021 |
| Date raised | 2026-05-28 |
| Raised by | CoWork — signal-widening plan 2026-05-28 |
| Client ID | china_monitor_001 (WS1) |
| Feedback items addressed | D-FB-003 (topic repetition); D-FB-004 (old articles); D-FB-005 (no source URLs); signal-widening advisory ADV-013 |
| Tier | 2 — Source-First Product Shape |
| Implementation layer | Agent prompt / build_agent_input_slim.py |
| Status | APPROVED — implementation pending |

---

## SECTION 1 — RATIONALE

The current WS1 output format — Executive Take (3 bullets) / Advisory Layer
(5 bullets) / LinkedIn Draft — was designed for an early product phase where
the primary deliverable was advisory prose. The bullets are the organizing
unit; sources support the prose.

The signal-widening plan inverts this logic. The source base becomes the
product. The agent's role is to organize, classify, and lightly interpret
the source landscape — not to lead with editorial conclusions.

The current format also embeds LinkedIn Draft as a default daily output.
This is inconsistent with the source-first direction and produces formulaic
content. LinkedIn is suppressed from the default output under this CP and
may return only as an optional downstream artifact from a selected signal
item, subject to a separate future operator decision.

This is the highest-risk CP in the signal-widening plan because it changes
the user-facing product experience materially. It requires a minimum of two
held-mode runs with full operator review before any live delivery.

**Gate streak impact:** The Phase D clean-delivery gate streak restarts on
the first live CP-021 delivery. Deliveries under the prior Executive Take /
Advisory Layer format do not count toward proving the source-first product
format.

---

## SECTION 2 — PROPOSED CHANGE

**Affected file:** `build_agent_input_slim.py` (agent prompt output format
section)

**New WS1 output structure:**

```
SECTION 1 — TOP SOURCE-BASED SIGNALS
5–8 source-backed developments. Each item:
  - Signal headline
  - Source(s) with source category label and freshness label
  - Factual summary (2–4 sentences; no unsupported claims)
  - One-line "why it matters" note

SECTION 2 — SOURCE ROUNDUP BY FAMILY
Sources grouped by category:
  A. Official / Regulatory
  B. State Media / Official Narrative
  C. Chinese Business / Financial Press
  D. Sector-Specific Sources
  E. Company / Disclosure Sources
  F. International Sources
  G. Platform / Lower-Authority Sources (where present)

SECTION 3 — WHAT IS ACTUALLY NEW
Freshness distribution of the source pool:
  NEW-24H: [list]
  FOLLOW-UP-48H: [list]
  CONTEXT-7D: [list]
  BACKGROUND: [list]

SECTION 4 — NARRATIVE AMPLIFICATION / DUPLICATE WATCH
Identify: state-media amplification chains, syndication patterns,
same-story duplicates. Label: UNIQUE SOURCE / SYNDICATED / SAME-STORY
DUPLICATE / OFFICIAL AMPLIFICATION / STATE-MEDIA AMPLIFICATION /
MULTI-SOURCE CORROBORATION. Note where source count overstates
source diversity.

SECTION 5 — LIGHT EDITORIAL READ
Maximum 3 bullets. Each bullet must cite at least one listed source.
No unsupported conclusions. No imperative constructions. No
alarm-grade superlatives. Conditional and hedged framing only
(T-04 rules apply).

SECTION 6 — SOURCES
[Deterministic source appendix — see CP-024 for full upgrade spec]
```

**LinkedIn:** Removed from default output instructions. Not generated
unless a future operator decision re-introduces it as an optional
downstream artifact.

**Change scope:** Replacement of the output format instruction block in
build_agent_input_slim.py. Single file. No retrieval, validation, scrubber,
or delivery gate changes. Scrubber template config (_TEMPLATE_CONFIG in
scrub_result_ids.py) and shell heuristics (run_light_to_lark.sh case block
from CP-012) will require corresponding updates — see implementation notes.

**Implementation dependency note:** The WS1 scrubber (CP-013) currently
expects {"EXECUTIVE TAKE", "ADVISORY LAYER"} as section headers. The shell
heuristic (CP-012) expects those same headers for the completeness gate.
Claude Code must update both when implementing CP-021:
  - scrub_result_ids.py: WS1 entry in _TEMPLATE_CONFIG updated to new
    SECTION 1–6 headers and new REQUIRED_CITED_SECTION
  - run_light_to_lark.sh: WS1 case block BRIEF_TITLE, COMPLETENESS_RE_1/2,
    ENRICHMENT_AWK_ANCHOR updated to match new section headers

---

## SECTION 3 — RISK ASSESSMENT

**Risk level:** HIGH

This is the most significant product change in the signal-widening plan.
The output experience changes materially for the operator and any downstream
recipient. The scrubber and shell heuristics have downstream dependencies
that must be updated in the same implementation session (multi-file, but
single-layer — all prompt/format changes; no retrieval or validation changes).

The primary risk is format-level: the new 6-section structure may produce
outputs that the scrubber rejects as incomplete until the scrubber config
is updated. Both files must be updated atomically.

LinkedIn suppression also removes a product element the operator has been
reviewing. The operator has confirmed this is the desired direction.

**Rollback plan:**

Claude Code creates backups before modification:
```
build_agent_input_slim.py.bak_YYYYMMDD_cp021
scrub_result_ids.py.bak_YYYYMMDD_cp021
run_light_to_lark.sh.bak_YYYYMMDD_cp021
```
Rollback: restore all three from backup. No other files affected.

---

## SECTION 4 — VALIDATION METHOD

**Validation criteria (both held-mode runs):**

1. py_compile exit 0 on modified build_agent_input_slim.py and
   scrub_result_ids.py; bash -n exit 0 on run_light_to_lark.sh
2. Held-mode output contains all 6 sections (SECTION 1 through SECTION 6)
3. Scrubber: ids_kept matches expected count; unsupported_groups=0;
   uncited_claims_removed=0
4. SECTION 1 contains 5–8 signal items with source labels and freshness labels
5. SECTION 4 contains at least one narrative amplification or deduplication note
6. SECTION 5 contains maximum 3 editorial bullets, each citing a listed source
7. SECTION 6 / SOURCES appendix present
8. No LinkedIn Draft section present in output
9. Validator GREEN; T-04 compliant (conditional framing in SECTION 5)
10. Operator reviews both held-mode runs and confirms format meets product bar

**Runs required:** 2 held-mode runs reviewed by operator; then live.
Gate streak restarts on first live delivery.

---

## SECTION 5 — SCOPE COMPLIANCE CHECK

- [x] Change confined to prompt/format layer (build_agent_input_slim.py,
      scrub_result_ids.py section headers, run_light_to_lark.sh heuristics)
- [x] All three affected files are format/orchestration — not retrieval or
      validation architecture
- [x] Rollback path documented (3 backups)
- [x] Within Phase D scope (output format / editorial quality improvement)

**Forbidden change check — all confirmed NO:**

- [x] Does NOT alter retrieval behavior
- [x] Does NOT weaken validator strictness
- [x] Does NOT weaken scrubber citation enforcement
- [x] Does NOT bypass or modify the Delivery Gate decision
- [x] Does NOT affect client namespace isolation
- [x] Does NOT introduce Brain Lite schema changes

---

## SECTION 6 — OPERATOR APPROVAL

| Field | Value |
|-------|-------|
| Approved by | Operator |
| Approval date | 2026-05-28 |
| Implementation assigned to | Claude Code |
| LinkedIn disposition | SUPPRESSED from default output |
| Gate streak restarts | Yes — on first live CP-021 delivery |
| Implementation confirmed date | |
| Backups confirmed | |

---

## SECTION 7 — POST-IMPLEMENTATION RESULTS

| Run # | Date | Mode | All 6 sections? | Scrubber clean? | Operator review | Validator | Notes |
|-------|------|------|-----------------|-----------------|-----------------|-----------|-------|
| 1 | | held | | | | | |
| 2 | | held | | | | | |
| 3 | | live | | | | | gate streak restarts |

**Overall outcome:** PENDING

---

*OPENCLAW-D-CP-021 | Version 1.0 | Created: 2026-05-28 | Status: APPROVED — implementation pending*
*Raised by: CoWork — signal-widening plan approval 2026-05-28*
*Operator approved: 2026-05-28 | Gate streak restarts on first live delivery*
