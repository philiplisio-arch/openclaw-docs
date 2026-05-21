---
document_id: OPENCLAW-ADV-009
version: 1.0
date: 2026-05-11
status: APPROVED WITH CONDITIONS — 2026-05-11
---

# OPENCLAW — ADVISORY MEMO
**Document:** OPENCLAW-ADV-009
**Date:** 2026-05-11
**Subject:** File Organization System — Approved Convention

---

## BACKGROUND

The main project folder contained three parallel naming conventions
(NN_ numeric prefix, OPENCLAW- prefix, SYS_ prefix) with no governing rule
determining which applies to what. This arose incrementally as Phase 6 and
Phase 7 introduced new document categories without auditing against the
existing scheme.

---

## APPROVED SYSTEM

### Folder Structure

```
/OpenClaw project/
  ├── [main — operational docs, numbered NN_]
  ├── governance/     ← phase docs, design docs
  ├── specs/          ← locked system specs
  ├── advisory/       ← ADV memos and replies
  ├── templates/      ← TPL_ files
  ├── config/         ← client config YAML files
  └── old/            ← archive (append-only, untouched)
```

### What Goes Where

**Main folder (numbered NN_, session-start docs and permanent anchors only):**
```
00_Master_Document_Index (5.3.26).md
00_System_Constitution (5.3.26).md
01_Foundation doc (5.5.26).md
03_Issues Log (current date).md
04_DAILY_STATUS (current date).md
05_OPERATING_PROTOCOL (current date).md        ← document_id: OPENCLAW-OPS-001
06_PHASE_GATE_CHECKLIST.md                     ← document_id: OPENCLAW-P7-GATE-001
OpenClaw_Phase7_Execution_Plan.docx            ← canonical reference, no number
```

**governance/ (OPENCLAW- prefix, formal document IDs retained):**
```
OPENCLAW-BRAIN-LITE-DESIGN (5.9.26).md
OPENCLAW-BRAIN-LITE-SCHEMA-v1 (5.9.26).md
OPENCLAW-COWORK-REPORT-TEMPLATE (5.9.26).md
OPENCLAW-TEST-HARNESS-DESIGN (5.9.26).md
```

**specs/ (legacy names retained per condition 4):**
```
07_OpenClaw_Structure_Defense (5.3.26).txt
08_Architecture_Map (5.3.26).md
09_Agent_Input_Contract (LOCKED 5.5.26).md
10_Control_Layer_Spec (LOCKED 5.1.26).txt
11_Validator_Layer_Spec (LOCKED 5.5.26).md
12_Scrubber_Layer_Spec (LOCKED 5.1.26).md
SYS_RETRIEVAL_FAILURE_HANDLING (5.1.26).md
SYS_Retrieval_Query_Planning_Rules (5.1.26).md
SYS_Retrieval_Query_Templates (5.1.26).md
SYS_Retrieval_orchestrator_Execution_plan (5.1.26).md
```

**advisory/ (OPENCLAW-ADV-NNN sequential numbering):**
```
OPENCLAW-ADV-002 (5.8.26).md
OPENCLAW-ADV-003 (5.9.26).md
OPENCLAW-ADV-004 (5.11.26).md
OPENCLAW-ADV-009 (5.11.26).md    ← this document
OPENCLAW-REPLY-ADV-003 (5.9.26).md
```

**templates/:**
```
TPL_OPENCLAW PROJECT — DAILY STATUS TEMPLATE (5.3.26).md
```

**config/:**
```
client_config_china_monitor_001.yaml
```

---

## NAMING RULES GOING FORWARD

**Rule 1 — Main folder:** Only session-start operational docs and permanent
anchors. Numbered NN_ prefix for operational docs. Next available slot: 07_.
Slots 00–02 reserved as permanent anchors.

**Rule 2 — governance/:** OPENCLAW- prefix. Formal document IDs retained
inside files. New governance docs require operator approval.

**Rule 3 — advisory/:** OPENCLAW-ADV-NNN sequential. Next memo: ADV-010.
Operator replies filed as OPENCLAW-REPLY-ADV-NNN.

**Rule 4 — specs/:** Existing locked specs retain legacy names. Future new
specs require operator approval and must follow OPENCLAW-SPEC-NNN naming.

**Rule 5 — Index:** Every document must be registered in
00_Master_Document_Index with both filename/location and formal document_id
where applicable.

**Rule 6 — old/:** Append-only. Nothing deleted from old/.

---

## APPROVAL CONDITIONS (operator-confirmed 2026-05-11)

1. Formal document_id values inside documents must not be changed by
   filename moves.
2. 00_Master_Document_Index must record both filename/location and formal
   document_id where applicable.
3. Root folder must be limited to session-start operational docs and
   permanent anchors only.
4. Existing locked specs may retain legacy names; future new specs require
   operator approval and OPENCLAW-SPEC naming.
5. CoWork must perform a post-move validation check before Claude Code
   syncs to VPS.
6. old/ remains append-only and untouched.

---

*OPENCLAW-ADV-009 | 2026-05-11 | APPROVED WITH CONDITIONS*
