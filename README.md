# Agent Skills monorepo

Three independently installable skills are grouped here. Their behavior files and package-specific materials are copied from the source repositories without rewriting them. The original repositories remain available.

| Skill | Host | Install folder in this repository | License |
| --- | --- | --- | --- |
| Cognitive Partner v1.0.0 | Agent Skills hosts, including Codex | [`packages/cognitive-partner/cognitive-partner/`](packages/cognitive-partner/cognitive-partner/SKILL.md) | Selection pending; see its [`LICENSE`](packages/cognitive-partner/LICENSE) |
| DecisionGuard v0.6.1 | Agent Skills hosts, including Codex | [`packages/decisionguard/skills/decisionguard/`](packages/decisionguard/skills/decisionguard/SKILL.md) | [MIT](packages/decisionguard/LICENSE) |
| web-feature-demo v1.0.0 | Claude Code | [`packages/web-feature-demo/`](packages/web-feature-demo/SKILL.md) | [MIT](packages/web-feature-demo/LICENSE) |

Install the **folder** shown for the skill you want, not this repository root. Codex users can install either Agent Skill with:

```text
$skill-installer install https://github.com/ChoMinGi/agent-skills/tree/main/packages/cognitive-partner/cognitive-partner
$skill-installer install https://github.com/ChoMinGi/agent-skills/tree/main/packages/decisionguard/skills/decisionguard
```

For Claude Code, copy `packages/web-feature-demo/` into the Claude Code skills directory as `web-feature-demo`; its `scripts/` and `references/` must stay with `SKILL.md`. The package's own README gives its runtime requirements.

The three skills are separate tools with different purposes. This repository groups their source, documentation, and checks; it does not merge their instructions into one agent behavior. Each package retains its own evaluation and installation guidance.

See [PROVENANCE.md](PROVENANCE.md) for the source revisions, [LICENSES.md](LICENSES.md) for licensing boundaries, and [VALIDATION.md](VALIDATION.md) for local checks. Run `python3 scripts/check_monorepo.py` to verify package integrity and relative links. Package-specific checks remain in each package.
