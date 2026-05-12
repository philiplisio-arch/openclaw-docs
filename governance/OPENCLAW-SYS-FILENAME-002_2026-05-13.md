# OPENCLAW — FILENAME & VERSION CONTROL STANDARD

Document ID: OPENCLAW-SYS-FILENAME-002
Date: 2026-05-13
Status: APPROVED — 2026-05-13

---

## OBJECTIVE

Establish a production-grade file naming and version control system that:
1. Eliminates upload/processing errors (ChatGPT, APIs, OS)
2. Maintains a single source of truth for all live documents
3. Provides full historical traceability and rollback capability
4. Prevents ambiguity, duplication, and system misreads
5. Scales cleanly into Phase 7+ document growth

---

## CORE DESIGN PRINCIPLE

Separate CURRENT STATE from VERSION HISTORY

- Current state = one clean, stable filename
- Version history = archived, timestamped, immutable records

This mirrors best practices used in:
- Git (HEAD vs history)
- Production config systems
- Audit-controlled environments

---

## SECTION 1 — FILENAME RULES (GLOBAL)

### ALLOWED CHARACTERS
- A–Z, a–z, 0–9
- underscore (_)
- hyphen (-)
- period (.)

### FORBIDDEN
- spaces
- parentheses ( )
- commas, colons, slashes
- multiple dots in filename body (e.g. v5.3.26)

---

### WORD SEPARATION
Use underscores only.

Correct: `03_Issues_Log.md`
Incorrect: `03 Issues Log.md`

---

### DATE FORMAT (WHEN USED)
Always: YYYY-MM-DD

Correct: `2026-05-13`
Incorrect: `5.13.26 / 13-05-26 / May13`

---

## SECTION 2 — FILE CATEGORIES & RULES

---

### 2.1 CORE OPERATIONAL DOCUMENTS (LIVE)

RULE:
- NO date in filename
- ONLY ONE active version exists

FORMAT: `NN_Descriptive_Name.md`

EXAMPLES:
- `00_Master_Document_Index.md`
- `03_Issues_Log.md`
- `04_DAILY_STATUS.md`

---

### VERSION CONTROL (MANDATORY)

Each document MUST include frontmatter:

```
document_id: 03_Issues_Log
version: v1.4
last_updated: 2026-05-13
status: ACTIVE
```

This is the authoritative version record.

---

### UPDATE PROCESS (STRICT)

When making a meaningful update:
1. Copy current file
2. Move copy to /old/
3. Add version + date to filename
4. Update live file
5. Increment version in frontmatter

---

### 2.2 ARCHIVE (/old/)

RULE:
- Immutable historical records
- Date REQUIRED
- Version STRONGLY recommended

FORMAT: `/old/NN_Descriptive_Name_vX.X_YYYY-MM-DD.md`

EXAMPLES:
- `/old/03_Issues_Log_v1.3_2026-05-10.md`
- `/old/00_Master_Document_Index_v2.1_2026-05-13.md`

---

### 2.3 ADVISORY DOCUMENTS (ADV)

RULE:
- Point-in-time documents
- Immutable
- Date REQUIRED

FORMAT: `OPENCLAW-ADV-NNN_YYYY-MM-DD.md`

EXAMPLES:
- `OPENCLAW-ADV-002_2026-05-08.md`
- `OPENCLAW-ADV-009_2026-05-11.md`

---

### 2.4 GOVERNANCE / PHASE / GATE DOCUMENTS

RULE:
- Versioned system artifacts
- Date REQUIRED

FORMAT: `[ID]_YYYY-MM-DD.md`

EXAMPLES:
- `OPENCLAW-P7-GATE-001_2026-05-07.md`
- `03_Phase_Exit_Criteria_2026-05-06.md`

---

### 2.5 CONFIG / TECHNICAL FILES

RULE:
- Stable names
- No date unless explicitly versioned

EXAMPLES:
- `client_config_china_monitor_001.yaml`
- `VPS_SYNC_PROTOCOL.md`

---

## SECTION 3 — VERSION INDEX

Maintained at: `governance/Document_Versions_Index.md`

FORMAT:
```
03_Issues_Log
- v1.4 (ACTIVE) → 03_Issues_Log.md
- v1.3 → /old/03_Issues_Log_v1.3_2026-05-10.md
```

---

## SECTION 4 — PROHIBITED PATTERNS (STRICT)

- Multiple current files with dates
- Filenames containing version ambiguity
- Editing archived files
- Mixing date formats
- Using filename as version control mechanism

---

## SECTION 5 — MIGRATION HISTORY

Migration executed 2026-05-13. All live documents renamed per this standard.
Archives written to /old/ with version+date suffixes.
`OPENCLAW_COWORK_OPERATING_PROTOCOL.md` retained as named exception —
required by project instruction reference.

---

## FINAL DECLARATION

This system establishes:
- One authoritative live document per function
- Explicit, auditable version history
- Zero ambiguity in system reads
- Full compatibility with ChatGPT, APIs, and OS constraints

Deviation from this standard requires explicit operator approval.
