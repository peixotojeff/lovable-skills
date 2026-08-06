---
name: api-contract-design
description: Use when designing or reviewing API contracts, request/response shapes, validation and versioning.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [api-design, contracts, validation, versioning, backend, system-design]
---

# API Contract Design

Use this skill when a system needs clean API boundaries between frontend, backend, integrations, or external clients.

## Purpose

Define APIs that are:

- predictable;
- validated;
- versioned;
- secure;
- evolvable;
- testable.

## What to design

- endpoints;
- payload shapes;
- validation rules;
- error format;
- auth rules;
- pagination;
- filtering;
- idempotency;
- versioning strategy.

## Checklist

1. **Define the contract**
   - request fields;
   - response fields;
   - required vs optional;
   - field types;
   - enums and limits.

2. **Define validation**
   - server-side validation first;
   - reject unknown or malformed fields;
   - never trust client-side checks alone.

3. **Define error semantics**
   - consistent error shape;
   - actionable messages;
   - no secret leakage;
   - stable status codes.

4. **Define versioning**
   - backward compatibility;
   - breaking-change strategy;
   - deprecation plan.

5. **Define access control**
   - public vs authenticated vs privileged;
   - role-based restrictions;
   - row ownership rules;
   - rate limiting where needed.

6. **Define operational behavior**
   - idempotency keys for writes;
   - pagination for lists;
   - limits for exports;
   - timeouts and retries.

## Red flags

- free-form payloads with no schema;
- response shapes that change silently;
- error messages that expose internals;
- missing auth rules on sensitive endpoints;
- list endpoints without pagination.

## Output format

Return:

- endpoint list;
- request/response model;
- validation rules;
- auth rules;
- versioning plan;
- risks.
