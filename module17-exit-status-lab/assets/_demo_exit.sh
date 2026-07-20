#!/usr/bin/env bash
# Track A demo for module17 — exit status (must allow non-zero)
set +e

echo "# real shell session (Track A)"
echo

printf '%s\n' "$ chmod u+x success.sh failure.sh check_file.sh"
chmod u+x success.sh failure.sh check_file.sh
echo

printf '%s\n' "$ ./success.sh"
./success.sh
ec=$?
printf '%s\n' "$ echo \$?"
echo "$ec"
echo

printf '%s\n' "$ ./failure.sh"
./failure.sh
ec=$?
printf '%s\n' "$ echo \$?"
echo "$ec"
echo

printf '%s\n' "$ ./check_file.sh README.md"
./check_file.sh README.md
ec=$?
printf '%s\n' "$ echo \$?"
echo "$ec"
echo

printf '%s\n' "$ ./check_file.sh missing.txt"
./check_file.sh missing.txt
ec=$?
printf '%s\n' "$ echo \$?"
echo "$ec"
echo

printf '%s\n' "$ true && echo ok"
true && echo ok
echo

printf '%s\n' "$ false || echo fallback"
false || echo fallback
echo
