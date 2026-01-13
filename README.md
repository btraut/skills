# Codex / Claude Agent Skills

Home for custom skills used by Codex CLI and Claude-based agents. Skills here define workflows, utilities, and helpers that can be discovered by the agents at startup.

## What’s inside
- `brainstorm/` – structured idea generation and spec facilitation with concise questions plus a beads-aware handoff to planning once the spec is confirmed.
- `enrich-pr/` – logging helper that keeps a running ledger of decisions, file changes, tests, and risks to streamline commit/PR summaries.
- `plan/` – comprehensive implementation planning workflow with tasks, files to touch, tests, docs, verification steps, and beads handoff guidance.
- `ship/` – ship workflow that commits changes, rebases onto production, fast-forwards production, pushes both branches, and returns to main.
- `ralph/` – controller-driven Ralph loop for sequential codex exec subprocesses and multi-pass reviews.

## Using these skills
1) Clone or place this repo where your agent looks for skills (e.g., `$CODEX_HOME/skills`).
2) Launch Codex or Claude with skills enabled; they will auto-discover entries in this directory.
3) Follow each skill’s `SKILL.md` for usage details and any supporting assets or scripts.

## Beads integration
Use beads for work that spans sessions, has dependencies, or needs durable context. Plans should link back to the bead (design field), while beads capture milestones and decisions in notes. For small, single-session work, skip beads and keep it lightweight.

## Changelog
- 2026-01-13: Ralph skill now uses per-run IDs and context isolation to avoid contention.
- 2026-01-13: Added ralph skill for controller-driven Ralph loops with sequential subprocess prompts.
- 2026-01-12: Brainstorm skill now adds a beads handoff step with guidance for single vs epic+milestone beads.
- 2026-01-12: Plan skill now adds beads handoff guidance and a suggested bead mapping summary.
- 2026-01-07: Ship skill now auto-stashes unrelated changes and restores them after shipping.
- 2026-01-07: Ship skill now allows committing on `main` without requiring confirmation.
- 2026-01-07: Added ship skill for committing changes, rebasing onto production, fast-forwarding production, pushing both branches, and returning to main.
- 2026-01-07: Brainstorm skill now explicitly asks to hand off to plan after spec approval and provides a concise spec recap to seed planning; removed the old "implementation plan" step from brainstorm.
