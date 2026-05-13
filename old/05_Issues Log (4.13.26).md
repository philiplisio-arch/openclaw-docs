OPENCLAW — ISSUE LOG
Last Updated: 2026-04-13

---

## 🔴 ACTIVE ISSUES

### Issue #21 — Enrichment Model Rejection (CRITICAL)

Status: 🔴 ACTIVE  
Impact: Blocks full report generation  

Description:
Moonshot/Kimi rejects enrichment prompt with:
"400 The request was rejected because it was considered high risk"

Observations:
• Retrieval completes successfully
• Orchestrator builds valid input
• Agent call fails at model layer
• Completeness gate blocks output (correct behavior)

Conclusion:
→ Not a system failure
→ Provider policy constraint

Next Actions:
• Add alternate model/provider
• OR implement fallback behavior
• OR redesign enrichment prompt (lower priority)

---

### Issue #22 — Single Provider Dependency

Status: 🔴 ACTIVE  
Impact: No fallback capability  

Description:
All agents configured with:
provider: moonshot (Kimi only)

Risk:
• Total system dependency on one model
• No resilience to policy rejection

Resolution Path:
• Introduce second provider (OpenAI / Anthropic / etc.)
• Enable agent-level model routing

---

## 🟡 RESOLVED ISSUES

### Issue #18 — Silent Hang / Execution Freeze

Status: ✅ RESOLVED  

Fixes:
• Outer timeout (420s)
• Inner timeout (240s)
• Docker execution isolation
• Session ID isolation

Result:
✔ No indefinite hangs

---

### Issue #19 — Output Not Returning to stdout

Status: ✅ RESOLVED  

Fixes:
• Proper RAW_OUTPUT capture
• Log-first fallback system

Result:
✔ Output always captured

---

### Issue #20 — Partial Reports Sent to Lark

Status: ✅ RESOLVED  

Fix:
• Completeness gate

Result:
✔ No incomplete outputs ever sent

---

## 🧠 KEY INSIGHT

System failure has transitioned from:

Execution instability  
→ Model constraint limitation

This is a major architectural milestone.