# AI Brain Decision Log

Status: Working draft  
Created: 2026-06-30  
Last updated: 2026-06-30  
Purpose: Track durable design decisions for the AI Brain architecture.

---

## Decision 001: GitHub is the official record

**Date:** 2026-06-30  
**Status:** Accepted

GitHub should hold durable commitments, architecture, specifications, decision logs, implementation notes, prompts, runbooks, and source-of-truth project documentation.

Obsidian may hold raw thinking and associative notes, but GitHub wins where the two disagree on formal project state or commitments.

---

## Decision 002: Obsidian is the associative memory layer

**Date:** 2026-06-30  
**Status:** Accepted

Obsidian should capture loose ideas, conversation summaries, cross-project thinking, research trails, themes, and project incubation notes.

The governing distinction is:

**Obsidian captures thinking. GitHub captures commitments.**

---

## Decision 003: Conversation is the primary interface

**Date:** 2026-06-30  
**Status:** Accepted

The system should not require Philip to begin with task management or document organization. Ideas, projects, and decisions should emerge from conversations across AI tools and other input streams.

---

## Decision 004: AI Brain should be designed as an AI Chief of Staff

**Date:** 2026-06-30  
**Status:** Working decision

The project should be framed less as a memory system and more as an AI Chief of Staff / external executive function.

The system's job is to maintain situational awareness, understand priorities, surface decisions, connect themes, and help convert conversation into coherent work.

---

## Decision 005: Projects are not created automatically

**Date:** 2026-06-30  
**Status:** Working decision

Projects should emerge through a life cycle:

```text
Conversation
  -> Interesting idea
  -> Recurring topic
  -> Candidate project
  -> Explicit project decision
  -> Active project
  -> Completed / archived / dormant
```

The AI may suggest that something has matured into a candidate project, but explicit user approval should govern promotion into active project status.

---

## Decision 006: Autonomy should be governed by transparency and thresholds

**Date:** 2026-06-30  
**Status:** Working decision

Philip is comfortable with a high degree of autonomous AI activity if the system is transparent, reversible, and governed by explicit approval thresholds.

The architecture should therefore include a governance model rather than a static permissions list.

---

## Decision 007: Architecture Discovery Process adopted

**Date:** 2026-06-30  
**Status:** Accepted

AI Brain architecture should be developed through an explicit Architecture Discovery Process:

```text
Discover -> Challenge -> Consolidate -> Synchronize -> Checkpoint -> Continue
```

The process should alternate between design discovery and reality checks.

---

## Decision 008: Checkpoint requires repository synchronization

**Date:** 2026-06-30  
**Status:** Accepted

A session checkpoint is incomplete until the relevant GitHub documents have actually been updated or the failure to update has been explicitly recorded.

A verbal summary without repository synchronization is not a completed checkpoint.

---

## Decision 009: GitHub is the boot loader for future sessions

**Date:** 2026-06-30  
**Status:** Accepted

At the start of each future AI Brain architecture session, the AI should reconstruct context from the GitHub documents rather than relying on prior chat history.

Recommended startup sequence:

1. Read `AI_BRAIN_CURRENT_TRUTH.md`
2. Read `AI_BRAIN_STATE_OF_PLAY.md`
3. Read `AI_BRAIN_DECISION_LOG.md`
4. Read `AI_BRAIN_OPEN_QUESTIONS.md`
5. Read `AI_BRAIN_ARCHITECTURE_PROCESS.md`
6. Consult the Manifesto only when deeper context is needed

---

## Decision 010: Execution beats explanation

**Date:** 2026-06-30  
**Status:** Accepted

When an action has been agreed and the required tool is available, the AI should execute first and explain afterward.

If the tool is unavailable, fails, or cannot be invoked, the AI should state that immediately and clearly.

Talking around an agreed execution task is a process failure.

---

## Decision 011: Documentation reflects understanding, not chronology

**Date:** 2026-06-30  
**Status:** Accepted

The official record should not accumulate every conversational turn. It should express the clearest current understanding.

The AI should update, consolidate, and refactor documentation when the architecture changes, rather than merely appending notes because a meeting happened.
