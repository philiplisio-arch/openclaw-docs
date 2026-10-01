# OPENCLAW — CUMULATIVE ISSUE LOG & FEATURE TRACKING (v3.3)
(Start Date: 2026-03-28 → Ongoing)
(Post Phase 4.5 — Retrieval Stability Mitigation Applied)

---

## 🧭 SYSTEM PRIORITY DASHBOARD

### 🔴 CRITICAL ACTIVE ISSUES
- None  

### 🟠 HIGH PRIORITY
- None  

### 🟡 MEDIUM PRIORITY
- #21 — Retrieval Stability / Accessibility (UPDATED)

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
- Retrieval execution controlled via cooldown guard  

---

## 🎯 ACTIVE SYSTEM FOCUS

- Retrieval stability observation (Issue #21 — passive monitoring)  
- Output quality / formatting refinement  

---

## 🧭 EXECUTION PRIORITY ORDER

1. Issue #21 — Retrieval stability (observe, not modify)  
2. Issue #20 — Performance (monitor only)  

---

## 🔁 RECURRING RISK TRACKING

| Issue | Type | Risk | Status |
|------|------|------|--------|
| #19 | Output | Medium | ✅ RESOLVED |
| #21 | Retrieval | Structural | ⚠️ MONITOR |
| #20 | Performance | Low | ⚠️ MONITOR |

---

## 🧠 ROOT CAUSE PATTERNS

1. Strict → Fragile → Failure (Resolved: #8, #9, #10)  
2. State not controlled → duplicate / stale output (Resolved: #11)  
3. UI layer ≠ system state confusion (Resolved: #12, #14)  
4. Retrieval visibility gap (Improved: #15 → validated)  
5. Low-signal fallback → narrative overreach (Resolved: #18)  
6. Repeated execution → retrieval degradation (NEW — #21)

---

## 📊 SYSTEM HEALTH SCORE

| Category | Status |
|--------|--------|
| Execution Stability | 🟢 Strong |
| Control Layer | 🟢 Strong |
| Distribution Layer | 🟢 Strong |
| Output Quality | 🟢 Strong |
| Retrieval Quality | 🟡 Functional but unstable under repeated runs |
| UX / Interface | 🟢 Strong |

---

## ⚠️ ISSUE LOG (MASTER RECORD)

### 🔴 ACTIVE ISSUES

None

---

### ISSUE #19 — Discord Output Formatting
Layer: Output / Distribution  
Priority: Medium  
Status: RESOLVED  

Failure Mode:
- Output was dense, poorly structured, and included unnecessary sections  

Fix Applied:
- Implemented Discord-specific formatter  
- Restricted output to header + Executive Take  
- Bullet formatting applied  

Validation:
- Confirmed readability and no truncation  

Follow-up Required:
No  

---

### ISSUE #21 — Retrieval Stability / Accessibility  
Layer: Retrieval / Execution  
Priority: Medium  
Status: MITIGATED (UNDER OBSERVATION)  

Failure Mode:
- First run produces strong signal  
- Subsequent rapid reruns degrade into weak or no-signal output  

Observed Pattern:
- Initial execution: strong sources (e.g., Yicai, SCMP)  
- Follow-on executions:
  - weaker signal  
  - “no developments” outputs  
  - explicit fetch failures (paywall / blocked / limited access)  

Refined Diagnosis:
- Retrieval is active and functional  
- Instability occurs under repeated execution  
- Not purely a “Chinese source depth” issue  

Root Cause (Working Hypothesis):
- Retrieval accessibility degradation due to:
  - rate limiting  
  - bot protection  
  - session degradation  
  - repeated rapid fetch attempts  

Fix Applied:
- Webhook-level cooldown guard:
  → Blocks RUN_FULL_MONITOR for 15 minutes after successful execution  
  → Prevents rapid rerun degradation  

Additional Improvements:
- Added run-history logging:
  → timestamp  
  → runtime  
  → return code  
  → stored at /root/openclaw_logs/run_history.log  

Validation:
- Cooldown behavior verified (block + allow)  
- Successful runs preserved  
- Logging confirmed operational  

Impact:
- Preserves first-run signal quality  
- Eliminates degraded rerun pattern  
- Introduces basic observability  

Status:
- Mitigated  
- Awaiting validation across multiple real runs  

Follow-up Required:
YES  
→ Observe 3–5 real runs  
→ Confirm stability  
→ Evaluate need for deeper retrieval diagnostics  

---

### ISSUE #20 — Runtime Performance Variability  
Layer: Execution  
Priority: Low  
Status: MONITOR  

Failure Mode:  
- Runtime ~2–3 minutes  

---

### ISSUE #16 — VPN / SSH Instability  
Layer: Infrastructure  
Priority: Low  
Status: ENVIRONMENTAL  

Failure Mode:  
- SSH disconnects  

---

## ✅ RESOLVED ISSUES

#### ISSUE #18 — LOW-SIGNAL HALLUCINATION IN ENRICHMENT LAYER  
Status: RESOLVED  
Date: 2026-04-01  

Fix:
- Low-signal handling logic enforced  
- Narrative generation blocked under no-signal  

Result:
- No hallucinated insights  
- Deterministic behavior  

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
| Active Issues | 0 Critical / 1 Medium |
| Monitoring Issues | 2 |
| Resolved Issues | 12+ |

---

## 🧭 CURRENT SYSTEM STATUS

SYSTEM STATUS: OPERATIONAL (STABLE + CONTROLLED)

- Fully controllable via UI  
- Multi-channel distribution active  
- Signal integrity enforced  
- Retrieval validated  
- Execution stabilized via cooldown control  

Remaining focus:  
→ Retrieval stability validation  
→ Output refinement  

---

## 🧠 FINAL NOTE

System capability improved:

→ The system now controls execution timing to preserve signal quality  

This establishes a key Phase 4 principle:

→ Stability is enforced at the control layer, not the prompt layer