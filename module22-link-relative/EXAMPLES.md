# Module 22 examples — Relative symlink pitfalls

Track A (real Unix). Each folder was adapted from `learn_unix / learn_git (legacy archive ignored)`.

## `link_relative/`

See [`examples/link_relative/README.md`](examples/link_relative/README.md).

**Try these:**

```bash
cd module22-link-relative/examples/link_relative/project

# Inspect the existing relative link (or recreate it)
ls -la external/
readlink external/lib.v
cat external/lib.v

# Recreate if missing:
# ln -sfn ../../shared/lib.v external/lib.v

# Absolute contrast (optional — remove afterward)
ln -s "$(realpath ../shared/lib.v)" external/abs_lib.v
ls -la external/
readlink external/abs_lib.v
rm external/abs_lib.v
```
