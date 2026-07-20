---
marp: true
title: man / --help discoverability
paginate: true
---

# man / --help discoverability

You will not memorize every flag

---

## Four ways to ask for help
- Use man when you want the full manual page for a command
- Use a help flag, often two dashes help, when you need a short usage reminder
- Use whatis for a one-line summary of what a command is
- Use apropos when you remember the idea but not the command name
- Pick the lightest tool that answers your question, then go back to work

---

## Browser lab
![man / --help lab starter](assets/lab-starter.png)

---

## Real shell practice
![Real shell — man and help](assets/real-shell.png)

---

## Real shell practice — try these

```
# whatis — one-line summary of a command
whatis ls

# ls --help — short usage / flags; head keeps the first lines
ls --help | head -n 12

# man — full manual; MANPAGER=cat prints instead of interactive pager
MANPAGER=cat man ls | head -n 20

```

---

## Pitfalls to watch
- Not every command has a man page on every machine
- Some tools use a help flag; others use a different switch
- Interactive man viewers need a quit key, or they feel “stuck.” And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On the real shell, run through the help example
- When you are ready, take the short quiz, then continue to absolute versus relative paths

