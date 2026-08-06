# Publishing Guide — GitHub + Lovable

This repository is the canonical source for the Lovable skills library.

## What lives here

- `skills/` — canonical skill files
- `skills/index.md` — human-readable catalog
- `skills-manifest.json` — machine-readable inventory
- `docs/` — maintenance and publishing notes

## Publish to GitHub

1. create the GitHub repository;
2. add the remote;
3. install local guardrails with `bash scripts/install-git-guardrails.sh`;
4. push `main`;
5. protect the default branch if this repo will be edited by multiple people.

Example:

```bash
git remote add origin git@github.com:YOUR_ORG/lovable-skills.git
git push -u origin main
```

## Prepare for Lovable

Lovable imports one skill package at a time.
The package must contain `SKILL.md` at the root, or inside one wrapping folder.

Recommended flow:

1. keep the canonical source here;
2. update the skill in this repository first;
3. export one skill at a time with `scripts/package_lovable_skill.py`;
4. keep `skills/index.md` and `skills-manifest.json` aligned;
5. import the generated ZIP from `dist/lovable-imports/<skill-name>.zip`.

Example:

```bash
python3 scripts/package_lovable_skill.py lovable-supabase-governance-audit
```

This produces:

- `dist/lovable-imports/lovable-supabase-governance-audit/`
- `dist/lovable-imports/lovable-supabase-governance-audit.zip`

## Versioning policy

- bump the skill version when behavior changes;
- keep descriptions short and specific;
- avoid duplicate skill names;
- prefer one skill per concern;
- keep system-design skills separate from audit/security skills.

## Recommended sync order

1. audit/security skill updates;
2. system design foundations;
3. platform hardening skills;
4. packaging/manifest update;
5. feature branch review and merge;
6. GitHub push;
7. Lovable sync/import.
