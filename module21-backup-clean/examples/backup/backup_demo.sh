#!/usr/bin/env bash
# Backup example: timestamped tar.gz of clean_build/sample_project (excludes build/ and logs/).
# Run from this directory: ./backup_demo.sh
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXAMPLES_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PROJECT_REL="clean_build/sample_project"
PROJECT_DIR="$EXAMPLES_DIR/$PROJECT_REL"
STAMP=$(date +%Y%m%d_%H%M%S)
ARCHIVE="backup_sample_project_${STAMP}.tar.gz"
cd "$EXAMPLES_DIR"
if [ ! -d "$PROJECT_DIR" ]; then
  echo "Project dir not found: $PROJECT_DIR"
  exit 1
fi
# Exclude generated dirs so the backup stays small and shareable
tar czf "$SCRIPT_DIR/$ARCHIVE" \
  --exclude='build' \
  --exclude='logs' \
  -C "$EXAMPLES_DIR" "$PROJECT_REL"
echo "Created: $SCRIPT_DIR/$ARCHIVE"
ls -la "$SCRIPT_DIR/$ARCHIVE"
