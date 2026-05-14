# OPENCLAW — VPS SYNC PROTOCOL

---
document_id: OPENCLAW-SYNC-001
version: 1.3
created: 2026-05-13
last_updated: 2026-05-14
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
scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" `
    openclaw_cowork@152.42.195.186:/root/openclaw_logs/light_to_lark.log `
    "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\light_to_lark.log"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" `
    openclaw_cowork@152.42.195.186:/root/openclaw_phase6/validation/validation_result.json `
    "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\validation_result.json"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" `
    openclaw_cowork@152.42.195.186:/root/openclaw_phase7/brain_lite/run_summaries/run_summary_china_monitor_001_20260511.json `
    "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\run_summary_china_monitor_001_20260511.json"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" `
    openclaw_cowork@152.42.195.186:/root/openclaw_phase7/brain_lite/run_summaries/run_summary_china_monitor_001_20260512.json `
    "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\run_summary_china_monitor_001_20260512.json"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" `
    openclaw_cowork@152.42.195.186:/root/openclaw_phase7/brain_lite/run_summaries/run_summary_china_monitor_001_20260513.json `
    "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\run_summary_china_monitor_001_20260513.json"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" `
    openclaw_cowork@152.42.195.186:/root/openclaw_phase7/brain_lite/run_summaries/run_summary_china_monitor_001_20260514.json `
    "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\run_summary_china_monitor_001_20260514.json"

scp -i "C:\Users\phil\Documents\OpenClaw project\config\cowork_key" `
    openclaw_cowork@152.42.195.186:/root/openclaw_phase5/data/final_output_scrubbed.txt `
    "C:\Users\phil\Documents\OpenClaw project\config\vps_sync\final_output_scrubbed.txt"

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

As new artifacts are added to the VPS (e.g., new run_summary files after
Brain Lite Runs 3–5, client_config yaml after Step 6), add a corresponding
`scp` line to the block above. Update this document when the standard sync
set changes.

---

## SYNCED FILES

| File | VPS Source | Purpose |
|------|-----------|---------|
| light_to_lark.log | /root/openclaw_logs/ | Full pipeline cron log |
| validation_result.json | /root/openclaw_phase6/validation/ | Latest validator result |
| run_summary_china_monitor_001_20260511.json | /root/openclaw_phase7/brain_lite/run_summaries/ | Brain Lite Run 1 |
| run_summary_china_monitor_001_20260512.json | /root/openclaw_phase7/brain_lite/run_summaries/ | Brain Lite Run 2 |
| run_summary_china_monitor_001_20260513.json | /root/openclaw_phase7/brain_lite/run_summaries/ | Brain Lite Run 3 |
| run_summary_china_monitor_001_20260514.json | /root/openclaw_phase7/brain_lite/run_summaries/ | Brain Lite Run 4 |
| final_output_scrubbed.txt | /root/openclaw_phase5/data/ | Delivered output — T-04 advisory language compliance review |

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

---

## ARCHITECTURE NOTE

GitHub is the shared remote between local workspace and VPS.
- Doc edits flow: CoWork edits locally → git push → VPS git pull
- Runtime artifacts flow: VPS pipeline writes → scp pull to local vps_sync/
- CoWork reads docs from local workspace; reads artifacts from config/vps_sync/
