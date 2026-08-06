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

- o `SKILL.md` de entrada;
- skills reutilizáveis organizadas em `skills/`.

## Como usar

- importe o diretório `lovable/` no Lovable;
- mantenha o `SKILL.md` da raiz como ponto de entrada principal;
- mantenha as skills de apoio organizadas em `skills/`;
- adicione ou remova skills apenas quando forem realmente úteis.

## Arquivos canônicos

- `SKILL.md` — ponto de entrada de importação do Lovable;
- `skills/` — skills importáveis do pacote leve.

## Regras de manutenção

1. atualize primeiro os arquivos-fonte aqui;
2. mantenha as descrições curtas e específicas;
3. evite nomes duplicados de skill;
4. mantenha as skills de segurança e governança separadas das de plataforma;
5. preserve a importabilidade a partir da raiz do repositório.
