# Module 21 examples — Backup & clean-build

Track A (real Unix). Each folder was adapted from `learn_unix / learn_git (legacy archive ignored)`.

## `backup/`

See [`examples/backup/README.md`](examples/backup/README.md).

```bash
cd module21-backup-clean/examples/backup
chmod u+x backup_demo.sh
./backup_demo.sh
ls -la backup_*.tar.gz
tar tzf backup_*.tar.gz | head
```

## `clean_build/`

See [`examples/clean_build/README.md`](examples/clean_build/README.md).

```bash
cd module21-backup-clean/examples/clean_build

# List first
find sample_project/build sample_project/logs -type f

# Backup sources (exclude generated), then clean when ready
tar czf /tmp/m21_backup.tar.gz \
  --exclude='build' --exclude='logs' \
  -C sample_project .
chmod u+x clean.sh
./clean.sh
ls sample_project/build sample_project/logs
```

To restore sample generated files after a clean (for another practice pass):

```bash
printf 'o\n' > sample_project/build/output.o
printf 't\n' > sample_project/build/output.tmp
printf 'v\n' > sample_project/build/wave.vcd
printf 'log\n' > sample_project/logs/run.log
```
