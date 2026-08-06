# Local Git Guardrails

This repository uses local hooks to mimic a lightweight branch-protection policy while keeping the GitHub repository private.

## What is enforced

- direct pushes to `main` / `master` are blocked unless explicitly allowed;
- staged secrets are blocked from commit;
- skill files must keep `name:` and `description:` frontmatter.

## Install

Run:

```bash
bash scripts/install-git-guardrails.sh
```

This sets `core.hooksPath=.githooks` for the repo.

## Push to protected branch intentionally

```bash
ALLOW_MAIN_PUSH=1 git push
```

## Notes

- This is a local safety net, not server-side branch protection.
- Keep the repo private if you do not want public exposure.
- Review `ALLOW_MAIN_PUSH=1` usage carefully to avoid bypassing the guardrail by accident.
