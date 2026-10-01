# Browser Retrieval Phase 1 — VPS Setup & Test Execution Guide

**Track:** Research-only parallel track  
**Isolation:** /root/openclaw_phase7/ only — zero contact with /root/openclaw_phase5/  
**Date:** 2026-05-21  

---

## Step 1 — Create directory and copy script

```bash
mkdir -p /root/openclaw_phase7/browser_retrieval/
```

Copy `fetch_article_text.py` from the workspace folder into:
```
/root/openclaw_phase7/browser_retrieval/fetch_article_text.py
```

---

## Step 2 — Install Playwright and Chromium

```bash
# Install playwright Python package
pip install playwright

# Download and install headless Chromium browser binary
playwright install chromium

# Install system-level dependencies (required on Ubuntu/Debian)
playwright install-deps chromium
```

**Expected output from `playwright install chromium`:**
```
Downloading Chrome for Testing 148.x.x.x ...
Chrome for Testing 148.x.x.x (playwright chromium v1223) downloaded to ...
```

**If `playwright` is not on PATH after pip install:**
```bash
pip install playwright
python -m playwright install chromium
python -m playwright install-deps chromium
```

**Verify install:**
```bash
python3 -c "from playwright.sync_api import sync_playwright; print('OK')"
```

---

## Step 3 — Find test URLs from recent retrieval_package.json

Locate a recent retrieval package (read-only):

```bash
# Find most recent retrieval_package.json in phase5 artifacts
ls -lt /root/openclaw_phase5/artifacts/ | head -5
# or
find /root/openclaw_phase5/ -name "retrieval_package.json" | sort | tail -3
```

Open the most recent file and pick:
- **URL_A**: One Brave search result URL (from `brave_results` array)
- **URL_B**: One Baidu search result URL (from `baidu_results` array)

**Example jq commands to extract candidate URLs:**
```bash
# Pick first Brave result URL from most recent package
cat /root/openclaw_phase5/artifacts/<latest>/retrieval_package.json \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['brave_results'][0]['url'])"

# Pick first Baidu result URL
cat /root/openclaw_phase5/artifacts/<latest>/retrieval_package.json \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['baidu_results'][0]['url'])"
```

---

## Step 4 — Run the 3-URL test suite

```bash
cd /root/openclaw_phase7/browser_retrieval/

# --- Test A: Brave result URL ---
python3 fetch_article_text.py "URL_A_PASTE_HERE" \
  --output /root/openclaw_phase7/browser_retrieval/test_output_brave.txt \
  2>&1 | tee /root/openclaw_phase7/browser_retrieval/test_log_brave.txt

# --- Test B: Baidu result URL ---
python3 fetch_article_text.py "URL_B_PASTE_HERE" \
  --output /root/openclaw_phase7/browser_retrieval/test_output_baidu.txt \
  2>&1 | tee /root/openclaw_phase7/browser_retrieval/test_log_baidu.txt

# --- Test C: Known paywall (WSJ) ---
python3 fetch_article_text.py "https://www.wsj.com/articles/latest" \
  --output /root/openclaw_phase7/browser_retrieval/test_output_wsj.txt \
  2>&1 | tee /root/openclaw_phase7/browser_retrieval/test_log_wsj.txt
```

---

## Step 5 — Collect results for findings report

After all three tests, run:

```bash
echo "=== BRAVE RESULT ===" && cat /root/openclaw_phase7/browser_retrieval/test_log_brave.txt
echo "=== BAIDU RESULT ===" && cat /root/openclaw_phase7/browser_retrieval/test_log_baidu.txt
echo "=== WSJ (PAYWALL) ===" && cat /root/openclaw_phase7/browser_retrieval/test_log_wsj.txt

# Word counts on extracted files
wc -w /root/openclaw_phase7/browser_retrieval/test_output_*.txt 2>/dev/null
```

Paste that output back to CoWork for the Phase 1 Findings Report.

---

## Expected stderr log format (one line per fetch)

```
[fetch_article] status=OK url=https://... words=847 selector='article' elapsed=4.3s
[fetch_article] status=OK url=https://... words=1203 selector='main' elapsed=5.1s
[fetch_article] status=FAIL [PAYWALL] url=https://www.wsj.com/... words=94 selector='article' elapsed=3.8s | error=None
```

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `playwright: command not found` | Use `python3 -m playwright install chromium` |
| `Host system is missing dependencies` | Run `playwright install-deps chromium` |
| `Error: browserType.launch: Executable doesn't exist` | Re-run `playwright install chromium` |
| `TimeoutError` on a URL | The site is slow; retry with `--timeout 60` |
| All tests fail with `UNEXPECTED_ERROR: BrowserType.launch` | Missing system deps; run `playwright install-deps` |

---

## Constraints reminder

- All output files go to `/root/openclaw_phase7/browser_retrieval/` only  
- Do NOT write to `/root/openclaw_phase5/` or any path under it  
- Do NOT run this script from any cron job  
- This script has no imports from orchestrator/, brain_lite/, or pipeline modules  
