---
marp: true
title: Permissions, umask, PATH
paginate: true
---

# Permissions, umask, PATH

Who can read a file, who can run a script

---

## Mode bits, umask, and PATH
- In a long listing, the nine permission letters are user, group
- Chmod changes those bits; a script needs execute before you can run it with dot-slash
- Umask masks bits off new files so you do not accidentally create world-writable junk
- PATH is a colon-separated search list

---

## Browser lab
![Permissions lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — permissions and umask](assets/real-shell.png)

---

## Real shell practice — try these

```
# ls -l — long listing; read the nine permission letters
ls -l

# chmod u+x hello.sh — add execute for your user (symbolic mode)
chmod u+x hello.sh

# ls -l hello.sh — confirm the user execute bit appears
ls -l hello.sh

# ./hello.sh — run the script in this directory (dot is usually not on PATH)
./hello.sh

# chmod 600 config.txt — owner read/write only (numeric mode)
chmod 600 config.txt

# ls -l — see both the script and the tightened config
ls -l

# umask — show the numeric default mask for new files
umask

# umask -S — same mask in symbolic form
umask -S

```

---

## Pitfalls to watch
- Avoid chmod seven-seven-seven unless you truly understand the risk
- Prefer user-plus-execute for scripts you own
- Remember: without dot-slash
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On the real shell, practice chmod, umask
- When you are ready, take the short quiz, then continue to dotfiles and config homes

