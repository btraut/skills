# Persona Selection

Choose reviewer personas from changed code and risk signals. No mandatory baseline personas.

## Inputs

- files changed
- lines changed
- file extensions and directories
- critical-path indicators (auth, payments, migrations, infra, public API, concurrency)
- intent keywords from context/commits

Useful checks:

```bash
git diff --shortstat <scope>
git diff --name-only <scope>
```

## Size tiers

- Tiny: `<= 4 files` and `<= 120` changed lines
- Small: `<= 15 files` and `<= 500` changed lines
- Medium: `<= 40 files` and `<= 1200` changed lines
- Large: above medium

## Dynamic selection rules

1. Score each persona in `references/personas/catalog.md` by:
   - file/path matches
   - risk signal matches
   - intent keyword matches
2. Select personas above threshold for the size tier.
3. For tiny scopes, raise threshold to avoid noisy over-review.
4. For medium/large scopes, lower threshold slightly to improve coverage.

## Team sizing by tier

- Tiny: 1-3 personas
- Small: 2-5 personas
- Medium: 4-7 personas
- Large: 6+ personas, split by domain/chunk, run in waves if needed

## Splitting strategy for large scope

When one persona is overloaded, duplicate that persona:

- split by top-level directory, service boundary, or feature area first
- keep each assignment around `<= 15 files` or `<= 400` changed lines
- keep slices disjoint
- label instances clearly (`performance-reviewer-a`, `performance-reviewer-b`)

## Sub-agent cap behavior

- If a hard cap is explicit in platform instructions, use it.
- If not explicit, assume max parallel reviewers = `6`.
- Queue remaining assignments in waves.

## User-facing preflight note

Before spawning reviewers, post a quick execution note:

```text
Swarm plan:
- Scope: <scope>
- Intent: <1-line summary>
- Reviewers: <designation -> ownership>
- Concurrency: <n at a time, waves if needed>
```

Do this as progress reporting, not a blocking confirmation step.
