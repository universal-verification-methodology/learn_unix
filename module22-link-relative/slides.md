---
marp: true
title: Relative symlink pitfalls
paginate: true
---

# Relative symlink pitfalls

Symlinks let a project point at shared IP without copying files

---

## Relative to the link, not your cwd
- The target string is resolved from the directory that contains the symlink
- From project slash external, shared lib is up two levels then shared slash lib
- Prefer relative inside a repo you will move; prefer absolute only for fixed system tools
- Moving only the symlink to a new folder often breaks a relative link

---

## Browser lab
![Link relative lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — relative link to shared IP](assets/real-shell.png)

---

## Real shell practice — try these

```
# ls -la external/ — see lib.v -> ../../shared/lib.v
ls -la external/

# readlink external/lib.v — print the stored relative target
readlink external/lib.v

# cat external/lib.v — follow the link and show shared content
cat external/lib.v

# ln -s "$(realpath …)" — absolute contrast (fixed path; breaks if tree moves)
ln -s "$(realpath ../shared/lib.v)" external/abs_lib.v
readlink external/abs_lib.v

# rm external/abs_lib.v — remove the absolute demo link
rm external/abs_lib.v

```

---

## Pitfalls to watch
- Count the dots from the link’s directory, not from the repo root by habit
- Do not move a relative symlink alone without updating its target string
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, run whole-tree relocate and move-only-link
- On the real shell, inspect the external lib link with readlink and cat
- When you are ready

