# OPENCLAW — VPS SYNC PROTOCOL

---
document_id: OPENCLAW-SYNC-001
version: 1.1
created: 2026-05-13
last_updated: 2026-05-13
---

## PURPOSE

This document defines the procedure for syncing VPS runtime artifacts to the
local workspace so CoWork can read them. CoWork's bash sandbox is fully
network-isolated and cannot initiate SSH connections. Claude Code runs on the
VPS and cannot push to the local machine. The sync must be pulled from the
local side each session.

---

## ⚠ SESSION-START REQUIREMENT

**Run the sync block below in Windows PowerShell before beginning any CoWork
session that involves pipeline review, Brain Lite status, or daily report work.**

Without this step, CoWork will be reading stale files from the previous sync.

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

---

## ARCHITECTURE NOTE

Claude Code runs on the VPS (152.42.195.186) — it cannot push files to the
local machine. CoWork runs locally — its bash sandbox cannot reach the VPS.
The sync is a local pull: the operator runs the scp block in local PowerShell,
files land in `config/vps_sync/`, and CoWork reads from there.
