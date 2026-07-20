#!/usr/bin/env bash
# Track A demo for module21 — list generated files, backup (exclude), list archive
set -e

echo "# real shell session (Track A)"
echo

printf '%s\n' "$ find sample_project/build sample_project/logs -type f"
find sample_project/build sample_project/logs -type f
echo

printf '%s\n' "$ tar czf /tmp/m21_backup_demo.tar.gz --exclude=build --exclude=logs -C sample_project ."
tar czf /tmp/m21_backup_demo.tar.gz --exclude='build' --exclude='logs' -C sample_project .
echo

printf '%s\n' "$ tar tzf /tmp/m21_backup_demo.tar.gz"
tar tzf /tmp/m21_backup_demo.tar.gz
echo

printf '%s\n' "$ find sample_project/build sample_project/logs -type f"
find sample_project/build sample_project/logs -type f
echo
printf '%s\n' "# (still present — clean only after you mean to)"
echo
