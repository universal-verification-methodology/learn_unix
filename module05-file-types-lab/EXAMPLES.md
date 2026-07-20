# Module 05 examples — File types & links

Track A (real Unix). Each folder was adapted from `learn_unix_git`.

## `file_types/`

See [`examples/file_types/README.md`](examples/file_types/README.md) if present.

**Try these** (from `examples/file_types`):

```bash
# ls -l — long listing; first character is the type
ls -l

# ls -l my_symlink — inspect the working symlink
ls -l my_symlink

# readlink my_symlink — print the target path
readlink my_symlink

# file sample.txt — classify the regular file
file sample.txt

# file my_symlink — classify the symlink
file my_symlink

# readlink broken_link — target even when missing
readlink broken_link

# ls -l broken_link — broken symlink in the listing
ls -l broken_link
```
