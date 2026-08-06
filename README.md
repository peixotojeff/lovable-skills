# Lovable Skills Central

Central local para manter skills reutilizáveis do Lovable organizadas, versionadas e fáceis de atualizar.

## Objetivo

- guardar skills úteis para desenvolvimento, system design e auditoria;
- manter uma fonte única de verdade;
- facilitar revisão, versionamento e distribuição;
- permitir evolução contínua sem espalhar arquivos soltos.

## Estrutura

- `skills/` — skills organizadas por tema;
- `skills/index.md` — catálogo rápido;
- `docs/` — convenções e notas operacionais, quando necessário.

## Categorias atuais

- `audit/` — governança, segurança, DevTools, Supabase.
- `system-design/` — arquitetura, contratos, dados, observabilidade, segurança.

## Padrão de manutenção

1. cada skill deve ter um `SKILL.md` com frontmatter válido;
2. quando a skill mudar, atualizar primeiro aqui;
3. depois exportar ou sincronizar para o Lovable;
4. manter as skills em português quando o uso principal for pt-BR;
5. instalar e respeitar os guardrails locais antes de puxar ou empurrar mudanças.

## Guardrails locais

Este repositório usa hooks em `.githooks/` para simular uma proteção de branch enquanto o GitHub privado não permite branch protection nativa.

- `pre-commit`: bloqueia segredos óbvios e SKILL.md sem frontmatter mínimo;
- `pre-push`: bloqueia push direto para `main`/`master` sem `ALLOW_MAIN_PUSH=1`.

Instalação:

```bash
bash scripts/install-git-guardrails.sh
```

## Fluxo de contribuição

- `CONTRIBUTING.md` — branch, revisão e checklist de publicação;
- `docs/branching-and-review.md` — processo resumido para PRs e merge;
- `.github/PULL_REQUEST_TEMPLATE.md` — checklist que acompanha cada PR.

## Skill inicial

- `skills/lovable-supabase-governance-audit/SKILL.md`

## System design pack

- `skills/system-design/system-design-alignment/SKILL.md`
- `skills/system-design/lovable-platform-architecture-review/SKILL.md`
- `skills/system-design/data-governance-and-rls-design/SKILL.md`
- `skills/system-design/observability-and-operability-design/SKILL.md`
- `skills/system-design/security-by-design-for-lovable/SKILL.md`
- `skills/system-design/api-contract-design/SKILL.md`
- `skills/system-design/async-jobs-and-queues/SKILL.md`
- `skills/system-design/multi-tenant-architecture/SKILL.md`
- `skills/system-design/deployment-and-rollback-design/SKILL.md`

## Próximos passos sugeridos

- adicionar skills de event-driven design;
- adicionar skills de compliance/auditoria;
- adicionar skills de mobile/backend API;
- adicionar skills de feature flags e release governance.
