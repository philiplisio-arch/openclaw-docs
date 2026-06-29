# AI Brain Decision Log

Status: Working draft  
Created: 2026-06-30  
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
