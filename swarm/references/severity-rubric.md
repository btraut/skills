# Severity Rubric

Use `P0-P3` only.

## P0

Critical breakage or exploitable vulnerability causing major data loss, outage, or compromise.

## P1

High-impact defect likely to affect users or operations in normal usage.

## P2

Moderate issue with meaningful downside (correctness risk, notable latency/cost hit, flakiness, maintainability trap).

## P3

Low-impact issue worth fixing but not urgent.

## Scoring rules

- Severity reflects impact if the issue is real.
- Confidence reflects certainty based on code evidence.
- Keep confidence in `0.00-1.00`.
- Report only findings with confidence `>= 0.50`.
- If impact is high but evidence is thin, keep severity and lower confidence.
