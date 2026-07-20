---
marp: true
title: sort / uniq / cut
paginate: true
---

# sort / uniq / cut

Logs and lists are messy until you order them, collapse duplicates, and pull out columns

---

## Order, dedupe, and columns
- Alphabetical sort is the default; numeric sort with dash-n puts ten after two, not before
- Uniq only collapses neighbors, so sort then uniq is the classic dedupe
- Uniq with dash-c prints a count beside each unique line
- Remember: uniq without sort misses scattered duplicates

---

## Browser lab
![sort uniq cut lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — sort and uniq](assets/real-shell.png)

---

## Real shell practice — try these

```
# cat names.txt — see the raw list with duplicates
cat names.txt

# sort names.txt — alphabetical order (duplicates become adjacent)
sort names.txt

# sort names.txt | uniq — unique lines after sorting
sort names.txt | uniq

# sort names.txt | uniq -c — unique lines with occurrence counts
sort names.txt | uniq -c

# sort numbers.txt — default (lexicographic) order — often wrong for numbers
sort numbers.txt

# sort -n numbers.txt — numeric sort (1, 2, 5, 10, …)
sort -n numbers.txt

```

---

## Pitfalls to watch
- Running uniq alone on an unsorted file skips non-adjacent duplicates, sort first
- Do not confuse lexicographic sort with numeric sort for version numbers or sizes
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On the real shell, practice sort, uniq dash-c
- When you are ready, take the short quiz, then continue to here-documents and here-strings

