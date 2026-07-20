# Module 14 examples — Shell history & reverse-search

Track A (real Unix). Each folder was adapted from `learn_unix_git`.

## `history/`

See [`examples/history/README.md`](examples/history/README.md).

**Try these** (interactive keys first, then listing):

```bash
cd module14-shell-history/examples/history

# View recent history
history
history | tail -20

# Navigate / edit (keyboard — not printable as output)
# ↑ / ↓ — previous / next command
# Ctrl+A / Ctrl+E — start / end of line
# Ctrl+U / Ctrl+K — clear to start / end
# Ctrl+R — reverse-search; type a substring, Enter to run

# Optional: re-run by history number (careful!)
# !123
```

**Demo seed** (non-interactive / capture-friendly):

```bash
set -o history
history -s 'pwd'
history -s 'ls -la'
history -s 'grep ERROR run.log'
history -s 'make sim'
history
history | tail -5
history | grep ERROR
```
