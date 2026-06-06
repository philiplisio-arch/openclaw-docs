**4.8 --Execute Phase 5.4 integration — connect orchestrator to RUN\_FULL\_MONITOR**





**KIMI**

SH3

sk-TKcYarJr4rw4hN287snHn7zc0Xa6bpijozltdyVe2a4z1Ril



**droplet**

yU+EKc4@u@4vTEx











ddfda36122d66a7475f20281bf6b5df86191992de03f850382ab6155c9b53b1



**SSH**





ssh root@152.42.195.186

KEEP OPEN:

**ssh -o ServerAliveInterval=60 -o ServerAliveCountMax=3 root@152.42.195.186**



SSH plus webtunnel:

ssh -L 18789:localhost:18789 root@152.42.195.186

&#x20;



**--Webhook Token**

bobstar1500!





**--RELAY**

source /root/.bashrc

source /root/venv/bin/activate

python /root/lark\_doc\_relay.py

\--

**Reconnect with SSH,**

tmux attach -t openclaw



we’re finished for the day

**LARK BOT**



cli\_a934d3d46cf85bcb



X2sv7fZm7RYNC1ti5hOONh8pKm7XN3Rt





curl -X POST https://open.feishu.cn/open-apis/auth/v3/tenant\_access\_token/internal \\

&#x20; -H "Content-Type: application/json" \\

&#x20; -d '{

&#x20;   "app\_id": "'"cli\_a934d3d46cf85bcb"'",

&#x20;   "app\_secret": "'"X2sv7fZm7RYNC1ti5hOONh8pKm7XN3Rt

"'"

&#x20; }'





echo $cli\_a934d3d46cf85bcb

echo $LARK\_X2sv7fZm7RYNC1ti5hOONh8pKm7XN3Rt

echo $PJDddA4ZxoWwxhxTxazcQwJbnah



LARK TEST DOC: DdZXdJIhFov3arxCHxvcFa9lnjc





\-- RUN SCRIPT: /root/run\_light\_to\_lark.sh





PHASE 1 COMMAND: python3 /root/run\_light\_to\_lark.py







SERPAPI - BAIDU API

fb837830dab1b01987bda0256561843740f22932b5f52d9950bf62cc3a31a664







sed -i 's/BRAVE\_API\_KEY = "REPLACE\_ME"/BRAVE\_API\_KEY = "BSAZPaJxnVKYvYYSu1O\_B4wbsnlOsep"/' /root/openclaw\_phase5/orchestrator/brave\_executor.py



