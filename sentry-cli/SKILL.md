---
name: sentry-cli
description: Investigate, triage, and resolve Sentry issues via sentry-cli from a local developer machine. Use when listing unresolved issues, inspecting issue details/events via the Sentry API, or resolving/ignoring issues; not for org/team management, billing, or deep performance tracing.
---

# Sentry CLI

## Preconditions
- Ensure `sentry-cli` is installed and on PATH.
- Ensure authentication is available via either:
  - `SENTRY_AUTH_TOKEN` set with at least `event:read`, `project:read`, and `event:write` scopes, or
  - `sentry-cli login` already completed (token stored in the local sentry-cli config).
- If any preconditions are missing, stop and ask the user to fix setup.

## Safety
- Never create or rotate auth tokens.
- Never delete issues.
- Never act on the wrong org/project; confirm `--org`/`--project` or defaults before running commands.
- Ask before resolving large numbers of issues or using `ignored`.

## Core workflows

### 1) List important issues
Use this to find what to investigate first.

```bash
sentry-cli issues list \
  -s unresolved \
  --query "level:error" \
  --max-rows 10
```

Variants:
- Most frequent: `--query "is:unresolved order by freq"`
- Recent: `--query "lastSeen:-24h"`
- Performance: `--query "issue.category:performance"`

### 2) Inspect an issue
Sentry CLI does not have a rich issue viewer; use the API via the CLI.

```bash
sentry-cli api GET /api/0/issues/<ISSUE_ID>/
sentry-cli api GET /api/0/issues/<ISSUE_ID>/events/latest/
```

Focus on:
- `exception.values`
- `stacktrace.frames`
- `culprit`
- `tags` (especially `environment` and `release`)

### 3) Resolve or ignore an issue
Only do this after a fix is confirmed or deployed.

```bash
sentry-cli api PUT /api/0/issues/<ISSUE_ID>/ \
  -d '{"status":"resolved"}'
```

Use `ignored` only if explicitly requested.

## Optional workflows

### Releases (only if asked)
Use these to associate fixes and auto-resolve issues. Do not invent release versions.

```bash
sentry-cli releases new <version>
sentry-cli releases set-commits --auto <version>
sentry-cli releases finalize <version>
```

## Reference
- Sentry CLI docs: https://docs.sentry.io/cli/
