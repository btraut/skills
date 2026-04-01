# Lean Plan Template

Best for small bugs, narrow improvements, and straightforward features.

Includes:
- concise overview
- implementation approach
- task breakdown
- acceptance criteria
- key references only

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
[Brief description of the work]

## Implementation Approach
[High-level approach]

## Task Breakdown

### Task 1: [PR-sized task]
- Goal: [What this task accomplishes]
- Depends on: [None | Task N]
- Parallelizable: [No | Yes, with Task N]
- Deliverables:
  - [Concrete output]

### Task 2: [PR-sized task]
- Goal: [What this task accomplishes]
- Depends on: [Task 1]
- Parallelizable: [No | Yes, with Task N]
- Deliverables:
  - [Concrete output]

## Acceptance Criteria
- [ ] Requirement or validation target

## Sources
- Origin document: [path]  # if applicable
- Relevant files: [path:line]
- Docs: [url]
```
