# SYS SPEC — CITATION ALIGNMENT CHECK (ADV-015 OPTION B)

---
document_id: SYS_ADV015_OptionB_Snippet_Alignment_Spec
version: v0.2
date: 2026-06-10
author: Claude Fable 5
status: OPERATOR APPROVED 2026-06-10 — IMPLEMENTED IN WARN-ONLY MODE same day (runtime commit 227f365: citation_alignment.py + entity_aliases.json + validator.py hook)

> **Calibration outcome (2026-06-10):** D17 fixture flagged `misaligned` ✓;
> grounded and cross-language (430,000≡43万) fixtures `aligned` ✓. The §5.2
> criterion ("June 9 produces 0 misaligned") was based on a false premise:
> replay showed the June 9 delivered brief contained **4 genuinely misaligned
> bullets** (contaminated-session era — see Issue #67) which the checker
> correctly caught. The clean-baseline criterion therefore TRANSFERS to the
> first deliveries under session isolation (2026-06-11 onward): warn-only
> must show 0 misaligned on operator-confirmed clean runs before any
> promotion-to-blocking proposal.
basis: OPENCLAW-ADV-015 (operator-approved 2026-06-06), Issue #66
---

## 1. Purpose

Detect **cross-source citation misbinding** (Issue #66): a bullet whose cited source does not support the specific claim, even though the result_id is real and syntax is valid. The check is deterministic, additive, and in v1 **warn-only** — it changes nothing about delivery, mirroring the ADV-014 rollout pattern (warn first; promote to blocking only after a calibration period and explicit operator approval).

Context update since ADV-015 was written: the 2026-06-10 diagnosis identified shared agent-session history as the likely *generator* of misbinding (now removed). Option B remains necessary as the *detector* — it is the only layer that would have caught D17 automatically.

## 2. Placement

Implemented as an additive function inside the existing validator stage (`openclaw_phase6/validation/`), running after citation extraction, before the result is written. Output goes into `validation_result.json` as a new `citation_alignment` block. The delivery gate logic is NOT modified in v1; warnings are visible to the operator (review packet + Option D spot-check targeting) and archived via ADV-016.

Rationale for validator placement (vs. a new pipeline stage): the validator already loads the scrubbed output and the retrieval package and already maps citations to sources — Option B reuses that mapping rather than re-deriving it.

## 3. Mechanism

For each delivered bullet B with cited sources S1..Sn (post-resolver mapping):

1. **Extract claim anchors from B** — script-invariant tokens that survive translation:
   - numbers, percentages, currency amounts, units (e.g., `81.8%`, `430,000`, `€200M`, `1.344 million`)
   - dates and month references
   - Latin-script proper tokens (e.g., `BYD`, `Nvidia`, `Reuters`, `PMI`, `NEV`)
   - CJK proper tokens when the claim contains CJK
2. **Build the evidence text** for B = concatenation of title + snippet of every cited source (NOT the whole package — that is what makes misbinding invisible today).
3. **Match with normalization**: numeric anchors match across formats (430,000 ≡ 43万 via a small unit-conversion table: 万=1e4, 亿=1e8, %, $/¥/€); entity anchors match via a maintained **alias table** (`entity_aliases.json`, e.g., Chery≡奇瑞, Geely≡吉利, EC≡欧盟委员会) — additive, operator-reviewable, starts with ~30 recurring entities harvested from the traceability archive.
4. **Score** = matched anchors / total anchors in B (bullets with <2 anchors are scored `insufficient_anchors` and never warned — prevents noise on soft/analytic bullets).
5. **Verdict per bullet**: `aligned` (score ≥ T_pass), `weak` (T_warn ≤ score < T_pass), `misaligned` (score < T_warn). Initial thresholds T_pass=0.5, T_warn=0.25 — TO BE CALIBRATED, see §5.

Output schema addition to `validation_result.json`:

```json
"citation_alignment": {
  "mode": "warn_only",
  "bullets_checked": 8,
  "aligned": 6, "weak": 1, "misaligned": 1, "insufficient_anchors": 0,
  "warnings": [
    {"bullet_index": 2, "section": "EXECUTIVE TAKE", "score": 0.0,
     "anchors": ["EC", "Yvette Cooper", "not sustainable"],
     "cited": ["res_0a5837f3bb9f"], "verdict": "misaligned"}
  ]
}
```

## 4. Known limits (stated up front, per ADV-015 risk note)

- Keyword overlap is a weak proxy for semantic support. The check catches D17-class misbinding (cited snippet about a *different topic*) reliably; it cannot catch a subtly wrong claim about the right topic. Option D spot-checks remain the human layer; the `weak`/`misaligned` bullets become the *targeted* spot-check candidates, making Option D cheaper and sharper.
- Chinese↔English coverage depends on the alias table and numeric anchors. Bullets whose only anchors are untranslated CJK entities against English snippets (rare in practice — snippets are mostly the CJK side) may score `weak` spuriously; this is what warn-only calibration measures.

## 5. Calibration plan (no runtime risk)

The ADV-016 archive makes offline calibration possible — this did not exist when ADV-015 was written:

1. Replay the checker over all archived `(final_output, filtered_retrieval_package)` pairs (June 6 onward, plus the D17 evidence preserved in ADV-015).
2. Required outcomes before going live in warn mode: D17 ET-Bullet-2 flagged `misaligned`; clean deliveries (June 9) produce 0 `misaligned`.
3. Run warn-only in production ≥10 deliveries; operator reviews warning precision in review packets.
4. Promotion to blocking (`misaligned` ⇒ hold delivery) is a separate operator decision with its own packet (same path ADV-014 L2 took).

## 6. Scope compliance

- No agent prompt change (Option A remains prohibited). No scrubber change. No delivery-gate change in v1. Validator strictness not weakened — only extended additively. Namespaced per client like all phase6 artifacts. Archived per ADV-016.

## 7. Implementation estimate

~1 session: checker function + alias table seed + replay script over archive + warn-only wiring. Rollback: remove the function call; `validation_result.json` consumers ignore unknown keys (verify during implementation).

## Approval requested

Operator approval of this spec (Lane 2) authorizes implementation in **warn-only mode** after the §5.1–5.2 offline calibration passes. It does NOT authorize blocking mode.
