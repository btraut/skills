# Preflight Risk Model

## Goal

Create a deterministic risk profile before persona selection. This profile drives reviewer scoring, ownership slicing, and wave planning.

## Inputs

- changed files (`git diff --name-only <scope>`)
- shortstat (`git diff --shortstat <scope>`)
- changed line counts per file
- path and extension signals
- added-line pattern signals from diff content

## Path Priority Bands

Assign each changed file to one band:

- `critical` (`+5`): auth, permissions, secrets, payment, billing, crypto
- `high` (`+4`): public API, database schema/migrations, runtime config, infra
- `medium` (`+3`): business logic services/controllers/handlers
- `low` (`+1`): tests/docs/stories/fixtures only
- `default` (`+2`): everything else

Use highest matching band per file.

## Risk Tags

Apply these tags from file paths and added-line evidence:

- `authz-boundary`: authn/authz paths, permission checks, identity/session/token handling
- `data-integrity`: migrations, schema transforms, backfills, correctness-sensitive data writes
- `public-contract`: API route/interface/schema/event changes with external clients
- `concurrency-fault`: retries, queues, locks, idempotency, async ordering, timeout handling
- `infra-runtime`: CI/CD, IaC, runtime config, deployment/rollback, observability wiring
- `secrets-exposure`: hardcoded credentials/tokens, unsafe logging of sensitive data
- `dependency-risk`: lockfile churn, dependency upgrades, supply-chain sensitive changes
- `frontend-a11y`: interaction, state flow, keyboard/focus/semantic and responsive UI behavior

## Added-Line Hazard Heuristics

Treat matches as risk-tag boosters, not final findings:

- hardcoded secret literals -> `secrets-exposure`
- SQL string concatenation -> `authz-boundary` and `data-integrity`
- disabled security/lint safeguards -> relevant domain tag
- debug stubs in critical paths -> domain tag and confidence warning

## Preflight Score

Calculate:

- `size_score`: small(1), medium(2), large(3)
- `path_score`: sum of top 20 file band values
- `tag_score`: sum of unique risk-tag weights
  - `authz-boundary` +4
  - `data-integrity` +4
  - `public-contract` +3
  - `concurrency-fault` +4
  - `infra-runtime` +3
  - `secrets-exposure` +4
  - `dependency-risk` +2
  - `frontend-a11y` +2

`preflight_score = size_score + path_score + tag_score`

Use this score only to tune reviewer depth and wave count. Do not map directly to report severity.

## Persona Boosts From Risk Tags

- `authz-boundary` -> security, reliability, correctness
- `data-integrity` -> data-migrations, reliability, testing, correctness
- `public-contract` -> api-contract, testing, correctness
- `concurrency-fault` -> reliability, performance, testing
- `infra-runtime` -> infra-operations, observability, reliability
- `secrets-exposure` -> security, dependency-supply-chain
- `dependency-risk` -> dependency-supply-chain, security, maintainability
- `frontend-a11y` -> frontend, testing

## Required Preflight Artifact

Record this before spawning:

```text
Preflight profile:
- Scope: <scope>
- Files changed: <n>
- Lines changed: <n>
- Risk tags: <ordered list>
- Preflight score: <n>
- Suggested depth: <light|standard|deep>
- Suggested concurrency: <n>
```

## Guardrails

- Preflight tags are routing hints, not findings.
- Never emit findings without code-grounded evidence.
- Never let heuristic hits bypass confidence gating.
