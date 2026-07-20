# Module 15 examples — Alias & functions

Track A (real Unix). Each folder was adapted from `learn_unix_git`.

## `aliases/`

See [`examples/aliases/README.md`](examples/aliases/README.md).

**Try these:**

```bash
cd module15-alias-lab/examples/aliases

# alias ll='…' — session shortcut for a long listing
alias ll='ls -alF'
ll

# alias — list active aliases; grep to find one
alias
alias | grep ll

# unalias ll — remove it from this session
unalias ll

# Optional persist: add alias lines to ~/.bashrc (or ~/.zshrc), then source it
```

## `functions/`

See [`examples/functions/README.md`](examples/functions/README.md).

**Try these:**

```bash
cd module15-alias-lab/examples/functions

# greet() { … } — function with one argument
greet() { echo "Hello, $1"; }
greet Alice

# type / declare -f — inspect the definition
type greet
declare -f greet
```
