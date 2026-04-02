---
name: beads-implement
description: Implement Beads or beads_rust work items from an issue id. Use when the user runs $beads-implement <bead-id> or asks to implement a bead/epic; if it is an epic, implement all sub-tasks, committing after each one and only interrupting when blocked or a decision is needed.
---

# Beads Implement

Use this skill to execute work from a bead or epic id with minimal back-and-forth. This skill must work with either classic Beads (`bd`) or beads_rust (`br`).

## Workflow

1. **Resolve the tracker first**
   - If the user explicitly says `bd`, `br`, `beads`, or `beads_rust`, obey that.
   - Otherwise detect what is actually installed:
     - If only `br` is installed, use `br`.
     - If only `bd` is installed, use `bd`.
     - If both are installed, prefer the tracker that already owns the current workspace/history.
     - If both are installed and the workspace is ambiguous, ask one targeted question instead of guessing.
   - Do not mix commands from both trackers in the same run.

2. **Prime the chosen tracker**
   - For `bd`:
     - Run `bd prime` first. It is still the fastest way to get the current "how to start this bead" primer.
     - If `bd prime` is unavailable or confusing, look for a loaded local skill for classic Beads and use that before anything else.
     - If no local `bd` skill exists, use local CLI help like `bd --help`, `bd show --help`, and `bd update --help`.
   - For `br`:
     - Look for a loaded local `br`, `beads_rust`, or equivalent tracker skill and use that first if it exists.
     - If no local `br` skill exists, use local CLI help like `br --help`, `br show --help`, `br update --help`, and `br epic --help`.
     - Set `ACTOR="${BR_ACTOR:-assistant}"`.
     - Use `br show <id> --json`, `br ready --json`, and `br blocked --json` for orientation instead of expecting a `prime` command.
     - Always use `--json` on agent-facing `br` commands when available.
     - Never run bare `bv`.
   - Do not send the user to public web docs from this skill.

3. **Open the bead**
   - For `bd`, use `bd show <id> --json` when possible and read the title, description, acceptance criteria, and dependencies.
   - For `br`, use `br show <id> --json` and read the title, description, acceptance criteria, design, notes, and dependencies.
   - If required info is missing or a dependency blocks progress, ask a single targeted question and wait.

4. **Start work in the tracker**
   - For `bd`, mark the bead `in_progress` if your workflow supports it (check `bd prime` / `bd update --help`).
   - For `br`, claim it with `br update --actor "$ACTOR" <id> --claim --json` or set `--status in_progress`.
   - Add a short note on your intended approach if the bead is ambiguous.

5. **Create a brief to-do list**
   - At the start of execution, create a short to-do list of the tasks/sub-tasks you plan to complete and update it as you go.

6. **Decide scope**
   - If the bead is a single task, implement it directly.
   - If the bead is an epic, identify all sub-tasks and implement them in dependency order.
   - For an epic, treat exactly one child bead as the active implementation target at a time unless the user explicitly asks for parallel implementation.
   - For `br` epics, use `br epic status <id>` or the dependency graph when it helps you understand child progress and closure readiness.

7. **Delegate narrowly (use sub-agents surgically)**
   - Use sub-agents for bounded slices of the current bead only.
   - Good sub-agent targets: repo exploration, API/library doc lookup, reproducer creation, test strategy, narrow refactors with a clear file list.
   - Give each sub-agent explicit ownership (files + expected output), and keep the write scope as small as possible.
   - If the target is an epic, the main agent owns sequencing. Sub-agents may work on the current child bead, but they must not start later child beads unless explicitly assigned.
   - Sub-agents must not close beads, close the epic, update the overall plan, or advance the workflow on their own.
   - Sub-agents must not assume their changes are integrated. They return results for the main agent to review, merge, and either accept or reject.

8. **Review gate before advancing**
   - For each bead or child bead, run this loop in order:
     1. implement
     2. review
     3. fix review findings
     4. run relevant checks/tests
     5. commit
     6. update Beads
   - Do not begin the next child bead until the current one has passed this gate.
   - If a sub-agent goes beyond scope, stop and verify what changed before using any of its output.

9. **Implement, commit, and write notes (repeat per task/sub-task)**
   - Implement, run relevant checks/tests, then commit once the review gate passes.
   - One commit per task/sub-task.
   - Commit message: include the bead id in the subject.
   - Commit body: write real notes (what changed, why, tests run, follow-ups/risk).
   - After the commit, add the same notes to the bead so the tracker survives compaction and future handoffs.
   - For `bd`, use the note/design workflow recommended by `bd prime` or the loaded local Beads skill.
   - For `br`, write the summary back with `br update --actor "$ACTOR" <id> --notes "..." --json` and use `br comments add` when a separate progress note is cleaner.
   - For `br`, remember sync is explicit. Run `br sync --flush-only` before committing tracker-state changes to git.

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

10. **Authority rules**
   - Only the main agent may mark a bead or epic complete.
   - Only the main agent may decide the current child bead is done and move on to the next child bead.
   - Only the main agent may integrate commits into the shared branch.
   - Sub-agents are workers and reviewers, not project managers.

11. **Communicate only when needed**
   - Do not interrupt the user while work is progressing.
   - Only pause to ask for help when blocked, when information is missing, or when a meaningful decision is required.

12. **Close out**
   - When complete, close the bead with a clear reason.
   - For `bd`, follow the session-end sync step recommended by `bd prime` or the loaded local Beads skill for the installed version.
   - For `br`:
     - Close with `br close --actor "$ACTOR" <id> --reason "Implemented X in commit abc123" --json`.
     - If you are closing an epic, check readiness first with `br epic status <id>` or `br epic close-eligible <id>`.
     - Run `br sync --flush-only` after the closing update so `.beads/` is current before git commit/push.

13. **Report progress**
   - State which tracker you used: `bd` or `br`.
   - Provide a concise summary of completed tasks, commits made, and what remains (if anything).
