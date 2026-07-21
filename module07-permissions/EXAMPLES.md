# Module 07 examples — Permissions, umask, PATH

Track A (real Unix). Each folder was adapted from `learn_unix / learn_git (legacy archive ignored)`.

## `permissions/` (start here)

See [`examples/permissions/README.md`](examples/permissions/README.md).

**Try these** (from `examples/permissions`):

```bash
# ls -l — long listing; read the nine permission letters
ls -l

# chmod u+x hello.sh — add execute for your user
chmod u+x hello.sh

# ls -l hello.sh — confirm the user execute bit
ls -l hello.sh

# ./hello.sh — run via ./ (cwd is usually not on PATH)
./hello.sh

# chmod 600 config.txt — owner read/write only
chmod 600 config.txt

# ls -l — see both files
ls -l

# umask / umask -S — default mask for new files
umask
umask -S
```

> On Windows-mounted paths (WSL `/mnt/...`), `chmod` may not change what `ls -l` shows. Copy the files to a Linux filesystem (e.g. `/tmp`) if you need visible mode bits.

## `umask/`

See [`examples/umask/README.md`](examples/umask/README.md).

## `ownership/` · `groups/` · `path_and_script/` · `environment/` · `env_export/`

See each folder’s README for deeper practice (ownership, groups, PATH scripts, and environment / export).
