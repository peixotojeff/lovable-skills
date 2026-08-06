---
name: system-design-alignment
description: Use when turning an idea into system design. Translate product goals into boundaries, NFRs, data flows and architecture.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [system-design, architecture, requirements, nfr, product, backend]
---

# System Design Alignment

Use this skill when the user has a product idea, platform request, or feature brief and needs it aligned into a system design that is realistic, secure, and buildable.

## Goal

Transform vague product intent into:

- clear scope;
- domain boundaries;
- functional requirements;
- non-functional requirements;
- data and integration flows;
- risks and trade-offs;
- an architecture that can survive real usage.

## When to use

- the user asks for system design;
- a Lovable prototype is becoming a real product;
- a landing page must evolve into a platform;
- the team needs architecture alignment before coding.

## Procedure

1. **Define the real outcome**
   - What user problem is being solved?
   - What success looks like?
   - What is in scope and out of scope?

2. **Identify actors and use cases**
   - end user;
   - admin;
   - operator;
   - automation / webhook / batch job.

3. **Extract constraints**
   - auth model;
   - data sensitivity;
   - scale assumptions;
   - latency expectations;
   - audit/compliance needs;
   - budget and team size.

4. **Break the system into domains**
   - auth;
   - core business domain;
   - storage;
   - async processing;
   - notifications;
   - observability;
   - admin tooling.

5. **Define NFRs**
   - availability;
   - reliability;
   - security;
   - maintainability;
   - cost;
   - performance;
   - data retention.

6. **Recommend architecture shape**
   - monolith vs modular monolith vs services;
   - synchronous vs async;
   - event-driven where useful;
   - managed services vs custom infra.

7. **Surface trade-offs**
   - speed vs rigor;
   - flexibility vs simplicity;
   - low code vs control;
   - short-term delivery vs long-term safety.

## Output format

Return:

- problem statement;
- assumptions;
- bounded scope;
- proposed architecture;
- risks;
- next build steps.

## Guardrails

- do not assume the prototype architecture is enough for production;
- do not hide missing requirements;
- do not design security last;
- if the user is vague, ask for the missing system constraints before finalizing.
