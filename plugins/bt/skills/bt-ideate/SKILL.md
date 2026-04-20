name: bt:ideate
description: Explore an idea through collaborative dialogue without committing to a requirements document. Use when the user wants to clarify their thinking, test directions, or talk through a possible feature or improvement without deciding yet whether it should become a full project.
---

# bt:ideate

Use this skill to guide a user from a rough idea to a clearer understanding of what they might want. `bt:ideate` is for exploration, not durable artifact creation. It should help the user sharpen their thinking through focused questions, pressure-testing, and lightweight comparison of directions, then end with an in-chat summary and possible next steps.

This skill does not write files. If the user wants something durable, move into a more formal requirements flow as a next step rather than creating files here.

If the feature description is empty, ask: "What would you like to explore? Please describe the feature, problem, or improvement you're thinking about." Do not proceed until you have a concrete topic.

## Core Principles

1. **Keep it exploratory**
   - This is for clarifying thinking, not forcing commitment.
   - Do not turn a loose conversation into process theater.

2. **Use disciplined question flow**
   - Ask one question at a time.
   - Pressure-test the request.
   - Bring alternatives and tradeoffs instead of just interviewing.

3. **Stay lightweight unless the idea earns more rigor**
   - A shallow idea should stay shallow.
   - If the idea becomes substantial, surface that and suggest moving into a more formal requirements flow.

4. **Prefer shared understanding over artifact production**
   - The goal is a clearer mental model, not a requirements doc.
   - End with a summary the user can react to in chat.

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

### Phase 0: Assess and Orient

Figure out whether context matters and how much structure the conversation actually needs before you start pushing it.

1. **Decide whether repo context matters**
   - If the topic is abstract, exploratory, or product-only, skip repo scanning entirely.
   - If the topic is clearly tied to the current project, do a shallow context scan before substantive questions.

2. **When scanning, keep it light**
   - Search for the topic, related features, or obvious adjacent docs or code.
   - Skim only enough to avoid asking questions the repo can already answer.
   - Do not drift into deep implementation analysis.

3. **Check whether the user actually needs a more formal flow instead**
   - If the user is already converging on a real project, asking for durable requirements, or clearly wants something that could hand off to planning, note that a more formal requirements flow may be the better fit.
   - Do not force the switch. Keep ideating unless the user wants the more formal flow.

### Phase 1: Explore the Idea

Clarify the thinking, challenge weak framing, and surface better directions while the conversation is still exploratory.

1. **Pressure-test the request**
   - Ask whether this is the real problem or a proxy for one.
   - Ask what outcome actually matters.
   - Ask what happens if nothing changes.
   - Ask whether there is a simpler framing or adjacent move that would be more useful.
   - Use this to sharpen the conversation, not to bulldoze the user's intent.

2. **Run the collaborative dialogue**
   - Ask one question at a time.
   - Start broad when needed: problem, users, value, constraints.
   - Narrow later: preferences, exclusions, edge cases, tradeoffs.
   - Surface alternatives, reframes, and tradeoffs whenever they help clarify the direction.
   - When the idea genuinely has multiple serious directions, pause the normal question flow and compare those directions directly before continuing.
   - If the user changes an earlier answer, acknowledge the change explicitly and treat it as valid.
   - If that change alters the logic of the next question, say that and ask a different next question; otherwise say that it does not change the flow and ask the same next question again.
   - Stop asking questions once the idea is clear enough to summarize confidently, or once the user explicitly wants to move on.

3. **Compare approaches**
   - Do this when the idea genuinely has multiple serious directions and the user would benefit from seeing them compared side by side.
   - Do not manufacture options just to look thoughtful.
   - Present 2-3 concrete directions.
   - Lead with your recommendation and explain why.
   - When useful, include one higher-upside challenger option that could materially increase usefulness or reveal a better framing without disproportionate carrying cost.
   - For each option, keep it short and cover:
     - what it is
     - why it is attractive
     - what tradeoff or risk comes with it
     - when it is the right fit

### Phase 2: Shared Understanding Summary

Make the current understanding explicit so the user can confirm, correct, or sharpen it before choosing what happens next.

- Once the conversation is clear enough, explicitly switch from questions to summarizing the current understanding.
- Present the summary in sections of about `200-300 words` each rather than one long dump.
- Use sections such as:
  - the problem or opportunity being explored
  - the most promising direction or directions
  - notable constraints, tradeoffs, or open questions
  - what seems worth doing next, if anything
- After each section, ask whether it matches the user's understanding before moving to the next section.
- If the user corrects a section, acknowledge the correction explicitly and, when useful, briefly restate the updated understanding so the shared understanding is visible.
- Do not reply with a lazy "got it" and move on unless the correction is truly minor.
- Incorporate each correction into the remaining summary.
- Once all summary sections are confirmed, move on to next-step options.

### Phase 3: Next Steps

Give the user a clean choice between continuing exploration, formalizing the idea, starting implementation, or stopping without forcing an artifact.

1. **Offer lightweight next-step options**
   - Prefer the platform's blocking question tool when available.
   - Ask: "What would you like to do next?"
   - Present only the options that actually apply:
     - `Keep exploring (Recommended)` - continue the conversation and probe further
     - `Turn this into bt:btrainstorm` - move into the more formal requirements-doc flow
     - `Move toward implementation` - stop exploring and start doing the job directly in the current session
     - `Done for now`

2. **Handle the selected option**
   - If the user selects `Keep exploring (Recommended)`, return to Phase 1 and continue with one question at a time.
   - If the user selects `Turn this into bt:btrainstorm`, immediately run `bt:btrainstorm` in the current session using the clarified ideation summary as context. Do not write a file first.
   - If the user selects `Move toward implementation`, start working directly in the current session using the finalized ideation summary as context. Do not force a handoff to another skill first.
   - If the user selects `Done for now`, end cleanly with the confirmed in-chat summary.
