# Module 26 examples — Log / failure triage

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `logs/`

See [`examples/logs/README.md`](examples/logs/README.md).

**Try these** (triage the sample log before changing design):

```bash
cd module26-log-triage/examples/logs

# How long is the log? How did it end?
wc -l sample.log
tail -5 sample.log

# Find failure cues
grep -i error sample.log
grep -i warn sample.log
grep -n ERROR sample.log
```

Habit: classify before you fix — **fail** (RTL/TB), **env** (tool/PATH/license/disk), or **flake** (order/race/timeout).
