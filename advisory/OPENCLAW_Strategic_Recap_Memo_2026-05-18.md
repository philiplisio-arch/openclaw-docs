---
document_id: OPENCLAW-RECAP-001
date: 2026-05-18
status: REFERENCE ONLY — no system changes; no phase instructions
classification: Strategic discussion memo — operator-reviewed and approved
prepared_by: Claude CoWork
---

# OPENCLAW — STRATEGIC RECAP MEMO (REVISED)
## Phase-by-Phase Project History & Forward Roadmap

**Date:** 2026-05-18 (revised per operator feedback)
**Prepared by:** Claude CoWork
**Status:** REFERENCE ONLY — no system documents modified; no phase instructions issued
**Note:** Revised per operator feedback: Document Intelligence elevated as core bridge layer; Content Intelligence formalised as standing capability; AE Exoskeleton elevated to core product logic; status language tightened.

---

## CORE PRODUCT LOGIC — THE AE EXOSKELETON

Before the phase history: the central product logic that should inform
how every phase is evaluated.

OpenClaw's primary value proposition is not delivering intelligence to
senior partners. It is delivering intelligence through junior staff.

The target beneficiary is the Account Executive at a PR or public affairs
firm — the entry-level professional who currently spends a
disproportionate amount of time on monitoring, link collection, recap
writing, and client update preparation. OpenClaw functions as a
behind-the-scenes force multiplier: an AE with 18 months of experience
walks into a client conversation armed with the intelligence substrate
of a seasoned senior advisor.

This reframes the commercial argument. Rather than selling "better
intelligence" to senior partners, OpenClaw sells leverage to firm
leadership — the ability to serve more clients, handle more complexity,
and retain institutional knowledge that would otherwise walk out the door
when AEs churn. The intelligence lives in OpenClaw, not in the heads of
departing staff.

This is not speculative positioning. It is the core product logic that
should govern how Phase D output is designed, how the pilot client
relationship is structured, and how subsequent capability layers are
sequenced and prioritised.

---

## SYSTEM ARCHITECTURE VISION — THE FIVE-LAYER MODEL

The full system, understood correctly, is not a monitoring pipeline with
memory bolted on later. It is a five-layer intelligence architecture
where each layer enables the next:

```
Layer 1 — MONITORING
The current pipeline. Daily retrieval, citation-controlled output,
validator-gated delivery. Produces verified, structured intelligence
from live sources. This layer is operational.

Layer 2 — CONTENT INTELLIGENCE
A permanent, standing capability for turning system output into
client-grade advisory. Not a one-time editorial fix — a structured
process that governs output quality continuously. Introduced in Phase D.
This is what makes the monitoring output usable by an AE without
significant manual transformation.

Layer 3 — DOCUMENT INTELLIGENCE
The bridge between monitoring and memory. Ingestion of verified briefs,
curated documents, and structured research into a traceable, retrievable
corpus. Passage-level citation enforcement, document scrubber and
validator. This is not an optional extension — it is the layer that
makes pattern and query capabilities possible. Without it, the memory
layer has nothing structured to draw from.

Layer 4 — MEMORY
Accumulated intelligence across time. Brain Lite (current) is the
first step: a 7-day operational digest providing short-term context.
Brain Medium extends this to entity tracking. Brain Full activates the
full corpus and entity architecture built on the Document Intelligence
layer. The memory layer compounds in value the longer the system runs.

Layer 5 — SUPERPOWER / QUERY LAYER
On-demand brief generation triggered by a specific question rather than
a schedule. Pulls from the corpus and entity layers built beneath it.
The brief format holds in both scheduled and query modes — the same
trust architecture, pointed at a specific question. This is what
transforms OpenClaw from a daily monitoring product into a decision-
support platform capable of answering any client question in real time.
```

The sequencing of these layers is not arbitrary. Each one is a
prerequisite for the next. The implication for roadmap prioritisation:
Document Intelligence must be treated as a foundational investment, not
a deferred lab exercise, because it is the layer that makes Layers 4
and 5 credible and commercially viable.

---

## PHASES 1–3 | THE PROTOTYPE BUILD
*Completed: ~March 28, 2026*

The project started as a solo-operator experiment: build a China-focused
PR intelligence engine that could run daily and produce advisory-quality
output automatically.

Phase 1 (Pipeline Layer) established the basic execution chain: an AI
agent generated content, a Flask relay formatted it, and it landed in
Lark. Cron automation made it daily.

Phase 2 (Signal Layer) added structured regional intelligence — US,
Europe, Middle East — with two key developments per region, one
implication, and evidence-backed source lists.

Phase 3 (Enrichment Layer) layered the interpretive outputs on top:
Executive Take, Advisory Layer, and a LinkedIn Draft. The hard rule:
Phase 3 enrichment drew only from Phase 2 signal output. No new retrieval.

By end of Phase 3, the system was running daily and producing recognisable
advisory-format output. The Foundation Doc at this stage declared it "not
a prototype" and "commercially usable." That assessment was directionally
correct but premature — citation integrity had not yet been addressed,
and output quality had not been tested against a client-grade standard.

---

## PHASE 4 | CONTROL LAYER
*Completed: before Phase 5*

Transition from terminal-dependent system to one a non-technical operator
could run. Design model: ChatGPT as control interface → OpenClaw as
execution engine.

The five stages: chat-based control, trigger/workflow stabilisation,
retrieval reliability + Baidu integration, messaging-based workflow
control, and channel integration (Lark bot + WeChat). The key milestone
in Stage 4.3 was integrating Baidu as a second retrieval provider to
surface Chinese-language sources — a theme that has run through the
project ever since.

---

## PHASE 5 | INFRASTRUCTURE LAYER
*Completed: before Phase 6*

Built the VPS-based production infrastructure the current system runs on.
The key directories — /root/openclaw_phase5/ (orchestrator, data) and
/root/openclaw_phase6/ (validation artifacts) — trace back to this phase.
Retrieval pipeline, orchestration layer, and VPS cron scheduling all
established here.

---

## PHASE 6 — THE SOFT LAYER (6.1–6.8)
*Completed: 2026-05-07*

The most consequential engineering phase to date. The problem it
addressed: the agent was fabricating citations at a rate of approximately
48%. The output looked like intelligence; it wasn't verifiable. Phase 6
fixed that completely.

The architecture built across 6.1–6.8:

- **Locked citation schema** — the agent cites source numbers from a numbered VALID_SOURCES list. Citation becomes a selection task, not a generation task.
- **Resolver** — resolve_source_numbers.py maps source numbers to verified result_ids after agent execution.
- **Scrubber** — deterministic cleanup: strips invalid IDs, removes bullets with no surviving citation, rewrites citation groups. Runs post-resolver.
- **Validator** — final authority. Confirms every result_id in scrubbed output exists in the retrieval package. Produces PASS / WARN / FAIL.
- **Delivery Gate** — PASS and WARN deliver; FAIL blocks.
- **Conflict detection** — three-tier classification (⚠ factual / ↔ directional / ~ numeric) extracted per run.
- **Citation substitution** — result_id tokens swapped for human-readable publisher/date strings in Lark delivery. Full traceability retained in logs.

Phase 6.7 added uncited claim removal: any bullet with no verified
citation is stripped before delivery. If the Executive Take runs empty,
delivery is blocked.

Phase 6.8 completed the numbered-source architecture. Fabrication rate
confirmed at 0% across the validated run set. This is the gate that made
everything downstream credible.

Phases 6.9–6.11 were designed but never required — the 6.8 architecture
was sufficiently robust to skip them.

---

## PHASE 7 ENTRY — PHASE A | TRUST GATE
*2026-05-06 to 2026-05-11 — CLOSED*

Gate requirement: five consecutive clean deliveries with zero fabrication.
Runs confirmed: 2026-05-06, 05-07, 05-08, 05-09, 05-10.
Gate closed by operator: 2026-05-11.

---

## PHASE 7 ENTRY — PHASE B | INFRASTRUCTURE & ACCESS
*Completed 2026-05-09 — gate closed 2026-05-11*

Five deliverables completed in a single session:

- **Step 2A** — VPS documentation repository. /root/openclaw_docs/ and /root/openclaw_cowork/ initialised with Git. 21 system documents migrated. Baseline commit made and rollback verified.
- **Step 2B** — CoWork access model. openclaw_cowork system user (uid=999) created. Permission boundary enforced structurally: read to logs and validation artifacts; write to /root/openclaw_cowork/ only. No write to production scripts, cron, or secrets. All 7 verification tests passed.
- **Step 3** — Client config schema. client_config_china_monitor_001.yaml approved. Configuration model for first client: China Monitor.
- **Step 4** — CoWork daily report template. 11-field post-run report format approved.
- **Step 5** — Multi-client test harness design specification approved.

---

## PHASE 7 ENTRY — PHASE C | BRAIN LITE & CLIENT CONFIG IMPLEMENTATION
*Active as of 2026-05-18 — authorized 2026-05-11*

**Brain Lite (Step 6) — complete pending digest update**

The 14-field run_summary.json schema (locked) captures per-run metadata
after each delivery. build_brain_digest.py compresses the last 7 runs
into a digest injected into the agent input at run time (token-budgeted
at 1,200 tokens).

- Deployment: 2026-05-11.
- 5-run stability gate: Runs 1–5 confirmed (May 11–15). No pipeline disruption. brain_context: true activated 2026-05-15.
- Brain Lite Injection Runs 1–3 confirmed (May 16, 17, 18). All clean.
- Resolver on Run 3 (2026-05-18): source_numbers_dropped=0, out_of_range_numbers=0.
- Digest rebuild (to incorporate Injection Runs 1–3) is next queued action before Step 7 implementation begins.

**Client Config Loader (Step 7) — in progress**

OPENCLAW-SPEC-CONFIG-LOADER-001 v1.1 operator-approved 2026-05-18.
Step 7 unblocked. Next: hardcoded-filename audit via Claude Code across
the pipeline codebase — classifying all filenames requiring namespacing
under client_id — before implementation proceeds. Classification table
submitted for operator approval before any implementation begins.

Phase C closes when: hardcoded-filename audit approved, config loader
implemented, synthetic second client end-to-end test complete, and
cross-contamination verification passed.

---

## PHASE D | INTRODUCING THE CONTENT INTELLIGENCE LAYER
*Planned — begins after Phase C closes (~2026-05-28 est.)*
*Status: Direction operator-approved (ADV-012, 2026-05-14); implementation scope subject to operator approval at each step*

This phase is correctly understood not as a one-time editorial fix but
as the introduction of a permanent, standing Content Intelligence
capability — the structured process by which system output is
continuously transformed into client-grade advisory.

Content Intelligence is Layer 2 in the five-layer architecture. It is
what makes monitoring output usable by an AE without significant manual
transformation, and it is what the pilot client relationship depends on.

The diagnosis that makes this phase necessary: the pipeline is
infrastructure-valid but the output is not yet client-grade. It reads
like a lightly summarised geopolitical news digest. The target:

```
FROM: "Daily China monitoring brief"

TO:   "Daily China Exposure Brief — executive intelligence on policy,
       trade, geopolitical, regulatory, and market developments
       affecting multinational companies."
```

The client value standard:

> Could a senior PR partner read this in three minutes and immediately know what to tell a client?

**Five-step sequence:**

| Step | Description | Est. Duration |
|------|-------------|---------------|
| D.1 | Brief Audit — 5 consecutive delivered briefs reviewed against the client-grade standard. Prioritised issue list submitted for operator approval before D.2 begins. | 1 session |
| D.2 | Agent Prompt Redesign — targeted rewrite based on D.1 findings: advisory framing rules, Chinese-language source utilisation, source authority floor, LinkedIn Draft replacement. Operator approves before deployment. | 1–2 sessions |
| D.3 | Controlled Test Sequence — 5 consecutive runs under revised prompt. Full Analysis Contract applied to each. Go/no-go gate: D.1 failure patterns resolved? | 1 week / 5 cron runs |
| D.4 | Format Validation — brief format reviewed against PR industry expectations. May include external PR professional input. Approved format specification locked as system document. | 1 session + external review |
| D.5 | Pilot Readiness Sign-Off — final editorial quality gate. Brief meets approved standard → Phase D closes → paid pilot gate opens. | 1 session |

**Target output structure:**

```
1. Executive Signal Board
2. What Changed in the Last 24 Hours
   (NEW TODAY / CONTINUING / BACKGROUND / WATCH NEXT)
3. Client Exposure Map
   (Legal/Compliance / Public Affairs / Supply Chain / Treasury/Finance)
4. Advisory Layer
5. Watchlist — Next 72 Hours
6. Source Pack (structured table: source, date, type, signal, link)
7. Optional External Messaging Note
```

**Standing capability note:** Phase D introduces the Content Intelligence
layer for the first time. After the pilot, this layer continues as a
standing operational capability — not a project phase that closes and is
done. Governance of the output standard, ongoing prompt calibration, and
brief quality review all belong within it indefinitely.

**Estimated timeline:**

| Milestone | Estimated Date |
|-----------|----------------|
| Phase C close | ~2026-05-28 |
| D.1 Brief Audit | ~2026-05-30 |
| D.2 Prompt Redesign | ~2026-06-04 |
| D.3 Test Sequence | ~2026-06-11 |
| D.4 Format Validation | ~2026-06-18 |
| D.5 Pilot Readiness | ~2026-06-25 |
| **Paid pilot gate open** | **Late June 2026** |

---

## STEP 8 | CONTROLLED PILOT — FIRST PAID CLIENT
*Target: ~Month 3 from May 2026*

One real client. China-focused monitoring brief. Operator review gate on
every delivery for the first two weeks or ten deliveries. Ten consecutive
clean external deliveries with client confirmation = first revenue.

Content Intelligence layer active throughout. The pilot is not just a
system test — it is the first real-world stress test of the AE exoskeleton
value proposition. Client feedback from the pilot should feed back into
the Content Intelligence layer continuously.

---

## DOCUMENT INTELLIGENCE | CORE BRIDGE LAYER
*Planned — development begins after Step 8 stable*
*Status: Direction under active development; implementation scope to be formally specified before any build begins*

Document Intelligence is Layer 3 in the five-layer architecture. It is
correctly understood not as a deferred optional lab but as the bridge
layer that makes Layers 4 and 5 possible.

Without Document Intelligence, the Memory layer has no structured,
citation-traceable corpus to draw from. Without it, the Query layer
cannot retrieve source-backed chunks that preserve the trust chain.
The entire Superpower capability depends on this layer being built
correctly.

**What Document Intelligence builds:**

*Corpus Layer* — every verified brief and its underlying sources stored
as structured documents with full metadata: date, topics, companies,
source types, confidence levels, verification status. The corpus does
not summarise — it stores. Query retrieval pulls source-backed chunks
directly. The trust chain from original verified source is preserved
through the accumulation process.

*Entity Layer* — structured profiles for companies, regulatory bodies,
key actors, sectors, and events — built by processing the corpus over
time. Enables efficient profile and exposure query retrieval without
scanning the full corpus. Introduces no new claims — organises existing
verified ones.

*Document scrubber and validator* — passage-level citation enforcement,
mirroring the pipeline architecture applied to monitoring output.
Internal quality gate: not client-facing until ten consecutive zero-
uncited-claim internal test reports are confirmed.

*Corpus seeding* — the corpus does not need to start from zero.
Historical briefs, prior research, and curated external material can be
ingested at launch using a trust tiering model:

| Tier | Source | Trust Handling |
|------|--------|----------------|
| 1 | Pipeline intelligence | Full provenance chain, highest trust, primary citation |
| 2 | Prior OpenClaw briefs | High trust, tagged as pre-pipeline |
| 3 | Curated external research | Medium trust, tagged as externally derived |
| 4 | General historical documents | Background context only, clearly flagged |

**Architectural coupling note:** The seeding effort and the corpus
architecture are a single design decision. The corpus layer must be
specified before seeding can be planned, which means architecture
planning is a near-term priority even if implementation is longer horizon.

---

## MEMORY LAYER — BRAIN DEVELOPMENT ROADMAP
*Runs in parallel with Document Intelligence build*

- **Brain Lite (operational)** — 7-day digest, 14-field run metadata, short-term context injection. Schema locked. Currently in injection phase.
- **Brain Medium (next horizon)** — Extended window. Beginning of entity tracking: structured profiles for frequently-seen companies and regulatory bodies, grounded in verified pipeline output. Formal specification required before build begins.
- **Brain Full (longer horizon)** — Full activation of the corpus and entity layers built by Document Intelligence. Query retrieval operating across both. Requires Document Intelligence to be complete and stable first.

---

## QUERY LAYER — THE SUPERPOWER
*Longer horizon — enabled by Document Intelligence + Brain Full*

On-demand brief generation triggered by a specific question. The brief
format holds in both scheduled and query modes — the same citation-
controlled, scrubbed, validated trust architecture, pointed at a specific
question rather than a daily schedule.

**Two query types:**

*Profile and exposure queries* — "What challenges does Company X face in
the China pharmaceutical market?" Draws on accumulated monitoring of that
company, sector, and regulatory environment over time.

*Precedent and pattern queries* — "What is the effect of releasing an
M&A announcement on a Monday versus a Friday?" Draws on a historical
case library — verified examples with outcomes, framed for PR use.

**Commercial significance:** The longer OpenClaw runs, the richer the
corpus. This creates a compounding advantage for early clients — depth
of historical intelligence they cannot replicate by switching to a
later-arriving competitor — and a meaningful switching cost over time.

---

## FULL PLATFORM
*Target: ~Month 8–10 from May 2026*

Brain Full active. Multi-client scaling. Document Intelligence
client-facing. Query layer operational. Operator dashboard across all
active clients. Commercial launch of OpenClaw as a multi-client
business intelligence platform.

---

## OPEN STRATEGIC QUESTIONS

These questions are identified for consultant engagement — not as
immediate implementation decisions.

1. **Agency enablement vs. end-client model.** Option A (managed intelligence service directly to end clients) and Option B (internal productivity tool sold to PR firms for their AEs) imply different commercial motions, pricing structures, and brand positioning. May need resolution before the pilot client relationship is structured.

2. **China expertise gap.** The product acknowledges this risk but the mitigation remains directional. What is the concrete strategy for source authority, Chinese-language coverage, and editorial credibility in the China domain? This has implications for Phase D prompt design and pilot client selection.

3. **Query interface model.** When an AE issues a query, what is the interaction design? A dedicated interface? A follow-up layer within the brief delivery workflow? An integrated tool within existing PR firm systems?

4. **Minimum viable corpus.** At what point does the Document Intelligence corpus have sufficient depth to make query briefs commercially useful? This determines the sequencing dependency between Document Intelligence and the Query layer, and therefore the realistic timeline for the full platform.

5. **Corpus seeding strategy.** The architecture needs to be specified before seeding can be planned. This is a near-term planning item even if implementation is longer horizon.

---

## STATUS SUMMARY — 2026-05-18

| Layer | Status |
|-------|--------|
| Layer 1 / Monitoring | OPERATIONAL — fabrication rate 0% |
| Layer 2 / Content Intelligence | PHASE D DESIGN APPROVED — build begins after Phase C closes (~2026-05-28) |
| Layer 3 / Document Intelligence | DIRECTION ACTIVE — architecture and specification to be formally scoped; not yet in a formal build phase |
| Layer 4 / Memory | BRAIN LITE OPERATIONAL; Brain Medium and Brain Full pending Document Intelligence |
| Layer 5 / Query Layer | LONGER HORIZON — enabled by Layers 3 & 4 |

| Milestone | Status |
|-----------|--------|
| Phase C | IN PROGRESS — config loader spec approved 2026-05-18; hardcoded-filename audit next |
| Paid pilot gate | Target late June 2026 |
| Full platform | Target Month 8–10 |

The system has gone from a terminal-dependent prototype with 48%
citation fabrication to a VPS-hosted, validator-gated, stateful
intelligence pipeline with 0% fabrication across all post-Phase-6.8
runs. The foundation is credible. The next questions are not whether
the pipeline works — it does — but whether the output meets a client-
grade standard (Phase D) and whether the architecture beneath it is
being built in the right sequence to make the full product vision
realisable (Document Intelligence as core bridge, not deferred lab).

---

*OPENCLAW-RECAP-001 | 2026-05-18 | Claude CoWork*
*REFERENCE ONLY — no system changes; no phase instructions*
*Revised per operator feedback: Document Intelligence elevated as core bridge layer; Content Intelligence formalised as standing capability; AE Exoskeleton elevated to core product logic; status language tightened.*
