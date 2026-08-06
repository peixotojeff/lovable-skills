# Contributing to Lovable Skills Central

This repository is private and uses local guardrails to reduce accidental breakage.

## Branching model

- `main` stays protected by policy and should remain stable.
- create one feature branch per change.
- keep each branch focused on a single skill or documentation update.

Suggested branch names:

- `feature/add-api-contract-design`
- `feature/update-security-by-design`
- `docs/update-publishing-flow`

## Recommended workflow

1. sync `main` from origin.
2. create a feature branch.
3. edit the minimal files needed.
4. keep `skills/index.md` and `skills-manifest.json` aligned when skills change.
5. run the local guardrail install if needed:

```bash
bash scripts/install-git-guardrails.sh
```

6. validate the repo state:

```bash
git status --short
```

7. commit on the feature branch.
8. open a PR.
9. review the checklist in the PR template.
10. merge only after the branch is reviewed and ready.

## Review checklist

Before merging a PR, confirm:

- [ ] `SKILL.md` frontmatter is valid
- [ ] no secrets or tokens were added
- [ ] `skills/index.md` reflects the new or changed skill
- [ ] `skills-manifest.json` reflects the current catalog
- [ ] docs were updated if the workflow changed
- [ ] the change is scoped to the intended topic
- [ ] local guardrails were installed and respected

## Publication checklist

Before syncing to Lovable:

- [ ] source of truth updated in this repository first
- [ ] the target skill files are selected intentionally
- [ ] version numbers were reviewed if behavior changed
- [ ] the manifest and index are aligned
- [ ] the export/package was generated from the canonical repo
- [ ] the branch is clean
