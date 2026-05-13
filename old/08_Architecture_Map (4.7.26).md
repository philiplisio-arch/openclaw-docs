# 🏗️ ARCHITECTURE / SYSTEM MAP — OPENCLAW

---

## 📌 PURPOSE
Provide a clear, single reference for how the system works so issues can be diagnosed quickly and changes are controlled.

---

# 🔷 1. SYSTEM OVERVIEW

End-to-end flow:

User / Trigger  
→ Control Layer (cron / webhook / manual command)  
→ Retrieval Layer (Brave / Baidu / future sources)  
→ Retrieval Orchestrator (normalize + deduplicate + structure)  
→ Agent Layer  
→ Processing / Enrichment  
→ Relay Layer (Flask)  
→ Output Layer (Lark / Discord)

---

# 🔷 2. CORE COMPONENTS

## 🧠 Agent Layer
- Agents:
  - `china_pr_monitor_light` (signal generation)
  - `china_pr_enrichment` (advisory / synthesis layer)
- Runs inside Docker container:
  - `openclaw-openclaw-gateway-1`

### Rule
- Agents do **not** perform retrieval directly
- Agents read **structured retrieval inputs**
- Agent behavior should remain stable even as retrieval sources expand

---

## 🔍 Retrieval Layer
### Current
- Brave Search API

### Phase 5 Expansion
- Baidu API
- Future China-native sources:
  - WeChat sources
  - Zhihu
  - Weibo
  - other approved inputs

### Rule
- New retrieval sources are added **outside** the agent
- Retrieval sources must not be injected ad hoc into prompts

---

## 🧩 Retrieval Orchestrator (NEW CRITICAL LAYER)
### Function
Sits between retrieval and agent execution.

### Responsibilities
- Run approved retrieval sources
- Collect results from multiple providers
- Normalize output into one consistent structure
- Deduplicate overlapping results
- Preserve source traceability
- Pass structured input into agent

### Output Contract
Retrieval output should be transformed into a stable, structured payload before the agent sees it.

Example conceptual flow:

Brave result list  
+ Baidu result list  
→ normalized source bundle  
→ agent input

### Architectural Rule
This is now the official integration boundary for all external retrieval.

---

## ⚙️ Processing Layer
- LLM Provider:
  - Moonshot (Kimi k2.5)
- Behavior:
  - Consumes structured retrieval input
  - Produces structured signal output
  - Enrichment layer transforms signal into advisory output

### Rule
- Retrieval logic and agent reasoning are separate layers
- Prompt quality still matters, but retrieval control is now a system-layer concern

---

## 🔁 Relay Layer (Lark Integration)
- Script:
  - `/root/lark_doc_relay.py`
- Function:
  - Receives final output
  - Writes to Lark Doc via API
- Environment:
  - `/root/relay-venv`

---

## 🌐 Webhook / Control Layer
- Flask app (control layer)
- Port:
  - `8790`
- Functions:
  - Trigger runs
  - Provide basic UI / command interface
  - Enforce operational control patterns
  - Support controlled execution outside terminal usage

---

## ⏱️ Automation Layer (Cron)
- Runs scheduled workflows
- Example:
  - Daily monitoring run
- Role:
  - Scheduled trigger only
  - Should not contain retrieval logic itself
- Rule:
  - Cron triggers pipeline
  - Retrieval orchestration happens inside the pipeline, before agent execution

---

## 📄 Output Layer
### Lark (Feishu) Docx
- Main full output surface
- Output structure includes:
  - Timestamp header
  - Executive Take
  - Advisory Layer
  - Signal Layer
  - Evidence links

### Discord
- Secondary distribution layer
- Executive output / summarized output only, per current distribution rules

---

# 🔷 3. DATA FLOW (SIMPLIFIED)

Cron / Webhook / Manual Trigger  
→ Retrieval sources execute  
→ Retrieval Orchestrator combines results  
→ Structured retrieval package generated  
→ `china_pr_monitor_light` reads structured inputs  
→ Signal output generated  
→ `china_pr_enrichment` produces advisory output  
→ Relay script posts to Lark / distribution layer  
→ Final output delivered  

---

# 🔷 4. DATA FLOW (CANONICAL PHASE 5 MODEL)

### A. Trigger
- Cron
- Webhook
- Manual operator command

### B. Retrieval
- Brave
- Baidu
- future approved retrieval sources

### C. Orchestration
- normalize
- deduplicate
- filter
- structure
- preserve URLs / source traceability

### D. Signal Generation
- `china_pr_monitor_light`
- reads structured retrieval bundle
- generates region-based signals + evidence logic

### E. Enrichment
- `china_pr_enrichment`
- transforms signal into:
  - Executive Take
  - Advisory Layer
  - LinkedIn / summary output as applicable

### F. Delivery
- Relay to Lark
- optional channel delivery (Discord / future channels)

---

# 🔷 5. PORTS & SERVICES

- OpenClaw Gateway UI:
  - `18789–18790`
- Internal control listener:
  - `18791`
- Lark relay:
  - `8787`
- Webhook control:
  - `8790`

---

# 🔷 6. KEY FILE LOCATIONS

- OpenClaw config:
  - `/home/node/.openclaw/openclaw.json`

- Workspaces:
  - `/home/node/.openclaw/workspace-*`

- Relay script:
  - `/root/lark_doc_relay.py`

- Logs:
  - `/root/openclaw_logs/`

- Webhook / control script:
  - Phase 4 control layer script on server

---

# 🔷 7. LOGGING & DEBUG POINTS

When debugging, check in this order:

1. Trigger source  
   - cron / webhook / manual path

2. Retrieval execution  
   - was Brave called?
   - was Baidu called?
   - did retrieval return usable results?

3. Retrieval Orchestrator output  
   - were results normalized correctly?
   - were duplicates filtered?
   - were URLs preserved?

4. Agent input quality  
   - did signal agent receive structured retrieval input?

5. Agent output  
   - signal structure correct?
   - evidence mapping intact?

6. Enrichment output  
   - advisory quality / structure correct?

7. Relay success/failure  
   - HTTP response
   - Lark write confirmation

8. Final output verification  
   - Lark updated correctly
   - Discord output scope correct

---

# 🔷 8. CURRENT ARCHITECTURAL RULES

## Rule 1 — Retrieval happens outside the agent
Agents do not decide when or how to search.

## Rule 2 — External sources enter only through the Retrieval Orchestrator
No direct prompt injection of raw external retrieval.

## Rule 3 — Structured input before reasoning
The agent should receive normalized, controlled retrieval data.

## Rule 4 — One integration boundary
All future retrieval expansion must plug into the same orchestration layer.

## Rule 5 — Stability before expansion
Do not bypass orchestration to add new sources quickly.

---

# 🔷 9. KNOWN ISSUES / CURRENT FOCUS

### Previously observed / now clarified
- Retrieval visibility was historically weak
- Direct external retrieval integration created instability risk
- Earlier architecture assumed a simpler retrieval model than the system now requires

### Current focus
- Implement Retrieval Orchestration Layer cleanly
- Add Baidu through orchestrated pipeline, not direct injection
- Preserve Phase 4 stability while expanding Phase 5 capability

---

# 🔷 10. KNOWN FIXES / PLAYBOOKS

## Lark Integration Fixes
- Ensure correct root block ID
- Use correct API endpoint:
  `/open-apis/docx/v1/documents/{document_id}/blocks/{block_id}/children`
- Validate response:
  - HTTP 200
  - `"code": 0`

## Retrieval Expansion Fix Rule
- Do not append external retrieval directly into agent prompt
- Build retrieval outside agent
- Normalize first
- Pass structured data second

---

# 🔷 11. CHANGE RULE

When updating this document:

- Update only the section that has materially changed
- Keep architecture factual
- Do not mix roadmap language with system-state language
- If retrieval flow changes, update:
  - SYSTEM OVERVIEW
  - CORE COMPONENTS
  - DATA FLOW
  - ARCHITECTURAL RULES

---

# 🧠 FINAL PRINCIPLE

This document answers:

👉 “Where is the problem likely located?”

Primary diagnostic logic:

- If output quality is weak → check agent / enrichment
- If sources are weak or unstable → check retrieval / orchestration
- If delivery fails → check relay / output layer
- If run path differs → check trigger / control layer

If the document does not make that easy to see, simplify it.