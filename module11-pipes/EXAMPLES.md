# Module 11 examples — Pipes, redirection, xargs

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `pipes/` (start here)

See [`examples/pipes/README.md`](examples/pipes/README.md).

**Try these** (from `examples/pipes`):

```bash
# head -5 sample.log — peek at the start of the log
head -5 sample.log

# grep ERROR sample.log — lines containing ERROR
grep ERROR sample.log

# grep -i warning sample.log — case-insensitive warnings
grep -i warning sample.log

# grep -c ERROR sample.log — count matches
grep -c ERROR sample.log

# cat sample.log | grep INFO | head -5 — pipe filter then first five
cat sample.log | grep INFO | head -5

# grep -i error sample.log | wc -l — pipe into a line count
grep -i error sample.log | wc -l
```

## `redirection/` · `xargs/` · `combining/` · `troubleshooting/`

See each folder’s README for redirects (`>`, `2>&1`), xargs demos, combined workflows, and debug tips.
