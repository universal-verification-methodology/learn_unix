# Module 16 — Script control flow

**Module id:** module16-scripting  
**Lab:** scripting  
**Tracks:** A · B

## Slide 1 — Script control flow

A one-liner is fine until you need decisions and repetition. Scripts add a shebang, arguments, if tests, for loops, and case branches so you can automate greets, file sweeps, and tool dispatch. This module is the control-flow core of shell scripting—before you lean on exit status tricks in the next module.

## Slide 2 — If, for, and case

An if test with brackets checks a condition—file exists, string empty, and so on—then runs a then or else branch. A for loop walks a list, often a glob of files, and runs the body once per item. A case statement matches one value against patterns and is cleaner than a long if-elif chain for menus or file types. Quote variables, end case arms with double semicolon, and prefer a readable script file over a fragile pasted blob.

## Slide 3 — Browser lab

![Scripting lab](assets/lab-starter.png)

In the browser lab, load the starter example—safe-args with a name argument printing a hello line. Edit the script pane, set args or stdin when needed, and run. Try an if on a missing argument, a for loop, and a case on a mode string. Orient yourself with the editor, the run controls, and the challenge list, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — control flow script](assets/real-shell.png)

In the real Unix track, open this module’s control-flow example. Make the line-count script executable, then run it so the for loop walks each log file and the if check skips non-files. Compare with word-count on the log glob. Also explore script basics, arguments with a default name, and the case-statement greet when you want more practice. You will reuse for-over-files whenever a sim or log folder grows.

```bash
# chmod u+x count_lines.sh — make the control-flow script executable
chmod u+x count_lines.sh

# ./count_lines.sh — for each *.log: if it is a file, print line count
./count_lines.sh

# wc -l *.log — compare: word-count lines on the same logs
wc -l *.log
```

## Slide 5 — Pitfalls to watch

Spaces matter inside test brackets—write `[ -f "$file" ]`, not jammed tokens. Always quote `"$file"` and `"$1"` so names with spaces survive. And remember: the browser lab shows the idea; real automation still lives in scripts you chmod and run on a real shell.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On the real shell, run the control-flow script and try arguments or case greet next. When you are ready, take the short quiz, then continue to exit status and conditional chaining.
