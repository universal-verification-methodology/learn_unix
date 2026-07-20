#!/usr/bin/env bash
# Track A demo for module15 — alias + tiny function
set +e
shopt -s expand_aliases

echo "# real shell session (Track A)"
echo

printf '%s\n' "$ alias ll='ls -alF'"
alias ll='ls -alF'
echo

printf '%s\n' "$ ll"
ll
echo

printf '%s\n' "$ alias | grep ll"
alias | grep ll
echo

printf '%s\n' '$ greet() { echo Hello "$1"; }'
greet() { echo Hello "$1"; }
echo

printf '%s\n' "$ greet Alice"
greet Alice
echo

printf '%s\n' "$ type greet"
type greet
echo

printf '%s\n' "$ unalias ll"
unalias ll
echo
