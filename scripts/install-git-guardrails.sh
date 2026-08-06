#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

chmod +x .githooks/pre-commit .githooks/pre-push

git config core.hooksPath .githooks

echo "Installed git guardrails with core.hooksPath=.githooks"
