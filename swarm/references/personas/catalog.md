# Persona Catalog

Use this file to choose reviewers. Load only personas you actually select.

## Core personas

- `testing-reviewer.md`
  - Pick for all but the tiniest one-file changes.
- `maintainability-reviewer.md`
  - Pick for anything non-trivial or cross-file.

## Domain personas

- `security-reviewer.md`
  - Pick when auth, permissions, secrets, input handling, or public endpoints are touched.
- `performance-reviewer.md`
  - Pick when data access, loops, caching, heavy transforms, or hot paths are touched.
- `api-contract-reviewer.md`
  - Pick when API shapes, shared types, interfaces, SDK contracts, or event schemas change.
- `frontend-reviewer.md`
  - Pick when UI components, styles, interaction flows, or client-side state changes.
- `infra-operations-reviewer.md`
  - Pick when CI, deployment, IaC, containers, runtime config, or observability changes.
- `data-migrations-reviewer.md`
  - Pick when DB schemas, migrations, backfills, or compatibility windows are involved.
- `reliability-reviewer.md`
  - Pick when retries, queues, concurrency, idempotency, timeouts, or failure recovery change.

## Split guidance

Duplicate personas when scope is large:

- large frontend surface -> multiple `frontend-reviewer-*`
- many services/dirs -> split by directory
- many commits -> split by commit chunk

Name duplicates with stable suffixes (`-a`, `-b`, `-c`) and explicit ownership slices.
