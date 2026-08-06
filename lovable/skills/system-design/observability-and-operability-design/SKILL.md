---
name: observability-and-operability-design
description: Use when designing logs, metrics, alerts, retries and auditability for a Lovable-backed platform.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [observability, logging, metrics, alerts, reliability, ops]
---

# Observability and Operability Design

Use this skill when the user needs the system to be debuggable, supportable, and safe to operate.

## Purpose

Design the operational layer around the product:

- logs;
- metrics;
- alerts;
- audit trail;
- retries;
- idempotency;
- dead-letter handling;
- runbooks.

## Questions to answer

- What should be logged?
- What must never be logged?
- What alerts matter to the business?
- Which operations need retries?
- Which operations need idempotency keys?
- Which failures must be visible to an operator?

## Minimum operational design

1. **Structured logs**
   - include request id, actor, action, status;
   - do not log secrets or raw PII unless strictly required.

2. **Audit trail**
   - sensitive admin actions should land in a durable table or event store;
   - console logs are not enough.

3. **Metrics**
   - success rate;
   - error rate;
   - latency;
   - queue depth;
   - rate-limit triggers;
   - external API failures.

4. **Alerts**
   - auth failures spikes;
   - policy errors;
   - webhook failures;
   - background job retries;
   - unexpected bulk exports.

5. **Retries**
   - retry transient failures only;
   - use backoff;
   - avoid duplicating side effects;
   - make write operations idempotent.

## Red flags

- only `console.log` for important operations;
- no way to trace who did what;
- retry loops that can create duplicate records;
- silent truncation of results;
- background jobs without health signals.

## Output format

Return:

- operational risks;
- missing telemetry;
- recommended audit points;
- alert candidates;
- retry/idempotency recommendations.
