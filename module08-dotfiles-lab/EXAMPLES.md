# Module 08 examples — Dotfiles & config homes

Track A (real Unix). Each folder was adapted from `learn_unix / learn_git (legacy archive ignored)`.

## `dotfiles/`

See [`examples/dotfiles/README.md`](examples/dotfiles/README.md) if present.

**Try these** (from `examples/dotfiles`):

```bash
# ls — plain list; dot-names stay hidden
ls

# ls -a — show all names, including those starting with a dot
ls -a

# ls -la — long listing that includes hidden names
ls -la

# cat .hidden_file — read a hidden file (safe inspect)
cat .hidden_file

# cat .sample_rc — read an example config-style dotfile
cat .sample_rc

# ls -a ~ | head -12 — peek at real home dotfiles (read-only)
ls -a ~ | head -12
```
