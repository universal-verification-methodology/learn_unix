#!/usr/bin/env bash
# Create ~/unix_practice for Track A exercises.
set -euo pipefail
TARGET="${HOME}/unix_practice"
mkdir -p "$TARGET"/{notes,projects,src,tb,scripts,logs,build}
if [[ ! -f "$TARGET/notes/readme.txt" ]]; then
  cat > "$TARGET/notes/readme.txt" << 'EOF'
learn_unix Track A practice tree
Use this directory for checklist exercises.
EOF
fi
echo "Created/updated: $TARGET"
ls -la "$TARGET"
