# Persona Selection

Choose reviewer personas from changed code and risk signals using deterministic scoring.

## Inputs

- files changed
- lines changed
- file extensions and directories
- preflight risk tags from `references/preflight-risk-model.md`
- intent keywords from context and commit messages

Useful checks:

```bash
git diff --shortstat <scope>
git diff --name-only <scope>
```

## Size Tiers

- Tiny: `<= 4 files` and `<= 120` changed lines
- Small: `<= 15 files` and `<= 500` changed lines
- Medium: `<= 40 files` and `<= 1200` changed lines
- Large: above medium

## Persona Scoring Formula

For each persona in `references/personas/catalog.md`:

`persona_score = path_points + risk_points + intent_points + scope_points`

Scoring components:

- `path_points`: `+3` per strong path match, `+1` per weak path match, cap `9`
- `risk_points`: `+4` per strong risk-tag mapping, `+2` per secondary mapping, cap `12`
- `intent_points`: `+2` per explicit intent keyword match, cap `4`
- `scope_points`:
  - `+2` if persona covers a declared critical path
  - `+1` for medium/large scopes where the persona reduces blind spots

## Thresholds By Size Tier

Select personas meeting these minimum scores:

- Tiny: `>= 6`
- Small: `>= 5`
- Medium: `>= 4`
- Large: `>= 3`

Fallback rule:

- If no persona meets threshold, select `correctness-reviewer.md`.

## Team Sizing By Tier

- Tiny: 1-3 personas
- Small: 2-5 personas
- Medium: 4-7 personas
- Large: 6+ personas, split by domain/chunk and run in waves

## Assignment Matrix Requirement

Before spawn, build a matrix with disjoint scope slices:

```text
- designation: <persona-instance>
  persona_file: <file>
  wave: <1..n>
  ownership: <path/commit chunk>
  risk_tags: <subset>
  focus: <1-line objective>
```

Rules:

- Keep ownership slices disjoint.
- Avoid assigning one file to multiple reviewers unless conflict arbitration is expected.
- Keep each slice around `<= 15 files` or `<= 400` changed lines for deep review.

## Splitting Strategy For Large Scope

When one persona is overloaded, duplicate that persona:

- split by top-level directory or service boundary first
- keep slices disjoint
- label instances clearly (`performance-reviewer-a`, `performance-reviewer-b`)

## Sub-agent Cap Behavior

- If a hard cap is explicit in platform instructions, use it.
- If not explicit, assume max parallel reviewers = `6`.
- Queue remaining assignments in waves.

## User-facing Preflight Note

Before spawning reviewers, post a quick execution note:

```text
Review team plan:
- Scope: <scope>
- Intent: <1-line summary>
- Preflight: <risk tags + score>
- Reviewers: <designation -> ownership>
- Concurrency: <n at a time, waves if needed>
```

Do this as progress reporting, not a blocking confirmation step.
