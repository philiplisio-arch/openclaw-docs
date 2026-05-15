# AGENT INPUT CONTRACT — PHASE 6.8
OpenClaw Retrieval Orchestration Layer

---
document_id: OPENCLAW-AIC-001
version: v1.0
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
→ Resolver (resolve_source_numbers.py)
→ Scrubber
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

Every output claim must be traceable back to one or more source numbers, which map to result_ids, and through them to retrieval_provider + publisher + url.

**As of Phase 6.8, the agent cites by source number** using locked citation syntax:
- Claims: `[source_numbers: 1]` or `[source_numbers: 1, 2]`
- Advisory: `[based_on: 1]` or `[based_on: 1, 2]`

The agent must select only from the numbered VALID_SOURCES list provided in the agent input. It must not generate, infer, mutate, or fabricate source numbers outside that list.

After agent execution, `resolve_source_numbers.py` maps source numbers to result_ids before the scrubber runs. The agent does NOT write result_ids directly — that mapping is owned by the resolver.

Scrubber will remove any result_ids that do not exist in retrieval_package after resolution. Validator will confirm all retained IDs map to retrieval_package entries.

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

# PHASE 6.8 LOCKED OUTPUT FORMAT

## Purpose

Define the locked agent output format using numbered-source citation architecture
(Phase 6.8). The agent cites by source number from a numbered VALID_SOURCES list;
the Resolver maps source numbers to result_ids before the Scrubber runs.

The agent may write analysis, but citation behavior must be governed by a locked schema.

---

## Core Rule

The agent MUST only use result_ids provided in VALID_RESULT_IDS.

Any result_id not appearing in VALID_RESULT_IDS is invalid.

The agent must treat citation as a selection task, not a generation task.

---

## Required Agent Input Section

The generated agent input must include a numbered VALID_SOURCES list:

```
VALID_SOURCES
1. Title — Publisher (Date)
2. Title — Publisher (Date)
3. Title — Publisher (Date)
```

Rules:
- Source numbers are assigned sequentially from retrieval_package.results[]
- The numbered list must be generated before agent execution by build_agent_input_slim.py
- The agent must not cite source numbers outside the provided list
- The agent must not alter source numbers or invent intermediate values
- The resolver (resolve_source_numbers.py) uses this same numbered list to map source numbers → result_ids after agent execution

---

## Locked Report Structure

The agent MUST output exactly these sections:

1. EXECUTIVE TAKE
2. ADVISORY LAYER
3. LINKEDIN DRAFT
4. REGIONAL SOURCE LIST
5. CONFLICTS *(conditional — omit entirely if no conflicts detected)*

Phase 6.5 added section 5. All other sections remain required.

---

## Executive Take Format

```
EXECUTIVE TAKE
- Claim sentence. [source_numbers: 1]
- Claim sentence. [source_numbers: 1, 2]
- Claim sentence. [source_numbers: 3]
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
- Advisory implication sentence. [based_on: 1]
- Advisory implication sentence. [based_on: 1, 2]
- Advisory implication sentence. [based_on: 3]
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
- Title | Publisher | source_number: 1
Europe
- Title | Publisher | source_number: 2
Middle East
- Title | Publisher | source_number: 3
```

Note: Source numbers in the Regional Source List are resolved to result_ids by the resolver before scrubbing.

Rules:
- Only list retained sources from retrieval_package
- Each listed source must use one valid result_id
- Do not list sources not used in the report unless allowed by retrieval_package
- Do not invent publisher names

---

## Conflicts Section Format *(Phase 6.5)*

```
CONFLICTS
[TYPE:FACTUAL|SEVERITY:HIGH] Topic: <brief topic>. Claim A (result_id: res_xxxxxxxx): <claim>. Claim B (result_id: res_yyyyyyyy): <claim>.
[TYPE:DIRECTIONAL|SEVERITY:MEDIUM] Topic: <brief topic>. Source A: <direction>. Source B: <direction>.
[TYPE:NUMERIC|SEVERITY:LOW] Topic: <brief topic>. Source A: <number/stat>. Source B: <number/stat>.
```

Rules:
- Section header must be the exact string `CONFLICTS` on a standalone line
- Omit the section entirely if no conflicts are detected — do not output an empty CONFLICTS section
- Only report genuine factual contradictions between retained sources
- Do not report differences in framing, emphasis, or analytical interpretation
- Each line must begin with `[TYPE:` — no freeform text in this section
- Conflict type definitions:
  - `FACTUAL` — sources contradict on whether an event occurred, who acted, or what was decided
  - `DIRECTIONAL` — sources report opposite trends or outcomes for the same event
  - `NUMERIC` — sources report different numbers for the same metric
- Conflict lines are extracted by the scrubber and routed to conflict_log.json; they are not
  part of the citation-validated body and must not contain citation syntax outside this section

---

## Valid Citation Syntax

Agent output (before resolver):
```
[source_numbers: 1]
[source_numbers: 1, 2]
[based_on: 1]
[based_on: 1, 2]
```

Post-resolver (scrubber input):
```
[result_ids: res_xxxxxxxx]
[result_ids: res_xxxxxxxx, res_yyyyyyyy]
[based_on: res_xxxxxxxx]
[based_on: res_xxxxxxxx, res_yyyyyyyy]
```

Not allowed in agent output:
```
[result_ids: res_xxxxxxxx]   ← agent must not write result_ids directly
(result_id: res_xxxxxxxx)
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

By the time the validator runs, source numbers have been resolved to result_ids by the resolver, and invalid IDs have been removed by the scrubber. The validator operates on scrubbed_output.txt which contains only [result_ids: ...] and [based_on: ...] format.

Validator should accept only:
- [result_ids: ...]
- [based_on: ...]

Validator should reject or warn on:
- fabricated IDs (not present in retrieval_package)
- unsupported IDs
- repeated result_id groups
- publisher/date citation format
- uncited hard factual claims in Executive Take
- Advisory claims without based_on evidence

---

## Scrubber Expectation

The resolver (resolve_source_numbers.py) runs BEFORE the scrubber. By the time the scrubber receives input, all [source_numbers: N] and [based_on: N] citations have been converted to [result_ids: res_xxx] and [based_on: res_xxx] format. The scrubber operates on resolved result_ids only.

Scrubber should:

1. Extract IDs only from:
   - [result_ids: ...]
   - [based_on: ...]
2. Remove IDs not present in retrieval_package
3. Preserve groups with at least one valid ID
4. Flag groups with zero valid IDs as unsupported
5. Remove bullets with no valid citation remaining after ID removal
6. Extract CONFLICTS section (if present) before citation scrubbing — conflicts block
   must not be processed as body text
7. Write conflict_log.json per run (conflict_count=0 when no section found)
8. Return:
   - citation_groups_seen
   - ids_seen
   - ids_kept
   - ids_removed
   - unsupported_groups
   - uncited_claims_removed
   - conflicts_extracted
   - conflict_count

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

---

## PHASE D FORWARD NOTE

This contract governs agent input and output format through Phase C.

Phase D (Editorial Quality & Product Transformation) will introduce output format changes — including revised section structure, naming conventions, and the "China Exposure Brief" product format. Any changes to this contract required by Phase D will be implemented as a formal update with operator approval, per Hard Safety Rule R-02.

No Phase D changes may be applied to this contract prior to Phase C gate closure and explicit operator instruction.

---

*OPENCLAW-AIC-001 | Version v1.0 | Last updated: 2026-05-14 | Status: LOCKED*

*v1.0 changes (2026-05-14): Version format standardised. Phase D forward note added. Content unchanged from Phase 6.8 implementation.*