# OPENCLAW — ISSUES LOG (UPDATED)

---

## 🔴 ACTIVE ISSUES

---

### Issue #24 — Baidu Output Path Bug

Status: OPEN

• Baidu results not persisted correctly  
• Currently degraded due to SerpAPI quota exhaustion  

---

### Issue #31 — result_id Citation Integrity Failure

Status: PARTIALLY RESOLVED

• Prompt contamination removed  
• Further validation ongoing  

---

### Issue #32 — Legacy Citation Instructions

Status: RESOLVED

• All placeholder patterns removed  
• Prompt cleaned  

---

### Issue #33 — Model Execution Instability (CRITICAL)

Status: OPEN

Observed:

• Gemini Pro rate-limited  
• Gemini Flash blocked by shared auth cooldown  
• Kimi intermittent / unclear failure logging  

Impact:

• Agent produces no output  
• Control layer blocks delivery  
• System appears non-functional despite execution  

Root Cause:

• Over-reliance on single provider auth  
• Weak fallback independence  
• Insufficient logging  

Next Step:

• Establish one reliable model path  
• Improve agent logging  
• Ensure output produced under constraints  

Validation Required:

• Output generated  
• Control PASS  
• Delivery successful  

---

## 🟢 SYSTEM STATUS

Phase 6.3 → IN PROGRESS  
Phase 6.3s → ACTIVE (blocking)

---

END