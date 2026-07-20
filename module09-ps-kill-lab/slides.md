---
marp: true
title: Process list & signals
paginate: true
---

# Process list & signals

When a build or simulation hangs, you need to see what is running and how to stop it

---

## PID, exit status, and signals
- A process ID uniquely names a running program
- When a command finishes, it leaves an exit status, zero usually means success
- Signals are how you interrupt or stop a process
- Background jobs need kill with a PID, Control-C alone will not stop them

---

## Browser lab
![Process list and signals lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — processes and signals](assets/real-shell.png)

---

## Real shell practice — try these

```
# chmod u+x … — ensure the demo scripts are executable
chmod u+x show_pid.sh fail.sh

# ./show_pid.sh — run a script that prints its PID and exits successfully
./show_pid.sh

# echo $? — print the last exit status (0 = success)
echo $?

# ./fail.sh — run a script that exits with status 1
./fail.sh

# echo $? — confirm a non-zero failure status
echo $?

# ps aux | head -8 — list a few processes (USER, PID, COMMAND, …)
ps aux | head -8

# sleep 60 & — start a background job; kill it by PID (safe practice)
sleep 60 &
kill $!

```

---

## Pitfalls to watch
- Do not kill processes you do not own or understand
- Prefer terminate, then escalate only if needed
- Remember that Control-C stops the foreground job, not an arbitrary background PID
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On the real shell, practice exit status, listing processes
- When you are ready, take the short quiz, then continue to job control

