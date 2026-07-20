---
marp: true
title: Shell history & reverse-search
paginate: true
---

# Shell history & reverse-search

You will type the same kinds of commands again and again, build, grep a log, change directories

---

## Recall, edit, re-run
- Arrow up and arrow down step through previous commands
- Ctrl+A and Ctrl+E jump to the start or end of the line
- Ctrl+R starts reverse incremental search
- The history builtin lists numbered entries
- Faster recall means less friction when you iterate on simulators and scripts

---

## Browser lab
![Shell history lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — history listing](assets/real-shell.png)

---

## Real shell practice — try these

```
# set -o history — enable history in this shell session
set -o history

# history -s … — add a line to history without running it (demo seed)
history -s 'pwd'
history -s 'ls -la'
history -s 'grep ERROR run.log'
history -s 'make sim'

# history — list numbered past commands
history

# history | tail -5 — show only the most recent entries
history | tail -5

# history | grep ERROR — find past commands that mention ERROR
history | grep ERROR

```

---

## Pitfalls to watch
- Bang-number and bang-bang re-execute immediately
- Reverse-search can feel sticky; Ctrl+C cancels cleanly
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On the real shell, list history, search it with grep
- When you are ready, take the short quiz, then continue to aliases and functions

