🚀 ACTIVE EXECUTION PLAN (PHASE 5 ENTRY)

---

# 🎯 TODAY’S FOCUS (SOURCE OF TRUTH)

Define Retrieval Orchestration Layer architecture (Brave + Baidu, no implementation yet)

---

## ▶️ FIRST STEP (MANDATORY)

Define the full retrieval flow BEFORE the agent:

Trigger → Retrieval Sources → Orchestrator → Structured Input → Agent

---

## ✅ TASKS

1. Define retrieval architecture:
   - confirm retrieval occurs OUTSIDE agent
   - confirm orchestrator is single integration boundary

2. Define orchestrator responsibilities:
   - source execution (Brave, Baidu)
   - normalization
   - deduplication
   - filtering
   - source traceability preservation

3. Define structured output schema (CRITICAL):
   - exact JSON format passed to agent
   - required fields (title, URL, source, summary, region, timestamp)

4. Define agent input contract:
   - how structured retrieval is injected into prompt
   - what agent sees vs what is hidden

5. Define failure handling:
   - empty retrieval case
   - conflicting sources
   - partial retrieval (one source fails)

6. Confirm architectural rules:
   - NO direct API injection into prompts
   - NO agent-controlled retrieval
   - ALL sources pass through orchestrator

---

## 🔍 VALIDATION (SUCCESS CRITERIA)

- Retrieval flow fully defined end-to-end  
- Orchestrator responsibilities clearly specified  
- Output schema explicitly defined  
- Agent input contract unambiguous  
- Failure modes handled  
- No code written  
- No changes to pipeline  

---

## 🐞 RELATED ISSUES

#22 — Retrieval Integration Architecture (PRIMARY)  
#21 — Retrieval Stability / Accessibility (MONITOR)  
#16 — SSH Instability (environmental)  

---

## ⛔ OUT OF SCOPE

- Writing orchestrator code  
- Modifying pipeline  
- Prompt optimization  
- Multi-agent expansion  
- WeChat / other APIs  
- Output tuning  

---

## 🔁 UPDATE RULE

At end of next session:

- Update Daily Status → NEXT SESSION FOCUS  
- Copy into this doc  
- Define next FIRST STEP  

---

## 🧠 OPERATING PRINCIPLE

Design the full system before building any part of it  

No partial implementation  
No experimental integration  
No shortcuts around orchestration layer  

---

END