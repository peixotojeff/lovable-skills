# Lovable Skills Central

Central local para manter skills reutilizáveis do Lovable organizadas, versionadas e fáceis de atualizar.

## Objetivo

- guardar skills úteis para desenvolvimento e auditoria;
- manter uma fonte única de verdade;
- facilitar revisão, versionamento e distribuição;
- permitir evolução contínua sem espalhar arquivos soltos.

## Estrutura

- `skills/` — skills organizadas por tema;
- `skills/index.md` — catálogo rápido;
- `docs/` — convenções e notas operacionais, quando necessário.

## Padrão de manutenção

1. cada skill deve ter um `SKILL.md` com frontmatter válido;
2. quando a skill mudar, atualizar primeiro aqui;
3. depois exportar ou sincronizar para o Lovable;
4. manter as skills em português quando o uso principal for pt-BR.

## Skill inicial

- `skills/lovable-supabase-governance-audit/SKILL.md`

## Próximos passos sugeridos

- adicionar skills de CSP/XSS;
- adicionar skills de revisão de edge functions;
- adicionar skills de RLS e políticas Supabase;
- adicionar skills de revisão de logs/DevTools.
