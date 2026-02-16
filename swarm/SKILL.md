---
name: swarm
description: Run multi-agent code review by choosing reviewer personas based on change scope/risk, spawning sub-agents, and merging results into one severity-ordered report.
---

# Swarm

Use this skill when review quality matters and one reviewer would miss things.

## Load references in this order

- `references/scope-discovery.md`
- `references/intent-discovery.md`
- `references/persona-selection.md`
- `references/orchestration.md`
- `references/subagent-template.md`
- `references/severity-rubric.md`
- `references/output-format.md`
- `references/personas/catalog.md`
- Only the selected persona files in `references/personas/`

## Workflow

1. **Resolve review scope**
   - If there are working-copy changes, treat those as the default scope.
   - If working copy is clean, inspect unpushed commits and decide if they are the intended scope.
   - If scope is ambiguous, ask the user one direct question with options.

2. **Understand intent before reviewing**
   - Gather intent from conversation context, commit messages, PR/bead references, and docs.
   - If intent is still fuzzy, ask one short clarifying question.

3. **Profile change size and risk**
   - Measure file count, line count, file types, and critical paths touched.
   - Use this profile to choose personas and decide whether to split workload.

4. **Choose and announce reviewer designations**
   - Select personas from the catalog based on risk and touched domains.
   - For large scopes, duplicate personas and split files/chunks across them.
   - Before spawning, send a quick progress note listing selected designations and ownership.

5. **Spawn sub-agents with hard constraints**
   - Respect platform sub-agent limits when known.
   - If no clear limit is available, use a conservative cap of `6` concurrent sub-agents and run in waves.
   - Sub-agents are reviewers only; they do not edit code.
   - Each sub-agent must return findings in the shared template.

6. **Merge and normalize findings**
   - Dedupe overlaps.
   - Reconcile severity with `references/severity-rubric.md`.
   - If the same issue has different severities, keep the highest severity and set confidence from the strongest evidence.
   - Keep only actionable findings with code evidence.
   - Drop findings below `0.50` confidence.

7. **Produce one final report**
   - Organize primarily by severity.
   - Include a secondary domain summary.
   - Do not output an overall pass/fail verdict.
   - Keep the report issues-only.

## Non-negotiables

- No style-only nits unless they carry real operational risk.
- Every finding must include concrete file/line references.
- Every finding must include `Confidence: 0.00-1.00`.
- Suppress findings below `0.50` confidence.
- If no actionable findings exist, say so directly and list residual risks/testing gaps.
