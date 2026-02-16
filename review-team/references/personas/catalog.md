# Persona Catalog

Use this file to choose reviewers. Load only personas you actually select.

## Core Personas

- `correctness-reviewer.md`
  - Strong signals: changed branching logic, invariants, boundary conditions, data transforms.
  - Risk tags: `authz-boundary`, `data-integrity`, `public-contract`, `concurrency-fault`.
  - Intent keywords: correctness, regression, bugfix, parity.

- `testing-reviewer.md`
  - Strong signals: changed logic with sparse/weak test updates.
  - Risk tags: all, especially `public-contract` and `concurrency-fault`.
  - Intent keywords: test, coverage, reliability, regression.

- `maintainability-reviewer.md`
  - Strong signals: large refactors, duplicated logic, complexity spikes.
  - Risk tags: `dependency-risk`, `infra-runtime`.
  - Intent keywords: refactor, cleanup, simplify, ownership.

## Domain Personas

- `security-reviewer.md`
  - Pick when auth, permissions, secrets, trust boundaries, or public endpoints are touched.

- `performance-reviewer.md`
  - Pick when data access, loops, caching, payload size, or hot paths are touched.

- `api-contract-reviewer.md`
  - Pick when API shapes, shared types, interfaces, SDK contracts, or event schemas change.

- `frontend-reviewer.md`
  - Pick when UI components, styles, interactions, client state, or accessibility-sensitive flows change.

- `infra-operations-reviewer.md`
  - Pick when CI/CD, deployment, IaC, runtime config, containers, or rollback paths change.

- `data-migrations-reviewer.md`
  - Pick when DB schemas, migrations, backfills, or compatibility windows are involved.

- `reliability-reviewer.md`
  - Pick when retries, queues, concurrency, idempotency, timeouts, or partial failures change.

- `dependency-supply-chain-reviewer.md`
  - Pick when manifest/lockfiles, package upgrades, registry policies, or integrity controls change.

- `observability-reviewer.md`
  - Pick when behavior changes without clear logging/metrics/tracing/alerts coverage.

## Fallback and Coverage Rules

- If no persona crosses threshold, select `correctness-reviewer.md`.
- For non-trivial scopes, prefer at least one of: correctness, testing, or reliability.
- Avoid forcing broad baseline personas on tiny scopes when no signals exist.

## Split Guidance

Duplicate personas when scope is large:

- large frontend surface -> multiple `frontend-reviewer-*`
- many services/dirs -> split by directory/service boundary
- many commits -> split by commit chunk

Name duplicates with stable suffixes (`-a`, `-b`, `-c`) and explicit ownership slices.
