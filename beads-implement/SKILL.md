---
name: beads-implement
description: Implement Beads work items from a bead id. Use when the user runs $beads-implement <bead-id> or asks to implement a bead/epic; if it is an epic, implement all sub-tasks, committing after each one and only interrupting when blocked or a decision is needed.
---

# Beads Implement

Use this skill to execute work from a bead or epic id with minimal back-and-forth.

## Workflow

1. **Load beads guidance if needed**
   - If bd CLI usage or bead structure is unclear, read `/Users/btraut/Development/skills-external/beads/SKILL.md` and follow its session protocol.

2. **Open the bead**
   - Read the title, description, acceptance criteria, and dependencies.
   - If required info is missing or a dependency blocks progress, ask a single targeted question and wait.

3. **Create a brief to-do list**
   - At the start of execution, create a short to-do list of the tasks/sub-tasks you plan to complete and update it as you go.

4. **Decide scope**
   - If the bead is a single task, implement it directly.
   - If the bead is an epic, identify all sub-tasks and implement them in dependency order.

5. **Implement and commit**
   - For each task/sub-task: implement, run relevant checks/tests, then commit.
   - Use one commit per task; include the bead id in the commit message.

6. **Communicate only when needed**
   - Do not interrupt the user while work is progressing.
   - Only pause to ask for help when blocked, when information is missing, or when a meaningful decision is required.

7. **Report progress**
   - Provide a concise summary of completed tasks, commits made, and what remains (if anything).
