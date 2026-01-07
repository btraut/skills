---
name: brainstorm
description: Facilitate structured idea exploration and product/design specification. Use when a user wants to talk through an idea, refine it via iterative questions, and converge on a clear design/spec (and later an implementation plan), especially after inspecting the current project state.
---

# Brainstorm

Use this skill to guide a user from a rough idea to a clear design/spec by asking targeted questions, one at a time, after first inspecting the project state.

## Workflow

1. **Scan the project context**
   - Review the working directory to understand the current state, constraints, and any existing docs or code.
   - Summarize what you saw in 2-4 sentences only if it helps frame the next question.

2. **Ask refining questions (one per message)**
   - Ask exactly one question per response.
   - Prefer multiple-choice questions with 3-5 options; include an "Other: ____" option when helpful.
   - Use open-ended questions only when options would be misleading.
   - Sequence questions from highest-uncertainty to lowest-uncertainty.
   - Keep each question tightly scoped and decision-oriented.

3. **Converge on understanding**
   - Once the idea is clear enough to describe a design/spec, stop asking questions.
   - Explicitly indicate you are switching from questions to describing the design.

4. **Describe the design in sections**
   - Provide the design/spec in sections of ~200-300 words each.
   - After each section, ask whether it looks right so far before continuing.
   - Incorporate feedback and revise the next section accordingly.

5. **Confirm handoff to planning**
   - After the final spec section is approved, ask one question: whether the user wants to proceed to an implementation plan (plan skill).
   - If yes, provide a concise spec recap (goals, non-goals, UX, data/logic, constraints, acceptance criteria) to seed the plan.

## Style rules

- Ask only one question per message.
- Keep momentum: no long preambles or multi-paragraph lead-ins.
- Use concrete language and avoid filler.
- Do not announce the skill or preface with meta statements like "Using the brainstorm skill because...".
