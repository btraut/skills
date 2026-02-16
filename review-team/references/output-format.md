# Output Format

## Required Structure (manager output)

1. Scope and intent
2. Preflight profile
3. Reviewer coverage matrix
4. Findings by severity (primary)
5. Top fix actions
6. Domain summary (secondary)
7. Coverage gaps and suppressed findings summary
8. Open questions or assumptions (optional)

## Template

```text
Scope: <working-copy | commit-range | path list>
Intent: <1-3 lines>

Preflight profile:
- Files changed: <n>
- Lines changed: <n>
- Risk tags: <ordered list>
- Preflight score: <n>

Reviewer coverage:
- <designation> (<persona>): <ownership>
- ...

Findings (by severity):
P0:
- [if none, say "None"]

P1:
- [P1] <title>
  Domain: <security|performance|api|testing|maintainability|frontend|infra|data|reliability|correctness|dependency|observability>
  File: <path>
  Line: <n>
  Why it matters: <impact>
  Suggested fix: <minimal change>
  Evidence: <short evidence>
  Confidence: <0.50-1.00>

P2:
- ...

P3:
- ...

Top fix actions:
- [P0|P1|P2|P3] <action>
  Files: <paths>
  Owner: <designation>
  Why now: <impact>

Domain summary:
- <domain>: <count + one-line trend>
- <domain>: <count + one-line trend>

Coverage gaps:
- Reviewer failures/timeouts: <list or none>
- Dropped malformed findings: <count>
- Suppressed low-confidence findings: <count>

Open questions / assumptions:
- <question or assumption>
```

## Finding Requirements

- Keep findings ordered by severity then confidence.
- Every finding must include concrete file and line references.
- Every finding must include evidence and confidence.
- Omit findings below `0.50` confidence.
- Prefer short, actionable fixes over broad rewrites.

## If No Actionable Findings

Use:

```text
No actionable findings.
Residual risks: <short list>
Testing gaps: <short list>
Coverage gaps: <short list>
```
