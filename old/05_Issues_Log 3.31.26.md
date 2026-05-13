OPENCLAW — CUMULATIVE ISSUE LOG & FEATURE TRACKING (v3.1)

(Start Date: 2026-03-28 → Ongoing)
(Optimized Control Version — Post Phase 4.5)

---

# 🧭 SYSTEM PRIORITY DASHBOARD

## 🔴 CRITICAL ACTIVE ISSUES

- #18 — Signal Quality Degradation (“Silence Amplification”)

---

## 🟠 HIGH PRIORITY

- None

---

## 🟡 MEDIUM PRIORITY

- #19 — Discord Output Formatting
- #21 — Retrieval Depth / Chinese Source Utilization

---

## 🟢 MONITOR

- #20 — Runtime Performance Variability
- #16 — VPN / SSH Instability (Environmental)

---

## 🟢 CORE SYSTEM STATUS

- Execution pipeline stable  
- Control layer fully operational  
- Webhook + UI control validated  
- Multi-channel distribution active (Lark + Discord)  
- Locking and concurrency control working  

---

# 🎯 ACTIVE SYSTEM FOCUS

→ Signal integrity under low-data conditions (#18)  
→ Output quality / formatting (#19)  
→ Retrieval depth (Phase 5 — #21)

---

# 🧭 EXECUTION PRIORITY ORDER

1. Issue #18 — Signal integrity (CRITICAL)  
2. Issue #19 — Output formatting (MEDIUM)  
3. Issue #21 — Retrieval depth (Phase 5)  

---

# 🔁 RECURRING RISK TRACKING

| Issue | Type | Risk | Status |
|------|------|------|--------|
| #18 | Output | High (credibility risk) | 🔴 ACTIVE |
| #21 | Retrieval | Structural | ⚠️ MONITOR |
| #20 | Performance | Low | ⚠️ MONITOR |

---

# 🧠 ROOT CAUSE PATTERNS

1. Strict → Fragile → Failure  
   (Resolved: #8, #9, #10)

2. State not controlled → duplicate / stale output  
   (Resolved: #11)

3. UI layer ≠ system state confusion  
   (Resolved: #12, #14)

4. Retrieval visibility gap  
   (Improved: #15 → now validated)

5. Low-signal fallback → narrative overreach  
   (Active: #18)

---

# 📊 SYSTEM HEALTH SCORE

| Category | Status |
|--------|--------|
| Execution Stability | 🟢 Strong |
| Control Layer | 🟢 Strong |
| Distribution Layer | 🟢 Strong |
| Output Quality | 🟡 Needs refinement |
| Retrieval Quality | 🟡 Functional but uneven |
| UX / Interface | 🟢 Strong |

---

# ⚠️ ISSUE LOG (MASTER RECORD)

---

## 🔴 ACTIVE ISSUES

---

### ISSUE #18 — Signal Quality Degradation / “Silence Amplification”
Layer: Output  
Priority: CRITICAL  
Recurrence: Structural  
Status: ACTIVE  

Failure Mode:
- When no verifiable developments are found, the system generates strategic narrative instead of reporting absence
- “No signal” is transformed into speculative geopolitical interpretation

Description:
- Outputs show “no developments” but still include multi-paragraph Executive Take and Advisory Layer
- Narrative implies hidden activity without evidence

Impact:
- Undermines credibility with executive users  
- Introduces analytical bias and false signal  

Root Cause:
- Prompt conflict: system requires insight even under zero-data conditions  
- Weak retrieval triggers fallback narrative generation  

Required Fix:
- Enforce hard constraint:
  → IF no verified developments → NO strategic narrative  
  → Output must remain factual and minimal  

---

### ISSUE #19 — Discord Output Formatting
Layer: Output / Distribution  
Priority: Medium  
Status: ACTIVE  

Failure Mode:
- Raw pipeline output is truncated and poorly structured for chat consumption  

Description:
- Output limited to ~1800 characters  
- Includes unnecessary sections and inconsistent formatting  

Impact:
- Reduces readability and usefulness in distribution channel  

Next Step:
- Implement structured format:
  → Header + Executive Take + Key bullets only  
  → Remove LinkedIn and verbose sections  

---

### ISSUE #21 — Retrieval Depth / Chinese Source Utilization
Layer: Retrieval  
Priority: Medium  
Status: MONITOR (Phase 5)  

Failure Mode:
- System consults Chinese sources but does not consistently extract usable signals  

Description:
- Chinese sources listed but often not actually used  
- Western sources dominate when signal density is low  

Impact:
- Reduces differentiation and local insight quality  

Status Update:
- Retrieval confirmed functional (Phase 4.3 complete)  
- Now a depth/coverage optimization issue  

---

### ISSUE #20 — Runtime Performance Variability
Layer: Execution  
Priority: Low  
Status: MONITOR  

Failure Mode:
- Execution time varies between ~2–3 minutes  

Impact:
- Acceptable but slower than ideal for real-time workflows  

---

### ISSUE #16 — VPN / SSH Instability
Layer: Infrastructure  
Priority: Low  
Status: ENVIRONMENTAL  

Failure Mode:
- SSH sessions drop intermittently during operation  

Cause:
- External network / VPN instability  

Mitigation:
- SSH keepalive implemented  
- tmux recommended  

---

## ✅ RESOLVED ISSUES

- #8 — Script Crash on Parsing → RESOLVED  
- #9 — JSON Parsing Fragility → RESOLVED  
- #10 — Date Validation Failure → RESOLVED  
- #11 — Concurrent Run Collision → RESOLVED  
- #12 — Lock UX Confusion → RESOLVED  
- #13 — Command Wiring Failure → RESOLVED  
- #14 — UI Message Inaccuracy (429 Handling) → RESOLVED  
- #15 — Search Underutilization → RESOLVED (Phase 4.3 Validation)  
- #17 — Discord Integration Failure → RESOLVED  
- #15 (Updated) — Retrieval Functional but Uneven → RECLASSIFIED  

---

# 📊 SYSTEM STATE SUMMARY

| Category | Count |
|--------|------|
| Active Issues | 1 Critical / 2 Medium |
| Monitoring Issues | 2 |
| Resolved Issues | 10+ |

---

# 🧭 CURRENT SYSTEM STATUS

SYSTEM STATUS: OPERATIONAL

- Fully controllable via UI  
- Multi-channel distribution active  
- Retrieval validated and functional  
- Stable execution under load  

Remaining risk:
→ Output quality under weak signal conditions