---
name: ralph
description: Orchestrate a Ralph loop of sequential sub-agent runs using codex exec. Use when a user asks for /ralph N <prompt>, a ralph loop, or a multi-pass review where a controller agent composes subprocess prompts, collects outputs, and decides whether to continue or stop.
---

# Ralph Loop

Use this skill to act as the controller for a multi-pass loop. The controller runs N subprocesses via `codex exec`, gives each a structured prompt that includes the original request and the loop index, and then synthesizes outputs. Stop early if critical issues appear or recovery is impossible.

## Workflow

1. **Parse the request**
   - Expect `/ralph <count> <prompt>`.
   - If the count is missing or invalid, ask once or default to 3.
   - Preserve the original prompt verbatim.

2. **Prepare controller state**
   - Track a short `loop_context` summary after each subprocess run.
   - Define stop rules: stop if a subprocess returns `RALPH_STOP` or if you judge the loop unsafe to continue.

3. **Build the subprocess prompt**
   - Include: original prompt, loop index (1-based), total count, and current `loop_context`.
   - Require a detailed work log so the controller can evaluate the result.
   - Require an explicit stop signal when needed.

4. **Execute subprocesses sequentially**
   - Run one subprocess at a time using `codex exec`.
   - Capture the full output for review.

5. **Evaluate and decide**
   - If `RALPH_STOP` appears, stop immediately and report why.
   - Otherwise, update `loop_context` with the key deltas and proceed.

6. **Finalize**
   - Provide a consolidated summary and any changes you made.
   - Call out unresolved risks or follow-ups.

## Subprocess prompt template

Use this template (fill in the variables):

```
You are subprocess #{{index}} of {{total}} in a Ralph loop.
Original request:
{{original_prompt}}

Loop context so far:
{{loop_context}}

Do the work requested. Provide:
- DETAILED_WORKLOG: Describe what you checked and why.
- FINDINGS: Bugs, risks, or concerns.
- RECOMMENDATIONS: Concrete fixes or next steps.
- CONTROLLER_NOTES: A concise summary for the next loop.
- STOP: "NO" or "RALPH_STOP: <reason>" if critical and not recoverable.
```

## Controller stop rule

Stop the loop if any subprocess outputs `RALPH_STOP:` or if you determine the loop cannot continue safely. When you stop early, explain the exact reason and which loop index triggered it.

## Example usage (code review)

User request:

```
/ralph 5 review the uncommitted changes in git for bugs, architectural concerns, security concerns, or anything else, and then fix them
```

Controller behavior:
- Run 5 sequential subprocesses that analyze the working tree and diff.
- Synthesize results and make fixes yourself in the working tree.
- Stop early if a subprocess flags a critical, unrecoverable issue.

## Optional helper script

Use the bundled script to run a single Ralph step or to scaffold a loop. It creates a prompt file and, when `--run` is set, executes `codex exec` and checks for `RALPH_STOP`.

- Script: `ralph/scripts/ralph_step.sh`
- It creates a per-run directory at `.ralph/<run-id>/` to avoid contention between concurrent loops.
- Example (dry-run prompt generation with explicit run id):
  - `bash ralph/scripts/ralph_step.sh --index 1 --count 5 --prompt "<task>" --run-id ralph-20260113-abc --out-dir .ralph`
- Example (run one step with default run id):
  - `bash ralph/scripts/ralph_step.sh --index 1 --count 5 --prompt "<task>" --out-dir .ralph --run`

When running a full loop, the controller should update `.ralph/<run-id>/context.txt` between steps based on the latest output.
