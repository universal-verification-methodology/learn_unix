# Module 25 examples — Dry-run mindset

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `dry_run/`

See [`examples/dry_run/README.md`](examples/dry_run/README.md).

**Try these** (preview first, live only when the list looks right):

```bash
cd module25-dry-run-lab/examples/dry_run
chmod u+x remove_old.sh

./remove_old.sh --help
./remove_old.sh --dry-run

# Create a file older than 365 days so dry-run has something to show
touch -d 2020-01-01 old_file.txt
./remove_old.sh --dry-run

# Live remove only after you read the would-remove lines
./remove_old.sh
```

Habit: any script that deletes or overwrites should document `--dry-run` (or equivalent) and you should use it first.
