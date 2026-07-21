# Module 04 examples — Globs & wildcards

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `wildcards/`

See [`examples/wildcards/README.md`](examples/wildcards/README.md) if present.

**Try these** (from `examples/wildcards`):

```bash
# ls — see every name first
ls

# ls *.txt — all .txt files
ls *.txt

# ls report_*.txt — reports by prefix
ls report_*.txt

# ls data_?.log — exactly one character in the middle
ls data_?.log

# ls [abc].txt — one character from the set
ls [abc].txt
```
