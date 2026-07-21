# Module 12 examples — sort / uniq / cut

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `sort_uniq/` (start here)

See [`examples/sort_uniq/README.md`](examples/sort_uniq/README.md).

**Try these** (from `examples/sort_uniq`):

```bash
# cat names.txt — raw list with duplicates
cat names.txt

# sort names.txt — alphabetical; duplicates become adjacent
sort names.txt

# sort names.txt | uniq — unique lines
sort names.txt | uniq

# sort names.txt | uniq -c — unique lines with counts
sort names.txt | uniq -c

# sort numbers.txt — lexicographic (often wrong for numbers)
sort numbers.txt

# sort -n numbers.txt — numeric sort
sort -n numbers.txt
```

## `cut_columns/`

See [`examples/cut_columns/README.md`](examples/cut_columns/README.md).

**Try:** `cut -d',' -f1,3 csv_like.txt` and `cut -c1-5 fixed.txt`.
