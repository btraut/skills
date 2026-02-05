---
name: beads-create
description: Translate a finalized plan into Beads epics and issues with clear dependencies, design notes, and parallelization. Use when asked to file Beads from a plan/spec (OpenSpec, PRD, design doc), or when converting an external plan into a detailed Beads tracking structure.
---

# Beads Create

Use this skill to import a plan into Beads as a well-structured set of epics and issues.

## Workflow

1. **Load beads guidance if needed**
   - If bd CLI usage or bead structure is unclear, read `/Users/btraut/Development/skills-external/beads/SKILL.md` and follow its session protocol.

2. **Confirm the plan is ready**
   - Ensure there is a finalized plan or spec outside Beads.
   - If the plan is still fuzzy, ask for revisions first and iterate up to 5 times before importing.

3. **Translate the plan into Beads structure**
   - Create epics that map to major milestones or deliverables.
   - Create issues for concrete, implementable tasks.
   - **Hierarchy rule**: When an epic has child milestones/tasks, create them as
     hierarchical children (dotted IDs like `EPIC.1`, `EPIC.2`) rather than
     separate top-level issues with only parent-child deps. Follow the bd CLI
     “Create epic with hierarchical child tasks” flow (create the epic, then
     create children so bd auto-assigns `EPIC.N` IDs). Verify the returned IDs;
     if bd doesn’t assign dotted IDs, stop and ask the user how to proceed.
   - Add dependencies, ordering constraints, and opportunities for parallel work.

4. **Add implementation detail**
   - Include design notes, assumptions, and acceptance criteria on each issue.
   - Make tasks small and unambiguous so a fresh agent can pick up a single issue.

5. **Hand off to review**
   - Recommend running the `beads-review` skill to proofread and polish the filed beads.

6. **Restart the agent**
   - Finish this task, then stop. Encourage a fresh agent for the next task to keep sessions small.

## Output expectations

- Provide a concise mapping of epics and issues you created.
- Call out any dependencies or blockers that need user confirmation.
- If asked to iterate beyond 5 plan revisions, say you do not think it can be improved further.
