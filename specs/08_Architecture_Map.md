# OPENCLAW — ARCHITECTURE MAP

---
document_id: OPENCLAW-ARCH-001
version: v6.0
last_updated: 2026-05-14
status: ACTIVE — reflects Phase 6.8 pipeline
---

## 🔷 FULL PIPELINE (CURRENT — PHASE 6.8)

```
Trigger (cron / webhook)
  → Retrieval Layer
      - Brave executor
      - Baidu executor
  → Orchestrator
      - Normalize results
      - Deduplicate
      - Filter (freshness window, relevance)
      - Detect conflicts
      - Build retrieval_package.json
  → Agent (LLM)
      - Consumes structured retrieval_package only
      - Receives numbered VALID_SOURCES list (1. title, 2. title, ...)
      - Generates claims with [source_numbers: N] / [based_on: N] citations
      - Cites by source number — does NOT write result_ids directly
      - Produces agent_output.txt
  → Resolver (resolve_source_numbers.py)
      - Maps [source_numbers: N] → [result_ids: res_xxxxxxxx]
      - Maps [based_on: N] → [based_on: res_xxxxxxxx]
      - Uses source number → result_id lookup built from retrieval_package.json
      - Produces resolved agent output for scrubber input
  → Scrubber
      - Extracts all result_id tokens from resolved agent output
      - Validates each token against retrieval_package.json
      - Removes invalid / fabricated IDs
      - Rewrites citation groups
      - Removes uncited bullets before delivery
      - Produces scrubbed_output.txt + scrubber_report.json
  → Control Layer
      - Checks structural completeness of scrubbed_output.txt
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
| Agent | Signal generation, claim synthesis, citation by source number from VALID_SOURCES | Retrieval, source invention, result_id generation, conflict resolution |
| Resolver | Source number → result_id mapping; converts agent citation format for scrubber | Claim judgment, retrieval, validation |
| Scrubber | Deterministic citation cleanup, invalid ID removal, uncited bullet removal | Claim judgment, evidence matching |
| Control Layer | Structural completeness verification | Content evaluation, evidence integrity |
| Validator | Evidence integrity verification, PASS/WARN/FAIL classification | Output rewriting, retrieval |
| Delivery Gate | Delivery decision logic | Content evaluation |

---

## ⚙️ KEY FILES (RUNTIME)

- `retrieval_package.json` — structured evidence pool passed to agent
- `agent_output.txt` — raw agent output before resolver (contains [source_numbers: N] citations)
- `scrubbed_output.txt` — cleaned output passed to validator (contains resolved result_id citations)
- `conflict_log.json` — conflict records extracted from agent CONFLICTS section (/root/openclaw_phase6/validation/)
- `validation_result.json` — PASS/WARN/FAIL with full claim audit
- `build_agent_input_slim.py` — builds agent prompt including numbered VALID_SOURCES list (Phase 6.8)
- `resolve_source_numbers.py` — maps agent source_number citations to result_ids before scrubber runs (Phase 6.8)
- `citation_sub.py` — substitutes result_id tokens with publisher/date strings in Lark delivery output

---

## ⚙️ DELIVERY INFRASTRUCTURE

- Relay script: `/root/lark_doc_relay.py`
- Webhook control: port 8790
- Cron schedule: 06:30 Shanghai time
- Optional secondary delivery: Discord

---

## 📄 OUTPUT FORMAT (LOCKED — Phase 6.8)

Agent output sections (in order):

1. EXECUTIVE TAKE — claim bullets with `[source_numbers: N]` citations (resolved to result_ids by Resolver)
2. ADVISORY LAYER — implication bullets with `[based_on: N]` citations (resolved to result_ids by Resolver)
3. LINKEDIN DRAFT — plain-language summary, no citations required
4. REGIONAL SOURCE LIST — retained sources grouped by region

Lark delivery output: result_id tokens substituted with publisher/date strings by citation_sub.py.

---

## 🔷 DATA FLOW (SIMPLIFIED)

```
Trigger
→ Retrieval
→ Orchestrator
→ Agent
→ Resolver
→ Scrubber
→ Control Layer
→ Validator
→ Delivery Gate
→ Lark
```
