#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if [[ ! -f offline-web/index.html ]]; then
  echo "offline-web/index.html is missing."
  echo "Run ./tools/capture_official_web.sh first."
  exit 1
fi

PORT="${PORT:-8765}"
URL="http://127.0.0.1:${PORT}/"

python3 tools/serve.py --directory offline-web --port "$PORT" &
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null || true' EXIT INT TERM

sleep 0.8
if command -v xdg-open >/dev/null 2>&1; then
  xdg-open "$URL" >/dev/null 2>&1 || true
fi

wait "$SERVER_PID"
