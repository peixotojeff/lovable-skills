---
name: async-jobs-and-queues
description: Use when designing background jobs, queues, retries and event-driven processing.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [async, jobs, queues, events, retries, background-processing, system-design]
---

# Async Jobs and Queues

Use this skill when the system needs work that should not happen in the request/response path.

## Purpose

Design safe asynchronous processing for:

- heavy tasks;
- third-party integrations;
- email or notifications;
- data enrichment;
- report generation;
- scheduled work;
- workflow orchestration.

## Checklist

1. **Classify the work**
   - synchronous user-facing;
   - async but immediate feedback;
   - scheduled;
   - event-triggered;
   - manual retry.

2. **Choose the queue model**
   - simple job table;
   - managed queue;
   - event stream;
   - cron/scheduler.

3. **Design idempotency**
   - job key;
   - deduplication;
   - safe retry semantics;
   - no duplicate side effects.

4. **Design retries**
   - exponential backoff;
   - transient vs permanent failures;
   - dead-letter or failure table.

5. **Design observability**
   - job status;
   - attempt count;
   - last error;
   - timestamps;
   - owner/actor.

6. **Design isolation**
   - no secret leakage to the client;
   - server-side credentials only;
   - limited blast radius.

## Red flags

- long tasks in the browser;
- duplicate jobs without deduplication;
- no retry policy;
- no failure visibility;
- jobs that mutate data without audit trail.

## Output format

Return:

- job types;
- queue choice;
- retry model;
- idempotency model;
- failure handling;
- operational risks.
