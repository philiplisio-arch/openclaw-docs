# AGENT INPUT CONTRACT — PHASE 6.3a
OpenClaw Retrieval Orchestration Layer

---
document_id: OPENCLAW-AIC-001
version: updated 2026-05-01 (original: Phase 5.1)
status: LOCKED
---

---

## PURPOSE

Define exactly what the agent receives, what it does not receive, and how it must behave when consuming orchestrated retrieval.

This contract is mandatory.

The agent is a reasoning layer only.

It is NOT a retrieval layer.

---

## CORE RULE

The agent receives ONLY structured retrieval input produced by the Retrieval Orchestrator.

The agent does NOT:
- execute retrieval
- call Brave
- call Baidu
- inspect raw API payloads
- decide whether retrieval should run
- inject new evidence outside orchestrated input

---

## CANONICAL FLOW

Trigger
→ Retrieval Sources
→ Retrieval Orchestrator
→ Structured Retrieval Package
→ Agent
→ Output

---

## AGENT INPUT: ALLOWED FIELDS

The agent may receive ONLY these top-level objects:

1. run_metadata
2. retrieval_status
3. results
4. conflicts

The agent may also receive task/output instructions supplied by the system prompt.

The agent must NOT receive raw retrieval payloads.

---

## WHAT THE AGENT SEES

### 1. run_metadata
The agent may see:
- run_id
- trigger_type
- run_timestamp
- workflow
- report_title
- region_scope
- query_bundle_id

Purpose:
- contextualize the run
- understand intended coverage
- apply output structure correctly

### 2. retrieval_status
The agent may see:
- overall_status
- brave_status
- baidu_status
- dedup_applied
- filtering_applied
- conflict_flag
- notes

Purpose:
- understand retrieval completeness
- detect partial/empty/conflicted states
- adjust certainty level

### 3. results
The agent may see normalized retained retrieval items only.

Each retained result may include:
- result_id
- title
- url
- retrieval_provider
- publisher
- summary
- region
- timestamp
- language
- query
- retrieved_at
- provider_rank
- dedup_group_id
- trace

Purpose:
- provide the full evidence pool for reasoning

### 4. conflicts
The agent may see:
- conflict_id
- type
- description
- affected_result_ids
- status
- resolution_note

Purpose:
- prevent silent fact collapse
- preserve uncertainty where unresolved

---

## WHAT IS HIDDEN FROM THE AGENT

The agent must NOT see:

- raw Brave response bodies
- raw Baidu response bodies
- transport payloads
- HTTP status plumbing
- retry logic
- timeout internals
- raw logs
- secret values
- API keys
- debugging traces not explicitly normalized into the allowed schema
- discarded results
- malformed retrieval results that failed validation

---

## INJECTION FORMAT

Structured retrieval must be injected as a clearly separated input block.

Recommended prompt order:

1. system rules
2. task instructions
3. structured retrieval input
4. output format requirements

Example structure:

SYSTEM RULES
...
TASK
...
STRUCTURED RETRIEVAL INPUT
<normalized package>
OUTPUT FORMAT
...

Hard rule:
Structured retrieval input must remain separate from instruction text.

No raw search dump may be appended directly into freeform prompt text.

---

## AGENT PROHIBITIONS

The agent must NOT:

1. Perform retrieval
2. Invent a source
3. Invent a URL
4. Invent a publisher
5. Invent a timestamp
6. Use sources not present in retained results as evidence
7. Treat “sources consulted” as equivalent to retained evidence
8. Smooth over unresolved conflicts as though they are settled facts
9. Present partial retrieval as if retrieval were complete
10. Introduce numeric claims not supported by retained results
11. Mutate facts across sections
12. Merge duplicate/near-duplicate records unless already resolved by orchestrator
13. Resolve unresolved conflicts silently

---

## EVIDENCE USAGE RULE

Every substantive factual claim in agent output must map to one or more retained result_ids.

The agent may synthesize across retained results.

The agent may NOT use:
- non-retained sources
- “consulted sources” lists
- general background assumptions
- inferred URLs
- unstated numeric details

Retained results are the only evidence base.

---

## FACT CONSISTENCY RULE

If the same fact appears in multiple output sections, the agent must preserve the same value across sections unless:
- the orchestrator has explicitly preserved multiple conflicting values
- the conflict is surfaced clearly as unresolved uncertainty

The agent must not output one number in Executive Take and a different number in a region section unless the conflict is explicitly disclosed.

---

## BEHAVIOR BY RETRIEVAL STATE

### A. overall_status = ok
Agent behavior:
- generate full output
- use retained results normally
- maintain evidence discipline
- no extra caveat required beyond normal precision

### B. overall_status = ok_with_conflicts
Agent behavior:
- generate output
- do not silently collapse conflicting facts
- prefer resolved conflicts only if conflict status says:
  - resolved_by_rule
  - resolved_by_priority
- if unresolved:
  - either avoid the disputed detail
  - or state uncertainty explicitly

### C. overall_status = partial
Agent behavior:
- generate output from surviving retained evidence only
- reduce confidence where coverage may be incomplete
- do not imply full source completeness
- do not compensate by inventing bridging narrative

### D. overall_status = empty
Agent behavior:
- enter low-signal mode
- do not force themes
- do not fabricate developments
- use the approved “no significant new developments” style where appropriate

### E. overall_status = failed
Agent behavior:
- do not behave as if evidence exists
- output must reflect retrieval failure state if the workflow is designed to continue
- no substantive analytical claims may be made without retained evidence

---

## LOW-SIGNAL RULE

When retrieval is empty, too thin, or operationally degraded:

- reduce claims
- reduce synthesis intensity
- avoid narrative overreach
- avoid pattern-forcing
- avoid “filling the silence”

No significant development is preferable to a fabricated development.

---

## CONFLICT RULE

If a conflict is marked unresolved:
- the agent must preserve uncertainty
- the agent must not choose one side silently
- the agent may either:
  - omit the disputed numeric/detail claim
  - or mention that reports differ

If a conflict is resolved by orchestrator:
- the agent may use the resolved value
- but must not re-open the conflict on its own

---

## REGION RULE

The agent must use orchestrator-assigned region values.

The agent must NOT reclassify results freely.

If a retained result is marked:
- United States
- Europe
- Middle East
- Cross-region
- Unknown

the agent must honor that classification when building sections.

Cross-region items may be used in synthesis layers without being forced into a single regional bucket.

---

## OUTPUT CONSTRUCTION RULE

Executive Take, Advisory Layer, LinkedIn Draft, and regional sections must all be generated from the SAME retained result pool.

The agent must NOT:
- use one evidence pool for Executive Take
- and a different mutated fact set for regional sections

All layers must remain anchored to the same orchestrated package.

---

## TRACEABILITY RULE

Every output claim must be traceable back to one or more result_ids, and through them to retrieval_provider + publisher + url.

**As of Phase 6.3a, result_ids MUST be exposed in final output** using locked citation syntax:
- Claims: `[result_ids: res_xxxxxxxx, ...]`
- Advisory: `[based_on: res_xxxxxxxx, ...]`

The agent must select only from VALID_RESULT_IDS provided in the agent input. It must not generate, infer, mutate, or fabricate result_ids.

Scrubber will remove any invalid IDs. Validator will confirm all retained IDs map to retrieval_package entries.

---

## LEGACY TRANSITION RULE

This rule applied during transition to orchestrated retrieval in Phase 5. Orchestrated retrieval is now fully implemented.

Allowed temporary fallback values (still accepted if metadata is incomplete):
- retrieval_provider = unknown
- query = unknown
- provider_rank = null

All retained results must have explicit provider traceability. If fields are missing, they must be labeled as incomplete in retrieval_status — the agent must not assume completeness.

---

## FINAL OPERATING PRINCIPLE

The agent is an interpreter of structured evidence.

It is NOT:
- a search engine
- a retrieval router
- a source selector
- a conflict resolver of first resort

Retrieval discipline must be enforced before the agent runs.

---

# PHASE 6.3 LOCKED OUTPUT FORMAT

## Purpose

Convert agent citation behavior from freeform result_id generation into constrained result_id selection.

The agent may write analysis, but citation behavior must be governed by a locked schema.

---

## Core Rule

The agent MUST only use result_ids provided in VALID_RESULT_IDS.

Any result_id not appearing in VALID_RESULT_IDS is invalid.

The agent must treat citation as a selection task, not a generation task.

---

## Required Agent Input Section

The generated agent input must include:

```
VALID_RESULT_IDS
- res_xxxxxxxx
- res_yyyyyyyy
- res_zzzzzzzz
```

Rules:
- IDs must be extracted from retrieval_package.results[].result_id
- The list must be generated before agent execution
- The agent must not create IDs outside this list
- The agent must not alter ID strings

---

## Locked Report Structure

The agent MUST output exactly these sections:

1. EXECUTIVE TAKE
2. ADVISORY LAYER
3. LINKEDIN DRAFT
4. REGIONAL SOURCE LIST

No extra sections are allowed unless explicitly approved in a later phase.

---

## Executive Take Format

```
EXECUTIVE TAKE
- Claim sentence. [result_ids: res_xxxxxxxx]
- Claim sentence. [result_ids: res_xxxxxxxx, res_yyyyyyyy]
- Claim sentence. [result_ids: res_xxxxxxxx]
```

Rules:
- 2–4 bullets
- Each bullet must contain at least one valid result_id
- Prefer 1–2 result_ids per bullet
- Maximum 3 result_ids per bullet unless absolutely necessary
- No unsupported factual claims
- No publisher/date citations inside claim bullets

---

## Advisory Layer Format

```
ADVISORY LAYER
- Advisory implication sentence. [based_on: res_xxxxxxxx]
- Advisory implication sentence. [based_on: res_xxxxxxxx, res_yyyyyyyy]
- Advisory implication sentence. [based_on: res_xxxxxxxx]
```

Rules:
- 3–5 bullets
- Use key exactly: based_on
- Every advisory must map to evidence
- Advisory language must be framed as implication, not fact creation
- Do not introduce new factual claims unless supported by listed IDs

---

## LinkedIn Draft Format

```
LINKEDIN DRAFT
Plain-language summary paragraph.
```

Rules:
- No result_id citations required
- No new facts beyond Executive Take / Advisory Layer
- No specific claims not already supported above
- No publisher/date citations
- No invented examples

---

## Regional Source List Format

```
REGIONAL SOURCE LIST
United States
- Title | Publisher | result_id: res_xxxxxxxx
Europe
- Title | Publisher | result_id: res_xxxxxxxx
Middle East
- Title | Publisher | result_id: res_xxxxxxxx
```

Rules:
- Only list retained sources from retrieval_package
- Each listed source must use one valid result_id
- Do not list sources not used in the report unless allowed by retrieval_package
- Do not invent publisher names

---

## Valid Citation Syntax

Allowed:
```
[result_ids: res_xxxxxxxx]
[result_ids: res_xxxxxxxx, res_yyyyyyyy]
[based_on: res_xxxxxxxx]
[based_on: res_xxxxxxxx, res_yyyyyyyy]
```

Not allowed:
```
(result_id: res_xxxxxxxx)
(result_id: res_xxxxxxxx, result_id: res_yyyyyyyy)
[Source: Reuters, 2026-05-01]
Reuters reported that...
Any publisher/date citation format inside core claim bullets
```

---

## Citation Density Rule

Use the minimum evidence needed.

Preferred:
- 1 result_id for one-source claim
- 2 result_ids for cross-source synthesis
- 3 result_ids maximum for complex synthesis

More citations are not better.
Valid citations are better.
Citation padding is prohibited.

---

## Failure Behavior

If evidence is insufficient, write:

```
- No sufficiently supported claim available for this region.
```

Do NOT compensate by:
- guessing
- generalizing
- inventing IDs
- using old citations
- using publisher/date fallback
- citing unavailable evidence

---

## Validator Expectation

Validator should accept only:
- [result_ids: ...]
- [based_on: ...]

Validator should reject or warn on:
- fabricated IDs
- unsupported IDs
- repeated result_id groups
- publisher/date citation format
- uncited hard factual claims in Executive Take
- Advisory claims without based_on evidence

---

## Scrubber Expectation

Scrubber should:

1. Extract IDs only from:
   - [result_ids: ...]
   - [based_on: ...]
2. Remove IDs not present in retrieval_package
3. Preserve groups with at least one valid ID
4. Flag groups with zero valid IDs as unsupported
5. Return:
   - citation_groups_seen
   - ids_seen
   - ids_kept
   - ids_removed
   - unsupported_groups

---

## Success Criteria

This contract is successful when:
- Agent uses locked citation syntax
- All cited IDs are parseable
- Invalid IDs are removable by scrubber
- Validator can deterministically check every claim
- PASS/WARN/FAIL behavior remains stable
- Two consecutive reports deliver successfully
- No fabricated citation reaches Lark

---

## Final Principle

The model may draft language.
The system owns evidence.
Citations must be selected, not generated.

---

END