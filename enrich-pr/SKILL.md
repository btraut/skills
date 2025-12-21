---
name: enrich-pr
description: Maintain a running ledger of session decisions, touched files, tests, and risks; use it later to draft high-quality commit messages and PR descriptions when the user asks to commit or open a PR (GitHub/Phabricator/etc.).
---

# Enrich PRs

Use this skill at the start of a coding session that might end with a commit or PR.

## Ledger setup (start of session)

- Create a plain-text ledger outside the repo, e.g., `/tmp/codex-ledger-<timestamp>-<random>.log`. Persist the chosen path in conversation notes and reuse it for the session.
- If a ledger path already exists in context, append to it rather than replacing it.
- Keep entries chronological and append-only; prefer concise bullet lines.

### If invoked late in the session

- Quickly reconstruct missing history: scan the current conversation, recent commands, and diffs to seed the ledger with a short catch-up block.
- Ask the user for a 3-5 bullet recap of what was done and what is untested; log it verbatim with a timestamp.
- Note any uncertainty ("possible gap: tests for workers not run") so it surfaces in the final commit/PR text.

## What to log (append after meaningful actions)

- **Decisions**: architecture choices, trade-offs, rejected options (note the why).
- **Changes**: files touched with short rationale (`file: change | reason`).
- **Tests**: what was run, results, and gaps still untested.
- **Risks**: potential regressions, perf/infra concerns, data safety.
- **Follow-ups/TODOs**: remaining work, docs to update, questions for the user.
- **Context**: env/setup steps, commands run, external references if relevant.

## Lightweight entry format (example)

- `[2025-12-21 14:05] change apps/api/src/routes/vision.ts: add SSE endpoint guard | prevents duplicate stream start`
- `[2025-12-21 14:07] test pnpm test vision --filter vision-route (pass)`
- `[2025-12-21 14:10] risk OCR queue throughput could drop if pubsub backpressure; monitor queue depth`

## Working guidance

- After each code edit or test run, add an entry immediately.
- When responding to the user, you can summarize, but always record the raw details in the ledger.
- Avoid leaking the ledger contents into normal replies unless the user asks or it is needed for clarity.

## When the user asks to commit

- Read the ledger and produce a commit title (<72 chars) plus a body describing key changes, rationale, tests (pass/fail), and known risks or TODOs.
- If multiple discrete concerns exist, suggest splitting commits; draft titles/bodies for each.

## When the user asks to open a PR

- Use the ledger to draft a PR description that helps reviewers:
  - Summary of changes and intent
  - Key files/sections to review first
  - Risks and mitigations
  - Test coverage and gaps
  - Follow-ups or deployment notes
- Tailor to the target tool (GitHub CLI, MCP, Phabricator) but keep content tool-agnostic unless specified.

## Housekeeping

- Keep the ledger path visible in conversation for transparency.
- Do not store secrets or user data in the ledger.
- If the session restarts without the ledger path, propose recreating it and continuing.
