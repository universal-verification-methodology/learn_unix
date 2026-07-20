# Module 27 — .env literacy

**Module id:** module27-env-file-lab
**Lab:** env-file-lab
**Tracks:** A · B

## Slide 1 — Dot-env literacy

Toolchains need paths and flags—TOOLS, SIM, WAVE—without hard-coding secrets in scripts you commit. A dot-env file holds KEY equals value lines you source locally. This module covers load order, example versus real env files, and keeping secrets out of Git.

## Slide 2 — Source, layers, and Git

Source or dot loads the file into the current shell. Commit a safe example template; keep the real env file gitignored. Later layers win—local overrides, then shell exports. Never commit tokens or private paths; document the keys teammates must set.

## Slide 3 — Browser lab

![Env file lab](assets/lab-starter.png)

In the browser lab, load the starter example. You will see a chip project with an example file, a real env file, and optional local overrides. Load env and watch which layer wins for each key. Orient yourself with the file tabs, the resolved table, and the challenge strip, then practice sourcing on a real shell.

## Slide 4 — Real shell practice

![Real shell — source env](assets/real-shell.png)

In the real Unix track, open this module’s env-file example. List the files and show the sample env so you see KEY equals value lines and comments. Make the helper script executable and run it—it sources the file and prints the variables. Then source the file in your shell and echo the values yourself. You will reuse this whenever a Make or sim flow expects TOOLS or similar settings.

```bash
# pwd — print working directory (where am I?)
pwd

# ls -la — list all entries, long format (what is here?)
ls -la

# cat sample.env — show KEY=value lines (and comments)
cat sample.env

# chmod u+x use_env.sh — make the helper script executable
chmod u+x use_env.sh

# ./use_env.sh — source sample.env inside the script and print vars
./use_env.sh

# source sample.env — load vars into the current shell
source sample.env

# echo MY_VAR=... — confirm MY_VAR is set after sourcing
echo MY_VAR=$MY_VAR

# echo ANOTHER_VAR=... — confirm ANOTHER_VAR is set
echo ANOTHER_VAR=$ANOTHER_VAR
```

## Slide 5 — Pitfalls to watch

Do not commit a real env file with secrets. Do not put spaces around the equals sign in KEY equals value lines. And remember: the browser lab shows load order; lasting habit means sourcing a local file on a real shell before blaming the RTL.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, clear a few challenges after the starter. On the real shell, source the sample env and confirm the variables print. When you are ready, take the short quiz, then continue to the course wrap.
