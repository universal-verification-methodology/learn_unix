---
marp: true
title: man / --help discoverability
paginate: true
---

# man / --help discoverability

You will not memorize every flag

---

## Four ways to ask for help
- Use the manual when you want the full story
- Use a help flag when you need a quick reminder of options
- Use whatis for a one-line summary
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
whatis ls
ls --help | head -n 12
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

