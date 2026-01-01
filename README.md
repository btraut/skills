# Codex / Claude Agent Skills

Home for custom skills used by Codex CLI and Claude-based agents. Skills here define workflows, utilities, and helpers that can be discovered by the agents at startup.

## What’s inside
- `brainstorm/` – structured idea generation prompts and facilitation flow for exploring options quickly, with concise questions and no meta skill preambles.
- `enrich-pr/` – logging helper that keeps a running ledger of decisions, file changes, tests, and risks to streamline commit/PR summaries.
- `plan/` – comprehensive implementation planning workflow with tasks, files to touch, tests, docs, and verification steps.

## Using these skills
1) Clone or place this repo where your agent looks for skills (e.g., `$CODEX_HOME/skills`).
2) Launch Codex or Claude with skills enabled; they will auto-discover entries in this directory.
3) Follow each skill’s `SKILL.md` for usage details and any supporting assets or scripts.
