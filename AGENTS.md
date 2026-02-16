If you add, remove, or modify a skill, update the README and add an entry to the changelog.

Every skill directory must include a `VERSION` file with a SemVer value (`MAJOR.MINOR.PATCH`).

Any change inside a skill directory (`SKILL.md`, `scripts/`, `references/`, `assets/`, etc.) must include a version bump in that skill's `VERSION` file:
- `MAJOR`: breaking workflow/contract changes.
- `MINOR`: backward-compatible new capability or significant behavior expansion.
- `PATCH`: backward-compatible fixes, clarifications, or small behavior adjustments.
