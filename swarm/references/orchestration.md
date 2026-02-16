# Swarm Orchestration

## Goal

Run a serious code review by assigning specialized reviewers in parallel, then merge to one report.

## Manager sequence

1. Resolve scope (`working copy`, `unpushed commits`, or explicit range).
2. Establish intent (goal + constraints).
3. Profile size/risk and pick reviewer designations.
4. Announce the planned designations and ownership to the user.
5. Spawn reviewers within concurrency limit.
6. Merge findings, remove duplicates, normalize severity/confidence.
7. Publish the final merged report.

## Sub-agent execution rules

- Every reviewer is read-only: no code edits, no commits.
- Review only assigned scope slice.
- Follow persona instructions strictly.
- Follow shared severity rubric.
- Return findings using `references/subagent-template.md`.

## Merge rules

- Collapse duplicates; keep the clearest version.
- If severity conflicts, keep the highest severity.
- Set confidence from the strongest available evidence.
- Keep findings factual and code-grounded. If evidence is weak, lower confidence.
- Suppress findings below `0.50` confidence.
- Do not pad output with generic advice.

## Fallback behavior

- If no findings: explicitly report no actionable findings plus residual risks/testing gaps.
- If a reviewer fails or times out: continue with completed reviewers and call out the coverage gap.
