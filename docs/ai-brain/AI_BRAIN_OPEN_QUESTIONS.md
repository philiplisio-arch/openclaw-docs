# AI Brain Open Questions

Status: Working draft  
Created: 2026-06-30  
Last updated: 2026-06-30  
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

---

## 9. Boot Sequence

What is the minimum startup context a fresh AI instance must read before continuing an AI Brain architecture session?

Current hypothesis:

1. `AI_BRAIN_CURRENT_TRUTH.md`
2. `AI_BRAIN_STATE_OF_PLAY.md`
3. `AI_BRAIN_DECISION_LOG.md`
4. `AI_BRAIN_OPEN_QUESTIONS.md`
5. `AI_BRAIN_ARCHITECTURE_PROCESS.md`
6. Manifesto only when deeper context is needed

Open issue: should this be automated through a single startup prompt or command?

---

## 10. Checkpoint Automation

How can the checkpoint process become deterministic rather than dependent on conversational discipline?

Future target:

```text
Architecture Checkpoint
  -> summarize session
  -> update current truth
  -> update state of play
  -> append decisions
  -> update open questions
  -> append session log
  -> generate diff
  -> commit as one checkpoint
```

Open issue: should this be implemented through Claude Code, a script, a GitHub Action, or a dedicated AI Brain command?

---

## 11. Tool Reliability

How should AI Brain handle required tools that appear available, then are not used, fail, or are mistakenly treated as unavailable?

Session 001 exposed this as a real issue.

Potential rule:

- If a required tool is available, execute.
- If it fails, report the actual failure.
- If the AI has not tried the tool, it must not claim the tool is unavailable.
- If repository synchronization fails, mark the checkpoint as pending, not complete.

---

## 12. Modeling the Decision Maker

How should AI Brain model Philip's decision-making style?

Sub-questions:

- How does Philip recognize a good idea?
- How does he decide what to pursue versus ignore?
- What makes him trust a recommendation?
- What makes him feel that the AI understands the work?
- How does he balance creative exploration against disciplined execution?
- What kinds of projects energize or drain him?
- What causes him to lose track?
