# Module 18 examples — Safe scripting

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `safe_scripting/`

See [`examples/safe_scripting/README.md`](examples/safe_scripting/README.md).

**Try these:**

```bash
cd module18-safe-scripting/examples/safe_scripting
chmod u+x clean_tmp.sh

# Dry run (default) — prints Would delete, keeps files
ls tmp/
./clean_tmp.sh
ls tmp/

# Actually delete only when ready
./clean_tmp.sh --confirm
ls tmp/

# Optional: recreate sample files for another practice pass
# printf 'x\n' > tmp/cache1.tmp
# printf 'y\n' > tmp/cache2.tmp
```
