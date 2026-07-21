# Module 10 examples — Job control

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `background/`

See [`examples/background/README.md`](examples/background/README.md) if present.

**Try these** (from `examples/background`):

```bash
# chmod u+x slow_output.sh — make the demo script executable
chmod u+x slow_output.sh

# ./slow_output.sh > bg.log 2>&1 & — background; log stdout/stderr
./slow_output.sh > bg.log 2>&1 &

# jobs — list this shell’s jobs
jobs

# sleep 2 — wait for a few log lines
sleep 2

# tail -5 bg.log — latest lines from the log
tail -5 bg.log

# kill %1 — stop job 1 (or kill by PID from jobs)
kill %1
```

Optional: `fg %1` to bring a job forward; `Ctrl+Z` then `bg %1` to suspend and resume in background; `tail -f bg.log` to follow the log live.
