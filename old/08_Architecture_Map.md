# 🏗️ ARCHITECTURE / SYSTEM MAP — OPENCLAW

---

## 📌 PURPOSE
Provide a clear, single reference for how the system works so issues can be diagnosed quickly and changes are controlled.

---

# 🔷 1. SYSTEM OVERVIEW

End-to-end flow:

User / Trigger  
→ OpenClaw Agent  
→ Retrieval (Brave / future APIs)  
→ Processing (LLM / agent logic)  
→ Relay Layer (Flask)  
→ Lark Document Output  

---

# 🔷 2. CORE COMPONENTS

## 🧠 OpenClaw Agent Layer
- Agents:
  - china_pr_monitor_light (Phase 2 signal generation)
  - china_pr_enrichment (Phase 3 enrichment)
- Runs inside Docker container:
  - `openclaw-openclaw-gateway-1`

---

## 🔍 Retrieval Layer
- Current:
  - Brave Search API (configured in openclaw.json)
- Future (not active yet):
  - Baidu API
  - WeChat sources
  - Zhihu / Weibo

---

## ⚙️ Processing Layer
- LLM Provider:
  - Moonshot (Kimi k2.5)
- Behavior:
  - Generates structured outputs
  - Should incorporate retrieval (if working correctly)

---

## 🔁 Relay Layer (Lark Integration)
- Script:
  - `/root/lark_doc_relay.py`
- Function:
  - Receives output
  - Writes to Lark Doc via API
- Environment:
  - `/root/relay-venv`

---

## 🌐 Webhook / Control Layer
- Flask app (Phase 4 control layer)
- Port:
  - 8790
- Functions:
  - Trigger runs
  - Provide basic UI / command interface

---

## ⏱️ Automation Layer (Cron)
- Runs scheduled workflows
- Example:
  - Daily monitoring run
- Known issue:
  - Previously produced stale/duplicate outputs

---

## 📄 Output Layer
- Lark (Feishu) Docx API
- Output structure:
  - Region-based sections
  - Evidence links
  - Timestamp header

---

# 🔷 3. DATA FLOW (SIMPLIFIED)

Cron / Webhook / Manual Trigger  
→ OpenClaw Agent executes  
→ Retrieval (Brave) invoked (if working)  
→ Output generated (structured text)  
→ Relay script posts to Lark  
→ Lark document updated  

---

# 🔷 4. PORTS & SERVICES

- OpenClaw Gateway UI:
  - 18789–18790  
- Internal control listener:
  - 18791  
- Lark relay:
  - 8787  
- Webhook control:
  - 8790  

---

# 🔷 5. KEY FILE LOCATIONS

- OpenClaw config:
  - `/home/node/.openclaw/openclaw.json`

- Workspaces:
  - `/home/node/.openclaw/workspace-*`

- Relay script:
  - `/root/lark_doc_relay.py`

- Logs:
  - `/root/openclaw_logs/`

---

# 🔷 6. LOGGING & DEBUG POINTS

When debugging, check:

1. Agent output logs  
2. Retrieval usage (Brave calls)  
3. Relay success/failure (HTTP response)  
4. Lark document updates  
5. Cron execution logs  

---

# 🔷 7. KNOWN ISSUES (CURRENT FOCUS)

- Stale / duplicate output from cron  
- Retrieval not clearly invoked  
- Possible reliance on model knowledge vs search  
- Occasional mismatch between webhook and cron outputs  

---

# 🔷 8. KNOWN FIXES / PLAYBOOKS

## Lark Integration Fixes
- Ensure correct root block ID  
- Use correct API endpoint:
  `/open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/children`  
- Validate response:
  - HTTP 200  
  - `"code": 0`

---

# 🔷 9. CHANGE RULE

When updating this document:

- ONLY update the section affected  
- Do NOT rewrite entire document  
- Keep it factual, not explanatory  

---

# 🧠 FINAL PRINCIPLE

This document answers:

👉 “Where is the problem likely located?”

If it doesn’t help you answer that quickly → it needs simplification, not expansion.