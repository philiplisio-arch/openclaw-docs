# OPENCLAW — ARCHITECTURE MAP

---
document_id: OPENCLAW-ARCH-001
version: 4.7.26b (updated 2026-05-01)
status: ACTIVE — reflects Phase 6.3a pipeline
---

---

## 🔷 FULL PIPELINE (CURRENT — PHASE 6.3a)

```
Trigger (cron / webhook)
  → Retrieval Layer
      - Brave executor
      - Baidu executor
  → Orchestrator
      - Normalize results
      - Deduplicate
      - Filter (3-day freshness window)
      - Detect conflicts
      - Build retrieval_package.json
  → Agent (LLM)
      - Consumes structured retrieval_package only
      - Generates claims with [result_ids: ...] / [based_on: ...] citations
      - Selects result_ids from VALID_RESULT_IDS only
      - Produces agent_output.txt
  → Scrubber
      - Extracts all result_id tokens from agent_output.txt
      - Validates each token against retrieval_package.json
      - Removes invalid / fabricated IDs
      - Rewrites citation groups
      - Produces scrubbed_output.txt + scrubber_report.json
  → Validator
      - Reads scrubbed_output.txt + retrieval_package.json
      - Confirms all cited result_ids exist in package
      - Returns PASS / WARN / FAIL
      - Produces validation_result.json
  → Delivery Gate
      - Control PASS + Validator PASS → deliver
      - Control PASS + Validator WARN → deliver with warning
      - Control PASS + Validator FAIL → block
      - Control FAIL → block (regardless of validator)
  → Lark (client delivery)
```

---

## 🧩 LAYER RESPONSIBILITIES

| Layer | Owns | Does NOT own |
|-------|------|--------------|
| Retrieval | Gathering, normalizing, deduplicating, packaging evidence | Reasoning, claim generation |
| Orchestrator | Query bundle, normalization, conflict detection, package build | Retrieval execution details |
| Agent | Signal generation, claim synthesis, citation selection | Retrieval, source invention, conflict resolution |
| Scrubber | Deterministic citation cleanup, invalid ID removal | Claim judgment, evidence matching |
| Validator | Evidence integrity verification, PASS/WARN/FAIL classification | Output rewriting, retrieval |
| Delivery Gate | Delivery decision logic | Content evaluation |

---

## ⚙️ KEY FILES (RUNTIME)

- `retrieval_package.json` — structured evidence pool passed to agent
- `agent_output.txt` — raw agent output before scrubbing
- `scrubbed_output.txt` — cleaned output passed to validator
- `scrubber_report.json` — citation audit: ids_seen, ids_kept, ids_removed
- `validation_result.json` — PASS/WARN/FAIL with full claim audit
- `build_agent_input_slim.py` — builds agent prompt including VALID_RESULT_IDS injection (Phase 6.3a active work)

---

## ⚙️ DELIVERY INFRASTRUCTURE

- Relay script: `/root/lark_doc_relay.py`
- Webhook control: port 8790
- Optional secondary delivery: Discord

---

## 📄 OUTPUT FORMAT

Agent output sections (in order):

1. Executive Take
2. Advisory Layer
3. Signal Layer (regional)
4. Evidence / Citation Block

---

## 🔷 DATA FLOW (SIMPLIFIED)

```
Trigger
→ Retrieval
→ Orchestrator
→ Agent
→ Scrubber
→ Validator
→ Delivery Gate
→ Lark
```
