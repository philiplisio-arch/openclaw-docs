# OPENCLAW — VALIDATOR LAYER SPEC

---
document_id: OPENCLAW-VAL-001
version: v2.0
status: LOCKED — Phase 6.8 complete; spec reflects implemented behavior
---

## PURPOSE

Define the current Validator Layer behavior as of Phase 6.8.

The validator verifies whether agent output is grounded in retained retrieval evidence before delivery.

It extends the Control Layer.

Control Layer = structural validity  
Validator Layer = evidence validity

---

## POSITION IN PIPELINE

Current Phase 6.8 pipeline:

Trigger
→ Retrieval
→ Orchestrator
→ Agent
→ Resolver (resolve_source_numbers.py)
→ Scrubber
→ Control Layer
→ Validator
→ Delivery Gate
→ Lark

---

## CORE PRINCIPLE

No unverified client-facing output.

The validator must answer:

Can each cited source and source-backed claim be traced to retrieval_package.json?

---

## INPUTS

Validator receives ONLY:

1. retrieval_package.json
2. final agent output text

Validator must NOT receive:

- raw provider API responses
- discarded retrieval results
- live web access
- new search results
- agent memory
- external context

---

## NON-GOALS

Validator must NOT:

- rewrite output
- improve wording
- add citations
- replace citations
- perform retrieval
- call Brave
- call Baidu
- ask an LLM to judge plausibility
- invent corrections

Validator only:

- checks
- classifies
- logs
- gates delivery

---

## VALIDATION SCOPE — V1

V1 validates:

1. Source existence
2. Publisher match
3. URL existence
4. Date / timestamp consistency
5. No fabricated citations
6. No source-backed claim referencing missing evidence

**Phase 6.3 Extension:** As of Phase 6.3, validation is primarily result_id-based. The validator confirms that all result_ids cited in scrubbed_output.txt exist in retrieval_package.json. Publisher/URL checks are secondary verification, subordinate to result_id matching.

**Phase 6.8 Extension:** As of Phase 6.8, the agent cites by source number ([source_numbers: N]) rather than by result_id directly. The resolver (resolve_source_numbers.py) maps source numbers to result_ids, and the scrubber removes invalid IDs — both steps run before the validator. By the time the validator receives scrubbed_output.txt, all citations are in resolved result_id format. The validator's role is unchanged: it confirms that all result_ids in scrubbed_output.txt exist in retrieval_package.json.

**Citation format in scrubbed_output.txt (validator input):** `[result_ids: res_xxx]` and `[based_on: res_xxx]` — resolved by the resolver, cleaned by the scrubber.

---

## VALIDATION TARGETS

Validator checks these sections first:

1. EXECUTIVE TAKE
2. ADVISORY LAYER
3. Regional source lists

LinkedIn Draft is checked only for hard factual claims in V1.

---

## SOURCE MATCHING RULES

A citation is valid only if it maps to a retained retrieval result.

Required retained fields:

- result_id
- publisher
- url
- title
- retrieved_at or published_date if available
- region
- query_id

---

## MATCH TYPES

### EXACT MATCH

Valid when:

- publisher matches retained source
- date matches retained source metadata or accepted fallback
- URL exists in retrieval_package

Status:
PASS

---

### ALIAS MATCH

Allowed only for approved aliases.

Examples:

- NYT → New York Times
- WaPo → Washington Post
- Xinhua → english.news.cn / Xinhua

Status:
WARN unless alias table confirms canonical match.

---

### DATE FALLBACK MATCH

Allowed when:

- publisher and URL match
- published date missing
- retrieved_at exists

Status:
WARN

---

### NO MATCH

Invalid when:

- publisher not found
- URL not found
- date impossible
- source not retained
- citation appears invented

Status:
FAIL

---

## CLAIM CHECKING — V1

V1 does not perform full semantic entailment.

It checks whether each source-backed claim has at least one matched citation.

Claim status values:

- matched
- weak_match
- unmatched
- not_checked

Rules:

1. Claims with explicit citations must map to retained results.
2. Claims in EXECUTIVE TAKE must have matched evidence.
3. Claims in ADVISORY LAYER must have matched evidence or be clearly framed as implication.
4. Regional source list items must match retained results.
5. Unsourced hard factual claims in core sections trigger WARN or FAIL depending on severity.

---

## CLASSIFICATION MODEL

Validator returns one of:

- PASS
- WARN
- FAIL

---

## PASS RULES

PASS if:

- all cited sources exist in retrieval_package
- all cited publishers match retained results
- all cited URLs exist or canonical-match
- no fabricated citations detected
- no unmatched cited claims in EXECUTIVE TAKE
- no unmatched cited claims in ADVISORY LAYER
- validation_result.json is written successfully

Delivery:
Allowed

Operator status:
GREEN

---

## WARN RULES

WARN if:

- source exists but publisher alias required
- source exists but date fallback used
- non-core claim has weak evidence mapping
- LinkedIn Draft contains broad synthesis but no fabricated citation
- regional source list has minor metadata mismatch
- validator completes but detects low-risk ambiguity

Delivery:
Allowed with warning

Operator status:
YELLOW

---

## FAIL RULES

FAIL if:

- cited publisher not found in retrieval_package
- cited URL not found in retained results
- citation appears fabricated
- EXECUTIVE TAKE contains unmatched cited claim
- ADVISORY LAYER contains unmatched cited claim
- source list references non-retained source
- retrieval_package.json cannot be read
- agent output cannot be read
- validation_result.json cannot be produced
- validator crashes

Delivery:
Blocked

Operator status:
RED

---

## VALIDATOR OUTPUT

File:

/root/openclaw_phase6/validation/validation_result.json

Required structure:

{
  "run_id": "",
  "validator_version": "phase6_v2_result_id_match",
  "validated_at": "",
  "status": "PASS | WARN | FAIL",
  "severity": "GREEN | YELLOW | RED",
  "input_files": {
    "agent_output": "",
    "retrieval_package": ""
  },
  "summary": {
    "claims_checked": 0,
    "citations_checked": 0,
    "sources_matched": 0,
    "warnings": 0,
    "failures": 0
  },
  "checked_claims": [],
  "matched_sources": [],
  "warnings": [],
  "failures": []
}

---

## FAILURE OBJECT STRUCTURE

Each failure must include:

{
  "type": "",
  "section": "",
  "output_text": "",
  "reason": "",
  "action": "block_delivery"
}

Allowed failure types:

- fabricated_citation
- missing_source
- publisher_mismatch
- url_not_retained
- date_mismatch
- unmatched_claim
- validator_runtime_error
- missing_input_file

---

## WARNING OBJECT STRUCTURE

Each warning must include:

{
  "type": "",
  "section": "",
  "output_text": "",
  "reason": "",
  "action": "deliver_with_warning"
}

Allowed warning types:

- publisher_alias_match
- date_fallback_used
- weak_claim_mapping
- non_core_uncited_synthesis
- metadata_incomplete

---

## LOGGING REQUIREMENTS

Each run must log:

- validator_started
- validator_input_loaded
- validator_sources_indexed
- validator_citations_extracted
- validator_claims_checked
- validator_result_written
- validator_passed OR validator_warned OR validator_failed
- delivery_allowed OR delivery_blocked

Example log lines:

[VALIDATOR][GREEN] PASS — 9 citations checked, 9 matched, 0 warnings, 0 failures

[VALIDATOR][YELLOW] WARN — 9 citations checked, 8 exact, 1 date fallback

[VALIDATOR][RED] FAIL — fabricated citation detected; delivery blocked

---

## DELIVERY GATE INTEGRATION

Delivery decision must use BOTH:

1. Control Layer structural result
2. Validator evidence result

Decision matrix:

CONTROL PASS + VALIDATOR PASS
→ deliver

CONTROL PASS + VALIDATOR WARN
→ deliver with warning

CONTROL PASS + VALIDATOR FAIL
→ block delivery

CONTROL FAIL
→ block delivery regardless of validator status

---

## RELATION TO CONTROL LAYER

The Control Layer already determines whether output is structurally complete.

The Validator Layer determines whether structurally complete output is trustworthy.

Control Layer must run before Validator.

Validator must never replace structural completeness checks.

---

## RELATION TO UNIFIED FAILURE MODEL

For cross-layer failure scenarios involving the Validator (FAIL, WARN, runtime error, missing input), refer to the **Unified Failure Matrix** in `SYS_RETRIEVAL_FAILURE_HANDLING`. That document is the canonical failure reference for the full pipeline. The failure types and delivery outcomes defined here are consistent with and subordinate to that matrix.

---

## RELATION TO ORCHESTRATOR

The orchestrator owns retrieval quality and package construction.

Validator does not change retrieval_package.

Validator only verifies whether agent output used retrieval_package correctly.

---

## RELATION TO AGENT

The agent remains a reasoning layer.

Validator must not be embedded inside the agent.

The agent must not self-certify.

---

## PHASE 6.1 EXIT CRITERIA

Phase 6.1 is complete when:

- validator runs every report
- validation_result.json produced every run
- GREEN / YELLOW / RED visible in logs
- PASS allows delivery
- WARN allows delivery with internal warning
- FAIL blocks Lark delivery
- fake citation test triggers FAIL
- missing source test triggers FAIL
- publisher alias test triggers WARN
- normal report triggers PASS or controlled WARN

---

## TEST CASES

### Test 1 — Clean Output

Input:
All citations match retrieval_package.

Expected:
PASS / GREEN / deliver

---

### Test 2 — Alias Match

Input:
NYT used instead of New York Times.

Expected:
WARN / YELLOW / deliver with warning

---

### Test 3 — Fabricated Source

Input:
Citation references source not in retrieval_package.

Expected:
FAIL / RED / block delivery

---

### Test 4 — Missing URL

Input:
Publisher exists but URL not retained.

Expected:
FAIL / RED / block delivery

---

### Test 5 — Validator Crash

Input:
retrieval_package unreadable.

Expected:
FAIL / RED / block delivery

---

## NON-NEGOTIABLE RULES

1. No output modification
2. No retrieval
3. No LLM judgment in V1
4. No silent pass
5. No fabricated correction
6. No delivery without validator result
7. No validator result = FAIL

---

## FINAL PRINCIPLE

The system may deliver incomplete execution if output is structurally valid.

The system must never deliver untrusted claims if evidence validity fails.

Control protects availability.

Validator protects trust.

END