---
name: data-governance-and-rls-design
description: Use when designing data models and RLS policies for Supabase-backed apps. Focus on privacy, role boundaries and sensitive fields.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [supabase, rls, governance, data-modeling, privacy, security]
---

# Data Governance and RLS Design

Use this skill when the user needs a secure data model for Supabase or a review of how sensitive data should be partitioned and protected.

## Purpose

Design or audit:

- tables;
- roles;
- policies;
- access boundaries;
- sensitive fields;
- audit trails;
- service_role usage.

## Core checklist

1. **Classify data**
   - public;
   - internal;
   - sensitive;
   - regulated / PII;
   - secrets / tokens.

2. **Define ownership**
   - who owns the row?
   - who can read it?
   - who can write it?
   - who can approve or revoke?

3. **Separate identity from profile data**
   - auth identity;
   - application role;
   - user profile;
   - permissions matrix.

4. **Design RLS first**
   - enable RLS on sensitive tables;
   - write both `USING` and `WITH CHECK`;
   - test self-access and admin access;
   - avoid implicit public access.

5. **Protect sensitive columns**
   - prefer row-level access, but also minimize column exposure;
   - do not return more columns than needed;
   - keep tokens/codes as tightly scoped as possible.

6. **Use service_role sparingly**
   - only in server-side functions;
   - only for privileged workflows;
   - always pair with explicit authorization.

## Red flags

- role stored in profile records instead of a dedicated authorization table;
- tables with PII and no RLS;
- functions that bypass policies without validating role;
- logs containing raw sensitive payloads;
- access tokens or share tokens exposed in client queries.

## Output format

Return:

- data classes;
- ownership model;
- recommended policies;
- risky tables/columns;
- immediate fixes.

## Guardrails

- do not treat UI guards as security;
- do not assume public keys are harmless if RLS is weak;
- do not expose secret values in the output.
