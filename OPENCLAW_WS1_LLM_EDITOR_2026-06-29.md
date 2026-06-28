# WS1 LLM Editor — Multi-Pass, Multi-Model Review Stage (Design Note)

---
document_id: OPENCLAW_WS1_LLM_EDITOR_2026-06-29
version: v1.0
last_updated: 2026-06-29
status: ACTIVE (advisory mode built and gated OFF; auto-apply not built)
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
- **The model proposes; code disposes.** The editor is a critic — it cannot introduce a fact
  absent from the verified evidence, and it cannot rewrite the brief in advisory mode.

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

## 4. Graduation path (not yet built)

1. Run advisory for several editions; score the editor's catches against real reader feedback
   and the brief-review-gate checklist.
2. Move proven, mechanical catch categories into **deterministic gates** (guarantees), not the
   editor.
3. Only then consider an **auto-apply** mode for safe, evidence-bound edits — gated, separate
   operator approval (P-02 cron change). Prose/depth judgment stays advisory.

## 5. Cost

- Advisory pass = one extra LLM call per run over the finished brief (~10–20K input tokens,
  ~2–4K output). Claude Opus 4.8 ≈ $0.10–0.15/run; Sonnet 4.6 ≈ $0.06–0.09/run. Inside the
  operator's standing small-spend pre-approval. Enabling it daily in the 07:10 cron is a
  separate approval.
- Key reused in place (`/root/.secrets/anthropic_api.env`); never created or echoed.

## 6. Files

- `cbiz_crawler/cbiz_editor.py` — the review stage (provider, prompt, JSON parse, sidecar writer).
- `cbiz_crawler/cbiz_daily.py` — gated hook after brief assembly, before delivery.
