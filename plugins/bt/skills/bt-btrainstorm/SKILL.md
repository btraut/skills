---
name: bt:btrainstorm
description: Explore requirements and approaches through collaborative dialogue before writing a right-sized requirements document and handing off implementation planning to bt:plan. Use for feature ideas, problem framing, vague or ambitious requests, "what should we build" conversations, or when a user wants to think through options before deciding what to build.
---

# bt:btrainstorm

Use this skill to guide a user from a rough idea to a clear requirements document. `bt:btrainstorm` answers `WHAT to build`. It should define product behavior, scope boundaries, and success criteria through collaborative dialogue, then write or update the requirements doc. It precedes `bt:plan`, which answers `HOW to build it`.

This skill does not implement code. It explores, clarifies, challenges weak framing, and produces a durable artifact for planning.

If the feature description is empty, ask: "What would you like to explore? Please describe the feature, problem, or improvement you're thinking about." Do not proceed until you have a concrete topic.

## Core Principles

1. **Scale the process to the job**
   - Small, clear work should stay light.
   - Ambiguous or cross-cutting work deserves more structure.
   - Do not add ceremony just because you can.

2. **Be a thinking partner, not a stenographer**
   - Bring alternatives.
   - Challenge bad framing.
   - Pressure-test the request instead of just extracting answers.

3. **Resolve product decisions here**
   - User-facing behavior, scope boundaries, and success criteria belong in this workflow.
   - Technical design belongs in `bt:plan` unless the brainstorm itself is about a technical product decision.

4. **Keep implementation details out unless they are the decision**
   - Avoid libraries, schemas, endpoints, file layouts, and code structure unless those are the thing being decided.

5. **Preserve momentum**
   - Ask one question at a time.
   - Keep outputs concise.
   - Move from uncertainty to clarity without meandering.

6. **Prefer simple value over speculative complexity**
   - Favor the simplest move that materially helps the user.
   - Do not gold-plate.
   - Do not reject low-cost, high-value polish just because it is not strictly necessary.

## Interaction Rules

1. **Ask one question per response**
   - Do not batch unrelated questions together.

2. **Prefer single-select multiple choice**
   - Use it when choosing one direction, one priority, or one next step.

3. **Use multi-select rarely**
   - Only use it for compatible sets like goals, constraints, or non-goals.
   - If prioritization matters, follow up by asking which selected item is primary.

4. **Use open-ended questions when options would be misleading**
   - Do not force multiple-choice structure onto fuzzy or novel answers.

5. **Mark exactly one option as recommended**
   - In Codex `request_user_input`, suffix the label with `(Recommended)`.
   - In Claude `AskUserQuestion`, use an explicit `recommended` flag when available or clearly label one option as recommended.
   - In other environments, make the recommendation explicit in the prompt or option label.

6. **Use the platform's question tool when available**
   - Prefer the blocking question tool for the current platform:
     - Codex: `request_user_input`
     - Claude Code: `AskUserQuestion`
     - Gemini: `ask_user`
   - If no blocking question tool exists, present numbered options in chat and wait for the user's reply before proceeding.

## Output Guidance

- Keep outputs concise.
- Prefer short sections and brief bullets.
- Only add as much detail as the next decision actually needs.

## Workflow

### Phase 0: Resume, Assess, and Route

Orient the conversation before you start asking questions, avoid duplicate work, and match the amount of process to the size of the idea.

1. **Look for an existing requirements doc first**
   - If the user references an existing brainstorm topic or doc, read it.
   - Otherwise, look for an obvious matching requirements doc using the repo's existing convention.
   - If no convention exists, check `docs/brainstorms/` for a likely match such as `*-requirements.md`.
   - If you find an obvious match, ask whether to resume from it or start fresh.
   - If resuming, update the existing doc instead of creating a duplicate.

2. **Check whether a full brainstorm is needed**
   - If the user already gave specific acceptance criteria, exact behavior, and tightly bounded scope, keep the interaction brief.
   - Do not force a long brainstorm when the work is already well-defined.
   - Still produce or update a short requirements doc once the understanding is clear.
   - In these cases, skip the heavy exploration steps and move quickly to either Phase 1.3 or Phase 3.

3. **Classify the scope**
   - Use the feature description plus a light repo scan to classify the work:
     - `Lightweight`: small, clear, low ambiguity
     - `Standard`: bounded feature or refactor with meaningful decisions
     - `Deep`: strategic, cross-cutting, or highly ambiguous
   - Use this classification to scale the depth of scanning, questioning, and the final doc.
   - If scope is unclear, ask one targeted question to disambiguate and then proceed.

### Phase 1: Understand the Idea

Pressure-test the request and resolve product decisions while the conversation is still flexible, so planning does not have to guess what the user meant.

1. **Scan context before asking avoidable questions**
   - Match scan depth to scope.
   - `Lightweight`: search for the topic, check whether something similar already exists, and move on.
   - `Standard` and `Deep`: do a quick constraint scan of repo instruction files and then a topic scan for relevant docs, specs, skills, or adjacent examples.
   - Do not drift into technical planning. Avoid deep dives into tests, migrations, deployment, or low-level architecture unless the brainstorm is itself about a technical decision.

2. **Pressure-test the request**
   - Match depth to scope.
   - `Lightweight`:
     - Is this solving the real user problem?
     - Are we duplicating something that already covers this?
     - Is there a clearly better framing with near-zero extra cost?
   - `Standard`:
     - Is this the right problem, or a proxy for a more important one?
     - What user or business outcome actually matters here?
     - What happens if nothing changes?
     - Is there a nearby framing that creates more value without disproportionate carrying cost?
     - Given the project state, constraints, and user goal, what is the single highest-leverage move right now: the request as framed, a reframing, one adjacent addition, a simplification, or doing nothing?
   - `Deep`:
     - Ask the `Standard` questions.
     - Also ask what durable capability this should create over the next 6-12 months.
     - Ask whether this move advances that capability or just patches a local problem.
   - Use this pressure test to sharpen the conversation, not to bulldoze the user's intent.

3. **Run the collaborative dialogue**
   - Ask one question at a time.
   - Start broad when needed: problem, users, value, constraints.
   - Narrow later: exclusions, success criteria, edge cases, tradeoffs.
   - Resolve product behavior here so `bt:plan` does not need to invent it later.
   - Surface alternatives, reframes, and tradeoffs whenever they help clarify the decision.
   - When the decision genuinely has multiple serious directions, pause the normal question flow and compare those directions directly before continuing.
   - If the user changes an earlier answer, acknowledge the change explicitly and treat it as valid.
   - If that change alters the logic of the next question, say that and ask a different next question; otherwise say that it does not change the flow and ask the same next question again.
   - Stop asking questions once the idea is clear enough to summarize confidently.

4. **Compare approaches**
   - Do this when the decision genuinely has multiple serious directions and the user would benefit from seeing them compared side by side.
   - Do not manufacture options just to look thoughtful.
   - Present 2-3 concrete directions.
   - Lead with your recommendation and explain why.
   - When useful, include one higher-upside challenger option that could materially increase usefulness, compounding value, or durability without disproportionate carrying cost.
   - Omit the challenger when the work is already over-scoped or the baseline request is clearly the right move.
   - For each option, keep it short and cover:
     - what it is
     - why it is attractive
     - what tradeoff or risk comes with it
     - when it is the right fit
   - If relevant, call out whether the choice is to reuse an existing pattern, extend an existing capability, or build something net new.
   - Stay at the product and UX level unless the brainstorm is explicitly about a technical or architectural choice.

### Phase 2: Requirements Recap

Prove shared understanding before turning the conversation into a durable artifact.

- Before writing the doc, summarize the shared understanding in plain language.
- Present the recap in sections of about `200-300 words` each rather than one long dump.
- Use chunks such as:
  - the problem being solved
  - the intended behavior
  - key scope boundaries
  - success criteria
  - unresolved questions, if any
- After each section, ask whether it matches the user's understanding before moving to the next section.
- If the user corrects a section, acknowledge the correction explicitly and, when useful, briefly restate the updated understanding so the shared understanding is visible.
- Do not reply with a lazy "got it" and move on unless the correction is truly minor.
- Incorporate each correction into the remaining recap and the final requirements doc.
- Once all recap sections are confirmed, move on to writing the requirements doc.

### Phase 3: Write or Update the Requirements Doc

Capture the decisions in a form that planning can use without re-inventing behavior, scope, or success criteria.

1. **Always produce or update the doc once the recap is confirmed**
   - Do this even for `Lightweight` work.

2. **Choose the doc location**
   - Prefer the repo's existing convention if one clearly exists.
   - Otherwise write to `docs/brainstorms/`.
   - When using the default convention, prefer a path like `docs/brainstorms/<topic>-requirements.md`.
   - Ensure the target directory exists before writing.

3. **Write a requirements doc, not an implementation spec**
   - This artifact should define `WHAT`.
   - `bt:plan` will define `HOW`.

4. **Required and optional content**
   - Required for non-trivial work:
     - problem frame
     - concrete requirements or intended behavior with stable IDs
     - scope boundaries
     - success criteria
   - Include when materially useful:
     - key decisions and rationale
     - dependencies or assumptions
     - outstanding questions
     - alternatives considered
     - high-level technical direction only when the brainstorm is inherently technical and that direction is itself part of the decision

5. **Use this standard structure and omit clearly irrelevant sections**

```md
---
date: YYYY-MM-DD
topic: <kebab-case-topic>
---

# <Topic Title>

## Problem Frame
[Who is affected, what is changing, and why it matters]

## Requirements
- R1. [Concrete user-facing behavior or requirement]
- R2. [Concrete user-facing behavior or requirement]

## Success Criteria
- [How we will know this solved the right problem]

## Scope Boundaries
- [Deliberate non-goal or exclusion]

## Key Decisions
- [Decision]: [Rationale]

## Dependencies / Assumptions
- [Only include if material]

## Outstanding Questions

### Resolve Before Planning
- [Affects R1][User decision] [Question that must be answered before planning can proceed]

### Deferred to Planning
- [Affects R2][Technical] [Question better answered during planning or codebase exploration]
- [Affects R2][Needs research] [Question likely requiring investigation during planning]

## Next Steps
[If `Resolve Before Planning` is empty: `→ bt:plan` for structured implementation planning]
[If `Resolve Before Planning` is not empty: `→ Resume bt:btrainstorm` to resolve blocking questions before planning]
```

6. **Formatting rules for the requirements doc**
   - For `Standard` and `Deep` work, use stable requirement IDs such as `R1`, `R2`, `R3`.
   - For very small requirements docs with only 1-3 simple requirements, plain bullets are acceptable.
   - Group requirements by logical theme when the work spans multiple concerns.
   - Keep the document tight. A short, sharp requirements doc beats a bloated fake PRD.
   - Do not include implementation details unless they are the subject of the decision.

7. **Handle unresolved questions explicitly**
   - Use `Resolve Before Planning` only for questions that truly block planning.
   - Put technical questions, research questions, or codebase-discovery questions under `Deferred to Planning` when they are better answered there.
   - If the user explicitly wants to proceed while blockers remain, convert each remaining item into an explicit decision, assumption, or deferred planning question before proceeding.
   - Carry deferred questions forward explicitly. Do not pretend they disappeared.

8. **Sanity check before finalizing**
   - Ask yourself:
     - Would `bt:plan` still have to invent product behavior?
     - Do any requirements depend on something claimed to be out of scope?
     - Are scope boundaries clear?
     - Are success criteria concrete?
     - Are unresolved items actually product decisions rather than planning questions?
     - Did implementation details leak in when they should not have?
     - Is there a low-cost change that would make this materially more useful?
   - If the answer is yes to the first question, the brainstorm is not done yet.

### Phase 4: Handoff

Help the user choose what to do next without forcing extra process that the current state of the work does not need.

1. **If `Resolve Before Planning` contains any items**
   - Keep asking those blocking questions by default.
   - Do not offer `Proceed to bt:plan` or `Proceed directly to work` while true blockers remain.
   - If the user explicitly wants to pause, present the brainstorm as paused or blocked rather than complete.
   - If the user explicitly wants to proceed anyway, first convert each remaining blocker into an explicit decision, assumption, or deferred planning question.

2. **Offer next-step options once the doc is ready**
   - Prefer the platform's blocking question tool when available.
   - Present only the options that actually apply:
     - `Proceed to bt:plan (Recommended)` - turn the requirements into an implementation spec and execution plan
     - `Proceed directly to work` - only when the work is `Lightweight`, success criteria are clear, scope boundaries are clear, and no meaningful technical or research questions remain
     - `Review and refine` - only when a requirements doc exists and it would benefit from another structured pass
     - `Ask more questions`
     - `Done for now`

3. **Handle the selected option**
   - If the user selects `Proceed to bt:plan (Recommended)`, immediately run `bt:plan` in the current session. Pass the requirements doc path when one exists. Otherwise pass a concise summary of finalized decisions. Do not print a closing summary first.
   - If the user selects `Proceed directly to work`, immediately run `bt:work` in the current session using the finalized brainstorm output as context. Pass the requirements doc path when one exists. Do not print a closing summary first.
   - If the user selects `Ask more questions`, return to Phase 1.3 and continue refining scope, preferences, exclusions, or edge cases one question at a time.
   - If the user selects `Review and refine`, review the requirements doc in place, strengthen weak spots, then return to the normal Phase 4 options.

4. **Closing summary**
   - Use the closing summary only when this run is ending or handing off.
   - When complete and ready for planning, display:

```text
Brainstorm complete.
Requirements doc: docs/brainstorms/<topic>-requirements.md
Key decisions:
- [Decision 1]
- [Decision 2]
Recommended next step: `bt:plan`
```

   - When paused with blocking questions still unresolved, display:

```text
Brainstorm paused.
Requirements doc: docs/brainstorms/<topic>-requirements.md
Planning is blocked by:
- [Blocking question 1]
- [Blocking question 2]
Resume with `bt:btrainstorm` when ready to resolve these before planning.
```
