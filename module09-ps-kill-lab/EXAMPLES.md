# Module 09 examples — Process list & signals

Track A (real Unix). Each folder was adapted from `learn_unix_git`.

## `processes/`

See [`examples/processes/README.md`](examples/processes/README.md) if present.

**Try these** (from `examples/processes`):

```bash
# chmod u+x … — ensure the demo scripts are executable
chmod u+x show_pid.sh fail.sh

# ./show_pid.sh — prints its PID and exits 0
./show_pid.sh

# echo $? — last exit status (0 = success)
echo $?

# ./fail.sh — exits with status 1
./fail.sh

# echo $? — confirm non-zero failure
echo $?

# ps aux | head -8 — list a few processes
ps aux | head -8

# sleep 60 & then kill $! — stop a background job you started
sleep 60 &
kill $!
```

Only kill processes you started (or clearly understand). Prefer plain `kill` before `kill -9`.
