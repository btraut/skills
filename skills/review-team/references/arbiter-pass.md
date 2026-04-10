# Arbiter Pass

## Goal

Resolve high-impact disagreements after merge-normalization without re-running the entire review team.

## When to Run

Run arbiter only for flagged conflicts from `references/merge-normalization.md`:

- severity gap `>= 2` levels on one fingerprint
- contradictory exploitability or outage claims
- confidence spread `>= 0.35` on one fingerprint

## Arbiter Selection

- Prefer persona closest to the disputed domain.
- If dispute spans domains, use `correctness-reviewer` plus one domain co-signer.
- Arbiter is read-only and reviews only disputed snippets.

## Arbiter Input

Provide:

- disputed finding payloads
- exact file snippets and nearby lines
- original reviewer evidence
- intent summary and constraints

## Arbiter Output

Return:

- chosen severity (`P0-P3`)
- chosen confidence (`0.00-1.00`)
- concise rationale tied to code evidence
- rejected claim summary

## Finalization Rules

- Arbiter output overrides prior conflicting severity/confidence for that fingerprint.
- If arbiter fails or times out, keep highest severity and lower confidence by `0.10` (floor `0.50`).
- Record unresolved arbitration in coverage gaps.
