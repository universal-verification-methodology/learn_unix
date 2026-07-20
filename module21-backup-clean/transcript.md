# Module 21 — Backup & clean-build

**Module id:** module21-backup-clean  
**Lab:** backup-clean  
**Tracks:** A · B

## Slide 1 — Backup and clean-build

Build folders and logs grow fast—waveforms, object files, run logs. Before you wipe them, take a timestamped backup of the sources you care about. Then list what a clean would remove, and only then delete. This module is the backup-first, clean-second habit for every chip project tree.

## Slide 2 — Timestamp, exclude, then clean

Name archives with a date stamp so versions do not overwrite each other. Exclude build and logs from the backup when you only need sources, docs, and scripts. For clean: list files under build and logs first, then remove—never start with a blind recursive delete. Align exclude patterns with your ignore file so archives and Git stay consistent.

## Slide 3 — Browser lab

![Backup and clean lab](assets/lab-starter.png)

In the browser lab, load the starter example. Follow the steps: backup to a timestamped tar, dry-run clean, then clean for real—the lab refuses clean until you back up. Orient yourself with the step strip, the project tree, and the action buttons, try a few challenges, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — backup then list clean targets](assets/real-shell.png)

In the real Unix track, open the clean-build sample project. List the generated files under build and logs. Create a timestamped tar of the project while excluding those generated dirs, then list the archive. Run find again as a dry-run of what a clean would remove—only run the clean script when you mean to empty those folders. You will reuse backup-then-clean before every big rebuild or share.

```bash
# find … -type f — list generated files under build/ and logs/
find sample_project/build sample_project/logs -type f

# tar czf backup_….tar.gz — timestamped archive excluding build and logs
tar czf /tmp/m21_backup_demo.tar.gz \
  --exclude='build' --exclude='logs' \
  -C sample_project .

# tar tzf … — list what was backed up (no build/logs)
tar tzf /tmp/m21_backup_demo.tar.gz

# find again — dry-run view of clean targets (do not delete yet)
find sample_project/build sample_project/logs -type f

# ./clean.sh — only when ready: delete files in build/ and logs/
# chmod u+x clean.sh && ./clean.sh
```

## Slide 5 — Pitfalls to watch

Never clean before you have a backup you can restore. Do not run recursive delete on a path you have not listed. And remember: the browser lab shows the idea; lasting project hygiene still means real archives and careful cleans on a real shell.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish the backup → dry-run → clean flow. On the real shell, make a timestamped archive and list clean targets before you delete. When you are ready, take the short quiz, then continue to relative symlink pitfalls.
