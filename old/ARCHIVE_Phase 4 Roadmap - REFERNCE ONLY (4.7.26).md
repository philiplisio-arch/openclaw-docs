Last Updated: 2026-03-28

━━━━━━━━━━━━━━━━━━━━━━

🔷 PHASE 4 — DETAILED EXECUTION PLAN  
Control \& Interface Layer

━━━━━━━━━━━━━━━━━━━━━━

OBJECTIVE

Build a system that is:  
• Fully controllable without terminal  
• Reliable and repeatable  
• Ready for non-technical team usage

\---

SUCCESS DEFINITION

Phase 4 is complete when:

• All workflows can be executed via chat  
• No terminal interaction is required  
• Search is visibly working and improving outputs  
• System can be used by a non-technical operator  
• System can operate inside messaging platforms

━━━━━━━━━━━━━━━━━━━━━━

🔶 STAGE 4.1 — CHAT-BASED CONTROL FOUNDATION

GOAL  
Enable control of the system through ChatGPT

\---

KEY TASKS

• Replace terminal commands with chat-based prompts  
• Define standard prompt → action patterns  
• Establish repeatable execution flow

\---

WORKING MODEL

User → Chat instruction → Agent → Relay → Lark

\---

OUTPUT REQUIREMENTS

• Same output quality as current cron pipeline  
• No manual script triggering required

\---

VALIDATION

• Run system 3–5 times via chat  
• Confirm identical behavior vs cron

\---

GATE CONDITION

Do not proceed until:

• All core workflows run via chat  
• Terminal is no longer required for daily use

━━━━━━━━━━━━━━━━━━━━━━

🔶 STAGE 4.2 — TRIGGER \& WORKFLOW STABILIZATION

GOAL  
Ensure system behaves consistently and predictably

\---

KEY TASKS

• Standardize trigger formats (daily run, test run)  
• Remove variability in outputs  
• Improve error handling  
• Ensure retry capability

\---

FAILURE MODES TO ELIMINATE

• Inconsistent output structure  
• Missing sections  
• Partial runs  
• Silent failures

\---

VALIDATION

• Run same workflow multiple times  
• Compare outputs for consistency

\---

GATE CONDITION

Do not proceed until:

• Outputs are consistent across runs  
• No unexplained failures remain  
• Cron and manual execution behave identically

━━━━━━━━━━━━━━━━━━━━━━

🔶 STAGE 4.3 — RETRIEVAL RELIABILITY \& CHINA API INTEGRATION

GOAL  
Ensure system uses real, high-quality, multi-source intelligence

\---

STEP 1 — VALIDATE EXISTING SEARCH

KEY TASKS

• Verify Brave API is being called  
• Confirm tool invocation in logs  
• Identify fallback behavior  
• Add logging for search usage

\---

VALIDATION

• Confirm “Search Used: YES” appears  
• Confirm tool call traces  
• Compare outputs with and without search

\---

GATE CONDITION

Do not proceed until:

• Search usage is visible and confirmed  
• Outputs change when search is enabled

\---

STEP 2 — CHINA API INTEGRATION (INCREMENTAL)

RULE

Add ONE source at a time

\---

PRIORITY 1 — BAIDU SEARCH

• Integrate Baidu via API provider  
• Validate Chinese-language coverage  
• Compare against Brave baseline

\---

PRIORITY 2 — WECHAT OFFICIAL ACCOUNTS

• Identify access method (API or scraping)  
• Test limited retrieval  
• Evaluate signal quality

\---

PRIORITY 3 — ZHIHU / WEIBO

• Add trend and sentiment layer  
• Monitor emerging narratives  
• Filter for relevance

\---

VALIDATION

• Confirm multi-source retrieval  
• Confirm Chinese sources appear  
• Confirm improved depth of insight

\---

GATE CONDITION

Do not proceed until:

• Outputs include multiple independent sources  
• China-specific sources are consistently present  
• Output quality is clearly improved





NOTE (POST-FOUNDATION UPDATE):



External retrieval integration (e.g. Baidu API) is NOT implemented in Phase 4.



Phase 4 validates retrieval behavior only.



All new retrieval sources are deferred to Phase 5 and must use the Retrieval Orchestration Layer.

━━━━━━━━━━━━━━━━━━━━━━

🔶 STAGE 4.4 — MESSAGING-BASED WORKFLOW CONTROL

GOAL  
Operate system through simple messaging commands

\---

KEY TASKS

• Execute workflows via chat instructions  
• Chain actions (run → refine → output)  
• Introduce simple command patterns

\---

TARGET USER

Non-technical operator

\---

VALIDATION

• Run workflows using only messaging  
• No system knowledge required

\---

GATE CONDITION

Do not proceed until:

• System can be used without technical knowledge  
• Instructions are simple and repeatable

━━━━━━━━━━━━━━━━━━━━━━

🔶 STAGE 4.5 — CHANNEL INTEGRATION (TEAM ENTRY POINT)

GOAL  
Move system into communication platforms

\---

KEY TASKS

• Lark bot integration  
• WeChat integration (priority)  
• Optional additional channels

\---

OUTPUT

• Commands executable inside messaging platforms  
• Results delivered in-channel

\---

VALIDATION

• Test full workflow inside Lark or WeChat

\---

GATE CONDITION

Phase 4 complete when:

• Team can operate system through messaging  
• No terminal or technical steps required

━━━━━━━━━━━━━━━━━━━━━━

🔴 OPERATING RULES

• Keep system single-threaded  
• Do not skip stages  
• Do not add APIs before search is verified  
• One change at a time  
• Log everything

━━━━━━━━━━━━━━━━━━━━━━

🧠 FINAL PRINCIPLE

This phase is about CONTROL

Not scale  
Not automation  
Not expansion

The system must be usable before it becomes powerful

━━━━━━━━━━━━━━━━━━━━━━

