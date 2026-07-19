#!/usr/bin/env bash
# Generic module helper: ./scripts/module.sh NN [--check|--demo|--help]
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NN="${1:-}"
shift || true
if [[ -z "$NN" || "$NN" == "--help" ]]; then
  echo "Usage: $0 NN [--check|--demo|--help]"
  echo "  NN = module number, e.g. 01 or 1"
  exit 0
fi
NN="$(printf '%02d' "$((10#$NN))")"
MOD_DIR="$(find "$ROOT" -maxdepth 1 -type d -name "module${NN}-*" | head -1)"
if [[ -z "$MOD_DIR" ]]; then
  echo "No module directory for $NN"
  exit 1
fi
ACTION="${1:---check}"
case "$ACTION" in
  --check)
    echo "Module $NN self-check (Track A environment)"
    echo "Module dir: $MOD_DIR"
    command -v bash >/dev/null && echo "[OK] bash"
    command -v ls >/dev/null && echo "[OK] ls"
    command -v pwd >/dev/null && echo "[OK] pwd: $(pwd)"
    if [[ -d "$MOD_DIR/examples" ]]; then
      echo "[OK] examples present:"
      ls "$MOD_DIR/examples"
    else
      echo "[INFO] no examples/ (intro/wrap or pending)"
    fi
    if [[ -d "${HOME}/unix_practice" ]]; then
      echo "[OK] ~/unix_practice exists"
    else
      echo "[INFO] run ./scripts/scaffold.sh to create ~/unix_practice"
    fi
    ;;
  --demo)
    echo "Demo: open $MOD_DIR/EXAMPLES.md and README.md"
    echo "Browser lab link is in README (Track B)."
    ;;
  *)
    echo "Unknown option: $ACTION"
    exit 1
    ;;
esac
