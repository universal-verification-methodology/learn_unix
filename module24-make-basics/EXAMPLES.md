# Module 24 examples — Makefile basics

Track A (real Unix). Each folder was adapted from `learn_unix_git`.

## `makefile_basics/`

See [`examples/makefile_basics/README.md`](examples/makefile_basics/README.md).

**Try these** (from the sample project root so Makefile paths resolve):

```bash
cd module24-make-basics/examples/makefile_basics/sample_project

# pwd — where am I?
pwd

# ls -la — see Makefile, src/, tb/, build/, logs/
ls -la

# make help — list targets
make help

# make — default (all → build)
make

# make run — demo that appends to logs/run.log
make run

# ls -la build logs — inspect outputs
ls -la build logs

# make clean — remove generated files
make clean
```

Habit: always `cd` to the directory that owns the Makefile before running `make`.
