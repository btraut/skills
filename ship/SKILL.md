---
name: ship
description: Commit and ship a branch to production by rebasing the current branch onto local production, fast-forwarding production, pushing both branches, and switching back to main. Use when a user asks to /ship, ship changes, ship everything, or to perform this exact production shipping workflow.
---

# Ship

Use this skill to execute the production shipping workflow the user described. There are two modes:

- **/ship changes (default)**: Commit only the changes made in this session.
- **/ship everything**: Commit all current working tree changes, even if unrelated to this session.

## Workflow

1. **Confirm current branch and repo state**
   - Run `git status -sb` and `git branch --show-current`.
   - If the current branch is `main`, proceed without asking for confirmation.
   - If the current branch is not `main`, stop and ask the user if they'd like to rebase the branch into `main` first.

2. **Select changes to commit**
   - **/ship changes**: Determine which files were touched in this session from the conversation and `git status --porcelain`.
     - Stage only those files (use explicit `git add <paths>`).
     - If you are unsure which files are in-scope, ask the user to confirm the list before staging.
     - If unrelated changes remain after staging, stash them automatically; rebases require a clean working tree.
   - **/ship everything**: Stage all changes with `git add -A`.

3. **Commit on the current branch**
   - Craft a concise commit message based on the session work.
   - If nothing is staged, stop and tell the user there is nothing to commit.
   - Commit with `git commit -m "..."`.
   - If unrelated changes are still present, stash them automatically before rebasing.

4. **Rebase current branch onto local production**
   - Ensure `production` exists locally (`git rev-parse --verify production`). If it does not, ask the user what branch to use.
   - Rebase: `git rebase production`.
   - If conflicts occur, resolve them, run `git rebase --continue`, and re-check `git status -sb`.

5. **Fast-forward production to the current branch**
   - Switch to production: `git switch production`.
   - Fast-forward merge: `git merge --ff-only <feature-branch>`.
   - If the merge is not a fast-forward, stop and ask the user how to proceed.

6. **Push both branches to origin**
   - Push feature branch: `git push origin <feature-branch>`.
   - Push production: `git push origin production`.
   - If a push is rejected due to non-fast-forward, ask before using `--force-with-lease`.

7. **Switch back to main**
   - Switch back: `git switch main`.
   - If `main` does not exist, ask which branch should be used instead.
   - If changes were stashed earlier, re-apply them on `main` and confirm `git status -sb`.

## Notes

- Keep the working tree clean between steps.
- Never force-push without explicit user confirmation.
