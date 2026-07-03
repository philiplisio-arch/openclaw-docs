# WS1 LLM Editor — Multi-Pass, Multi-Model Review Stage (Design Note)

---
document_id: OPENCLAW_WS1_LLM_EDITOR_2026-06-29
version: v1.1
last_updated: 2026-07-02
status: ACTIVE (auto-apply mode BUILT + LIVE on the daily cron since 2026-07-02; advisory mode retained as fallback)
builds_on: OPENCLAW_WS2B_EXECUTION_PLAN_2026-06-13 (per-stage-model, multi-pass schema)
scope: A review/edit stage for the WS1 (China Business Daily) daily brief. Brings the
  per-stage-model, evidence-first schema designed for the weekly ALJ packet to the daily
  brief, as the missing "Pass 3 — review" stage. The deterministic verification gate and
  verbatim-grounding trust foundation are UNCHANGED and remain authoritative.
---

## 1. Why

WS1 today runs a lean version of the multi-pass schema: a single model (DeepSeek V4 Flash)
does clustering, evidence extraction, and writing. The schema in
`OPENCLAW_WS2B_EXECUTION_PLAN_2026-06-13` specced **per-stage models with failover** and an
evidence-first pipeline; its missing piece on the daily brief is a dedicated **review pass**.

Reader feedback (Steve) is about *quality* — undated market moves, missing company glosses,
shallow summaries, wire reprints double-counted. A same-model self-edit catches little; a
**different** model as critic catches the writer's blind spots. That cross-model review is the
"multiple models" payoff the schema was pointing at.

## 2. Where it sits in the schema

```
extraction → cluster/theme → WRITE (DeepSeek V4 Flash) → REVIEW (Claude, cross-model) → VERIFY (code) → deliver
                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ new stage
```

Governing principles carried over from the WS2B plan:
- **"Writing instructions are requests; gates are guarantees."** Anything mechanically
  checkable (citation integrity, claim-strength, English-only) belongs in the deterministic
  gate, not the editor. The editor handles judgment the gate cannot: depth, prose, scope,
  rule-compliance triage.
- **Per-stage failover.** The reviewer names a primary and a fallback model; a provider outage
  must never block delivery.
- **The model proposes; code disposes.** The editor cannot introduce a fact absent from the
  verified evidence. In auto-apply mode (§3a) it may rewrite the brief, but only within that
  grounding constraint, and every deterministic house gate re-runs on the revised text.

## 3. Advisory mode (built)

- **Input:** the fully assembled brief markdown + a compact per-story evidence digest (headline,
  each grounded `fact_en`, source) + the living house-style rules (`cbiz_style.md`).
- **Reviewer:** Claude via the Messages API (raw HTTP, matching the codebase's `ds()` pattern;
  no new SDK dependency). Cross-model by design — a different family from the DeepSeek writer.
  Single knob `CBIZ_EDITOR_MODEL` (default `claude-opus-4-8`; set to `claude-sonnet-4-6` to trade
  a little judgment for ~40% lower cost on the daily cron).
- **Output:** strict-JSON findings, each `{severity, category, story, issue, suggestion,
  evidence_supported}`, plus an overall assessment and a `publish_recommendation`
  (ship / ship-with-fixes / hold). Written to `state/cbiz_daily/review_<ts>.json` and a readable
  `review_<ts>.md`. **The brief is not modified.**
- **Failover:** Claude key/call fails → degraded DeepSeek self-review (labeled), else skip. The
  pass is purely additive and non-fatal — the pipeline delivers with or without it.
- **Gating:** `CBIZ_EDITOR=1`, OFF by default. No effect on current production behavior.

## 3a. Auto-apply mode (built + LIVE, operator-approved 2026-07-02)

WS1 is not client-facing yet, so the operator authorized the editor to APPLY its own
evidence-grounded fixes rather than only critiquing (previously the flawed edition shipped with
the critique appended). The operator reviews the assessment in Lark ex post facto.

- **One call, two outputs.** `cbiz_editor.revise_brief()` asks the cross-model editor for BOTH a
  corrected brief body AND a findings log (`action_taken` per finding). The findings become the
  Lark assessment; the corrected body is what ships. `review_brief()` (advisory, §3) is retained
  as the failover when the revise call is unavailable.
- **Runs BEFORE assembly.** The editor edits the body upstream of the masthead + Sources build.
  Because those are derived from whatever survives in the body (`story_rendered_in_body`), a story
  the editor drops falls out of the counts and Sources automatically — no manual reconciliation.
- **Gates re-run on the revised text.** After the editor pass, the deterministic house repairs
  (ENGLISH-ONLY scrub, gloss grounding/relocation, undated-market detector, uncited-tail strip)
  re-run, so an LLM edit can never reintroduce a gated defect. Validated on the 2026-07-02 edition:
  11 fixes applied (merge dupes, reconcile counts, remove an invented gloss, correct a units
  error, drop unsupported attributions), delivered at 0 CJK / 0 undated-market.
- **Grounding held under fix pressure.** On findings needing a fact not in evidence, the editor
  logged "could not add — left out rather than invent." The proposes/disposes rule survives.
- **Fail-open.** Any error, or a too-short/truncated revised body, ships the writer's original
  edition unchanged. The pass never blocks delivery.
- **Gating:** still `CBIZ_EDITOR=1` (now ON in the daily cron); `CBIZ_REVISE_MAX_TOKENS` sizes the
  revise budget (default 16000, above the review-only 8000 since it emits a full brief).

## 4. Graduation path

1. Run advisory for several editions; score the editor's catches against real reader feedback
   and the brief-review-gate checklist.
2. Move proven, mechanical catch categories into **deterministic gates** (guarantees), not the
   editor. **DONE (first two, 2026-06-29):** the editor's two highest-frequency HIGH-severity
   catches — ENGLISH-ONLY (Chinese-character attributions) and MARKET-TIMING (undated market
   moves) — are now code gates in `cbiz_daily.py`: a mechanical repair + detectors that feed the
   synthesize retry loop and surface in `verify`. Validated: a dry-run that previously drew 8
   HIGH english-only/market-timing findings now delivers zero CJK, and the editor raises neither
   category — leaving it free for the judgment calls a gate cannot make (forecasts/TONE, sourcing
   breadth, depth).
3. Auto-apply mode for safe, evidence-bound edits. **DONE (operator-approved 2026-07-02):** built
   and live on the daily cron — see §3a. Fixes are applied to the body before assembly and the
   deterministic gates re-run on the result; the operator reviews the assessment in Lark ex post
   facto while WS1 remains internal (non-client-facing).

## 5. Cost

- Advisory pass = one extra LLM call per run over the finished brief (~10–20K input tokens,
  ~2–4K output). Claude Opus 4.8 ≈ $0.10–0.15/run; Sonnet 4.6 ≈ $0.06–0.09/run. Inside the
  operator's standing small-spend pre-approval. Enabling it daily in the 07:10 cron is a
  separate approval.
- Key reused in place (`/root/.secrets/anthropic_api.env`); never created or echoed.

## 6. Files

- `cbiz_crawler/cbiz_editor.py` — the review stage (provider, prompt, JSON parse, sidecar writer).
- `cbiz_crawler/cbiz_daily.py` — gated hook after brief assembly, before delivery.
