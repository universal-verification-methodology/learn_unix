---
marp: true
title: Project layout, archives, sed and diff
paginate: true
---

# Project layout, archives, sed and diff

A design project needs a clear tree, source, testbench, docs, scripts, and a build folder for generated noise

---

## Tree, search, edit, compare
- Keep RTL under src, tests under tb, notes under docs, helpers under scripts
- Find locates files by name; recursive grep finds a signal across the tree
- Sed substitutes on a stream, test without in-place first
- Unified diff is the same shape as git diff and feeds patch
- When you archive, ignore build and logs so the tarball stays small and shareable

---

## Browser lab
![Project archives lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — layout find sed diff](assets/real-shell.png)

---

## Real shell practice — try these

```
# ls / find — inspect sample_project layout
ls sample_project
find sample_project -type f

# find *.v — Verilog files under find_grep
find ../find_grep -name '*.v'

# grep -Rn — recursive content search with line numbers (Verilog only here)
grep -Rn CLOCK_SIGNAL ../find_grep --include='*.v'

# sed 's/old/new/g' — global substitute (stdout only; file unchanged)
sed 's/old/new/g' ../sed_basics/sample.txt

# diff -u — unified diff (patch-friendly)
diff -u ../diff_patch/original.txt ../diff_patch/modified.txt

```

---

## Pitfalls to watch
- Do not archive build and logs by default, they bloat shares and hide the real sources
- Always dry-run sed without in-place before you rewrite a file
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On the real shell, walk the sample project, practice find and grep, then sed and diff
- When you are ready, take the short quiz, then continue to tar versus zip

