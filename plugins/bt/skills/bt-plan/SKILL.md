---
name: bt:plan
description: Transform requirements, clarified ideas, bug reports, or improvement requests into structured implementation plans grounded in repo patterns. Use when the user wants a durable plan of work with PR-sized tasks, explicit dependencies, and a clear path to implementation.
argument-hint: "[requirements doc, feature description, bug report, or improvement idea]"
---

# Create an implementation plan

## Introduction

**Note: The current year is 2026.** Use this when dating plans and searching for recent documentation.

Transform a clarified idea, requirements document, bug report, or improvement request into a structured implementation plan. The durable output of this workflow is a plan document in `docs/plans/`. The plan should be specific enough that implementation can proceed without re-inventing the approach, but not so bloated that it becomes fake process.

The plan should break work into tasks that make good PR-sized units, with clear dependencies and explicit notes about what can run in parallel.

## Feature Description

<feature_description> #$ARGUMENTS </feature_description>

**If the feature description above is empty, ask the user:** "What would you like to plan? Please describe the feature, bug fix, or improvement you have in mind."

Do not proceed until you have a clear input to plan from.

## Phase 0: Gather the Right Starting Context

Use the strongest available input. Prefer durable upstream artifacts when they exist.

### 0.1 Check for a requirements document first

Before asking refinement questions, look for recent requirements documents in `docs/brainstorms/` that match the feature:

```bash
ls -la docs/brainstorms/*-requirements.md 2>/dev/null | head -10
```

**Relevance criteria:** A requirements document is relevant if:
- The topic from the filename or frontmatter semantically matches the feature description
- It was created within the last 14 days
- If multiple candidates match, use the most recent one

**If a relevant requirements document exists:**
1. Read it thoroughly.
2. Announce: "Found source document from [date]: [topic]. Using it as the foundation for planning."
3. Carry forward all materially relevant content into the plan:
   - key decisions and rationale
   - chosen approach and why alternatives were rejected
   - problem framing, constraints, and requirements
   - outstanding questions, preserving whether they block planning or are intentionally deferred
   - success criteria and scope boundaries
   - dependencies and assumptions
   - any high-level technical direction only when the source document is inherently technical
4. Skip the refinement questions below unless the source document still leaves important ambiguity.
5. Use the source document as the primary input to research and planning.
6. Reference carried-forward decisions with `(see origin: <source-path>)` where useful so the plan does not lose context.
7. If `Resolve Before Planning` contains any items, stop. Tell the user planning is blocked by unanswered brainstorm questions and direct them to resume `bt:btrainstorm` or answer those questions first.

**If multiple source documents could match:**
- Ask the user which source document to use, or whether to proceed without one.

### 0.2 If no requirements document exists, refine the input just enough

If no relevant requirements document is found, refine through collaborative dialogue:

- Ask questions one at a time.
- Prefer multiple choice when natural options exist.
- Focus on understanding purpose, constraints, risks, and success criteria.
- Continue until the idea is clear enough to plan, or the user says to proceed.

If the feature description is already detailed, offer:
"Your description is already clear. Should I proceed with research, or would you like to refine it further?"

### 0.3 Gather signals for research depth

During refinement and source review, note:
- **User familiarity**: do they know the codebase patterns, or point to examples?
- **User intent**: speed vs thoroughness, exploration vs execution
- **Topic risk**: security, payments, auth, data migrations, external APIs deserve more caution
- **Uncertainty level**: is the approach clear or open-ended?

## Phase 1: Local Research

Understand the local codebase before deciding whether external research is worth it.

### 1.1 Repo research

Research the repository directly. Look for:
- technology stack and versions
- architectural patterns
- existing implementations similar to the requested work
- conventions in `AGENTS.md` and any relevant local instruction files
- nearby plans, brainstorms, specs, or docs

Capture:
- relevant file paths
- useful examples
- repo conventions that should shape the plan

### 1.2 Internal documentation and prior decisions

If the repo contains internal documentation about prior decisions, solved problems, architectural notes, or implementation lessons, search it for relevant gotchas, patterns, and context worth carrying forward.

If nothing useful is found, say so and move on.

## Phase 2: Decide Whether External Research Is Needed

Decide explicitly whether outside research adds value.

**Always research externally for high-risk topics** such as:
- security
- payments
- auth and trust boundaries
- data privacy
- unfamiliar external APIs

**Usually skip external research when:**
- the codebase already contains strong local patterns
- repo guidance is clear
- the user already knows the desired approach
- external research would add little beyond what the repo already tells you

**Do external research when:**
- the codebase has no useful examples
- the user is exploring or uncertain
- the work depends on framework behavior or third-party APIs that could be misremembered
- current best practices materially affect the plan

Announce the decision briefly, then proceed.

### 2.1 External research, when warranted

If external research is justified:
- use primary sources first, especially official framework or library docs
- gather best practices and recent guidance relevant to the feature
- capture only the findings that materially affect implementation choices, constraints, or sequencing

## Phase 3: Consolidate Research

Summarize the planning inputs before writing the plan:
- relevant internal file paths and patterns
- institutional learnings, if any
- external docs or best practices, if used
- key constraints from `AGENTS.md` or related instruction files
- related issues, plans, or PRs discovered

If something looks materially uncertain, say so before proceeding.

## Phase 4: Shape the Plan

Think like an implementation lead, not a product manager performing theater.

### 4.1 Title and file naming

- Draft a clear, searchable title using conventional prefixes such as `feat:`, `fix:`, or `refactor:`
- Determine the plan type: enhancement, bug fix, refactor, migration, or similar
- Convert the title into a filename:
  - scan `docs/plans/` for files matching today's date pattern `YYYY-MM-DD-\d{3}-`
  - find the highest existing sequence number for today
  - increment by 1, zero-padded to 3 digits
  - use a descriptive kebab-case name with `-plan` suffix
  - example: `feat: Add user authentication` -> `2026-03-31-001-feat-add-user-authentication-plan.md`

### 4.2 Break the work into implementation units

The heart of the plan is the task breakdown.

For each planned task:
- keep it small enough to make a good PR-sized unit
- make ownership boundaries obvious
- state what depends on what
- call out what can run in parallel
- define what "done" means for that unit

Use these heuristics:
- prefer linear sequencing when tasks genuinely build on one another
- call out parallelizable work explicitly when the write scopes or responsibilities are separate
- split oversized tasks until they feel like something one strong agent or engineer could finish without thrashing
- do not create fake parallelism when the tasks are tightly coupled

### 4.3 Validate plan quality before writing

Before you write the plan, check:
- does the task breakdown reflect the chosen approach?
- are dependencies explicit rather than implied?
- would each task make a sane PR?
- are risky or foundational tasks front-loaded?
- does the plan include necessary validation, rollout, and cleanup work?
- would implementation still have to invent major execution structure?

If the answer to the last question is yes, the plan is not ready yet.

## Phase 5: Choose Detail Level

Select the level that best fits the size and risk of the work.

### `Lean`

- Use this for small bugs, narrow improvements, and straightforward features.
- Load [lean-template.md](./references/lean-template.md) and follow it.

### `Standard`

- Use this for most features, complex bugs, and changes spanning multiple units of work.
- Load [standard-template.md](./references/standard-template.md) and follow it.

### `Comprehensive`

- Use this for major features, architectural changes, complex integrations, and risky migrations.
- Load [comprehensive-template.md](./references/comprehensive-template.md) and follow it.

Prefer the simplest level that still does the job.

## Phase 6: Write the Plan File

**This step is mandatory.** `bt:plan` exists to create a plan document.

Write the plan file to `docs/plans/` before presenting any options.

```bash
mkdir -p docs/plans/
today=$(date +%Y-%m-%d)
last_seq=$(ls docs/plans/${today}-*-plan.md 2>/dev/null | grep -oE "${today}-[0-9]{3}" | tail -1 | grep -oE '[0-9]{3}$')
next_seq=$(printf "%03d" $(( ${last_seq:-0} + 1 )))
```

Use the final filename format:

```text
docs/plans/YYYY-MM-DD-NNN-<type>-<descriptive-name>-plan.md
```

Examples:
- `docs/plans/2026-03-31-001-feat-user-authentication-plan.md`
- `docs/plans/2026-03-31-002-fix-checkout-race-condition-plan.md`

Confirm: "Plan written to docs/plans/[filename]"

## Phase 7: Offer Next Actions

After writing the plan, detect whether Beads tooling exists:

```bash
command -v bd >/dev/null 2>&1 && echo bd
command -v br >/dev/null 2>&1 && echo br
```

Use the platform's blocking question tool when available. Ask:

`Plan ready at docs/plans/YYYY-MM-DD-NNN-<type>-<name>-plan.md. What would you like to do next?`

Present only the options that actually apply:
- `Open plan in editor`
- `Review and refine`
- `Create beads from this plan` — only if `bd` or `br` is installed
- `Start bt:work`
- `Done for now`

### Handle the selected option

- **Open plan in editor**: open the plan file in the user's default editor.
- **Review and refine**: review the plan in place, improve weak sections, and then return to the options.
- **Create beads from this plan**:
  - If `bd` or `br` usage details are unclear, consult the official Beads guidance first.
  - Translate the plan into epics and issues with this quality bar:
    - epics map to milestones or major deliverables
    - tasks are concrete and small enough for one agent or engineer
    - dependencies and opportunities for parallel work are explicit
    - split oversized tasks
    - polish titles, acceptance criteria, and design notes
    - when using `bd` and an epic has child tasks, prefer hierarchical dotted IDs like `EPIC.1`, `EPIC.2`
  - After creating beads, provide a concise mapping of what was created and any blockers or confirmations needed.
- **Start bt:work**: immediately begin work from the plan in the current session.
- **Done for now**: stop after confirming the plan path.

NEVER CODE while running `bt:plan`. Research, synthesize, and write the plan only.
