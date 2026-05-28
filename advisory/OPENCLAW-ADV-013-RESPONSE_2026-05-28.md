---
document_id: OPENCLAW-ADV-013-RESPONSE
date: 2026-05-28
classification: PHASE D ADVISORY — OPERATOR RESPONSE (REVISED)
status: OPERATOR APPROVED
---

# OPENCLAW — OPERATOR RESPONSE MEMO (REVISED)
**Subject:** Response to Signal-Widening Advisory — 2026-05-24
**Date:** 2026-05-28
**Prepared by:** CoWork Consultant (on behalf of Operator)
**In response to:** OPENCLAW Advisory Memo ADV-013 — Best-in-Class Strategy
  for Widening China-Based Signal in ALJ Monitoring and the Core China
  Monitoring Report (2026-05-24)
**Revision note:** Incorporates targeted revisions per Consultant Review
  Memo OPENCLAW-ADV-013-REVIEW 2026-05-28
**Status:** OPERATOR APPROVED 2026-05-28

---

## I. ASSESSMENT OF THE ORIGINAL MEMO

The memo's central diagnosis is accepted: signal quality is the current
weak link, and the appropriate near-term direction is a source-first
intelligence product rather than an automated advisory writer. The
recommended China Signal Architecture — source taxonomy labels, freshness
labels, narrative amplification detection, structured query families, and
a deterministic source appendix — is coherent, proportionate to the current
phase, and implementable through existing mechanisms without architectural
change.

One structural issue with the original memo: its proposed CP numbering
(011–017) conflicts with change packets already deployed to the pipeline.
The memo was drafted on the same day CPs 011–014 were deployed. All work
flowing from this memo uses new CP numbers beginning at CP-020.

Partial implementation of the memo's direction is already underway:

  CP-004 (deployed)  Source provenance labels [CN]/[INTL]/[CN+INTL]
  CP-007 (deployed)  Freshness and topic differentiation rules
  CP-008/010 (dep.)  SOURCES appendix with title|publisher|date|URL
  CP-009 (deployed)  ALJ 8-section output format
  CP-011 (deployed)  ALJ 7-day Baidu freshness window

---

## II. RECOMMENDED ACTION PLAN

Work is staged across four tiers. Each tier validates before the next begins.
No tier begins without explicit operator approval of each change packet.

─────────────────────────────────────────────────────────────────────────
TIER 0 — IN-FLIGHT

  In-flight stabilization / cleanup (not conceptual blockers to CP-020):
    CP-018   Brain Lite digest auto-rebuild
    CP-019   Geographic footer suppression

  ALJ pre-live blockers (block ALJ external delivery):
    CP-015   SIGNAL block leak fix
    CP-016   ALJ Lark routing (doc_id pending)
    CP-017   LAST_HASH_FILE namespace fix

─────────────────────────────────────────────────────────────────────────
TIER 1 — Shared Labeling Foundation

  CP-020 — Source Taxonomy + Freshness Labels
    Layer: Agent prompt / build_agent_input_slim.py
    Source category labels: CN-OFFICIAL, CN-REGULATORY, CN-STATE,
      CN-BUSINESS, CN-SECTOR, CN-COMPANY, CN-ASSOCIATION, INTL-WIRE,
      INTL-BUSINESS, PLATFORM, UNKNOWN
    Freshness labels: NEW-24H, FOLLOW-UP-48H, CONTEXT-7D, BACKGROUND
    WS1: labels active from first live delivery after deployment
    ALJ: schema included; labels validate in held/pre-live mode only;
      ALJ labels do not go live until ALJ pre-live blockers clear
    Risk: LOW | Validates on: 1 held-mode run

─────────────────────────────────────────────────────────────────────────
TIER 2 — Source-First Product Shape + Early Retrieval Dry Run

  CP-021 — Source-First Output Restructuring (WS1)
    Layer: Agent prompt / build_agent_input_slim.py
    New output structure:
      SECTION 1 — Top Source-Based Signals (5–8 items)
      SECTION 2 — Source Roundup by Family
      SECTION 3 — What Is Actually New (freshness distribution)
      SECTION 4 — Narrative Amplification / Duplicate Watch
      SECTION 5 — Light Editorial Read (max 3 bullets, source-cited)
      SECTION 6 — Sources
    LinkedIn: SUPPRESSED from default output
    Gate streak: RESTARTS on first live CP-021 delivery
    Risk: HIGH | Validates on: 2 held-mode runs + operator review
    Implementation dependency: scrub_result_ids.py and run_light_to_lark.sh
      section headers must be updated in the same implementation session

  CP-022A — WS1 Expanded Query Family Held-Mode Dry Run
    Layer: Query templates (held mode only — no live delivery)
    Scope: Test proposed CP-022 query families; compare against current
      WS1 source baseline across retained count, Chinese sources, business
      press, official sources, sector sources, duplication rate, publisher
      concentration, operator usefulness score
    Risk: LOW-MEDIUM | Validates on: 2 held-mode runs; operator confirms
      material improvement before CP-022 proceeds

  CP-024 — Source Appendix Upgrade
    Layer: citation_sub.py
    Upgrade: add source_category + freshness_label fields to SOURCES
      appendix; add source mix summary header
    Deterministic labeling: labels derived from publisher/domain/date
      metadata where possible; UNKNOWN fallback — not agent-inferred
    Depends on: CP-020
    Risk: LOW | Validates on: 1 held-mode run

─────────────────────────────────────────────────────────────────────────
TIER 3 — WS1 Retrieval Expansion Live

  CP-022 — WS1 Core China Query Family Expansion
    Layer: Query templates (china_monitor_v1 or successor)
    Seven query families: official/regulatory | state-media narrative |
      Chinese business/financial press | sector-specific rotation |
      company/corporate | international corroboration | geopolitical/trade
    Blocked on: CP-022A gate (2 held-mode runs; operator confirms)
    Also blocked on: Browser Retrieval Phase 1 findings (operator Phase 2
      go/no-go decision before live deployment)
    Risk: MEDIUM
    Validation criteria (2 live runs):
      15+ retained sources; 8+ appendix sources; 4+ CN sources;
      2+ CN business press; 1+ official; no publisher >35%;
      operator score ≥4

─────────────────────────────────────────────────────────────────────────
TIER 4 — ALJ Signal Expansion

  CP-023 — ALJ Query Family Expansion
    Layer: Query templates (alj_china_auto_weekly_v1 or successor)
    Eight query families: official/regulatory auto | industry association/
      market data | Chinese auto sector media | business/financial press |
      company/competitor watch | China-to-Middle-East/Saudi bridge |
      policy/regulation | battery/charging/supply chain
    Blocked on: ALJ pre-live blockers (CP-015/016/017) + 1 baseline held run
    External ALJ live delivery NOT required before held-mode testing
    Risk: MEDIUM | Validates on: 2 held-mode runs vs minimum source standard

─────────────────────────────────────────────────────────────────────────
PARALLEL — Browser Retrieval Phase 1

  No new CP required. Memo fetch-priority guidance incorporated into
  existing Phase 1 implementation brief.
  Integration:
    Phase 1 implementation begins during Tier 1
    CoWork findings report produced during Tier 2
    Operator Phase 2 go/no-go decision before Tier 3 (CP-022) live deployment
  Phase 2 remains out of scope until separately authorized.

---

## III. OPERATOR DECISIONS — RESOLVED

  Decision 1 — Tier sequencing: APPROVED with revisions (CP-022A added;
    Tier 0 distinction; ALJ CP-023 timing revised)
  Decision 2 — CP-020 ALJ inclusion: APPROVED — shared schema; ALJ
    held/pre-live only
  Decision 3 — LinkedIn disposition: SUPPRESSED from default WS1 output
  Decision 4 — Gate streak: RESTARTS on first live CP-021 delivery

---

## IV. WHAT THIS PLAN DOES NOT CHANGE

Pipeline architecture, retrieval layer, scrubber, validator, and delivery
gate are unchanged until each specific CP is individually approved and
implemented. Brain Lite schema is unchanged. Operating Protocol phase lock
is unchanged.

---

*OPENCLAW-ADV-013-RESPONSE | 2026-05-28 | OPERATOR APPROVED*
*Revised per OPENCLAW-ADV-013-REVIEW 2026-05-28*
*CP specs: CP-020 through CP-024 + CP-022A filed in phase_d/*
