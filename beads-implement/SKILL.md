---
name: beads-implement
description: Implement Beads work items from a bead id. Use when the user runs $beads-implement <bead-id> or asks to implement a bead/epic; if it is an epic, implement all sub-tasks, committing after each one and only interrupting when blocked or a decision is needed.
---

# Beads Implement

Use this skill to execute work from a bead or epic id with minimal back-and-forth.

## Workflow

1. **Prime bd (always)**
   - Run `bd prime` first. It is the fastest way to get the current "how to start this bead" primer.
   - If `bd prime` is unavailable or confusing, consult the official Beads GitHub repo at `https://github.com/steveyegge/beads` for workflow guidance.

2. **Open the bead**
   - Use `bd show <id>` and read the title, description, acceptance criteria, and dependencies.
   - If required info is missing or a dependency blocks progress, ask a single targeted question and wait.

3. **Start work in Beads**
   - Mark the bead `in_progress` if your bd workflow supports it (check `bd prime` / `bd update --help`).
   - Add a short note on your intended approach if the bead is ambiguous.

4. **Create a brief to-do list**
   - At the start of execution, create a short to-do list of the tasks/sub-tasks you plan to complete and update it as you go.

5. **Decide scope**
   - If the bead is a single task, implement it directly.
   - If the bead is an epic, identify all sub-tasks and implement them in dependency order.
   - For an epic, treat exactly one child bead as the active implementation target at a time unless the user explicitly asks for parallel implementation.

6. **Delegate narrowly (use sub-agents surgically)**
   - Use sub-agents for bounded slices of the current bead only.
   - Good sub-agent targets: repo exploration, API/library doc lookup, reproducer creation, test strategy, narrow refactors with a clear file list.
   - Give each sub-agent explicit ownership (files + expected output), and keep the write scope as small as possible.
   - If the target is an epic, the main agent owns sequencing. Sub-agents may work on the current child bead, but they must not start later child beads unless explicitly assigned.
   - Sub-agents must not close beads, close the epic, update the overall plan, or advance the workflow on their own.
   - Sub-agents must not assume their changes are integrated. They return results for the main agent to review, merge, and either accept or reject.

7. **Review gate before advancing**
   - For each bead or child bead, run this loop in order:
     1. implement
     2. review
     3. fix review findings
     4. run relevant checks/tests
     5. commit
     6. update Beads
   - Do not begin the next child bead until the current one has passed this gate.
   - If a sub-agent goes beyond scope, stop and verify what changed before using any of its output.

8. **Implement, commit, and write notes (repeat per task/sub-task)**
   - Implement, run relevant checks/tests, then commit once the review gate passes.
   - One commit per task/sub-task.
   - Commit message: include the bead id in the subject.
   - Commit body: write real notes (what changed, why, tests run, follow-ups/risk).
   - After the commit, add the same notes to the bead (so the bead survives compaction and future handoffs). Use `bd update <id>` and whatever flag/subcommand your bd version uses for notes (check `bd prime`).

   Minimal commit template:

   ```text
   <BEAD-ID>: <imperative summary>

   Why:
   - ...

   What:
   - ...

   Tests:
   - ...

   Notes/Risks:
   - ...
   ```

9. **Authority rules**
   - Only the main agent may mark a bead or epic complete.
   - Only the main agent may decide the current child bead is done and move on to the next child bead.
   - Only the main agent may integrate commits into the shared branch.
   - Sub-agents are workers and reviewers, not project managers.

10. **Communicate only when needed**
   - Do not interrupt the user while work is progressing.
   - Only pause to ask for help when blocked, when information is missing, or when a meaningful decision is required.

11. **Close out**
   - When complete, close the bead (or mark it done) with a clear reason.
   - After closing, run the session-end sync step recommended by `bd prime` for your installed `bd` version.
   - If `bd prime` is unavailable, verify the session-close command in the official Beads GitHub repo at `https://github.com/steveyegge/beads` before ending the session.

12. **Report progress**
   - Provide a concise summary of completed tasks, commits made, and what remains (if anything).
