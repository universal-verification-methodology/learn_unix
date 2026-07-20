---
marp: true
title: Safe scripting
paginate: true
---

# Safe scripting

Scripts that delete files or stop builds can hurt when they run by accident

---

## Fail fast, quote, dry-run
- Set dash-euo pipefail at the top
- Always quote expansions like dollar-file so spaces do not split paths
- For deletes and cleans
- Check that directories exist before you walk them

---

## Browser lab
![Safe scripting lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — dry-run clean](assets/real-shell.png)

---

## Real shell practice — try these

```
# ls tmp/ — see the sample cache files before cleaning
ls tmp/

# chmod u+x clean_tmp.sh — make the clean script executable
chmod u+x clean_tmp.sh

# ./clean_tmp.sh — dry run by default (prints Would delete, keeps files)
./clean_tmp.sh

# ls tmp/ — confirm the files are still there
ls tmp/

# ./clean_tmp.sh --confirm — only when ready: actually delete *.tmp
# ./clean_tmp.sh --confirm

```

---

## Pitfalls to watch
- Unquoted variables break on spaces and can make rm touch the wrong paths
- Skipping dry-run on a clean script is how accidents happen
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On the real shell, run the dry-run clean and only use confirm when you intend to delete
- When you are ready, take the short quiz, then continue to project layout, archives, sed

