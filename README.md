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
4. manter as skills em português quando o uso principal for pt-BR.

## Skill inicial

- `skills/lovable-supabase-governance-audit/SKILL.md`
- `skills/system-design/system-design-alignment/SKILL.md`
- `skills/system-design/lovable-platform-architecture-review/SKILL.md`
- `skills/system-design/data-governance-and-rls-design/SKILL.md`
- `skills/system-design/observability-and-operability-design/SKILL.md`
- `skills/system-design/security-by-design-for-lovable/SKILL.md`

## Próximos passos sugeridos

- adicionar skills de CSP/XSS;
- adicionar skills de revisão de edge functions;
- adicionar skills de API design;
- adicionar skills de eventos, filas e jobs assíncronos;
- adicionar skills de revisão de logs/DevTools.
