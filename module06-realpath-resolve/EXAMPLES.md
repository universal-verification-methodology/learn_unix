# Module 06 examples — realpath / readlink

Track A (real Unix). Each folder was adapted from `learn_unix / learn_git (legacy archive ignored)`.

## `realpath/`

See [`examples/realpath/README.md`](examples/realpath/README.md) if present.

If `link_to_file` is missing: `ln -s a_file.txt link_to_file`

**Try these** (from `examples/realpath`):

```bash
# pwd — where you are before resolving
pwd

# realpath . — absolute canonical path of cwd
realpath .

# realpath a_file.txt — absolute path of the sample file
realpath a_file.txt

# ls -l link_to_file — see the symlink arrow
ls -l link_to_file

# readlink link_to_file — stored target string
readlink link_to_file

# realpath link_to_file — follow to canonical absolute path
realpath link_to_file

# readlink -f link_to_file — Linux-style canonical path
readlink -f link_to_file
```
