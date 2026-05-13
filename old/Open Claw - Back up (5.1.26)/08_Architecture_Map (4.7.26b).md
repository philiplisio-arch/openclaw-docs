## ⚙️ PROCESSING & DELIVERY (SIMPLIFIED)

### Processing
- LLM consumes structured retrieval input  
- Produces signal + enrichment output  

### Delivery
- Relay writes to Lark  
- Optional distribution to Discord  

### Automation
- Cron / webhook trigger execution  
- No retrieval logic at trigger level  

---

## 🧩 IMPLEMENTATION NOTES (NON-CORE)

- Relay script: `/root/lark_doc_relay.py`  
- Webhook control: port 8790  
- Gateway + logs remain unchanged  
- Output format includes:
  - Executive Take  
  - Advisory Layer  
  - Signal Layer  
  - Evidence  

---

## 🔷 DATA FLOW (FINAL — SIMPLIFIED)

Trigger  
→ Retrieval  
→ Orchestrator  
→ Agent  
→ Enrichment  
→ Delivery