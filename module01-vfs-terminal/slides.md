---
marp: true
title: Virtual filesystem terminal
paginate: true
---

# Virtual filesystem terminal

This module is your first real practice: moving around a directory tree and listing what is there

---

## The shell has a current directory
- A terminal session always has a current working directory
- Print it with pwd, print working directory
- Change it with cd, change directory
- List what is here with ls, list
- Relative paths are resolved against where you are now

---

## Browser lab
![Virtual filesystem terminal starter](assets/lab-starter.png)

---

## Real shell practice
![Real WSL shell — navigation example](assets/real-shell.png)

---

## Real shell practice — try these

```
# pwd — print working directory (where am I?)
pwd

# ls -la — list all entries, long format (what is here?)
ls -la

# cd sample_repo — change into this directory
cd sample_repo

# ls — list names only
ls

# cd .. — go up one directory
cd ..

```

---

## Pitfalls to watch
- Do not confuse a directory name with a file name when you change directories
- Remember that a leading slash starts from the filesystem root
- Hidden files start with a dot and may not show unless you ask for them with a flag like
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On the real shell
- When you are ready

