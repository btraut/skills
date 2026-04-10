# Severity Rubric

Use `P0-P3` only.

## P0

Critical breakage or exploitable vulnerability with major data loss, outage, or compromise.

Typical anchors:

- exploitable authz bypass on public surface
- irreversible data corruption path
- deploy path that can take production down immediately

## P1

High-impact defect likely to affect users or operations in normal usage.

Typical anchors:

- contract break for existing clients without compatibility handling
- high-probability reliability fault under expected load
- migration/deploy sequencing likely to fail in production

## P2

Moderate issue with meaningful downside (correctness risk, notable latency/cost hit, flakiness, maintainability trap).

Typical anchors:

- correctness edge case with realistic trigger
- performance regression likely visible at scale
- observability gap that blocks diagnosis of changed behavior

## P3

Low-impact issue worth fixing but not urgent.

Typical anchors:

- narrow-scope issue with limited blast radius
- minor reliability or maintainability issue with clear fix

## Scoring Rules

- Severity reflects impact if the issue is real.
- Confidence reflects certainty based on code evidence.
- Keep confidence in `0.00-1.00`.
- Report only findings with confidence `>= 0.50`.
- If impact is high but evidence is thin, keep severity and lower confidence.

## Tie-break Rules

When severity disagrees for the same issue:

1. Keep highest severity during initial merge.
2. Keep confidence from strongest evidence.
3. Run arbiter pass if disagreement is `>= 2` severity levels.
