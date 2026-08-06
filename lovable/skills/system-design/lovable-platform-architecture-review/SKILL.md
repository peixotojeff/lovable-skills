---
name: lovable-platform-architecture-review
description: Use when reviewing if a Lovable app can grow from landing page to platform. Check boundaries, backend needs, security and operability.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [lovable, platform, architecture, backend, scalability, review]
---

# Lovable Platform Architecture Review

Use this skill when the user says Lovable is great for landing pages, but the real challenge is turning it into a platform with durable backend structure.

## Purpose

Evaluate whether the current Lovable project is still a UI-first prototype or already needs stronger platform architecture.

## What to inspect

- domain boundaries;
- shared data model;
- auth and roles;
- admin workflows;
- background jobs;
- webhooks and integrations;
- audit trail;
- rate limits;
- deploy and rollback story;
- security surface;
- data retention and privacy.

## Questions to answer

- Which pieces can stay in the Lovable frontend?
- Which pieces need a backend service?
- Which flows require server-side validation?
- Which flows need async processing?
- Which flows need stronger auditability?
- Which modules are too risky to keep purely in the browser?

## Red flags

- all business logic in the client;
- admin logic only guarded by UI;
- direct writes to sensitive data from the browser;
- large collections of edge functions without a shared contract;
- no clear domain model;
- no rollback or audit story;
- secrets or elevated permissions in browser-reachable code.

## Output format

Return a short architecture review with:

- keep in Lovable;
- move to backend;
- needs redesign;
- should be protected immediately.

## Guidance

Lovable can accelerate:

- landing pages;
- marketing flows;
- admin dashboards;
- fast UI prototypes.

But for real platforms, always validate:

- data boundaries;
- security boundaries;
- backend contracts;
- observability;
- error handling;
- scale and maintainability.
