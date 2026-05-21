# OPENCLAW — CUMULATIVE ISSUE LOG & FEATURE TRACKING (v3.2)
(Start Date: 2026-03-28 → Ongoing)
(Post Phase 4.5 — Signal Integrity Fix Applied)

---

## 🧭 SYSTEM PRIORITY DASHBOARD

### 🔴 CRITICAL ACTIVE ISSUES
- None  

### 🟠 HIGH PRIORITY
- None  

### 🟡 MEDIUM PRIORITY
- #19 — Discord Output Formatting  
- #21 — Retrieval Depth / Chinese Source Utilization  

### 🟢 MONITOR
- #20 — Runtime Performance Variability  
- #16 — VPN / SSH Instability (Environmental)  

---

## 🟢 CORE SYSTEM STATUS

- Execution pipeline stable  
- Control layer fully operational  
- Webhook + UI control validated  
- Multi-channel distribution active (Lark + Discord)  
- Locking and concurrency control working  
- Signal integrity enforcement implemented (low-signal handling fixed)  

---

## 🎯 ACTIVE SYSTEM FOCUS

- Output quality / formatting (#19)  
- Retrieval depth (Phase 5 — #21)  

---

## 🧭 EXECUTION PRIORITY ORDER

1. Issue #19 — Output formatting  
2. Issue #21 — Retrieval depth  
3. Issue #20 — Performance (monitor only)  

---

## 🔁 RECURRING RISK TRACKING

| Issue | Type | Risk | Status |
|------|------|------|--------|
| #19 | Output | Medium | 🟡 ACTIVE |
| #21 | Retrieval | Structural | ⚠️ MONITOR |
| #20 | Performance | Low | ⚠️ MONITOR |

---

## 🧠 ROOT CAUSE PATTERNS

1. Strict → Fragile → Failure (Resolved: #8, #9, #10)  
2. State not controlled → duplicate / stale output (Resolved: #11)  
3. UI layer ≠ system state confusion (Resolved: #12, #14)  
4. Retrieval visibility gap (Improved: #15 → validated)  
5. Low-signal fallback → narrative overreach (**Resolved: #18**)  

---

## 📊 SYSTEM HEALTH SCORE

| Category | Status |
|--------|--------|
| Execution Stability | 🟢 Strong |
| Control Layer | 🟢 Strong |
| Distribution Layer | 🟢 Strong |
| Output Quality | 🟡 Needs refinement |
| Retrieval Quality | 🟡 Functional but uneven |
| UX / Interface | 🟢 Strong |

---

## ⚠️ ISSUE LOG (MASTER RECORD)

### 🔴 ACTIVE ISSUES

### ISSUE #19 — Discord Output Formatting
Layer: Output / Distribution  
Priority: Medium  
Status: RESOLVED  

Failure Mode:
- Output was dense, poorly structured, and included unnecessary sections (Advisory Layer, LinkedIn, full signal dump)
- Not optimized for chat consumption

Fix Applied:
- Implemented Discord-specific formatter in webhook layer
- Restricted output to:
  → Header  
  → Executive Take only  
- Converted lines to bullet format (•)
- Removed all downstream sections (Advisory, LinkedIn, Signal)

Validation:
- Triggered full pipeline via webhook
- Confirmed:
  ✔ Clean formatting in Discord  
  ✔ No truncation  
  ✔ High readability  
  ✔ Lark output unaffected  

Follow-up Required:
No 

---

#### ISSUE #21 — Retrieval Depth / Chinese Source Utilization  
**Layer:** Retrieval  
**Priority:** Medium  
**Status:** MONITOR (Phase 5)  

**Failure Mode:**  
- Chinese sources not consistently producing usable signals  

**Description:**  
- Western sources dominate under weak signal conditions  

**Impact:**  
- Reduced differentiation and insight depth  

---

#### ISSUE #20 — Runtime Performance Variability  
**Layer:** Execution  
**Priority:** Low  
**Status:** MONITOR  

**Failure Mode:**  
- Runtime ~2–3 minutes  

---

#### ISSUE #16 — VPN / SSH Instability  
**Layer:** Infrastructure  
**Priority:** Low  
**Status:** ENVIRONMENTAL  

**Failure Mode:**  
- SSH disconnects  

---

### ✅ RESOLVED ISSUES

#### ISSUE #18 — LOW-SIGNAL HALLUCINATION IN ENRICHMENT LAYER  
**Status:** RESOLVED  
**Date:** 2026-04-01  

**Problem:**  
- Strategic narrative generated without signal  

**Root Cause:**  
1. No low-signal logic  
2. “Always produce insight” bias  
3. No guardrails  
4. Fragile prompt injection  

**Fix Implemented:**  
- Low-signal override  
- Region-level no-signal rule  
- Strict output enforcement  
- Prompt stabilization  

**Validation:**  
- Real runs: grounded  
- Zero-signal test: minimal output  
- Deterministic behavior confirmed  

**Result:**  
- Correct signal vs no-signal distinction  
- Eliminated hallucinated narratives  

**Principle:**  
→ Absence of evidence must NOT be converted into insight  

---

#### OTHER RESOLVED ISSUES

- #8 — Script Crash → RESOLVED  
- #9 — JSON Parsing → RESOLVED  
- #10 — Date Validation → RESOLVED  
- #11 — Concurrent Run Collision → RESOLVED  
- #12 — Lock UX Confusion → RESOLVED  
- #13 — Command Wiring → RESOLVED  
- #14 — UI Message Handling → RESOLVED  
- #15 — Search Underutilization → RESOLVED  
- #17 — Discord Integration → RESOLVED  

---

## 📊 SYSTEM STATE SUMMARY

| Category | Count |
|--------|------|
| Active Issues | 0 Critical / 2 Medium |
| Monitoring Issues | 2 |
| Resolved Issues | 11+ |

---

## 🧭 CURRENT SYSTEM STATUS

**SYSTEM STATUS: OPERATIONAL (STABLE + CONTROLLED)**  

- Fully controllable via UI  
- Multi-channel distribution active  
- Signal integrity enforced  
- Retrieval validated  
- Execution stable  

**Remaining Focus:**  
- Output formatting (Discord)  
- Retrieval depth (China sources)  

---

## 🧠 FINAL NOTE

This fix establishes a core system capability:

→ The system now knows when NOT to generate insight  

This is a prerequisite for client-grade intelligence output.