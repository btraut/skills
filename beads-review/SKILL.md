---
name: beads-review
description: Review, proofread, refine, and polish existing Beads epics and issues for clarity, completeness, and smooth implementation. Use after Beads have been filed, or when asked to audit/improve a Beads tracker.
---

# Beads Review

Use this skill to improve an existing Beads epic/issue set so implementers have a smooth path.

## Workflow

1. **Load the current Beads set**
   - Identify all epics and issues under review.
   - If the original plan/spec exists, keep it nearby as the source of truth.

2. **Review for clarity and completeness**
   - Fix vague titles, missing acceptance criteria, or unclear scope.
   - Ensure each issue can be done by one agent in a single task.
   - Verify dependencies, sequencing, and opportunities for parallel work.

3. **Refine and polish**
   - Add missing design notes or decision context.
   - Split oversized issues; merge duplicates; remove fluff.

4. **Single-pass review**
   - Complete one focused pass in the current context.
   - If additional passes are needed, call them out explicitly and recommend either re-running the review or using the `ralph` skill for isolated multi-pass work.

## Output expectations

- Provide a concise summary of changes and any remaining risks or open questions.
- Call out any issues that need user decisions before work begins.
