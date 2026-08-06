---
name: lovable-supabase-governance-audit
description: Use when auditing Lovable/Supabase data governance.
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [lovable, supabase, governance, security, devtools, localStorage, rls, auth, audit, csp, xss]
---

# Lovable + Supabase Governance Audit

Use this skill when reviewing a Lovable project or any Supabase-backed web app for:

- data governance risks;
- exposure of tokens or sensitive data in browser DevTools;
- client-side storage of auth/session material;
- RLS / access-control gaps;
- insecure use of Supabase keys;
- logging/debugging leaks;
- unsafe admin/service-role usage;
- XSS / HTML-sink risks;
- weak CSP / browser hardening;
- public webhook or unauthenticated handler issues.

This is a **read-only audit skill**. Do not change code during an audit. If remediation is needed, report it separately.

## Core principle

Treat anything exposed to the browser as potentially observable in:

- DevTools;
- console output;
- network tab;
- localStorage/sessionStorage;
- page source and JS bundle;
- error boundaries and client logs.

Assume the public Supabase anon key is visible by design. The real control boundary is:

1. RLS;
2. server-side authorization;
3. server-only secrets;
4. minimal client storage.

## What to inspect

### 0) Administrative edge functions
Inspect `supabase/functions/**` for:

- `service_role` usage;
- auth/role gates;
- admin endpoints that return bulk PII;
- raw error forwarding to clients;
- logs that include emails, IDs, tokens, or payloads;
- absence of rate limits or audit trails;
- create/update/delete loops that could be abused for cost or privilege escalation.

### 0b) Front-end exposure
Inspect the browser-facing app for:

- `localStorage` / `sessionStorage` usage;
- Supabase tokens or auth state visible in DevTools;
- `dangerouslySetInnerHTML`, `ReactMarkdown`, `marked(`, `DOMPurify`, or any HTML sink;
- Content-Security-Policy in the document `<head>`;
- accidental `service_role` / admin secret exposure in the client bundle;
- public routes or webhooks that accept unauthenticated input.

### 1) Project structure
Identify, at minimum:

- `src/integrations/supabase/client.ts`
- `src/integrations/supabase/types.ts`
- auth/session modules such as `src/lib/auth-session.ts`
- `src/contexts/AuthContext.tsx`
- route guards such as `ProtectedRoute`, `AdminRoute`, `MentorRoute`, `ConsultorRoute`
- role or permission docs such as `docs/Roles.md`
- `supabase/config.toml`
- `supabase/functions/**`
- `supabase/migrations/**`
- any `.env` or build-time config files that feed the client

### 1b) High-risk data domains
If `types.ts` exposes any of these, treat them as priority RLS targets:

- `user_roles`
- `profiles`
- `gestor_permissions`
- `mentor_profiles`
- `consultor_profiles`
- any table with `cpf`, `email`, `whatsapp`, `full_name`, `access_code`, `access_token`, `share_token`, `room_slug`, `risk_scores`, `dados_brutos`, or private identifiers

For each of those tables, verify in migrations that:

- RLS is enabled;
- `FORCE ROW LEVEL SECURITY` is considered where appropriate;
- every operation has explicit `USING` and `WITH CHECK` policies;
- admin-only access is deliberately scoped;
- public tables are truly intended to be public; and
- no permissive `GRANT` accidentally bypasses the intended policy model.

### 2) Supabase client configuration
Check for:

- `import.meta.env.VITE_SUPABASE_URL`
- `import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY` or anon key
- `persistSession`
- `autoRefreshToken`
- explicit storage selection (`localStorage`, `sessionStorage`, memory)
- use of `service_role` or admin credentials in client code

### 3) Session/token storage
Look for:

- `localStorage` / `sessionStorage`
- Supabase storage prefix such as `sb-`
- cleanup logic for stale auth artifacts
- token recovery / refresh handling
- any code that serializes auth state into app storage

### 4) Access control model
Check for:

- role sources (`public.user_roles`, `profiles`, profile flags, etc.)
- guards that are only UX-level versus actual server enforcement
- RLS policies on tables that hold private data
- SECURITY DEFINER functions used for authorization
- any edge function that uses elevated privileges

### 5) DevTools / client leakage
Check for evidence of:

- sensitive data in DOM, inline scripts, or bundle constants
- debug flags or dev-only panels
- user records, tokens, API payloads, or Supabase metadata shown in console logs
- code paths that persist data in browser storage
- query results that expose more data than needed

### 6) Public webhooks / unauthenticated endpoints
Check routes or server handlers for:

- missing signature validation
- missing shared secret checks
- no replay protection / no timing-safe comparison
- any public handler that can mutate data without auth

### 7) CSP / browser hardening
Check whether the app ships a strong CSP and whether it avoids obvious footguns:

- `default-src 'self'`
- no unnecessary `unsafe-inline`
- minimal `connect-src`
- `object-src 'none'`
- `base-uri 'self'`
- `form-action 'self'`

If a CSP exists but is too loose, mark it as a mitigation item.

### 8) Secrets and keys
Treat as red flags:

- `service_role` or admin secrets in browser code
- backend keys stored in client-reachable files
- private tokens printed in logs or returned in API errors
- any secret that appears in DevTools, bundle output, or raw network responses

## Required audit output
Return findings in this order:

1. **Architecture snapshot**
   - project shape
   - auth flow
   - where Supabase is used
   - where roles/policies live

2. **Observed risks**
   - rank as high / medium / low
   - include why it matters
   - distinguish client-side exposure from true backend risk

3. **What is acceptable by design**
   - for example, public anon key in the bundle
   - why it is acceptable only if RLS is correct

4. **Remediation priorities**
   - top fixes first
   - keep them practical and ordered

5. **Future verification checklist**
   - a reusable checklist for other Lovable/Supabase projects

## Reporting format

Use a simple severity legend:

- **Verde** — audited, no action.
- **Amarelo** — mitigate soon.
- **Vermelho** — fix now.

For each red item, explain the risk clearly and keep the recommendation actionable.

## Fail-closed rules

- If you cannot inspect a file or tool output, say so explicitly.
- Do not infer that RLS is safe unless you inspected the policies or the project documentation proves it.
- Do not reveal secret values, tokens, refresh tokens, or private keys.
- If you see storage keys, report the presence and risk, not the raw values.
- Do not claim DevTools are safe because you didn’t see issues; only report what was observed.
- Do not change code during an audit; if a fix is needed, describe it separately.

## Future-project verification checklist

Use this exact order:

- identify Supabase client file
- identify auth/session storage strategy
- identify role model and guards
- inspect RLS and privileged functions
- inspect edge functions for service_role, logging and rate limits
- check for `service_role` or admin key exposure
- verify whether session data is in `localStorage`/`sessionStorage`
- inspect bundle, console, and DOM for debug leakage
- inspect CSP and HTML rendering sinks
- confirm whether any sensitive data can be seen without auth
- summarize risk and mitigation

## Suggested audit phrasing
When reporting, prefer language like:

- “public by design”
- “acceptable only if RLS is correct”
- “client-visible but not necessarily insecure”
- “high risk if XSS exists”
- “backend policy gap, not a front-end bug”

## Example one-line conclusion

“Supabase is configured in the client with public env vars and browser storage; that is acceptable only if RLS is strict, because tokens and session state are visible to DevTools and vulnerable to XSS.”
