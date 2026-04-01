# Standard Plan Template

Best for most features, complex bugs, and changes spanning multiple units of work.

Includes everything from `Lean` plus:
- problem framing and motivation
- more explicit technical approach
- dependency graph and parallelism notes
- risks and validation strategy

```markdown
---
title: [Plan Title]
type: [feat|fix|refactor]
status: active
date: YYYY-MM-DD
origin: docs/brainstorms/YYYY-MM-DD-<topic>-requirements.md  # include if applicable
---

# [Plan Title]

## Overview
[Comprehensive description]

## Problem Statement / Motivation
[Why this work matters]

## Proposed Approach
[High-level implementation shape]

## Task Breakdown

### Task 1: [PR-sized task]
- Goal: [What this task accomplishes]
- Depends on: [None | Task N]
- Parallelizable: [No | Yes, with Task N]
- Scope:
  - [Files, systems, or responsibilities]
- Deliverables:
  - [Concrete output]
- Validation:
  - [Tests, checks, or review targets]

### Task 2: [PR-sized task]
- Goal: [What this task accomplishes]
- Depends on: [Task 1]
- Parallelizable: [No | Yes, with Task N]
- Scope:
  - [Files, systems, or responsibilities]
- Deliverables:
  - [Concrete output]
- Validation:
  - [Tests, checks, or review targets]

## Dependency and Parallelism Notes
- [Explain sequencing]
- [Call out tasks that can run in parallel]

## Risks and Mitigations
- [Risk]: [Mitigation]

## Acceptance Criteria
- [ ] Functional requirement
- [ ] Validation or testing expectation

## Sources & References
- Origin document: [path]  # if applicable
- Similar implementations: [path:line]
- Docs: [url]
- Related plans or PRs: [path or reference]
```
