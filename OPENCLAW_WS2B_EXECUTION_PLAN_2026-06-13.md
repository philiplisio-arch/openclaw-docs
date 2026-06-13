# WS2B Execution Plan — Source Packet Intelligence Mode + Tiered Model Architecture

---
document_id: OPENCLAW_WS2B_EXECUTION_PLAN_2026-06-13
date: 2026-06-13
author: Claude Fable 5 (with operator direction)
status: v1.2 — operator decisions incorporated 2026-06-13; awaiting final implementation approval
scope: items 2 (WS2B build) and 3 (per-stage model structure) from operator direction 2026-06-13
context: WS1/WS2 are being reconfigured as alert mechanisms (advisory content removed, done separately); WS2B becomes the analytical product. Source packets are operator-assembled weekly, almost entirely text files (PDF support minimal, phase-2). Licensing is handled by the operator and out of scope here.
---

## 1. System overview

```
packets/2026-W25/           OPERATOR (manual, weekly)
  manifest.yaml      ─┐
  T1_caixin_*.txt     │  A. INGESTION        watcher/CLI: hash, register, validate
  T1_reuters_*.txt    ├─▶ B. NORMALIZATION   per-format text extraction → UTF-8 + metadata
  T2_yicai_*.txt      │  C. EVIDENCE EXTRACT LLM pass per doc → structured evidence records
  ...                ─┘  D. EVIDENCE STORE   SQLite + JSONL audit trail
                          E. SYNTHESIS        pass 1: theme map · pass 2: executive brief
                          F. VERIFICATION     deterministic citation/alignment gates (ported)
                          G. DELIVERY         labeled Lark delivery (existing relay, clickable cites)
```

Existing assets that port unchanged: citation scrubber + citation cap, alignment checker + alias glossary, deterministic appendix builder, clickable-citation renderer, INTERNAL TEST labeling, traceability archive, Lark relay (append mode), per-client config loader. Estimated reuse: ~70% of the trust layer.

## 2. Components in detail

### A. Ingestion
- Drop folder per ISO week: `/root/openclaw_packets/<client>/<YYYY-Www>/`.
- `manifest.yaml` — one entry per file: `{file, source_name, source_tier (1-3), pub_date, lang, notes}`. A helper CLI (`packet ingest`) pre-fills entries by parsing the filename convention `T<tier>_<source>_<YYYY-MM-DD>_<slug>.txt` and flags gaps for the operator.
- Idempotent: files keyed by SHA-256; re-drops update, never duplicate.
- **Tools: none new** — Python stdlib + PyYAML (already installed).

### B. Normalization
- TXT (dominant case): encoding detection (`charset-normalizer`), whitespace/boilerplate cleanup.
- HTML: `trafilatura` (best-in-class article extraction, pip-installable, offline).
- DOCX: `python-docx` or `mammoth` (pip).
- PDF (minimal per operator): `pdfplumber` for text-layer PDFs; **no OCR in phase 1** (scanned PDFs are flagged `needs_manual_text` in the manifest rather than engineered around).
- Output: `normalized/<doc_id>.txt` + per-doc metadata JSON.

### C. Evidence extraction (LLM stage 1)
- One call per document. Prompt: extract structured records — `claim | statistic | quote | event | entity` — each with `{evidence_id, doc_id, type, text_en, text_orig (verbatim), entities[], date, locator (para index)}`.
- Strict JSON output; schema-validated (`pydantic`); failed parses retried once, then flagged.
- Per-document = parallelizable, retryable, cheap; one bad document never kills the packet.
- **Model: Kimi k2.5 (Moonshot)** — Chinese-native comprehension, already credentialed and live-tested in this stack. Fallback: Gemini 2.5 Flash (also credentialed).

### D. Evidence store
- **SQLite** (single file per client, no server, no new infra; stdlib `sqlite3`): tables `documents`, `evidence`, `entities`, `themes`, plus FTS5 full-text index for retrieval-by-keyword across packets (week-over-week memory comes free).
- JSONL append-only audit copy per packet (consistent with existing traceability philosophy).
- Embeddings are **deliberately deferred** (phase 3 option for cross-week similarity): at packet scale (50–200 evidence records/week) FTS + LLM clustering is sufficient; adding a vector store now is premature infrastructure.

### E. Synthesis (LLM stages 2–3)
- **Pass 1 — theme map** (one call): input = all evidence records (JSON, compact — well under context limits). Output: 4–7 themes, each with member evidence IDs, conflicts noted, materiality rank. Model: Kimi k2.5 or Gemini 2.5 Pro (A/B during pilot).
- **Pass 2 — brief** (one call): input = theme map + selected evidence records only. Output: the report (format below), every claim citing `evidence_id`s. **Model: premium writer — Gemini 2.5 Pro on the existing Google key** (one-line model upgrade from today's Flash); optional later A/B against Claude/GPT if keys are added. Writing is once-weekly: cost is negligible; never economize on this stage.
- Per-stage failover declared in config (primary/fallback model per stage) — directly addresses the 4 provider outages observed 2026-06-12.

### F. Verification (deterministic, no LLM)
- Citation gate: every `evidence_id` cited must exist; cap per claim (existing cap logic).
- Alignment: claim anchors vs the cited evidence's `text_orig`/`text_en` (existing checker; *stronger* here because evidence text is exact, not fetched-page approximate).
- Tier gate: claims marked strong/quantitative require ≥1 Tier-1/2 evidence record; Tier-3-only support downgrades wording or flags the claim.

### G. Reporting & delivery
- Format (advisory-free per operator direction): **1. KEY DEVELOPMENTS** (ranked, synthesized, each with "why it matters" framed as significance—not advice); **2. DATA POINTS** (the week's hard numbers, tabulated); **3. CONFLICTS & UNCERTAINTIES** (where sources disagree); **4. INTERNATIONAL CONTEXT**; deterministic appendix (per-document: source, tier, date, used/unused, clickable link where a URL exists).
- Delivered through the existing labeled Lark path as client `alj_packet_001` (new namespace; zero contact with WS1/WS2 alert paths).

## 3. Model structure (consolidated)

| Stage | Calls/week | Model (primary → fallback) | Why |
|---|---|---|---|
| Normalization | 0 (no LLM) | — | determinism |
| Evidence extraction | 20–60 | **Kimi k2.5 → Gemini Flash** | Chinese-native, cheap, parallel/retryable |
| Theme map | 1 | **Kimi k2.5 ↔ Gemini 2.5 Pro** (pilot A/B) | cross-doc reasoning |
| Brief writing | 1 | **Gemini 2.5 Pro → Kimi k2.5** | best executive English available on current keys |
| Verification | 0 (no LLM) | — | code checks, models write |
| WS1/WS2 alerts | daily | Gemini Flash (current) | speed/cost; signal lists |

## 4. New tools / dependencies (complete list)

- Python packages: `trafilatura`, `python-docx`, `pdfplumber`, `pydantic`, `charset-normalizer`, PyYAML (present). All pip-installable, offline-capable, no services.
- Database: **SQLite (stdlib)** — no server, no ops burden. Revisit Postgres only if multi-operator concurrency ever arrives.
- No new SaaS, no vector DB, no queue/workflow engine in phase 1-2 (cron + the existing run-script pattern suffice at weekly cadence).
- Model credentials: already in place (Google, Moonshot). Optional later: one premium-writer key (Anthropic/OpenAI) for the writing A/B.

## 5. Roadmap & timeline

- **Phase 1 — MVP (week 1):** ingestion + manifest CLI, TXT/HTML normalization, evidence extraction with schema validation, SQLite store, single-pass brief from evidence, citation gates ported, labeled Lark delivery. Exit test: one real operator packet → delivered brief, every claim traceable to a packet document.
- **Phase 2 — analytical product (week 2-3):** two-pass synthesis (theme map), tier gate, conflicts section, premium-writer stage with per-stage failover, DOCX/PDF(text-layer) support, 2–3 weekly packets iterated with operator feedback.
- **Phase 3 — leverage (week 4+):** WS1/WS2 alert output feeds packet curation ("signals worth pulling premium coverage for"), cross-week FTS recall in the theme pass ("what we reported last week; what changed"), optional embeddings, optional writing-model A/B.

## 6. Risks & mitigations

1. **Evidence extraction misses/garbles** → schema validation + per-doc status surfaced in the appendix (label philosophy: failures visible, never silent); operator spot-checks flagged docs.
2. **Operator packet burden** (the product's quality floor) → manifest auto-fill from filenames; WS1/WS2 alerts shortlist what to pull; measure assembly time in phase 2 — if >2 hrs/week, that cost goes to the board explicitly.
3. **Provider outage** (observed 4× on 2026-06-12) → per-stage primary/fallback config; extraction is per-document retryable.
4. **Prompt-size ceilings** (hit twice in current system) → evidence-first design keeps every LLM call small by construction; the theme/writing passes consume compact JSON, never raw documents.
5. **Model behavior drift on upgrade** → every stage output is archived per run (existing traceability pattern); model/version stamped in run metadata.

## 7. Estimated quality improvement vs current WS2

Source authority: step-change (operator-curated Tier-1 vs Baidu portal ceiling — the binding constraint this week's 8 optimization cycles confirmed empirically). Traceability: equal or better (verbatim evidence anchors). Depth: the two-pass evidence-first design is the mechanism the current single-pass system structurally lacks. Candid net: current WS2 ceiling ≈ good news digest; WS2B phase-2 target ≈ consultant-grade weekly draft needing light human polish.

## 8. v1.1 amendments (external consultant review, accepted 2026-06-13)

1. **Evidence quality schema (Phase 1, not retrofitted):** every evidence record additionally carries `evidence_type` (factual | numerical | quoted | interpretive | speculative), `claim_strength` (confirmed | reported | indicated | suggested), `confidence`, `pub_date`, `extraction_status`.
2. **Claim-strength language as a GATE, not a prompt rule** (strengthened beyond the review): the deterministic verification layer checks that report claim verbs match the evidence behind them — Tier 1 + multi-source evidence permits "data confirms"; Tier 2 permits "reporting indicates"; Tier 3 caps at "industry commentary suggests". Mismatches are downgraded or flagged, never silently passed. (Rationale: four separate prompt rules failed and required mechanical enforcement during 2026-06-12 testing; writing instructions are requests, gates are guarantees.)
3. **Packet health report before synthesis:** deterministic pre-flight over manifest + evidence store — source mix, tier distribution, topic coverage vs the client's coverage map (policy / OEM / dealer channel / international), extraction failures. Delivered to the operator BEFORE synthesis so coverage gaps can be filled while it still matters.
4. **Contradiction non-smoothing, mechanized:** conflicts identified in the theme pass MUST surface in the report's Conflicts section; the verification gate checks that theme-map conflict pairs appear in the output. The synthesis model is prohibited from silently resolving disagreement between credible sources.
5. **Timeline reframed to the consultant's four weeks, with one amendment — walking skeleton in week 1:** a crude end-to-end path (ingestion → evidence → report) runs in week 1 to surface integration risk early; weeks 2–3 deepen each layer in place (validation+appendix, then two-pass synthesis+gates); week 4 = held-mode pilot on real operator packets. Report generation is not back-loaded.

## 9. v1.2 — operator decisions (2026-06-13)

1. **Input packets provided by operator BEFORE build starts** (removes the week-4 dependency; real data from week 1).
2. **Delivery to existing WS1/WS2 Lark docs** (append-mode, WS2B-labeled — already allowlisted; no new destination).
3. **Third LLM provider as additional fallback** — one new API key required (recommendation: DeepSeek — Chinese-native, OpenAI-compatible, cheap; alternative: Anthropic for premium writing A/B). Per-stage failover becomes primary → fallback → fallback-2.
4. Permission-boundary handling accepted (batched requests if hit).
5. **Operator feedback milestones (fixed):** M1 end wk1 — walking-skeleton brief from a real packet (15-min review); M2 end wk2 — evidence quality + packet health report review; M3 end wk3 — first full two-pass analytical brief (operator scores); M4 wk4 — held-mode pilot review = go/no-go for weekly operation.
6. **Timeline compression accepted:** operator supplies multiple packets up front, so cross-week features validate earlier; M3/M4 may merge if M2 is clean.
7. Outage risk resolved by decision 3.

**Architecture note (consequence of decisions 3+4):** WS2B LLM stages call provider APIs **directly from host-side Python** (as already live-proven with the Kimi credential test) rather than through the gateway container — this gives trivial per-stage model assignment, removes the container argv/permission constraints entirely, and leaves the gateway untouched for WS1/WS2 alert duty.
