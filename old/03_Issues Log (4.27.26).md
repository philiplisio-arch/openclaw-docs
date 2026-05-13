🧠 OPENCLAW — ISSUES LOG (UPDATED)

---

## 🔴 ACTIVE ISSUES

---

### Issue #24 — Baidu Output Path Bug

Status: OPEN

Observed:

• Baidu executor writes to:
`/rootopenclaw_phase5/data/baidu_raw.json`
• Missing slash after `/root`

Impact:

• Baidu results not persisted correctly
• retrieval_package may exclude Baidu
• Breaks multi-source integrity

Root Cause:

• Incorrect file path in baidu_executor.py

Next Step:

• Fix path:
`/root/openclaw_phase5/data/baidu_raw.json`

Validation Required:

• Confirm baidu_raw.json is written
• Confirm Baidu results appear in normalized_results.json
• Confirm presence in retrieval_package.json

---

### Issue #31 — result_id Citation Integrity Failure

Status: OPEN (CRITICAL)

Observed:

• Agent outputs (result_id: XXX) citations
• Only subset match retrieval_package
• Remaining result_ids are invalid

Example:

• 7 citations extracted
• 1 valid
• 6 invalid → validator FAIL → delivery blocked

Impact:

• System cannot deliver output
• Evidence traceability unreliable
• Phase 6.3 blocked

Root Cause:

• Agent still probabilistic
• Not strictly binding to provided result_id set
• Prompt constraints insufficient

Conclusion:

→ Prompt-based citation control FAILED

Next Step:

• Extract all result_id from output
• Compare against retrieval_package valid IDs
• Identify mismatch pattern

Validation Required:

• 100% result_id match rate
• Zero fabricated IDs
• Validator PASS on real runs

---

### Issue #32 — Legacy Citation Instructions Still Present

Status: OPEN

Observed:

• agent_input_slim.txt still contains:
  - [Source: ...]
  - [Based on: ...]
  - allowed_citations references

Impact:

• Conflicting instructions to agent
• Undermines Phase 6.3 enforcement

Root Cause:

• Incomplete removal from build_agent_input_slim.py

Next Step:

• Fully purge:
  - allowed_citations
  - legacy citation examples
  - all Source/Based on references

Validation:

• grep returns ZERO matches for:
  [Source:
  [Based on:
  allowed_citations

---

## 🟡 MONITORING

---

### Issue #25 — Agent Intermittent No Reply

Status: MONITOR

Observed:

• Intermittent "No reply from agent"

Root Cause:

• Provider instability / overload

Fix:

• Default model switched to:
google/gemini-2.5-pro

• Timeout tuning applied

Current State:

• Improved but not guaranteed stable

Monitoring Rule:

• Watch logs for:
"No reply from agent"

---

## 🟢 RESOLVED ISSUES

---

### Issue #26 — Validator Layer (Phase 6.1 — V1)

Status: ✅ RESOLVED

✔ PASS / WARN / FAIL behavior validated  
✔ Fabrication detection confirmed  
✔ Deterministic validation working  

---

## 🔵 SYSTEM STATUS SUMMARY

---

Phase 5.6: ✅ COMPLETE  
Phase 6.1: ✅ COMPLETE  
Phase 6.2: ❌ FAILED (prompt-based citation control ineffective)  
Phase 6.3: 🚧 IN PROGRESS  

System is now:

✔ Deterministic  
✔ Observable  
✔ Recoverable  
✔ Validator-enforced  
✔ Blocking invalid outputs  

But NOT yet:

✖ Deterministic evidence traceability  
✖ Agent citation reliability  

---

## 🔷 CURRENT PHASE

---

### Phase 6.3 — Evidence Traceability System (ACTIVE)

Objective:

• Replace freeform citations with result_id system  
• Enforce deterministic evidence mapping  
• Eliminate hallucinated sourcing  

---

## 🔶 NEXT CRITICAL ACTION

---

→ Diagnose result_id mismatch pattern

END