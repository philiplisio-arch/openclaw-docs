# RETRIEVAL ORCHESTRATOR EXECUTION PLAN
OpenClaw Project

---
document_id: OPENCLAW-OEP-001
version: 5.2 (updated 2026-05-01 for Phase 6 steps)
status: ACTIVE — reflects implemented pipeline
---

## PURPOSE

Define the full execution sequence from trigger to delivery, covering the retrieval pipeline (Steps 1–10) and the Phase 6 validation chain (Steps 11–14).

---

## CANONICAL FLOW

Trigger
→ Build query bundle
→ Execute Brave retrieval
→ Execute Baidu retrieval
→ Normalize results
→ Deduplicate results
→ Filter results
→ Detect conflicts
→ Build structured package
→ Pass package to agent
→ Agent generates output

---

## STEP 1 — BUILD QUERY BUNDLE

### Purpose
- Ensure consistent retrieval across providers
- Maintain traceability
- Standardize run behavior

### Structure
Each run produces:
- query_bundle_id
- run_id
- region_scope
- list of queries

### Query Design (Initial Policy)
Per region:
- 1 precision query
- 1 recall query

Regions:
- United States
- Europe
- Middle East

Total:
- 6 queries per run

### Rules
- Query bundle created once per run
- Same logical queries used across Brave and Baidu
- No dynamic expansion in v1

---

## STEP 2 — EXECUTE PROVIDER RETRIEVAL

### Execution Model
- Brave and Baidu run in parallel
- Orchestrator waits for both or timeout

### Provider Responsibilities
Each provider returns:
- results per query
- raw rank
- title
- URL
- snippet/summary
- retrieval timestamp
- error status if any

### Timeout Rule
- Each provider has a fixed timeout
- If timeout:
  → mark provider_status = timeout
  → continue with available data

---

## STEP 3 — NORMALIZE RESULTS

### Purpose
Convert all provider outputs into a common schema.

### For each result:
- assign result_id
- map URL → canonical URL
- set retrieval_provider (Brave or Baidu)
- extract publisher if available
- normalize summary
- attach query
- attach provider_rank
- attach retrieved_at
- attach timestamp if available
- assign provisional region
- assign language
- preserve raw trace internally

### Rule
Normalization must occur BEFORE deduplication.

---

## STEP 4 — ASSIGN REGION

### Allowed values
- United States
- Europe
- Middle East
- Cross-region
- Unknown

### Assignment priority
1. query origin
2. content/topic
3. geographic references
4. fallback to Cross-region or Unknown

### Rule
Do not force precision when uncertain.

---

## STEP 5 — DEDUPLICATE RESULTS

### Level 1 — Exact duplicate
Same URL → merge

### Level 2 — Strong duplicate
Same event/article → merge and preserve trace

### Level 3 — Ambiguous duplicate
Uncertain → retain both

### Merge rules
- preserve all raw URLs
- preserve all provider ranks
- track providers_seen
- assign dedup_group_id

### Rule
Dedup must be conservative.

---

## STEP 6 — FILTER RESULTS

### Drop if:
- no usable URL
- irrelevant to scope
- navigation/homepage only
- malformed data
- empty or unusable summary
- spam/SEO noise
- duplicate adds no value

### Retain if:
- relevant
- valid URL
- meaningful summary
- region assigned
- trace preserved

### Retain but flag if:
- missing timestamp
- partial duplication
- conflicting data
- incomplete metadata

---

## STEP 7 — DETECT CONFLICTS

### Conflict types
- numeric_claim_conflict
- date_conflict
- entity_conflict
- narrative_conflict
- duplicate_uncertain

### Detection scope
- within dedup groups
- across similar events
- across providers

### Actions
- populate conflicts[]
- set conflict_flag = true
- set overall_status = ok_with_conflicts

### Rule
Do not resolve silently.

---

## STEP 8 — SCORE AND TRIM RESULTS

### Purpose
Limit agent input to high-quality evidence

### Target limits
Per region:
- 2–4 results ideal
- max 5

Cross-region:
- max 2

### Scoring factors
- relevance
- provider rank
- uniqueness
- source completeness
- region alignment
- trace quality

### Rule
Scoring ranks results but does not invent confidence.

---

## STEP 9 — BUILD STRUCTURED PACKAGE

### Package structure
- run_metadata
- retrieval_status
- results
- conflicts
- errors

### Rules
- include only retained results
- include all conflicts
- include provider errors
- enforce schema compliance
- no raw payload leakage

### Status assignment
- ok
- partial
- empty
- failed
- ok_with_conflicts

---

## STEP 10 — PASS TO AGENT

### Injection order
1. system rules
2. task instructions
3. structured retrieval package
4. output instructions

### Agent receives ONLY:
- normalized structured package

### Agent does NOT receive:
- raw provider outputs
- discarded results
- logs
- execution traces

---

## EXECUTION MODEL (FULL — PHASE 6.3a)

Per run:
1. build query bundle
2. run Brave
3. run Baidu
4. normalize all results
5. deduplicate globally
6. filter retained results
7. detect conflicts
8. build package (retrieval_package.json)
9. invoke agent (with VALID_RESULT_IDS injection)
10. agent produces agent_output.txt
11. **Scrubber** runs on agent_output.txt → produces scrubbed_output.txt + scrubber_report.json
12. **Control Layer** checks structural completeness of scrubbed_output.txt
13. **Validator** runs on scrubbed_output.txt + retrieval_package.json → produces validation_result.json (PASS/WARN/FAIL)
14. **Delivery Gate** applies decision matrix and delivers to Lark or blocks

---

## WHAT NOT TO DO

Do NOT:
- inject raw retrieval into prompts
- normalize inside the agent
- let agent choose sources
- filter via prompt instructions
- resolve conflicts in agent layer
- bypass orchestrator

---

## INTERNAL STATUS CHECKPOINTS (LOGGING)

Retrieval phase:
- query_bundle_built
- brave_started
- baidu_started
- brave_completed|failed|timeout
- baidu_completed|failed|timeout
- normalization_completed
- dedup_completed
- filtering_completed
- conflicts_evaluated
- package_built

Agent phase:
- agent_invoked
- agent_completed

Phase 6 validation chain:
- scrubber_started
- scrubber_completed (ids_seen, ids_kept, ids_removed logged)
- control_layer_checked (structural completeness result logged)
- validator_started
- validator_completed (PASS|WARN|FAIL logged)
- delivery_allowed|delivery_blocked

---

## INITIAL POLICY CONSTRAINTS (V1)

### Query
- 2 queries per region
- fixed bundle

### Execution
- parallel providers
- no retries

### Dedup
- exact + strong only

### Filtering
- strict URL + relevance

### Conflict
- flag only, minimal resolution

---

## FINAL PRINCIPLE

All retrieval must be:

- completed BEFORE agent execution
- normalized BEFORE reasoning
- bounded and traceable
- explicitly labeled for failure and conflict

The agent consumes evidence.

It does not create it.

---

END