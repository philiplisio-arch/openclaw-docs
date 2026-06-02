# OPENCLAW — VPS SYNC PROTOCOL

---
document_id: OPENCLAW-SYNC-001
version: 1.7
created: 2026-05-13
last_updated: 2026-06-03
---

## PURPOSE

This document defines the procedure for syncing VPS runtime artifacts to the
local workspace so CoWork can read them. CoWork's bash sandbox is fully
network-isolated and cannot initiate SSH connections. Claude Code runs on the
VPS and cannot push to the local machine. The sync must be pulled from the
local side each session.

---

## ⚠ SESSION-START CHECKLIST (run in PowerShell before opening CoWork)

**Step 1 — Pull latest doc changes from GitHub:**
```powershell
cd "C:\Users\phil\Documents\OpenClaw project"
git pull
```

**Step 2 — Pull latest VPS runtime artifacts:**

Run the scp block below. Without this step, CoWork will be reading stale
pipeline files from the previous sync.

---

## STANDARD SYNC COMMAND (Windows PowerShell)

Copy and run in PowerShell on your local machine:

```powershell
scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" openclaw_cowork@152.42.195.186:/root/openclaw_logs/light_to_lark.log "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\light_to_lark.log"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" openclaw_cowork@152.42.195.186:/root/openclaw_phase6/validation/validation_result_china_monitor_001.json "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\validation_result_china_monitor_001.json"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" openclaw_cowork@152.42.195.186:/root/openclaw_phase7/brain_lite/run_summaries/run_summary_china_monitor_001_20260524.json "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\run_summary_china_monitor_001_20260524.json"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" openclaw_cowork@152.42.195.186:/root/openclaw_phase5/data/final_output_scrubbed_china_monitor_001.txt "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\final_output_scrubbed_china_monitor_001.txt"

# WS2 — ALJ artifacts (manual pilot runs only)
scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" openclaw_cowork@152.42.195.186:/root/openclaw_phase5/data/final_output_scrubbed_alj_china_auto_001.txt "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\final_output_scrubbed_alj_china_auto_001.txt"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" openclaw_cowork@152.42.195.186:/root/openclaw_phase6/validation/validation_result_alj_china_auto_001.json "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\validation_result_alj_china_auto_001.json"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" openclaw_cowork@152.42.195.186:/root/openclaw_phase7/brain_lite/run_summaries/run_summary_alj_china_auto_001_20260601.json "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\run_summary_alj_china_auto_001_20260601.json"

echo "VPS sync complete"
```

---

## NOTES

- **Authentication:** ed25519 keypair; private key at `config/cowork_key`;
  public key installed in `/home/openclaw_cowork/.ssh/authorized_keys` on VPS.
- **User:** `openclaw_cowork` (uid=999, non-root). All source paths are
  world-readable despite living under `/root/` — /root is mode 711 (execute-only
  for others), subdirectories are 755.
- **No `-r` flag:** Windows OpenSSH scp cannot handle recursive copy to paths
  containing spaces. Pull run_summary files individually.
- **Key permissions error:** If PowerShell complains about key permissions,
  run: `icacls "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" /inheritance:r /grant:r "$($env:USERNAME):(R)"`

---

## ADDING NEW FILES TO THE SYNC

As new artifacts are added to the VPS (e.g., new run_summary files, additional
client artifacts), add a corresponding `scp` line to the block above. Update
this document when the standard sync set changes.

---

## SYNCED FILES

| File | VPS Source | Purpose |
|------|-----------|---------|
| light_to_lark.log | /root/openclaw_logs/ | Full pipeline cron log |
| validation_result_china_monitor_001.json | /root/openclaw_phase6/validation/ | Latest WS1 validator result |
| run_summary_china_monitor_001_20260524.json | /root/openclaw_phase7/brain_lite/run_summaries/ | Brain Lite — 2026-05-24 (Phase D Delivery 4) |
| final_output_scrubbed_china_monitor_001.txt | /root/openclaw_phase5/data/ | WS1 delivered output |
| final_output_scrubbed_alj_china_auto_001.txt | /root/openclaw_phase5/data/ | WS2 pilot output (manual runs) |
| validation_result_alj_china_auto_001.json | /root/openclaw_phase6/validation/ | WS2 validator result |
| run_summary_alj_china_auto_001_20260601.json | /root/openclaw_phase7/brain_lite/run_summaries/ | WS2 Brain Lite — 2026-06-01 pilot run |

---

## ⚠ SESSION-CLOSE CHECKLIST

**Step 1 — Commit and push doc changes from local (PowerShell):**
```powershell
cd "C:\Users\phil\Documents\OpenClaw project"
git add -A
git commit -m "YYYY-MM-DD session close: [brief description]"
git push
```

**Step 2 — Pull on VPS (root terminal):**
```bash
cd /root/openclaw_docs && git pull
```

> ⚠ **Doc files go via git only** (Steps 1+2 above). Do NOT use direct scp
> to push docs to VPS — git is the source of truth. Direct scp overwrites
> without a commit record and will be clobbered on the next git pull.
>
> If you need to push a file to VPS outside the git repo (e.g., a secrets
> file or a script not tracked in docs), use scp with the `-i` key flag:
> ```powershell
> scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" "LOCAL_FILE" openclaw_cowork@152.42.195.186:/REMOTE_PATH/
> ```

---

## ARCHITECTURE NOTE

GitHub is the shared remote between local workspace and VPS.
- Doc edits flow: CoWork edits locally → git push → VPS git pull
- Runtime artifacts flow: VPS pipeline writes → scp pull to local vps_sync/
- CoWork reads docs from local workspace; reads artifacts from config/vps_sync/
