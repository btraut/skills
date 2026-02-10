---
name: plan
description: Break a goal into a beads-ready set of work items with clear scope, deps, acceptance criteria, and test/verification steps. Use when the user wants a detailed execution breakdown (tasks, files to touch, tests, checks), especially for engineers with minimal project context.
---

# Plan

Use this skill to produce a high-quality task breakdown. The point is not "a markdown file", it's work items that are the right size and have enough detail to implement without flailing.

## Workflow

1. **Inspect the repo**
   - Scan the working directory for architecture, conventions, docs, and relevant code paths.
   - Identify any existing spec/doc location (often `docs/`) and whether something already exists you should align to.

2. **Clarify scope (if needed)**
   - Ask only the minimum questions needed to lock scope; prefer 1-3 concise questions.
   - If the user already provided a prompt or requirements, proceed without delay.

3. **Break the goal into beads-ready work items**
   - Produce a small set of milestones/epics and implementable issues with:
     - clear ordering/dependencies
     - explicit acceptance criteria
     - concrete verification steps (commands + expected results)
   - Keep items sized so one agent can finish one item in 1-3 hours.
   - Prefer fewer, sharper items over a giant list of micro-tasks.

4. **Add the details that stop future-you from hating present-you**
   - For each work item, include:
     - the likely files/areas to touch (or where new code should live)
     - the key code changes (not prose: the actual moves)
     - tests to add/run and how to validate locally
     - risky parts and how to de-risk them (spikes, flags, smaller PRs)

5. **Optional: write/append to a spec doc**
   - Only do this if the user explicitly wants a doc artifact, or there is already a canonical spec you should update.
   - If you do write a doc, keep it single-source-of-truth: append/merge into the existing spec rather than creating a second competing doc.

6. **Beads handoff (usual output)**
   - If a bead already exists, update its design field with the plan path.
   - If no bead exists and the work is multi-session or large, recommend creating a bead and ask whether to use a single bead or an epic with milestone beads.
   - Recommend running the `beads-create` skill to file the work items into Beads (and do the polish pass).
   - For sequential projects, prefer a single bead unless explicit checkpoints or handoffs are needed; if using milestones, add linear dependencies.
   - Keep bead count low: one bead per major milestone, not per tiny task.
   - In your response, provide a short bead mapping (titles + dependencies) when applicable.

## Plan requirements

- Provide **beads-ready tasks** with clear ordering and rationale.
- Each task must include:
  - **Scope**: what is in/out
  - **Acceptance criteria**: how we know it is done
  - **Implementation notes**: files/areas to touch + key code changes
  - **Tests/verification**: what to run and what success looks like
- Emphasize **DRY**, **YAGNI**, and **frequent commits**.
- Use plain language; avoid jargon unless defined.
- Provide testing guidance for engineers who are weak at test design.
- Add a brief **Beads handoff** summary in your response when the work merits beads.
- If a doc artifact is requested, write/append it; otherwise, optimize for a clean work breakdown.

## Output structure (recommended)

- Goal + short context summary
- Non-goals (optional but useful)
- Assumptions and constraints
- Work items (milestones/epics + issues) with deps
- Testing and verification strategy
- Risks/rollout (if applicable)
- Beads mapping (what to create, what depends on what)
- Open questions (only if truly blocking)

## Style rules

- Be exhaustive but focused; avoid speculative extras.
- Prefer concrete paths and commands over vague guidance.
- Keep each task small enough to complete in 1-3 hours.
