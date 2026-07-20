---
marp: true
title: Pre-push, Make, and env checklist
paginate: true
---

# Pre-push, Make, and env checklist

Before you push or hand off a build, run a short local checklist

---

## Status, env, then the green build
- Git status shows uncommitted noise, commit or stash before push
- A short log confirms what you are about to send
- Tools often need a TOOLS path or env file
- Prefer dry-run cleans when unsure
- Exit zero is the handshake CI and teammates expect

---

## Browser lab
![Workflow lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — check_ready](assets/real-shell.png)

---

## Real shell practice — try these

```
# chmod u+x check_ready.sh — make the pre-push helper executable
chmod u+x check_ready.sh

# ./check_ready.sh — status + recent log; exit 1 if dirty (run from a Git repo)
./check_ready.sh

# which make — confirm Make is on PATH
which make

# make --version — one-line toolchain sanity check
make --version | head -n 1

```

---

## Pitfalls to watch
- Do not push with a dirty tree and hope CI sorts it out
- Do not blame the RTL when TOOLS or env was never sourced
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, clear a few challenges after the starter
- On the real shell, run check-ready from a clean tree and confirm Make is available
- When you are ready, take the short quiz, then continue to Makefile basics

