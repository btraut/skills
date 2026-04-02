---
name: beads-create
description: File Beads or beads_rust epics/issues from a finalized plan/spec AND do the polish pass (clarity, acceptance criteria, sizing, deps). Use when asked to create Beads from a plan/spec (OpenSpec, PRD, design doc), convert an external plan into issue tracker structure, or review/refine an existing Beads set.
---

# Beads Create

Use this skill to create Beads from a plan/spec and do the review pass so implementers can just pick up issues and ship. This skill must work with either classic Beads (`bd`) or beads_rust (`br`).

## Workflow

1. **Resolve the tracker first**
   - If the user explicitly says `bd`, `br`, `beads`, or `beads_rust`, obey that.
   - Otherwise detect what is actually installed:
     - If only `br` is installed, use `br`.
     - If only `bd` is installed, use `bd`.
     - If both are installed, prefer the tracker that already owns the current workspace/history. Check the local `.beads/` state and the existing workflow docs before guessing.
     - If both are installed and the workspace is still ambiguous, ask one targeted question instead of winging it.
   - Do not mix commands from both trackers in the same run.

2. **Load the right local guidance if needed**
   - Look for a loaded local skill on the user's machine that covers the chosen tracker and use that first.
   - For `bd`, prefer the local `beads` skill if it is available.
   - For `br`, prefer any loaded local `br`, `beads_rust`, or equivalent tracker skill if it is available.
   - If no local skill exists, rely on local CLI help and the installed tool itself:
     - `bd --help`, `bd create --help`, `bd update --help`
     - `br --help`, `br create --help`, `br update --help`
   - Do not send the user to public web docs from this skill.
   - For `br`, use `--json` on agent-facing commands whenever available.

3. **Decide which mode you are in**
   - If the user has a finalized plan/spec and wants Beads filed: do Create mode.
   - If the user already has Beads and wants them improved: do Review mode (skip straight to step 6).

4. **Confirm the plan is ready (Create mode)**
   - Ensure there is a finalized plan or spec outside Beads.
   - If the plan is still fuzzy, ask for revisions first and iterate up to 5 times before importing.

5. **Translate the plan into tracker structure (Create mode)**
   - Create epics that map to major milestones or deliverables.
   - Create issues for concrete, implementable tasks.
   - For `bd`:
     - When an epic has child milestones/tasks, create them as hierarchical children with dotted IDs like `EPIC.1`, `EPIC.2`, not as loose top-level issues.
     - Follow the `bd create ... --parent <epic-id>` flow so `bd` auto-assigns `EPIC.N` IDs.
     - Verify the returned IDs. If `bd` does not assign dotted IDs, stop and ask the user how to proceed.
   - For `br`:
     - Use the epic/parent relationship, but do not require dotted child IDs. `br` supports parent-child structure without the old `bd` dotted-ID contract.
     - Create the epic first, then create or update child issues with `--parent <epic-id>`.
     - Add explicit dependencies where sequencing matters, and keep the graph acyclic with `br dep cycles --json`.
   - Add dependencies, ordering constraints, and opportunities for parallel work.

6. **Review and polish (Create mode + Review mode)**
   - Fix vague titles, missing acceptance criteria, or unclear scope.
   - Ensure each issue is something one agent can do in a single task.
   - Verify dependencies, sequencing, and opportunities for parallel work.
   - Add missing design notes / decision context.
   - Split oversized issues; merge duplicates; delete fluff.
   - For `br`, prefer structured updates over freeform ambiguity:
     - `br update ... --description`
     - `br update ... --design`
     - `br update ... --acceptance-criteria`
     - `br update ... --notes`
   - For `bd`, use the locally available `bd` fields/workflow for description, design, notes, and acceptance criteria on the installed version.

7. **Add implementation detail**
   - Include design notes, assumptions, and acceptance criteria on each issue.
   - Make tasks small and unambiguous so a fresh agent can pick up a single issue.

8. **Validate tracker state before leaving**
   - For `br`, run `br dep cycles --json` and make sure it is empty.
   - For `br`, remember sync is explicit. If you changed tracker state and need the JSONL export updated, run `br sync --flush-only`.
   - For `bd`, follow the local sync/export workflow supported by the installed version.

9. **Single-pass**
   - Do one focused pass in the current context.
   - If another pass is needed, say so explicitly and recommend a separate follow-up run.

10. **Restart the agent**
   - Finish this task, then stop. Encourage a fresh agent for the next task to keep sessions small.

## Output expectations

- Provide a concise mapping of epics and issues you created.
- State which tracker you used: `bd` or `br`.
- Call out any dependencies or blockers that need user confirmation.
- If asked to iterate beyond 5 plan revisions, say you do not think it can be improved further.
