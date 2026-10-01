# AI Brain Architecture Manifesto

Status: Working draft  
Owner: Philip Lisio  
Created: 2026-06-30  
Last updated: 2026-06-30  
Repository: openclaw-docs  
Purpose: Preserve and evolve the foundational architecture emerging from AI Brain design conversations.

---

## 1. Executive Summary

AI Brain is not primarily a note-taking system, memory system, automation layer, or project-management tool.

AI Brain is an emerging **external executive function**: a human-AI operating model designed to help Philip maintain situational awareness across many projects, preserve important context, surface decisions, prevent valuable ideas from being lost, and translate ongoing conversations into coherent work.

The original GitHub + Obsidian question remains useful, but it is now understood as one implementation layer beneath a broader architecture.

The durable architecture should be organized around behaviors, governance, continuity, and execution discipline, not around today's tools.

---

## 2. Core Insight

The central interface is conversation.

Philip thinks out loud with ChatGPT, Claude, Claude Code, voice notes, Telegram/WhatsApp-style inputs, and other interfaces. Valuable work emerges from these conversations gradually. The system should therefore treat conversation as the primary input stream and convert it into structured understanding over time.

The system should not assume every idea is a project. Ideas mature through repeated discussion, relevance, user emphasis, AI judgment, and explicit graduation into project status.

---

## 3. Working Definition

AI Brain is an AI Chief of Staff and operating system for long-term human-AI collaboration.

Its job is to maintain an increasingly accurate model of Philip's evolving priorities, projects, principles, decisions, and working style, then use that model to answer:

- What exists?
- What matters?
- What changed?
- What needs attention?
- What decisions are required?
- What can be done autonomously?
- What should be ignored, archived, or revisited?

---

## 4. Foundational Principles

### 4.1 Conversation is the primary interface

The system should not require Philip to start by organizing files, tickets, or folders. He should be able to think freely in conversation. Structure should emerge from interpretation, review, and promotion.

### 4.2 Understanding is more valuable than storage

The goal is not to remember everything. The goal is to understand what matters, why it matters, and how it relates to current and future work.

### 4.3 Memory is curated, not accumulated

A useful long-term system must forget, compress, archive, and promote selectively. Raw memory without judgment becomes noise.

### 4.4 Projects emerge from repeated thought

Projects are not automatically created from every idea. They move through a life cycle:

```text
Conversation
  -> Interesting idea
  -> Recurring topic
  -> Candidate project
  -> Explicit project decision
  -> Active project
  -> Completed / archived / dormant
```

### 4.5 The AI should exercise judgment, not merely retrieval

The system should behave less like a searchable database and more like a trusted chief of staff. It should notice patterns, connect themes, push back when appropriate, and surface what deserves attention.

### 4.6 Trust and validation are constitutional principles

The OpenClaw validation pipeline is not merely a component of the business-intelligence workflow. It is a governing philosophy for AI Brain as a whole.

The system must distinguish between:

- raw input
- inferred interpretation
- proposed memory
- verified evidence
- user-approved decision
- execution-ready instruction

Important recommendations and claims should have provenance wherever practical.

### 4.7 Autonomy requires transparency and approval thresholds

Philip is comfortable with a high degree of autonomous AI activity provided it is transparent, reversible, and governed by explicit approval thresholds.

The question is not simply "what may the AI do?" but "what governance rule determines whether the AI may observe, suggest, prepare, execute, or require approval?"

### 4.8 The system exists to reduce cognitive load, not replace judgment

AI Brain should help Philip stop losing track across many projects while preserving his ability to think freely, make final decisions, and steer priorities.

### 4.9 Documentation reflects understanding, not chronology

The GitHub record should not become a transcript or museum of prior thinking. It should become the clearest expression of the current architecture.

Documents should be updated when understanding changes, not merely because a conversation occurred.

### 4.10 The AI has an editorial responsibility

The AI's role in architecture sessions is not only to answer questions or archive discussion. It must also act as an architectural editor: identifying conceptual thresholds, consolidating durable insights, pruning obsolete formulations, and keeping the official record coherent.

### 4.11 Execution beats explanation

When an action has been agreed and the required tool is available, the AI should execute first and explain afterward. If the tool is unavailable or fails, it should say so immediately and clearly.

Talking around a required action is a process failure.

### 4.12 Checkpoints require repository synchronization

An Architecture Discovery session is not complete until the relevant GitHub documents have actually been updated or the failure to update has been explicitly recorded.

A verbal checkpoint without repository synchronization is incomplete.

### 4.13 GitHub is both repository of truth and boot loader

GitHub is not only where official architecture is stored. It is also the boot sequence for future AI instances.

Each new architecture session should begin by reconstructing context from the GitHub documents rather than relying on chat history.

---

## 5. Architectural Model

The working model is:

```text
Philip
  -> Conversation streams
  -> AI Chief of Staff
  -> Entity / project / principle model
  -> Governance engine
  -> Execution layer
  -> Dashboard / briefing layer
  -> Checkpoint / repository synchronization layer
```

### 5.1 Conversation streams

Inputs may include:

- ChatGPT conversations
- Claude conversations
- Claude Code sessions
- voice notes
- Telegram/WhatsApp-style notes
- project documents
- GitHub commits and issues
- research outputs

### 5.2 AI Chief of Staff

The Chief of Staff layer interprets inputs, maintains context, identifies priorities, and determines what deserves attention.

Key behaviors:

- notice recurring ideas
- identify candidate projects
- surface forgotten but important items
- connect themes across projects
- update project state
- prepare morning briefings
- recommend decisions
- challenge drift or inconsistency
- identify when a checkpoint is needed
- synchronize durable understanding into GitHub

### 5.3 Entity model

The core unit is not a note. The core unit is a persistent entity with history and current state.

Entities may include:

- projects
- clients
- people
- companies
- themes
- principles
- decisions
- workflows
- ideas
- assets

A project such as Steve, OpenClaw, or Foote Group Website should be understood as a long-lived object with goals, decisions, related files, conversations, tasks, status, risks, and dependencies.

### 5.4 Governance engine

The governance layer determines whether the AI should:

- observe only
- capture silently
- suggest
- prepare a draft
- execute autonomously
- request approval
- block action

Governance should be based on risk, reversibility, source confidence, user impact, and whether the action changes the official record.

### 5.5 Execution layer

Execution tools include:

- GitHub
- Claude Code
- VS Code
- scripts and automations
- future agents
- reports and dashboards

The execution layer should act only within the governance model.

### 5.6 Dashboard / briefing layer

The dashboard is not the primary interface. It is the cockpit.

It should help answer:

- Where are we?
- What changed?
- What matters today?
- What decisions are pending?
- Which projects are active, incubating, blocked, dormant, or complete?
- What should be ignored for now?

### 5.7 Checkpoint / repository synchronization layer

The checkpoint layer converts a work session into durable architecture.

It should answer:

- What did we learn?
- Did our understanding change?
- Which documents must change?
- Were the documents actually updated?
- What is the next starting point?

---

## 6. Tool Roles: Current Implementation Hypothesis

### GitHub

GitHub is the official record for commitments and the boot loader for future sessions.

It should contain:

- current truth / startup context
- architecture documents
- approved decisions
- operating principles
- specifications
- prompt libraries
- implementation notes
- session logs
- status reports
- runbooks
- source-of-truth documentation

### Obsidian

Obsidian is the associative memory and thinking layer.

It should contain:

- raw conversation notes
- free associations
- cross-project reflections
- loose ideas
- research trails
- theme notes
- project incubation notes
- items to promote later

### Claude / ChatGPT

Reasoning interfaces for conversation, synthesis, critique, drafting, and strategic thinking.

### Claude Code

Execution agent for editing files, updating repositories, implementing scripts, running checks, and operationalizing decisions.

### VS Code

Execution cockpit for repository work, local files, terminal workflows, and Claude Code interaction.

### Dashboard

Orientation layer for state of play, not the source of truth.

---

## 7. Obsidian vs GitHub Rule

The governing distinction:

**Obsidian captures thinking. GitHub captures commitments.**

Promote from Obsidian to GitHub only when an item becomes:

- a decision
- a principle
- a specification
- an operating procedure
- a project state update
- an implementation requirement
- a reusable prompt or template
- a source-of-truth reference
- a checkpoint record

---

## 8. Proposed GitHub Documentation Structure

Current and proposed structure:

```text
docs/ai-brain/
  AI_BRAIN_CURRENT_TRUTH.md
  AI_BRAIN_ARCHITECTURE_MANIFESTO.md
  AI_BRAIN_STATE_OF_PLAY.md
  AI_BRAIN_DECISION_LOG.md
  AI_BRAIN_OPEN_QUESTIONS.md
  AI_BRAIN_SESSION_LOG.md
  AI_BRAIN_ARCHITECTURE_PROCESS.md
```

Recommended future renaming, if desired:

```text
docs/ai-brain/
  00_CURRENT_TRUTH.md
  01_MANIFESTO.md
  02_STATE_OF_PLAY.md
  03_DECISION_LOG.md
  04_OPEN_QUESTIONS.md
  05_SESSION_LOG.md
  06_ARCHITECTURE_PROCESS.md
```

---

## 9. Proposed Obsidian Structure

```text
AI Brain Vault/
  00 Inbox/
  01 Daily Notes/
  02 Conversations/
  03 Ideas/
  04 Projects/
    OpenClaw/
    Foote Group AI/
    China Media Discovery/
    Steve Mascot/
    Family Education/
    Personal Operating System/
  05 Themes/
    Memory/
    Trust/
    Retrieval/
    Dashboards/
    Human in the Loop/
    China Source Coverage/
    AI Agents/
  06 Decisions/
  07 To Promote to GitHub/
  08 Archive/
```

---

## 10. Promotion Workflow

```text
Conversation
  -> Obsidian capture
  -> light tagging and linking
  -> review for significance
  -> candidate promotion
  -> GitHub source-of-truth update
  -> dashboard/state update
```

Promotion checklist:

- Is this a real decision?
- Is this needed for execution?
- Would a future AI need this as source of truth?
- Is this stable enough to version-control?
- Does this change a project, principle, workflow, or architecture?
- Does this belong in a README, spec, decision log, prompt library, status report, or runbook?

---

## 11. Architecture Discovery Process

AI Brain should be designed by using AI Brain principles.

The Architecture Discovery Process is:

```text
Discover -> Challenge -> Consolidate -> Synchronize -> Checkpoint -> Continue
```

A session is complete only after repository synchronization has succeeded or failed transparently.

---

## 12. Initial Operating Loop

The practical loop should be:

```text
Capture -> Understand -> Model -> Advise -> Execute -> Review -> Learn
```

Daily behavior:

- ingest recent conversation and work activity
- update entity/project state
- surface changes
- identify pending decisions
- recommend next actions
- note items requiring approval

Weekly behavior:

- review active and incubating projects
- promote durable insights to GitHub
- archive stale notes
- update state-of-play documents
- refine governance thresholds

---

## 13. Current Open Questions

1. What exact entity schema should AI Brain maintain?
2. What makes something a project versus an idea versus a theme?
3. What approval thresholds should govern different types of AI action?
4. What should the first dashboard show?
5. How should raw conversations be captured across ChatGPT, Claude, and other interfaces?
6. How should the system represent uncertainty, inference, and provenance?
7. What should count as a misunderstanding of Philip's priorities?
8. What should the minimum boot sequence be for a new AI instance?
9. Should AI Brain eventually have its own repository separate from openclaw-docs?

---

## 14. Immediate Implementation Plan

### Day 1

Create this manifesto as the working architecture spine.

### Day 2

Create companion files:

- `AI_BRAIN_STATE_OF_PLAY.md`
- `AI_BRAIN_DECISION_LOG.md`
- `AI_BRAIN_OPEN_QUESTIONS.md`

### Day 3

Create boot and process files:

- `AI_BRAIN_CURRENT_TRUTH.md`
- `AI_BRAIN_SESSION_LOG.md`
- `AI_BRAIN_ARCHITECTURE_PROCESS.md`

### Day 4

Import recent AI Brain / Obsidian / GitHub / OpenClaw conversation summaries.

### Day 5

Define entity model v0.1.

### Day 6

Define governance thresholds v0.1.

### Day 7

Create first dashboard/state-of-play prototype.

---

## 15. Current Status

This document represents the first consolidation of the AI Brain design-discovery interview.

The project has moved from a tools question to a higher-level architecture:

```text
From: GitHub + Obsidian memory architecture
To: AI Chief of Staff / external executive function / human-AI operating system
```

Session 001 also exposed a process defect: the AI explained the need for GitHub synchronization but did not immediately execute it. That failure produced an important rule:

```text
Checkpoint incomplete until repository updated.
```

This document should now serve as the living reference document for subsequent AI Brain architecture conversations.
