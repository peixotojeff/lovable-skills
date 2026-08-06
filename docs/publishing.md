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

## Preparar para o Lovable

O alvo leve recomendado para importação é `lovable/`.
Esse subdiretório contém apenas o essencial: `SKILL.md` na raiz e as skills que realmente valem ficar no pacote importável.

Fluxo recomendado:

1. mantenha a fonte canônica no repositório raiz;
2. atualize os arquivos canônicos primeiro;
3. importe `lovable/` no Lovable;
4. use `skills/index.md` e `skills-manifest.json` só no repositório raiz, como apoio humano e de manutenção;
5. use o script opcional somente se quiser gerar um ZIP de uma skill individual.

Destino direto de importação:

- `lovable/`
- ou um ZIP gerado a partir de `lovable/`, preservando `SKILL.md` na raiz do arquivo

Exportação opcional de skill individual:

```bash
python3 scripts/package_lovable_skill.py lovable-supabase-governance-audit
```

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
