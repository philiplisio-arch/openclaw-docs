# 📄 OPENCLAW — ISSUES LOG (UPDATED 2026-04-24)

---

## 🔴 ACTIVE / RECENT ISSUES

---

### 🐛 Issue #18 — Signal Integrity Drift (“Silence Amplification”)

**Status:** ✅ Resolved  
**Phase:** 4.5  

**Problem:**  
- Under low-signal conditions, system generated:
  - speculative narratives  
  - forced pattern recognition  
  - fabricated “developments”

**Root Cause:**  
- Agent overcompensating for weak retrieval  
- No enforced low-signal behavior  

**Fix:**  
- Introduced low-signal rule:
  - allow “no significant developments” output  
  - prohibit narrative filling  

**Result:**  
- No fabricated insights under weak retrieval  
- Output integrity restored  

---

### 🐛 Issue #23 — Cron Output Suppression on Non-Zero Exit

**Status:** ⚠️ Fix Applied — Pending Production Validation  
**Phase:** 5.6  

---

#### Symptom

- Cron run produced:
  - `[FAIL] Phase 5 run aborted: orchestrator exited non-zero (code 1)`
  - No report delivered to Lark  

- Despite:
  - valid agent output existing  

---

#### Root Cause

Wrapper completeness logic incorrectly required:

- `EXECUTIVE TAKE`  
- `ADVISORY LAYER`  
- **`LINKEDIN DRAFT` (incorrectly treated as mandatory)**  

This violated system design:

- LinkedIn Draft is **optional**  
- Core output validity = Executive + Advisory  

---

#### Fix Applied (2026-04-24)

Updated wrapper logic in:

1. Recovery heuristic  
2. Completeness gate  

New requirement:

- `EXECUTIVE TAKE`  
- `ADVISORY LAYER`  

Removed requirement:

- `LINKEDIN DRAFT`  

---

#### Manual Validation Result

Observed:

- `exit code = 1`  
- `output complete heuristic = true`  
- recovery triggered  
- full report generated  
- Lark delivery successful (`HTTP 200`)  

---

#### Current Status

- Manual run: ✅ confirmed working  
- Cron run (post-fix): ⏳ pending validation  

---

#### Next Validation Step

Next scheduled cron run must confirm:

- recovery triggers correctly on non-zero exit  
- output is delivered (not suppressed)  
- Lark push returns HTTP 200  
- no failure notice sent  

---

#### Decision Rule

- If cron passes → mark issue **Resolved**  
- If cron fails → investigate runtime divergence  

---

## 🟡 STRUCTURAL / FUTURE ISSUES

---

### 🧠 Issue #30 — No Output Validation Layer (Client Trust Risk)

**Status:** 🟡 Open (Planned Phase 6)  
**Phase:** 6 (planned)

---

#### Problem

- System produces:
  - plausible outputs  
- But does not verify:
  - whether claims map to real sources  
  - whether citations are valid  

---

#### Risk

- Hallucinated citations  
- Misattributed claims  
- Reduced client trust  

---

#### Proposed Solution

Introduce **Validator Layer** between:

Agent → Delivery  

Validator responsibilities:

- verify source existence  
- verify URL validity  
- enforce claim → evidence mapping  
- block or flag invalid outputs  

---

#### Status

- Not yet implemented  
- To be designed as first Phase 6 component  

---

## 🧠 SYSTEM INSIGHT (IMPORTANT)

Recent issues confirm:

> The primary failure mode is NOT generation quality  
> It is **control-layer misclassification of valid output**

This reinforces:

- need for strong validation  
- need for accurate failure detection  
- importance of observability over assumptions  

---

## 📊 CURRENT SYSTEM RISK PROFILE

| Area | Status |
|------|--------|
| Retrieval | ✅ stable |
| Orchestrator | ✅ stable |
| Agent output | ✅ stable |
| Control layer | ⚠️ stabilizing |
| Delivery (Lark) | ✅ stable |
| Validation layer | ❌ missing |

---

## ▶️ NEXT PRIORITY

1. Confirm Issue #23 resolution via cron  
2. Close Phase 5.6  
3. Enter Phase 6  
4. Build Validator Layer  

---

## 🧠 FINAL NOTE

System is now operating at:

> **High output capability, medium operational trust**

Phase 6 objective:

> **Move to high trust, client-grade reliability**