---
name: deployment-and-rollback-design
description: Use when designing safe deployment, release and rollback flows for a platform.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [deployment, rollback, release, ci-cd, system-design, reliability]
---

# Deployment and Rollback Design

Use this skill when the product needs a safer release process than "just ship it".

## Purpose

Design how the system moves from development to production with minimal risk.

## Checklist

1. **Define environments**
   - local;
   - preview;
   - staging;
   - production.

2. **Define release mechanics**
   - manual approval;
   - CI checks;
   - migration order;
   - feature flags;
   - asset/version management.

3. **Define rollback strategy**
   - app rollback;
   - migration rollback or forward-fix;
   - data migration safety;
   - feature-flag fallback.

4. **Define safety checks**
   - smoke tests;
   - health checks;
   - auth checks;
   - security checks;
   - key user journeys.

5. **Define blast radius**
   - partial deploys;
   - canary or phased rollout if relevant;
   - quick disable path for risky features.

6. **Define release observability**
   - deployment logs;
   - error spikes;
   - latency spikes;
   - rollback triggers.

## Red flags

- database changes with no rollback plan;
- production deploys without smoke tests;
- no clear owner for rollback;
- feature toggles without cleanup plan;
- releases that can break auth or payments silently.

## Output format

Return:

- environment map;
- release flow;
- rollback strategy;
- verification checks;
- high-risk release points.
