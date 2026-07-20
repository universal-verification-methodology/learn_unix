---
marp: true
title: Pipes, redirection, xargs
paginate: true
---

# Pipes, redirection, xargs

Shell power often means connecting small tools

---

## Pipe, redirect, and feed arguments
- The vertical bar connects stdout of the left command to stdin of the right
- Greater-than overwrites a file with stdout
- Xargs reads items from stdin and builds argument lists, handy when you have many filenames
- Together they turn a noisy log into a short list of errors

---

## Browser lab
![Pipes lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — pipes and grep](assets/real-shell.png)

---

## Real shell practice — try these

```
# head -5 sample.log — peek at the start of the log
head -5 sample.log

# grep ERROR sample.log — lines containing ERROR
grep ERROR sample.log

# grep -i warning sample.log — case-insensitive warning lines
grep -i warning sample.log

# grep -c ERROR sample.log — count matching lines
grep -c ERROR sample.log

# cat sample.log | grep INFO | head -5 — pipe: filter then take first five
cat sample.log | grep INFO | head -5

# grep -i error sample.log | wc -l — pipe: count error-like lines
grep -i error sample.log | wc -l

```

---

## Pitfalls to watch
- A pipe only carries stdout by default
- Overwrite with one greater-than destroys the previous file
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few pipeline challenges after the starter
- On the real shell
- When you are ready, take the short quiz, then continue to sort, uniq, and cut

