# Local validation (2026-11-13)

- All 240 package files matched their source snapshots byte for byte when assembled.
- `scripts/check_monorepo.py` passed: package hashes, three skill entry points, and root Markdown links.
- A full scan of relative Markdown links across the three packages found no broken local targets.
- Cognitive Partner's package validator passed 153 static checks on the current `main` snapshot. Its behavioral and human learning evaluations were not run.
- DecisionGuard's release check passed for 175 public files; its unit suite passed 149 tests.
- web-feature-demo's installation shell script passed syntax checking and `scripts/demo-kit.mjs` passed `node --check`. Its browser demo was not run here.
- License boundaries remain separate; Cognitive Partner has no selected reuse license.

This validates a source layout and local scripts. It does not prove that all three skills behave well together or that installation in every host succeeds.
