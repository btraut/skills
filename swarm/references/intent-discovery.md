# Intent Discovery

Do not review blind. First figure out what the author was trying to accomplish.

## Sources to check

1. Current conversation context
2. Commit messages in scope
3. Branch name hints
4. PR/bead/ticket references mentioned in commit text or docs
5. Nearby docs/specs if clearly linked

Useful checks:

```bash
git log --oneline --decorate <scope>
git show --stat --summary <commit>
```

## Minimal intent statement

Before spawning personas, write a 1-3 line intent summary:

- target behavior change
- key constraints (compatibility, performance, security)
- what must not regress

## If intent is unclear

Ask one direct question:

```text
I can review for correctness, but intent is unclear.
What is the primary goal of these changes?
```

Proceed after you get this answer.
