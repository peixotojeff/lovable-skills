---
name: lovable-skills-central
description: Use when you need a Lovable-ready central catalog of reusable skills for development, system design, governance and security.
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Central de Skills Lovable

Este repositório é a fonte de verdade pronta para Lovable, com skills reutilizáveis para desenvolvimento, system design, governança e segurança.

## Objetivo

Use este repositório como um pacote importável diretamente no Lovable.
A raiz contém `SKILL.md`, então o repositório pode ser importado como está, sem script de adaptação.

## O que este pacote contém

- um catálogo central de skills;
- skills de system design;
- skills de governança e segurança;
- documentação de publicação e manutenção;
- notas auxiliares para humanos.

## Como usar

- importe a raiz do repositório no Lovable;
- mantenha o `SKILL.md` da raiz como ponto de entrada principal;
- mantenha as skills de apoio organizadas em `skills/`;
- atualize os arquivos de catálogo quando as skills mudarem.

## Arquivos canônicos

- `SKILL.md` — ponto de entrada de importação do Lovable;
- `skills/index.md` — catálogo das skills disponíveis;
- `skills-manifest.json` — inventário máquina-legível;
- `docs/` — notas de fluxo e publicação.

## Regras de manutenção

1. atualize primeiro os arquivos-fonte aqui;
2. mantenha as descrições curtas e específicas;
3. evite nomes duplicados de skill;
4. mantenha as skills de segurança e governança separadas das de plataforma;
5. preserve a importabilidade a partir da raiz do repositório.
