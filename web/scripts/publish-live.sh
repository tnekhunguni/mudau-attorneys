#!/usr/bin/env bash
# Builds the production site and pushes it to the `live` branch,
# which Plesk deploys to httpdocs on mudauattorneys.com.
# Usage (from the web/ folder):  bash scripts/publish-live.sh
# Then in Plesk: Websites & Domains > Git > Pull now.
set -euo pipefail
cd "$(dirname "$0")/.."
REMOTE=$(git remote get-url origin)
unset PUBLIC_REVIEW
npm run build
TMP=$(mktemp -d)
cp -a dist/. "$TMP/"
cd "$TMP"
git init -q -b live
git remote add origin "$REMOTE"
git fetch -q --depth 1 origin live && git reset -q --soft origin/live || true
git add -A
git commit -q -m "Publish website build ($(date "+%Y-%m-%d %H:%M"))" || { echo "Nothing changed."; exit 0; }
git push origin live
echo "Pushed. Now click 'Pull now' in Plesk (Websites & Domains > Git)."
