---
name: ship
description: Commit to local main and push to origin/main. Use when a user asks to /ship, ship changes, ship everything, or to perform this exact main-branch shipping workflow.
---

# Ship

Use this skill to execute the main-branch shipping workflow the user described. There are two modes:

- **/ship changes (default)**: Commit only the changes made in this session.
- **/ship everything**: Commit all current working tree changes, even if unrelated to this session.

## Workflow

1. **Confirm current branch and repo state**
   - Run `git status -sb` and `git branch --show-current`.
   - If the current branch is `main`, proceed without asking for confirmation.
   - If `main` does not exist, ask the user which branch should be treated as `main`.
   - If the current branch is not `main`, stop and ask the user if they'd like to merge or rebase the branch into `main` first.

2. **Select changes to commit**
   - **/ship changes**: Determine which files were touched in this session from the conversation and `git status --porcelain`.
     - Stage only those files (use explicit `git add <paths>`).
     - If you are unsure which files are in-scope, ask the user to confirm the list before staging.
   - **/ship everything**: Stage all changes with `git add -A`.

3. **Commit on `main`**
   - Craft a concise commit message based on the session work.
   - If nothing is staged, stop and tell the user there is nothing to commit.
   - Commit with `git commit -m "..."`.

4. **Push `main` to origin**
   - Push: `git push origin main`.
   - If the push is rejected due to non-fast-forward, ask before using `--force-with-lease`.

## Notes

- Never force-push without explicit user confirmation.
