#!/usr/bin/env bash
# Track A demo for module22 — relative symlink inspect (+ brief absolute contrast)
set -e

echo "# real shell session (Track A)"
echo

cd project

printf '%s\n' "$ ls -la external/"
ls -la external/
echo

printf '%s\n' "$ readlink external/lib.v"
readlink external/lib.v
echo

printf '%s\n' "$ cat external/lib.v"
cat external/lib.v
echo

printf '%s\n' "$ ln -s \"\$(realpath ../shared/lib.v)\" external/abs_lib.v"
ln -s "$(realpath ../shared/lib.v)" external/abs_lib.v
echo

printf '%s\n' "$ ls -la external/"
ls -la external/
echo

printf '%s\n' "$ readlink external/abs_lib.v"
readlink external/abs_lib.v
echo

printf '%s\n' "$ rm external/abs_lib.v"
rm external/abs_lib.v
echo
