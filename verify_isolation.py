#!/usr/bin/env python3
"""
verify_isolation.py
OPENCLAW — Phase C Namespace Isolation Verification
Per OPENCLAW-TEST-HARNESS-DESIGN v1.1, Section 5 and Section 6

Verifies zero cross-contamination between:
  Client A (live):      china_monitor_001
  Client B (synthetic): test_client_002

Run after Step 9.7 manual test run completes.
Usage: python3 verify_isolation.py
Exit code: 0 = ALL PASS, 1 = ONE OR MORE FAILURES
"""

import os
import json
import glob
import sys

# ─── Client identifiers ──────────────────────────────────────────────────────

CLIENT_A = "china_monitor_001"
CLIENT_B = "test_client_002"

# ─── Artifact paths ───────────────────────────────────────────────────────────

DATA_DIR       = "/root/openclaw_phase5/data"
VALIDATION_DIR = "/root/openclaw_phase6/validation"
SUMMARIES_DIR  = "/root/openclaw_phase7/brain_lite/run_summaries"

# All artifact types that must be namespaced
NAMESPACED_ARTIFACT_TYPES = [
    "retrieval_package_{}.json",
    "final_output_{}.txt",
    "final_output_scrubbed_{}.txt",
    "agent_input_{}.txt",
    "agent_input_slim_{}.txt",
    "conflict_log_{}.json",
]

VALIDATION_ARTIFACT_TYPES = [
    "scrubber_report_{}.json",
    "validation_result_{}.json",
]

# Legacy (unsuffixed) artifact names — any of these still present = namespacing failure
LEGACY_ARTIFACT_NAMES = [
    "retrieval_package.json",
    "final_output.txt",
    "final_output_scrubbed.txt",
    "scrubber_report.json",
    "validation_result.json",
    "conflict_log.json",
    "agent_input.txt",
    "agent_input_slim.txt",
]

# Content keywords: china_monitor_001 topic set
# If any appear in CLIENT_B artifacts → contamination
CHINA_MONITOR_KEYWORDS = [
    "china", "us-china", "europe", "middle east",
    "sina", "reuters", "cctv", "baidu",
    "trade policy", "regulatory", "macroeconomic",
]

# ─── Result tracking ──────────────────────────────────────────────────────────

results = []

def check(name, passed, detail=""):
    status = "PASS" if passed else "FAIL"
    results.append({"step": name, "status": status, "detail": detail})
    marker = "✓" if passed else "✗"
    print(f"  {marker} [{status}] {name}")
    if detail:
        print(f"       {detail}")

# ─── Step 5.1 — Artifact filename audit ──────────────────────────────────────

print("\n── Step 5.1  Artifact filename audit ──────────────────────────────")

for tmpl in NAMESPACED_ARTIFACT_TYPES:
    for client in [CLIENT_A, CLIENT_B]:
        fname = tmpl.format(client)
        fpath = os.path.join(DATA_DIR, fname)
        check(
            f"Artifact exists: {fname}",
            os.path.isfile(fpath),
            f"Expected at {fpath}"
        )

for tmpl in VALIDATION_ARTIFACT_TYPES:
    for client in [CLIENT_A, CLIENT_B]:
        fname = tmpl.format(client)
        fpath = os.path.join(VALIDATION_DIR, fname)
        check(
            f"Validation artifact exists: {fname}",
            os.path.isfile(fpath),
            f"Expected at {fpath}"
        )

# Check no legacy unsuffixed artifacts remain
print("\n── Step 5.1b  Legacy artifact check ────────────────────────────────")
for fname in LEGACY_ARTIFACT_NAMES:
    for d in [DATA_DIR, VALIDATION_DIR]:
        fpath = os.path.join(d, fname)
        check(
            f"No legacy artifact: {fname} in {os.path.basename(d)}/",
            not os.path.isfile(fpath),
            f"Found orphan at {fpath}" if os.path.isfile(fpath) else ""
        )

# ─── Step 5.2 — Cross-identifier contamination check ────────────────────────

print("\n── Step 5.2  Cross-identifier contamination check ──────────────────")

def files_for_client(client):
    """Return all artifact file paths for a given client."""
    paths = []
    for tmpl in NAMESPACED_ARTIFACT_TYPES:
        p = os.path.join(DATA_DIR, tmpl.format(client))
        if os.path.isfile(p):
            paths.append(p)
    for tmpl in VALIDATION_ARTIFACT_TYPES:
        p = os.path.join(VALIDATION_DIR, tmpl.format(client))
        if os.path.isfile(p):
            paths.append(p)
    return paths

def grep_string_in_files(needle, file_paths):
    """Return list of (filepath, line_number, line) for each hit."""
    hits = []
    for fpath in file_paths:
        try:
            with open(fpath, "r", errors="replace") as f:
                for i, line in enumerate(f, 1):
                    if needle.lower() in line.lower():
                        hits.append((fpath, i, line.rstrip()))
        except Exception as e:
            hits.append((fpath, 0, f"READ ERROR: {e}"))
    return hits

# CLIENT_B identifier must not appear in CLIENT_A artifacts
hits_b_in_a = grep_string_in_files(CLIENT_B, files_for_client(CLIENT_A))
check(
    f"No '{CLIENT_B}' identifier in {CLIENT_A} artifacts",
    len(hits_b_in_a) == 0,
    f"{len(hits_b_in_a)} hit(s) found" if hits_b_in_a else ""
)

# CLIENT_A identifier must not appear in CLIENT_B artifacts
hits_a_in_b = grep_string_in_files(CLIENT_A, files_for_client(CLIENT_B))
check(
    f"No '{CLIENT_A}' identifier in {CLIENT_B} artifacts",
    len(hits_a_in_b) == 0,
    f"{len(hits_a_in_b)} hit(s) found" if hits_a_in_b else ""
)

# ─── Step 5.3 — Content cross-check: CLIENT_B artifacts ─────────────────────

print("\n── Step 5.3  Content cross-check: CLIENT_B artifacts ───────────────")

b_final = os.path.join(DATA_DIR, f"final_output_{CLIENT_B}.txt")
if os.path.isfile(b_final):
    for kw in CHINA_MONITOR_KEYWORDS:
        hits = grep_string_in_files(kw, [b_final])
        check(
            f"No china_monitor keyword '{kw}' in {CLIENT_B} final output",
            len(hits) == 0,
            f"{len(hits)} hit(s)" if hits else ""
        )
else:
    check(f"CLIENT_B final_output exists for keyword scan", False,
          f"File not found: {b_final}")

# ─── Step 5.4 — Content cross-check: CLIENT_A artifacts ─────────────────────

print("\n── Step 5.4  Content cross-check: CLIENT_A artifacts ───────────────")

a_final = os.path.join(DATA_DIR, f"final_output_{CLIENT_A}.txt")
if os.path.isfile(a_final):
    hits = grep_string_in_files(CLIENT_B, [a_final])
    check(
        f"No '{CLIENT_B}' reference in {CLIENT_A} final output",
        len(hits) == 0,
        f"{len(hits)} hit(s)" if hits else ""
    )
else:
    check(f"CLIENT_A final_output exists for keyword scan", False,
          f"File not found: {a_final}")

# ─── Step 5.5 — Validator result_id cross-check ─────────────────────────────

print("\n── Step 5.5  Validator result_id cross-check ───────────────────────")

def extract_result_ids(validation_result_path):
    """Extract all result_id values from a validation_result.json."""
    try:
        with open(validation_result_path) as f:
            data = json.load(f)
        ids = set()
        # Support both flat and nested structures
        for item in data if isinstance(data, list) else data.get("results", []):
            if isinstance(item, dict) and "result_id" in item:
                ids.add(item["result_id"])
        return ids, None
    except Exception as e:
        return set(), str(e)

val_a = os.path.join(VALIDATION_DIR, f"validation_result_{CLIENT_A}.json")
val_b = os.path.join(VALIDATION_DIR, f"validation_result_{CLIENT_B}.json")

ids_a, err_a = extract_result_ids(val_a)
ids_b, err_b = extract_result_ids(val_b)

if err_a:
    check(f"validation_result_{CLIENT_A}.json readable", False, err_a)
elif err_b:
    check(f"validation_result_{CLIENT_B}.json readable", False, err_b)
else:
    overlap = ids_a & ids_b
    check(
        "Zero result_id overlap between CLIENT_A and CLIENT_B validation results",
        len(overlap) == 0,
        f"Overlapping IDs: {overlap}" if overlap else
        f"CLIENT_A: {len(ids_a)} IDs, CLIENT_B: {len(ids_b)} IDs, overlap: 0"
    )

# ─── Step 5.6 — Brain Lite run_summary cross-check ──────────────────────────

print("\n── Step 5.6  Brain Lite run_summary cross-check ────────────────────")

summaries_a = glob.glob(os.path.join(SUMMARIES_DIR, f"run_summary_{CLIENT_A}_*.json"))
summaries_b = glob.glob(os.path.join(SUMMARIES_DIR, f"run_summary_{CLIENT_B}_*.json"))

check(
    f"run_summary files exist for {CLIENT_A}",
    len(summaries_a) > 0,
    f"Found: {[os.path.basename(p) for p in summaries_a]}" if summaries_a
    else f"No run_summary_{CLIENT_A}_*.json in {SUMMARIES_DIR}"
)

check(
    f"run_summary files exist for {CLIENT_B}",
    len(summaries_b) > 0,
    f"Found: {[os.path.basename(p) for p in summaries_b]}" if summaries_b
    else f"No run_summary_{CLIENT_B}_*.json in {SUMMARIES_DIR} (expected after Step 9.7 run)"
)

# Cross-check: no CLIENT_B references in CLIENT_A summaries and vice versa
for sp in summaries_a:
    hits = grep_string_in_files(CLIENT_B, [sp])
    check(
        f"No '{CLIENT_B}' in {os.path.basename(sp)}",
        len(hits) == 0,
        f"{len(hits)} hit(s)" if hits else ""
    )

for sp in summaries_b:
    hits = grep_string_in_files(CLIENT_A, [sp])
    check(
        f"No '{CLIENT_A}' in {os.path.basename(sp)}",
        len(hits) == 0,
        f"{len(hits)} hit(s)" if hits else ""
    )

# ─── Summary ──────────────────────────────────────────────────────────────────

print("\n══════════════════════════════════════════════════════════════════════")
passed = [r for r in results if r["status"] == "PASS"]
failed = [r for r in results if r["status"] == "FAIL"]
print(f"  RESULT: {len(passed)} PASS  |  {len(failed)} FAIL  |  {len(results)} total checks")

if failed:
    print("\n  FAILURES:")
    for r in failed:
        print(f"    ✗ {r['step']}")
        if r["detail"]:
            print(f"      {r['detail']}")
    print("\n  ISOLATION VERIFICATION: *** FAIL ***")
    print("  One or more contamination checks failed.")
    print("  Per OPENCLAW-TEST-HARNESS-DESIGN Section 6: halt, log issue, do not proceed.")
    sys.exit(1)
else:
    print("\n  ISOLATION VERIFICATION: PASS")
    print("  Zero cross-contamination detected across all artifact types.")
    print("  Phase C exit criterion 3 and 4 confirmed.")
    sys.exit(0)
