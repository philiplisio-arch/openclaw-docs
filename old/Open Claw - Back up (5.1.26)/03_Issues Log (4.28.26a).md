# OPENCLAW — ISSUES LOG

---

## Issue #34 — Citation System Instability

---

### Description

Agent produced:

* Fabricated result_id values
* Invalid citation groupings
* Zero-citation outputs under strict constraints

Result:

* Validator failures
* Delivery blocked
* System instability

---

### Root Cause

* Over-reliance on prompt-based enforcement
* Conflicting rules (precision vs recall)
* Model probabilistic nature

---

### Resolution

#### 1. Validator Upgrade

* result_id-based validation
* multi-ID extraction fix

#### 2. Scrubber Layer (NEW)

* Removes invalid IDs
* Rewrites citation groups
* Tracks unsupported groups

#### 3. Prompt Strategy Shift

* High-recall approach
* Removed “omit if unsure”
* Encouraged redundancy

#### 4. Tolerance Model

* Partial failure allowed
* Full failure only if all groups unsupported

---

### Outcome

* Fabricated citations eliminated
* Delivery stabilized
* System robust to model error

---

### Status

✅ RESOLVED
