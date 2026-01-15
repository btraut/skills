---
name: plan
description: Write comprehensive implementation plans for a project or feature. Use when the user wants a detailed plan for execution (tasks, files to touch, code/tests/docs, testing strategy) especially for engineers with minimal project context.
---

# Plan

Use this skill to produce a full, step-by-step implementation plan aimed at a capable engineer who lacks project/tooling/domain context and needs explicit guidance.

## Workflow

1. **Inspect the repo**
   - Scan the working directory for architecture, conventions, docs, and relevant code paths.
   - Identify the canonical spec/doc location in `docs/` and whether a spec already exists.

2. **Clarify scope (if needed)**
   - Ask only the minimum questions needed to lock scope; prefer 1-3 concise questions.
   - If the user already provided a prompt or requirements, proceed without delay.

3. **Write the plan into `docs/`**
   - If a spec already exists in `docs/`, append/merge the plan into that spec file.
   - If no spec exists, create a single spec+plan document in `docs/` and use that going forward.
   - Assume the reader is new to the codebase and tools.

4. **Beads handoff**
   - If a bead already exists, update its design field with the plan path.
   - If no bead exists and the work is multi-session or large, recommend creating a bead and ask whether to use a single bead or an epic with milestone beads.
   - Recommend running the `beads-create` skill once the plan is finalized to translate it into Beads epics/issues.
   - For sequential projects, prefer a single bead unless explicit checkpoints or handoffs are needed; if using milestones, add linear dependencies.
   - Keep bead count low: one bead per major milestone, not per tiny task.
   - In your response, provide a short bead mapping (titles + dependencies) when applicable.

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
- Add a brief **Beads handoff** summary in your response when the work merits beads.
- Always keep the plan in the existing spec under `docs/`, or create a single spec+plan document in `docs/` if none exists.

## Output structure (recommended)

- Title + short context summary (as a new section in the spec file)
- Assumptions and constraints
- Implementation tasks (numbered)
- Testing strategy and checkpoints
- Rollout/risks (if applicable)
- Beads handoff (if applicable)
- Appendix: commands or references

## Style rules

- Be exhaustive but focused; avoid speculative extras.
- Prefer concrete paths and commands over vague guidance.
- Keep each task small enough to complete in 1-3 hours.
