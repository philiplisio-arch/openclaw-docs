🔄 SESSION HANDOVER

---

## 🎯 MISSION

Define Retrieval Orchestration Layer architecture (Brave + Baidu, Phase 5.1)

---

## ▶️ FIRST STEP

Define correct system flow BEFORE agent execution:

Trigger → Retrieval Sources → Orchestrator → Structured Input → Agent → Output

---

## 🐞 RELATED ISSUES

#22 — Retrieval Integration Architecture (PRIMARY)  
#21 — Retrieval Stability / Accessibility  
#16 — SSH Instability (environmental)  

---

## ⚠️ FOCUS RULE

Work ONLY on architecture.

Do NOT:

- Write orchestrator code  
- Modify scripts  
- Inject retrieval directly into prompts  
- Change pipeline execution  
- Test partial integrations  

If issues arise → log them, do not switch focus.

---

## 🧠 ARCHITECTURAL RULES (MANDATORY)

- Retrieval occurs OUTSIDE the agent  
- Orchestrator is the ONLY integration boundary  
- All sources (Brave, Baidu) must pass through orchestrator  
- Agent receives ONLY structured retrieval input  
- No direct API → prompt injection  

---

## 🧱 TARGET OUTPUT OF THIS SESSION

By end of session, you must have:

1. Defined retrieval flow (end-to-end)  
2. Defined orchestrator responsibilities  
3. Defined structured output schema (JSON)  
4. Defined agent input contract  
5. Defined failure handling approach  

No ambiguity allowed.

---

END