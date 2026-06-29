# AI Brain Open Questions

Status: Working draft  
Created: 2026-06-30  
Purpose: Track unresolved questions that should guide future AI Brain design conversations.

---

## 1. Entity Model

What is the minimum useful entity schema for AI Brain?

Possible entity types:

- project
- idea
- theme
- principle
- decision
- person
- client
- company
- workflow
- asset
- source
- task

Open question: which of these are essential for v0.1?

---

## 2. Project Graduation

What exact signals indicate that an idea should move from conversation to candidate project?

Possible signals:

- repeated discussion over time
- user explicit interest
- connection to existing strategic priorities
- readiness for execution
- AI judgment that the idea is recurring or important
- user approval

---

## 3. Governance Thresholds

What actions can AI Brain take autonomously, and which require approval?

Examples to classify:

- summarize conversations into Obsidian
- update project state
- suggest links between projects
- draft GitHub documentation
- create tasks for Claude Code
- launch research
- change architectural specifications
- archive projects
- merge code or publish externally

---

## 4. Dashboard Requirements

What should the first dashboard show?

Potential modules:

- active projects
- incubating projects
- blocked projects
- decisions needed today
- recently changed items
- forgotten-but-important items
- autonomous work completed
- recommended next actions
- risks and stale areas

---

## 5. Capture Pipeline

How should conversations be captured across ChatGPT, Claude, Claude Code, Telegram/WhatsApp-style notes, voice notes, and other inputs?

Open issue: what can be automated now versus what requires manual export or summary?

---

## 6. Trust and Provenance

How should AI Brain represent the difference between:

- raw user input
- AI inference
- summarized memory
- verified evidence
- user-approved decision
- execution-ready instruction

---

## 7. Misunderstanding

What does it mean for AI Brain to misunderstand Philip?

Possible failure modes:

- pushing projects he no longer cares about
- failing to connect related conversations
- forgetting a repeatedly emphasized principle
- recommending actions inconsistent with his decision style
- treating casual thoughts as commitments
- failing to surface important but dormant ideas

---

## 8. Repository Strategy

Should AI Brain eventually have its own repository separate from `openclaw-docs`?

Current answer: not yet. Use `openclaw-docs` for now, then split later if AI Brain becomes a sufficiently independent operating system.
