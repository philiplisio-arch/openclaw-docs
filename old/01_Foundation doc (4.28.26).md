# OPENCLAW — FOUNDATION DOCUMENT (PHASE 6.3b — LOCKED STATE)

---

## 🎯 PROJECT OBJECTIVE

Build a **trusted, client-grade PR intelligence system** that delivers:

- Verified, retrieval-backed insights
- Zero hallucinated citations
- Deterministic correctness
- Reliable daily delivery
- Full traceability from claim → evidence → source

---

## 🧠 CORE PRINCIPLE

> The system must be **correct by design, not by model behavior**

- The model is **probabilistic**
- The system is **deterministic**

All correctness is enforced by **system layers**, not prompts.

---

## 🏗️ SYSTEM ARCHITECTURE (CURRENT — TRUE STATE)

```text
Trigger (cron / webhook)
    ↓
Retrieval Layer (Brave + Baidu)
    ↓
Retrieval Orchestrator
    ↓
Agent (china_pr_enrichment)
    ↓
Scrubber (Phase 6.3b — HARD GATE)
    ↓
Validator (Phase 6)
    ↓
Control Layer
    ↓
Delivery (Lark)
```

---

## 📦 DATA FLOW

### 1. Retrieval Layer
- Brave: PRIMARY (working)
- Baidu: SECONDARY (currently degraded due to quota)

Outputs:
- Raw provider results

---

### 2. Retrieval Orchestrator

Transforms raw retrieval into structured evidence:

Outputs:
- `retrieval_package.json`
- `agent_input_slim.txt`

Responsibilities:
- Normalize
- Deduplicate
- Filter
- Assign result_id
- Enforce structure

Rule:
> Agent NEVER sees raw retrieval

---

### 3. Agent Layer (LLM)

Consumes:
- Structured retrieval only

Produces:
- EXECUTIVE TAKE
- ADVISORY LAYER
- LINKEDIN DRAFT

Citation format:
```
(result_id: res_xxxxxx)
```

Constraints:
- No retrieval
- No external knowledge
- No manual citations

---

### 4. Scrubber Layer (NEW — Phase 6.3b)

File:
```
/root/openclaw_phase6/validation/scrub_result_ids.py
```

Role:
- Deterministic correction layer
- Removes invalid result_ids
- Rewrites citation groups

Behavior:

| Condition | Action |
|----------|--------|
| Valid IDs present | Keep |
| Invalid IDs | Remove |
| Empty citation group | Replace with `(UNSUPPORTED_RESULT_ID_REMOVED)` |

Exit codes:

- `exit 0` → deliverable
- `exit 1` → BLOCK

Critical rule:
> If unsupported_groups > 0 → SYSTEM MUST NOT DELIVER

---

### 5. Validator Layer (Phase 6)

File:
```
/root/openclaw_phase6/validation/validator.py
```

Role:
- Verifies all citations exist in retrieval_package

Checks:
- result_id exists
- mapping valid
- no fabricated citations

Output:
```
validation_result.json
```

Status:
- PASS → deliver
- WARN → deliver (with warning)
- FAIL → BLOCK

---

### 6. Control Layer

Evaluates:

- structural completeness
- execution integrity

Key principle:
> Execution success ≠ Output validity

---

### 7. Delivery Layer

Condition for delivery:

```
Scrubber PASS
AND
Validator PASS/WARN
AND
Control PASS
```

Else:
→ BLOCK

---

## 🔒 EVIDENCE MODEL (LOCKED)

Allowed:

```
(result_id: res_xxxxxx)
```

Forbidden:
- Publisher names
- URLs
- Dates
- Freeform citations

---

## 🧪 SYSTEM BEHAVIOR MODEL

### Agent
- Probabilistic
- May hallucinate IDs

### Scrubber
- Deterministic correction
- Removes hallucinations

### Validator
- Deterministic enforcement
- Guarantees correctness

---

## 🧠 SYSTEM PHILOSOPHY

```
Model = generator (untrusted)
Scrubber = correction
Validator = enforcement
System = truth engine
```

---

## ✅ CURRENT SYSTEM STATE

```
Phase 1–5: COMPLETE
Phase 6.1: COMPLETE (Validator)
Phase 6.2: COMPLETE (Delivery Gate)
Phase 6.3: COMPLETE (result_id system)
Phase 6.3s: COMPLETE (stabilization)
Phase 6.3b: ACTIVE (scrubber enforcement)
```

---

## 📍 CAPABILITIES (ACHIEVED)

✔ Deterministic citation correctness  
✔ Automatic hallucination removal  
✔ Delivery gating  
✔ Repeatable successful runs  
✔ Full pipeline observability  
✔ No fabricated citations reach output  

---

## ⚠️ KNOWN LIMITATIONS

- Agent still over-generates IDs
- Scrubber required for cleanup
- Baidu degraded (quota)
- Model instability (Issue #33)

---

## 🚫 FAILURE MODES (CONTROLLED)

| Failure | Outcome |
|--------|--------|
| Invalid result_id | Removed |
| Empty citation group | Block |
| Validator FAIL | Block |
| No output | Block |
| Partial retrieval | Allowed |

---

## 📊 SUCCESS CRITERIA (CURRENTLY MET)

✔ Multiple successful runs  
✔ Validator PASS  
✔ Scrubber enforcement working  
✔ Lark delivery confirmed  
✔ No hallucinated citations delivered  

---

## 🚀 NEXT PHASE OPTIONS

### Phase 6.4 — Retrieval Quality
- Improve Baidu
- Improve signal density

### Phase 6.5 — Conflict Handling
- Better contradiction modeling

### Phase 6.6 — Low Signal
- Improve fallback behavior

### Phase 6.7 — Output Quality
- Sharper insights

---

## 🚨 DEVELOPMENT RULES

DO NOT:
- Remove scrubber
- Bypass validator
- Trust model output
- Modify architecture casually

ALWAYS:
- Preserve deterministic layers
- Maintain phase discipline
- Validate before delivery

---

## 🧾 FINAL CONCLUSION

System has evolved from:

```
Prompt-driven AI tool
```

to:

```
Deterministic intelligence system
```

This is the **critical milestone** required for:

- client trust
- production reliability
- scalable expansion

---

END