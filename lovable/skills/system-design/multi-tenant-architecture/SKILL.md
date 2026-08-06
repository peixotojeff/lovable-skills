---
name: multi-tenant-architecture
description: Use when designing systems that must isolate customers, workspaces or organizations.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [multi-tenant, tenancy, isolation, rls, orgs, workspace, system-design]
---

# Multi-Tenant Architecture

Use this skill when the product serves multiple customers, workspaces, teams, or organizations and must keep their data isolated.

## Purpose

Design tenant-safe systems with clear boundaries for:

- data;
- auth;
- roles;
- storage;
- background jobs;
- auditing;
- billing.

## Core questions

- What is the tenant boundary?
- Is the tenant a user, workspace, company, or account?
- Can a user belong to more than one tenant?
- Which data is tenant-scoped?
- Which admin actions cross tenant boundaries?

## Checklist

1. **Define tenant identity**
   - tenant id;
   - membership table;
   - role within tenant.

2. **Enforce isolation**
   - RLS or server-side tenant filters;
   - no cross-tenant reads by default;
   - no cross-tenant writes without explicit admin rules.

3. **Separate platform admin from tenant admin**
   - platform admin should be rare and auditable;
   - tenant admin should only manage its own workspace.

4. **Isolate storage and jobs**
   - tenant-scoped buckets or paths;
   - job payloads carry tenant id;
   - no global leaks in shared queues.

5. **Plan migrations and billing**
   - tenant creation flow;
   - tenant deletion or offboarding;
   - billing/account limits;
   - data retention by tenant.

## Red flags

- single table with no tenant scope;
- admin endpoints that can read every tenant without audit;
- user records that can be linked across tenants unexpectedly;
- job queues that ignore tenant id;
- storage paths that are globally guessable.

## Output format

Return:

- tenant model;
- isolation strategy;
- privileged roles;
- risky flows;
- migration/ops notes.
