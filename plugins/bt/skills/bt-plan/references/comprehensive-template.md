# Comprehensive Plan Template

Best for major features, architectural changes, complex integrations, and risky migrations.

Includes everything from `Standard` plus:
- phased rollout or migration structure
- alternative approaches considered
- system-wide impact analysis
- explicit validation and rollout planning

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
[Executive summary]

## Problem Statement
[Detailed analysis]

## Proposed Approach
[Comprehensive solution design]

## Implementation Phases

### Phase 1: [Foundation]
- Purpose: [Why this phase exists]
- Tasks:
  - [Task name]
  - [Task name]

### Phase 2: [Core Implementation]
- Purpose: [Why this phase exists]
- Tasks:
  - [Task name]
  - [Task name]

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
  - [Tests, checks, review targets]
- Risks:
  - [Risk]

## Alternative Approaches Considered
- [Approach]: [Why rejected or not chosen]

## System-Wide Impact
- Interaction graph: [callbacks, events, middleware, or cross-layer effects]
- Error propagation: [how failures move through the system]
- State lifecycle risks: [partial-failure or consistency concerns]
- API surface parity: [other interfaces that may need analogous changes]
- Integration scenarios: [cross-layer scenarios worth validating]

## Dependency and Parallelism Notes
- [Detailed sequencing notes]
- [Parallel work boundaries]

## Risks and Mitigations
- [Risk]: [Mitigation]

## Rollout / Validation Strategy
- [How to validate safely]
- [How to stage or roll out if relevant]

## Acceptance Criteria
- [ ] Functional requirement
- [ ] Non-functional requirement
- [ ] Quality gate

## Sources & References
- Origin document: [path]  # if applicable
- Internal references: [path:line]
- External references: [url]
- Related work: [path, PR, or issue]
```
