# Module 25 — Dry-run mindset

**Module id:** module25-dry-run-lab
**Lab:** dry-run-lab
**Tracks:** A · B

## Slide 1 — Dry-run mindset

Before a clean deletes build junk, preview what would change. Dry-run—Make’s dash-n, script flags like dry-run, or echo-first—lets you read the list, then run live only when it looks right. This module builds that habit for Make, rm, and cleanup scripts.

## Slide 2 — Preview, read, then live

Prefer preview first: make dash-n clean, git clean with dry flags, or a script’s dry-run switch. Read every path on the list. Live run only after the list matches what you meant to remove. Echo-first is the same idea—print the command before you paste the real one.

## Slide 3 — Browser lab

![Dry-run lab](assets/lab-starter.png)

In the browser lab, load the starter example. You will see a chip tree with junk in build and logs, dry versus live buttons, and a preview list. Prefer dry-run, scan the targets, then try a live clean only when the list looks right. Orient yourself with the habit flow and the challenge strip, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — dry-run remove](assets/real-shell.png)

In the real Unix track, open this module’s dry-run example. Make the remove script executable and ask for help. Run dry-run first—it may report zero files. Create an intentionally old file, dry-run again to see would-remove lines, then run without the flag to delete for real and list the directory. You will reuse dry-run-first whenever a script deletes or overwrites.

```bash
# pwd — print working directory (where am I?)
pwd

# ls -la — list all entries, long format (what is here?)
ls -la

# chmod u+x remove_old.sh — make the cleanup script executable
chmod u+x remove_old.sh

# ./remove_old.sh --help — show usage (dry-run flag)
./remove_old.sh --help

# ./remove_old.sh --dry-run — preview only; no deletes yet
./remove_old.sh --dry-run

# touch -d 2020-01-01 old_file.txt — create a file older than 365 days
touch -d 2020-01-01 old_file.txt

# ls -la old_file.txt — confirm the stamped file exists
ls -la old_file.txt

# ./remove_old.sh --dry-run — preview would-remove for the old file
./remove_old.sh --dry-run

# ./remove_old.sh — live remove (files older than 365 days)
./remove_old.sh

# ls -la — confirm old_file.txt is gone
ls -la
```

## Slide 5 — Pitfalls to watch

Do not run a live clean because dry-run felt slow. Do not ignore paths you do not recognize on the preview list. And remember: the browser lab trains the habit; lasting safety means dry-run on a real shell before deletes.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, clear a few challenges after the starter. On the real shell, dry-run the remove script, then live-run only when the list looks right. When you are ready, take the short quiz, then continue to log and failure triage.
