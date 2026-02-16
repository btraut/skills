# Merge and Normalization Rules

## Goal

Convert multiple reviewer payloads into one deduplicated, severity-consistent, confidence-gated finding set.

## Input Contract

- Reviewer output must match `references/findings-schema.json`.
- Findings without required fields are dropped.

## Normalization Steps

1. Normalize severity labels to `P0-P3`.
2. Normalize paths to stable relative forms.
3. Trim noisy title prefixes and whitespace.
4. Clamp confidence to `0.00-1.00`.
5. Suppress findings below `0.50` confidence.

## Duplicate Detection

Compute fingerprint per finding:

```text
fingerprint = normalize(file) + line_bucket(line, +/-3) + domain + normalize(title)
```

If fingerprints match, treat as one issue.

## Conflict Resolution

For duplicate findings:

- Severity: keep highest severity.
- Confidence: keep highest confidence backed by strongest evidence.
- Evidence: union unique evidence snippets.
- Suggested fix: keep the most minimal actionable fix.

## Arbitration Flagging

Mark a finding for arbiter pass when any condition holds:

- severity gap is `>= 2` levels across reviewers
- exploitability/safety claim contradicts between reviewers
- confidence spread is `>= 0.35` on the same fingerprint

Arbiter process is defined in `references/arbiter-pass.md`.

## Ordering Rules

Sort merged findings by:

1. severity (`P0`, `P1`, `P2`, `P3`)
2. confidence (descending)
3. file path
4. line number

## Coverage Gap Accounting

Always track:

- timed-out reviewers
- failed reviewers
- dropped malformed finding count
- suppressed low-confidence finding count

Include these in the final report.
