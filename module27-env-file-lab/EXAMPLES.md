# Module 27 examples — .env literacy

Track A (real Unix). Each folder was adapted from `learn_unix_git`.

## `env_file/`

See [`examples/env_file/README.md`](examples/env_file/README.md).

**Try these** (source locally; do not commit secrets):

```bash
cd module27-env-file-lab/examples/env_file

cat sample.env
chmod u+x use_env.sh
./use_env.sh

source sample.env
echo "$MY_VAR"
echo "$ANOTHER_VAR"
```

Habit: commit `.env.example`; gitignore `.env` / `.env.local`; source before Make when TOOLS or SIM must be set.
