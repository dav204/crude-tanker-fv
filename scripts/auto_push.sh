#!/bin/bash
# Auto-push (owner ruling 2026-09-10: "yes" to pushing without a hand on the keyboard).
# Pushes main ONLY when the repo is in a state a human would have pushed: unpushed commits
# exist, the working tree carries nothing but automation drift, and the drift gate reads
# 0 UNEXPLAINED. Anything else is left alone and noted — a push is never a way past a red gate.
set -u
cd "$(dirname "$0")/.." || exit 1
ahead=$(git rev-list --count origin/main..HEAD 2>/dev/null || echo 0)
[ "$ahead" -gt 0 ] || { echo "[auto-push] nothing to push"; exit 0; }
allowed=$(grep -v '^#' scripts/drift_files.txt 2>/dev/null | sed '/^$/d')
dirt=$(git status --porcelain | awk '{print $2}' | while read -r f; do echo "$allowed" | grep -qx "$f" || echo "$f"; done)
[ -z "$dirt" ] || { echo "[auto-push] HELD: non-drift dirt in the tree: $(echo "$dirt" | tr '\n' ' ')"; exit 3; }
gate=$(PYTHONPATH=src ./.venv/bin/python -m crude_tanker_fv.drift_gate 2>&1 | grep -E "rows:" || true)
echo "$gate" | grep -q " 0 UNEXPLAINED" || { echo "[auto-push] HELD: gate not clean — $gate"; exit 4; }
if git push origin main; then
  echo "[auto-push] pushed $ahead commit(s): $(git log --oneline -1 | cut -c1-80)"
else
  echo "[auto-push] push FAILED (auth? network?)"; exit 5
fi
