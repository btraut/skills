# Scope Discovery

Pick scope in this order, then move on without dithering.

## 1) Working copy wins by default

If there are local edits (staged, unstaged, or untracked), use them as scope.

Useful checks:

```bash
git status --short
git diff --name-only
git diff --cached --name-only
```

## 2) Otherwise check unpushed commits

If working copy is clean, inspect ahead commits on current branch.

Useful checks:

```bash
git rev-parse --abbrev-ref HEAD
git rev-parse --abbrev-ref --symbolic-full-name @{u}
git rev-list --count @{u}..HEAD
git log --oneline @{u}..HEAD
```

If branch is ahead and commits are coherent, use `@{u}..HEAD` as scope.

Treat commit set as coherent when most of these are true:

- commit messages describe one feature/fix theme
- changed paths cluster in related areas
- no obvious unrelated WIP or mixed-purpose commits
- no long stack of unrelated chores jammed together

If coherence is weak, ask the user instead of guessing.

## 3) If scope is ambiguous, ask once

Ask one targeted question with options:

```text
Which scope should I review?
1) Working copy only
2) Unpushed commits on current branch
3) Specific range/path you provide
```

Do not start persona review until scope is explicit.

## 4) Record scope in final report

Always include a clear scope line such as:

- `working-copy`
- `origin/main..HEAD`
- `commit-range: <a>..<b>`
- `paths: <list>`
