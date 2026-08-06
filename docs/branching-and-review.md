# Branching and Review Flow

This document describes the lightweight review process for the Lovable skills central.

## Goals

- keep `main` stable;
- review changes on a feature branch;
- avoid accidental secret leakage;
- make publication to Lovable predictable.

## Flow

1. Pull the latest `main`.
2. Create a feature branch.
3. Make the smallest useful change.
4. Update catalog files when skills change.
5. Run local guardrails.
6. Commit the feature branch.
7. Open a pull request.
8. Review the checklist.
9. Merge only after approval.
10. Sync or package for Lovable.

## Required checks

- frontmatter on every `SKILL.md`;
- matching catalog updates for catalog changes;
- no secrets in staged files;
- intentional use of `ALLOW_MAIN_PUSH=1` only when absolutely needed.

## Feature branch examples

```bash
git checkout -b feature/add-event-driven-design
```

```bash
git checkout -b docs/update-publishing-guide
```
