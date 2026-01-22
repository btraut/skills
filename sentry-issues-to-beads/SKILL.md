---
name: sentry-issues-to-beads
description: Triage Sentry issues via sentry-cli and recommend actions. Use when you want to scan unresolved issues (all projects or a specified project/issue id), decide which are actionable, detect duplicates that already have beads, and summarize what to do before asking the user to proceed.
---

# Sentry Issues To Beads

## Workflow

1. **Confirm prerequisites**
   - Ensure `sentry-cli` is installed and authenticated (`sentry-cli info`).
   - Run `sentry-cli --help` and confirm an `api` subcommand exists.
   - If org/project defaults are unclear, ask for the org slug and project slug(s).

2. **Determine scope**
   - If the user provides an issue ID, target only that issue.
   - Else if the user provides project slug(s), scope to those projects.
   - Else, use all unresolved issues across all projects in the org.

3. **Fetch issues via the Sentry API**
   - Always include `is:unresolved` in the query.
   - Use `sentry-cli api` with the syntax shown by `sentry-cli api --help` (either query params in the path or CLI flags).
   - Typical patterns:
     - List issues: `sentry-cli api 0/issues/?query=is:unresolved&project=<project>` (repeat `project=` for multiple)
     - Single issue: `sentry-cli api 0/issues/<issue_id>/`
   - If pagination is required, follow the cursor/Link headers until complete or a user-specified limit.

4. **Check for duplicates**
   - Look for existing beads that already track the issue (search by issue ID, short ID, or Sentry URL).
   - If a duplicate is found, ignore the issue and record it under a "duplicates" list with the matching bead ID.

5. **Triage for actionability**
   - Use judgment only (no hard cutoff).
   - If an issue looks non-actionable (e.g., stale, insufficient context, flake/noise), mark it as non-actionable.
   - For every non-actionable issue, record a short reason.

6. **Recommend actions (do not execute yet)**
   - For actionable issues, recommend creating one bead per issue (no epic).
   - Suggested bead fields:
     - **Title**: `Sentry: <issue title>`
     - **Description**: issue summary, shortId/id, culprit, last seen, level, environment/tags, link
     - **Design**: hypotheses about root cause + next debugging steps
     - **Acceptance**: issue resolved + validation plan (e.g., fix confirmed, no new events after deploy)

7. **Report results and ask to proceed**
   - Provide three lists:
     - **Actionable (recommend bead)** with issue links
     - **Non-actionable (recommend close/ignore)** with reasons
     - **Duplicates (already tracked)** with bead IDs
   - Summarize counts for each category.
   - Ask the user whether to proceed with actions, such as:
     - create beads for actionable issues
     - close or ignore non-actionable issues
   - If the user confirms, perform the requested actions.
