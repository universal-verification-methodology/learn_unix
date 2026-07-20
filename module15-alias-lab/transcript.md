# Module 15 — Alias & functions

**Module id:** module15-alias-lab  
**Lab:** alias-lab  
**Tracks:** A · B

## Slide 1 — Alias & functions

Typing the same long command again and again is slow. An alias is a short name for a fixed command string. A shell function is a named block that can take arguments and run several steps. This module shows when to use each—and how they differ from a separate script file.

## Slide 2 — Shortcut vs helper with args

An alias expands to text before the shell runs the line—great for `ll` meaning a long listing. Aliases are awkward with real arguments; prefer a function when you need `$1` or `"$@"`. Functions run in the current shell, so they can change directory or set variables for you. Scripts run in a subshell—better when you want a file to share and version. Session aliases and functions vanish when the shell exits unless you add them to your startup file.

## Slide 3 — Browser lab

![Alias lab](assets/lab-starter.png)

In the browser lab, load the starter example. You get an `ll` alias and a `greet` function—run `ll`, then `greet lab`, and notice how arguments work differently. Orient yourself with the terminal, the definitions table, and the alias-versus-function cards. Try a few challenges, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — alias and function](assets/real-shell.png)

In the real Unix track, open this module’s aliases example. Define `ll` as a long listing shortcut, run it, then list aliases and filter for `ll`. Define a tiny `greet` function that prints Hello and the first argument, call it with a name, and use `type` to see that it is a function. Finish by removing the alias with `unalias`. Persist only after you are comfortable—add lines to your shell startup file and reload. You will reuse short helpers every day in project directories.

```bash
# alias ll='…' — define a session alias for a long listing
alias ll='ls -alF'

# ll — run the alias (expands to ls -alF)
ll

# alias | grep ll — list aliases and keep lines matching ll
alias | grep ll

# greet() { … } — define a function that uses the first argument
greet() { echo Hello "$1"; }

# greet Alice — call the function with one argument
greet Alice

# type greet — show whether greet is an alias, function, or command
type greet

# unalias ll — remove the ll alias from this session
unalias ll
```

## Slide 5 — Pitfalls to watch

Do not put spaces around the equals in `alias name='cmd'`. Remember aliases do not take arguments the way functions do—use a function when you need `$1`. And remember: the browser lab teaches the idea; lasting shortcuts still live in your real shell startup file.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On the real shell, define an alias and a small function, then try `type` and `unalias`. When you are ready, take the short quiz, then continue to script control flow.
