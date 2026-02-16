# Codex / Claude Agent Skills

Home for custom skills used by Codex CLI and Claude-based agents. Skills here define workflows, utilities, and helpers that can be discovered by the agents at startup.

## What’s inside
- `beads-create/` – translate finalized plans/specs into Beads epics/issues and do the polish pass (clarity, sizing, acceptance criteria, deps).
- `beads-implement/` – implement Beads tasks or epics from a bead id with per-task commits and minimal interruptions.
- `brainstorm/` – structured idea generation and spec facilitation with concise questions plus a beads-aware handoff to planning once the spec is confirmed.
- `export-chatgpt/` – export a ChatGPT shared conversation to Markdown or JSON.
- `plan/` – comprehensive implementation planning workflow with tasks, files to touch, tests, docs, verification steps, and beads handoff guidance (appends plans into existing specs in `docs/`).
- `review-team/` – orchestrate multi-agent code review with scope and intent discovery, deterministic preflight risk tagging, weighted persona selection, structured reviewer JSON output, merge normalization with arbitration, and action-first reporting.

## Using these skills
1) Clone or place this repo where your agent looks for skills (e.g., `$CODEX_HOME/skills`).
2) Launch Codex or Claude with skills enabled; they will auto-discover entries in this directory.
3) Follow each skill’s `SKILL.md` for usage details and any supporting assets or scripts.

## Beads integration
Use beads for work that spans sessions, has dependencies, or needs durable context. Plans should link back to the bead (design field), while beads capture milestones and decisions in notes. For small, single-session work, skip beads and keep it lightweight. Beads-related skills assume the canonical beads skill lives at `/Users/btraut/Development/skills-external/beads` for bd CLI workflow guidance.

## Changelog
- 2026-02-16: Renamed `swarm` skill to `review-team` (folder and frontmatter name) and updated identity labels across its docs/contracts.
- 2026-02-16: Review Team v2 (formerly Swarm) added deterministic preflight risk modeling, explicit persona scoring thresholds, assignment matrix planning, JSON reviewer output schema, merge normalization and arbiter-pass rules, action synthesis guidance, expanded severity/output contracts, and three new personas (correctness, dependency-supply-chain, observability) with checklist-based reviewer instructions.
- 2026-02-16: Review Team (formerly Swarm) uses dynamic persona selection without mandatory baselines, P0-P3-only outputs (no overall verdict), coherent-ahead-commit scope auto-pick rules, and confidence gating that suppresses findings below 0.50.
- 2026-02-15: Expanded swarm with scope detection rules, intent discovery, persona catalog/selection, sub-agent cap handling, and standardized reviewer/manager output templates.
- 2026-02-15: Added swarm skill for orchestrating multi-agent, persona-based code review workflows.
- 2026-02-10: Plan skill now prioritizes a beads-ready task breakdown over writing a `docs/` markdown artifact.
- 2026-02-10: beads-implement now runs `bd prime`, encourages sub-agents, and requires detailed notes in both git commits and the bead.
- 2026-02-10: Folded beads-review into beads-create; removed beads-review skill.
- 2026-02-10: Removed ship, sentry-cli, and sentry-issues-to-beads skills.
- 2026-02-05: Added export-chatgpt skill for exporting ChatGPT share links to Markdown or JSON.
- 2026-02-04: Removed ralph skill and updated beads-review guidance for multi-pass reviews.
- 2026-01-30: Brainstorm skill now routes questions through request_user_input (Codex) or AskUserQuestion (Claude).
- 2026-01-28: Beads-create now requires epic children to be created as hierarchical dotted IDs (EPIC.N).
- 2026-01-25: Ship skill now commits to local main and pushes to origin/main (no production branch).
- 2026-01-23: Updated Sentry skills to use `sentry-cli issues list` (no generic `api` subcommand).
- 2026-01-22: Added sentry-issues-to-beads skill for creating Beads from actionable Sentry issues via sentry-cli.
- 2026-01-21: Beads-implement skill now prompts a brief to-do list at the start of execution.
- 2026-01-21: Beads skills now point to the external beads skill for bd CLI workflow guidance.
- 2026-01-21: Added beads-implement skill for implementing beads tasks or epics with per-task commits.
- 2026-01-17: Brainstorm skill now avoids asking questions that can be trivially answered by inspecting the repo or using tools.
- 2026-01-16: Updated sentry-cli skill to align with official CLI docs (releases, debug files, sourcemaps, crons) and removed issue-triage API usage.
- 2026-01-16: Updated sentry-cli skill preconditions to allow `sentry-cli login` auth.
- 2026-01-16: Added sentry-cli skill for Sentry issue triage and resolution via sentry-cli.
- 2026-01-15: Beads-review skill now uses a single-pass review and points multi-pass work to ralph or re-runs.
- 2026-01-15: Plan skill now appends plans into existing specs in `docs/` and recommends beads-create handoff.
- 2026-01-15: Added beads-create skill for translating plans into Beads epics/issues.
- 2026-01-15: Added beads-review skill for polishing Beads epics/issues before implementation.
- 2026-01-13: Removed enrich-pr skill.
- 2026-01-13: Ralph skill now uses per-run IDs and context isolation to avoid contention.
- 2026-01-13: Added ralph skill for controller-driven Ralph loops with sequential subprocess prompts.
- 2026-01-12: Brainstorm skill now adds a beads handoff step with guidance for single vs epic+milestone beads.
- 2026-01-12: Plan skill now adds beads handoff guidance and a suggested bead mapping summary.
- 2026-01-07: Ship skill now auto-stashes unrelated changes and restores them after shipping.
- 2026-01-07: Ship skill now allows committing on `main` without requiring confirmation.
- 2026-01-07: Added ship skill for committing changes, rebasing onto production, fast-forwarding production, pushing both branches, and returning to main.
- 2026-01-07: Brainstorm skill now explicitly asks to hand off to plan after spec approval and provides a concise spec recap to seed planning; removed the old "implementation plan" step from brainstorm.
