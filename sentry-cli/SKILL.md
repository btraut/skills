---
name: sentry-cli
description: Use sentry-cli for release management, debug information files/source maps, sending events, and cron monitor check-ins. Use when configuring authentication, verifying CLI setup, uploading debug files, or running monitors via sentry-cli; not for issue triage/resolution, org/team management, or billing.
---

# Sentry CLI

## Preconditions
- Ensure `sentry-cli` is installed and on PATH.
- Ensure authentication is available via either:
  - `sentry-cli login` already completed (token stored in `~/.sentryclirc`), or
  - `SENTRY_AUTH_TOKEN` set (env var or `~/.sentryclirc`).
- For Crons check-ins, ensure `SENTRY_DSN` is configured (env or `~/.sentryclirc`).
- If any preconditions are missing, stop and ask the user to fix setup.

## Safety
- Never create or rotate auth tokens.
- Never act on the wrong org/project; confirm `--org`/`--project` or defaults before running commands.
- Ask before changing or deleting releases or artifacts.

## Quick audit
- Run `sentry-cli --help` to confirm available subcommands; do not assume a generic `api` command exists.
- Run `sentry-cli info` to verify authentication, org/project defaults, and server URL.

## Core workflows

### 1) Debug information files (DIFs)
Use these commands to validate and upload debug files so events can be symbolicated.

```bash
sentry-cli debug-files check /path/to/file
sentry-cli debug-files find <debug_id>
sentry-cli debug-files upload -o <org> -p <project> /path/to/files...
```

Optional helpers:
```bash
sentry-cli debug-files bundle-sources /path/to/files...
sentry-cli debug-files upload --include-sources /path/to/files...
```

### 2) Cron monitor check-ins
Use this to run a scheduled job and emit check-ins.

```bash
sentry-cli monitors run <monitor_slug> -- <command> <args>
```

Optional schedule/config flags:
```bash
sentry-cli monitors run -s "* * * * *" -- <command> <args>
sentry-cli monitors run --check-in-margin 5 --max-runtime 30 --timezone "UTC" <monitor_slug> -- <command> <args>
```

## Optional workflows

### Releases (only if asked)
Use these to create and finalize releases. Do not invent release versions.

```bash
sentry-cli releases new <version>
sentry-cli releases set-commits --auto <version>
sentry-cli releases finalize <version>
sentry-cli deploys new --release <version> -e <environment>
```

### Source maps (only if asked)
Use the sourcemaps upload command for release artifacts.

```bash
sentry-cli sourcemaps upload /path/to/sourcemaps
```

### Sending events / logs (only if asked)
Follow the Sentry CLI docs for the exact commands; do not assume subcommands beyond what `sentry-cli --help` shows.

## Non-goals
- Issue triage/resolution via CLI subcommands.
- Org/team management, billing, or alert configuration.

## Reference
- Sentry CLI docs: https://docs.sentry.io/cli/
- Configuration and Authentication: https://docs.sentry.io/cli/configuration/
- Release Management: https://docs.sentry.io/cli/releases/
- Debug Information Files: https://docs.sentry.io/cli/dif/
- Crons (CLI): https://docs.sentry.io/cli/crons/
