# Module 17 examples — Exit status & && / ||

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `exit_codes/`

See [`examples/exit_codes/README.md`](examples/exit_codes/README.md).

**Try these:**

```bash
cd module17-exit-status-lab/examples/exit_codes
chmod u+x success.sh failure.sh check_file.sh

# ./success.sh — exits 0; echo $? shows 0
./success.sh
echo $?

# ./failure.sh — exits 1; echo $? shows 1
./failure.sh
echo $?

# ./check_file.sh — 0 if file exists, 1 otherwise
./check_file.sh README.md
echo $?
./check_file.sh missing.txt
echo $?

# Short-circuit chaining
true && echo ok
false || echo fallback

# Branch on a script’s status
if ./success.sh; then echo OK; fi
if ./failure.sh; then echo OK; else echo Failed; fi
```
