---
name: plan
description: Write comprehensive implementation plans for a project or feature. Use when the user wants a detailed plan for execution (tasks, files to touch, code/tests/docs, testing strategy) especially for engineers with minimal project context.
---

# Plan

Use this skill to produce a full, step-by-step implementation plan aimed at a capable engineer who lacks project/tooling/domain context and needs explicit guidance.

## Workflow

1. **Inspect the repo**
   - Scan the working directory for architecture, conventions, docs, and relevant code paths.
   - Identify where plans live (e.g., `docs/plans/`).

2. **Clarify scope (if needed)**
   - Ask only the minimum questions needed to lock scope; prefer 1-3 concise questions.
   - If the user already provided a prompt or requirements, proceed without delay.

3. **Write the plan into `docs/plans/`**
   - Create or update a plan document in `docs/plans/` as requested.
   - Assume the reader is new to the codebase and tools.

## Plan requirements

- Provide **bite-sized tasks** with clear ordering and rationale.
- For each task, specify:
  - **Files to touch** (or where to add new files)
  - **Code changes** to make
  - **Tests** to write/run (favor TDD and test design guidance)
  - **Docs** to consult or update
  - **How to verify** (commands, expected outcomes)
- Emphasize **DRY**, **YAGNI**, and **frequent commits**.
- Use plain language; avoid jargon unless defined.
- Provide testing guidance for engineers who are weak at test design.

## Output structure (recommended)

- Title + short context summary
- Assumptions and constraints
- Implementation tasks (numbered)
- Testing strategy and checkpoints
- Rollout/risks (if applicable)
- Appendix: commands or references

## Style rules

- Be exhaustive but focused; avoid speculative extras.
- Prefer concrete paths and commands over vague guidance.
- Keep each task small enough to complete in 1-3 hours.
