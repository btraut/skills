# Output Format

## Required structure (manager output)

1. Scope and intent
2. Reviewer coverage summary
3. Findings by severity (primary)
4. Domain summary (secondary)
5. Open questions or assumptions (optional)

## Template

```text
Scope: <working-copy | commit-range | path list>
Intent: <1-3 lines>

Reviewer coverage:
- <designation>: <owned files/chunk>
- ...

Findings (by severity):
P0:
- [if none, say "None"]

P1:
- [P1] <title>
  Domain: <security|performance|api|testing|maintainability|frontend|infra|data|reliability>
  File: <path:line>
  Why it matters: <impact>
  Suggested fix: <minimal change>
  Confidence: <0.50-1.00>

P2:
- ...

P3:
- ...

Domain summary:
- <domain>: <count + one-line trend>
- <domain>: <count + one-line trend>

Open questions / assumptions:
- <question or assumption>
```

## Finding requirements

- Keep findings ordered by severity then confidence.
- Every finding must include a concrete file reference.
- Every finding must include confidence.
- Omit findings below `0.50` confidence.
- Prefer short, actionable fixes over broad rewrites.

## If no actionable findings

Use:

```text
No actionable findings.
Residual risks: <short list>
Testing gaps: <short list>
```
