Every skill directory must include a `VERSION` file with a SemVer value (`MAJOR.MINOR.PATCH`).

Do not update README files, changelog entries, or skill `VERSION` files during incremental work.
Only do that once the change set is actually being finalized for commit or PR scope.

When it is time to finalize:
- Update the relevant README documentation for released user-facing changes.
- Add a changelog entry if the change belongs in the changelog.
- Bump the affected skill `VERSION` file exactly once for the final scoped change set:
  - `MAJOR`: breaking workflow/contract changes.
  - `MINOR`: backward-compatible new capability or significant behavior expansion.
  - `PATCH`: backward-compatible fixes, clarifications, or small behavior adjustments.
