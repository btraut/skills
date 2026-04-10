# Action Synthesis

## Goal

Turn merged findings into a short, prioritized action list that teams can execute immediately.

## Action Item Format

```text
[P0|P1|P2|P3] <action title>
Files: <paths>
Owner: <best-fit persona designation>
Why now: <impact in one line>
```

## Synthesis Rules

1. Group findings by root cause key:
   - domain
   - risk tag (if present)
   - normalized issue category
2. Keep the highest-severity representative per group.
3. Prefer minimal-change fixes over broad rewrites.
4. Limit to top `12` actions unless user asks for full list.

## Category to Action Mapping

- `secrets-exposure` -> remove secret from code, rotate credential, add secret scanning guard
- `authz-boundary` -> enforce server-side authorization at boundary, add denial-path test
- `public-contract` -> restore compatibility or version API/schema, add contract tests
- `data-integrity` -> sequence migration safely, add rollback/backfill validation
- `concurrency-fault` -> enforce timeout/retry/idempotency policy, add failure-mode test
- `infra-runtime` -> add rollout guard and telemetry checks, verify rollback path
- `dependency-risk` -> upgrade or pin dependency safely, capture changelog impact test
- `frontend-a11y` -> fix semantic/focus/keyboard behavior, add regression test

## Priority Assignment

- Any group with representative `P0` -> action priority `P0`
- Any group with representative `P1` -> action priority `P1`
- Any group with representative `P2` -> action priority `P2`
- Any group with representative `P3` -> action priority `P3`

## Tie-breakers

When two actions share priority, sort by:

1. higher confidence
2. broader blast radius
3. lower implementation effort for immediate risk reduction
