# Module 23 examples — Pre-push / Make / env checklist

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `pre_push_checks/`

See [`examples/pre_push_checks/README.md`](examples/pre_push_checks/README.md).

**Try these** (from inside a Git repo — e.g. this learning monorepo):

```bash
cd module23-workflow/examples/pre_push_checks
chmod u+x check_ready.sh

# Must run with cwd inside a Git work tree
cd ../../../../..   # → learning repo root (adjust if needed)
./courses/learn_unix/module23-workflow/examples/pre_push_checks/check_ready.sh

# Manual checklist
git status
git log --oneline -5
# git pull && git push   # when clean and ready
```

## `scripts/`

See [`examples/scripts/README.md`](examples/scripts/README.md).

Habit: run project scripts from the **project root**, capture logs with `> logs/run.log 2>&1`, and use `--help` when available. The next module covers Make targets in more depth.
