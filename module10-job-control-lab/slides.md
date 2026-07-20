---
marp: true
title: Job control
paginate: true
---

# Job control

Long builds and simulations should not lock your terminal forever

---

## Background, stop, and resume
- An ampersand at the end of a command starts it in the background, you get the prompt back
- Jobs lists this shell’s jobs
- Control-Z suspends the foreground job; it is stopped, not killed
- Bg resumes a stopped job in the background
- Redirect output to a log, then tail the log while the job runs

---

## Browser lab
![Job control lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — job control](assets/real-shell.png)

---

## Real shell practice — try these

```
# chmod u+x slow_output.sh — make the demo script executable
chmod u+x slow_output.sh

# ./slow_output.sh > bg.log 2>&1 & — run in background; stdout/stderr to a log
./slow_output.sh > bg.log 2>&1 &

# jobs — list this shell’s background jobs
jobs

# sleep 2 — give the script a moment to write lines
sleep 2

# tail -5 bg.log — show the latest log lines while the job runs
tail -5 bg.log

# kill %1 — stop job 1 (or: kill $(jobs -p))
kill %1

```

---

## Pitfalls to watch
- Control-Z stops
- Jobs only lists jobs for this shell, not every process on the machine
- Closing the terminal can hang or kill background jobs unless you plan for that
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On the real shell, practice ampersand, jobs, and tailing a log
- When you are ready, take the short quiz, then continue to pipes, redirection, and xargs

