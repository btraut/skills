# Review Team Orchestration

## Goal

Run a serious code review by assigning specialized reviewers in parallel, then merge to one report with explicit coverage and action items.

## Manager Sequence

1. Resolve scope (`working copy`, `unpushed commits`, or explicit range).
2. Establish intent (goal plus constraints).
3. Build preflight profile and risk tags.
4. Score personas and produce assignment matrix.
5. Announce planned designations, ownership, and waves.
6. Spawn reviewers within concurrency limit.
7. Validate and normalize findings.
8. Run arbiter pass for unresolved severity conflicts.
9. Synthesize top actions and publish final merged report.

## Assignment Matrix Rules

Use one row per spawned reviewer instance:

```text
designation | persona_file | wave | ownership | risk_tags | focus
```

Requirements:

- Ownership must be disjoint across reviewers.
- One reviewer owns one scope slice.
- Duplicate personas when needed for large scope.
- Prefer path/service splits over random chunking.

## Sub-agent Execution Rules

- Every reviewer is read-only: no code edits, no commits.
- Review only assigned scope slice.
- Follow persona instructions strictly.
- Follow shared severity rubric.
- Return JSON matching `references/findings-schema.json`.

## Merge Pipeline

1. Validate each reviewer payload against `references/findings-schema.json`.
2. Discard malformed findings and report the dropped count.
3. Normalize findings with `references/merge-normalization.md`.
4. Reconcile severity and confidence.
5. Run arbiter pass when unresolved conflicts meet criteria.
6. Suppress findings below `0.50` confidence.
7. Generate grouped actions with `references/action-synthesis.md`.

## Fallback Behavior

- If no findings: explicitly report no actionable findings plus residual risks/testing gaps.
- If a reviewer fails or times out: continue with completed reviewers and call out coverage gaps.
- If arbiter cannot run: keep highest severity, lower confidence, and mark unresolved disagreement.
