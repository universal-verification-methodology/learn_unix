# Environment file example

Practice **loading variables** from a file (e.g. config or .env-style) with `source` or `set -a`.

## Layout

```
env_file/
├── README.md       # this file
├── sample.env      # KEY=value lines (no spaces around =)
├── use_env.sh      # sources sample.env and prints (chmod u+x)
└── commands_to_try.txt
```

## Try these (from this directory)

```bash
cd module27-env-file-lab/examples/env_file
cat sample.env
chmod u+x use_env.sh
./use_env.sh
source sample.env
echo "$MY_VAR"
echo "$ANOTHER_VAR"
```

## 1. source (dot)

- **`source file`** or **`. file`** — run the file in the **current shell**. Variables stay set.
- **`source sample.env`** — if it contains `MY_VAR=hello`, then `echo "$MY_VAR"` prints `hello`.

## 2. File format

- **`KEY=value`** — one per line; no spaces around `=`.
- **`# comment`** — comment lines for humans (and for filters that skip `#`).

## 3. Git habit

- Commit **`.env.example`** (safe defaults, no secrets).
- Gitignore **`.env`** / **`.env.local`** (local paths, tokens).

Use env files for local config (paths, flags) so the same script can run with different settings without editing the script.
