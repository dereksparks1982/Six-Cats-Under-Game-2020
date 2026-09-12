#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 tools/capture_web.py \
  --url "https://html-classic.itch.zone/html/2267583/index.html?v=1591301667" \
  --output offline-web

echo
echo "Capture complete."
echo "Run ./play.sh to launch the preserved web build."
