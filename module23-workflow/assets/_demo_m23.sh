#!/usr/bin/env bash
# Track A demo for module23 — pre-push check in a tiny clean Git repo
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CHECK="$SCRIPT_DIR/../examples/pre_push_checks/check_ready.sh"
DEMO="$(mktemp -d /tmp/m23_workflow_XXXXXX)"

echo "# real shell session (Track A)"
echo

printf '%s\n' "$ # demo: tiny clean Git repo (stand-in for your project)"
cd "$DEMO"
git init -q
git config user.email "learner@example.com"
git config user.name "Learner"
echo "hello" > README.md
git add README.md
git commit -q -m "initial commit"
pwd
echo

printf '%s\n' "$ chmod u+x check_ready.sh"
chmod u+x "$CHECK"
echo

printf '%s\n' "$ ./check_ready.sh"
bash "$CHECK"
echo

printf '%s\n' "$ which make"
which make
echo

printf '%s\n' "$ make --version | head -n 1"
make --version | head -n 1
echo

rm -rf "$DEMO"
exit 0
