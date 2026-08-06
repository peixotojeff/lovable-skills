---
name: security-by-design-for-lovable
description: Use when reviewing auth, CSP, XSS, webhooks and secret exposure in Lovable projects.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [security, lovable, xss, csp, auth, webhooks, secrets]
---

# Security by Design for Lovable

Use this skill when the user wants to harden a Lovable project or verify that it is not safe only by accident.

## Focus areas

- authentication;
- authorization;
- browser storage;
- CSP;
- HTML injection;
- webhooks;
- secrets;
- admin endpoints;
- external integrations.

## Checklist

1. **Auth**
   - validate sessions server-side;
   - do not rely on route guards alone;
   - separate auth identity from app role.

2. **Browser storage**
   - inspect `localStorage` and `sessionStorage`;
   - assume anything there is readable in DevTools;
   - keep secrets out of the browser.

3. **CSP**
   - confirm the app has a meaningful CSP;
   - minimize inline script risk;
   - minimize external origins.

4. **XSS / HTML sinks**
   - check for `dangerouslySetInnerHTML`, markdown renderers, raw HTML, or untrusted rich text;
   - sanitize or avoid raw HTML paths.

5. **Webhooks**
   - require signature validation;
   - use timing-safe comparison;
   - defend against replay;
   - reject unauthenticated mutation.

6. **Secrets**
   - `service_role` only in server-only code;
   - no private keys in bundles;
   - no tokens in logs or UI.

7. **Admin actions**
   - require explicit privileged checks;
   - add audit trail;
   - add rate limits where abuse is possible.

## Output format

Return:

- exposed surface;
- trust boundaries;
- highest-risk findings;
- fix-now items;
- mitigation checklist.

## Guardrail

If the app is only secure because “users won’t look”, it is not secure enough.
