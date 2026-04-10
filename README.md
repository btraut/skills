# Codex / Claude Agent Skills

Home for custom skills used by Codex CLI and Claude-based agents. Skills here define workflows, utilities, and helpers that can be discovered by the agents at startup.

## What’s inside
- `skills/` – standalone skills shipped directly by this repo.
- `plugins/` – plugin bundles with their own packaged skills and metadata.

Current standalone skills:
- `skills/beads-create/` – translate finalized plans/specs into Beads epics/issues and do the polish pass (clarity, sizing, acceptance criteria, deps).
- `skills/beads-implement/` – implement Beads tasks or epics from a bead id with per-task commits, strict main-agent orchestration, and per-child review gates before advancing.
- `skills/brainstorm/` – structured idea generation and spec facilitation with concise questions, explicit recommended options, and a beads-aware handoff to planning once the spec is confirmed.
- `skills/export-chatgpt/` – export a ChatGPT shared conversation to Markdown or JSON.
- `skills/review-team/` – orchestrate multi-agent code review with scope and intent discovery, deterministic preflight risk tagging, weighted persona selection, structured reviewer JSON output, merge normalization with arbitration, and action-first reporting.

## Installing these skills

```bash
npx skills add btraut/skills
```

Fallback: clone this repo locally and wire up the subdirectories your agent expects from `skills/` and `plugins/`.

## Skill versioning
Every skill directory includes a `VERSION` file containing the canonical SemVer for that skill.

- Bump `MAJOR` for breaking workflow/contract changes.
- Bump `MINOR` for backward-compatible new capability.
- Bump `PATCH` for backward-compatible fixes/clarifications.

Quickly list local skill versions:

```bash
for d in skills/*/ plugins/*/skills/*/; do
  [ -f "$d/VERSION" ] && printf "%-20s %s\n" "${d%/}" "$(cat "$d/VERSION")"
done | sort
```

## Beads integration
Use beads for work that spans sessions, has dependencies, or needs durable context. Plans should link back to the bead (design field), while beads capture milestones and decisions in notes. For small, single-session work, skip beads and keep it lightweight. The `beads-create` and `beads-implement` skills now detect whether the workspace is using classic Beads (`bd`) or beads_rust (`br`) and branch to the appropriate local skill or local CLI guidance instead of assuming one CLI.

## Changelog
- 2026-04-10: Moved standalone skills under `skills/` so the repo layout cleanly separates standalone skills from plugin bundles in `plugins/`.
- 2026-04-01: `beads-create` and `beads-implement` now detect `bd` vs `br` at runtime, keep `bd`-specific dotted-child guidance where it belongs, use `br`-specific workflow rules when the Rust tracker is installed, and prefer loaded local skills or local CLI help over web docs.
- 2026-03-15: Added `agents/openai.yaml` for `brainstorm` and `review-team`, with `allow_implicit_invocation: false` so both skills require explicit invocation in Codex.
- 2026-03-28: beads-implement now requires narrow sub-agent delegation, explicit main-agent authority over sequencing/closure/integration, and a review gate on each child bead before advancing; bumped `beads-implement` to `1.1.0`.
- 2026-03-09: README now uses a shorter `npx skills add btraut/skills` install flow as the primary path, with manual cloning kept as fallback.
- 2026-03-08: Beads-related docs now defer to `bd prime` and the official upstream GitHub repo `steveyegge/beads`; removed hard-coded local filesystem paths and repo-local workflow assumptions.
- 2026-02-27: Corrected the "What’s inside" list to match the skills currently present in this repository.
- 2026-02-25: Brainstorm skill now requires exactly one recommended option on each multiple-choice prompt (including beads/plan handoff), with explicit labeling guidance for Codex and Claude.
- 2026-02-19: Removed `plan` skill from this repository.
- 2026-02-19: Added `docs-hygiene-sweep`, `design-system-extraction-sweep`, and `ssr-first-response-audit` skills based on recurring maintenance workflows.
- 2026-02-16: Added per-skill `VERSION` files for all current skills and documented mandatory SemVer bump rules in `AGENTS.md` and this README.
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
