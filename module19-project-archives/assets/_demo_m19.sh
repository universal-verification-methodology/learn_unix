#!/usr/bin/env bash
# Track A demo for module19 — layout, find/grep, sed, diff
set +e

echo "# real shell session (Track A)"
echo

printf '%s\n' "$ ls sample_project"
ls sample_project
echo

printf '%s\n' "$ find sample_project -type f"
find sample_project -type f
echo

printf '%s\n' "$ find ../find_grep -name '*.v'"
find ../find_grep -name '*.v'
echo

printf '%s\n' "$ grep -Rn CLOCK_SIGNAL ../find_grep --include='*.v'"
grep -Rn CLOCK_SIGNAL ../find_grep --include='*.v'
echo

printf '%s\n' "$ sed 's/old/new/g' ../sed_basics/sample.txt"
sed 's/old/new/g' ../sed_basics/sample.txt
echo

printf '%s\n' "$ diff -u ../diff_patch/original.txt ../diff_patch/modified.txt"
diff -u ../diff_patch/original.txt ../diff_patch/modified.txt || true
echo
exit 0
