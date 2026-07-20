# Module 26 — Log / failure triage

**Module id:** module26-log-triage
**Lab:** log-triage
**Tracks:** A · B

## Slide 1 — Log and failure triage

When make sim fails, the log is your first stop—not a random rewrite of the RTL. This module teaches triage: skim the end of the log, search for error and warn lines, then classify the failure as a real design fail, an environment problem, or a flake.

## Slide 2 — Tail, grep, then classify

Start with the last lines—tail shows where the run stopped. Grep for error and warn, case-insensitive, so you do not miss mixed case. Ask: is this expect-got in the testbench, command not found on PATH, or something that passes alone and fails in parallel? Classification decides whether you fix RTL, fix env, or chase timing.

## Slide 3 — Browser lab

![Log triage lab](assets/lab-starter.png)

In the browser lab, load the starter example. You will see short Make and sim log snippets and buttons to mark fail, env, or flake. Read the cues, classify a few cases, and notice how env failures look different from assertion mismatches. Orient yourself with the case list and the challenge strip, then practice the same search habits on a real shell.

## Slide 4 — Real shell practice

![Real shell — log triage](assets/real-shell.png)

In the real Unix track, open this module’s sample log. Print where you are and list the files. Count the lines, then show the last five so you see how the run ended. Grep for error and warn, then for ERROR with line numbers. You will reuse this pattern on every CI and local sim log.

```bash
# pwd — print working directory (where am I?)
pwd

# ls -la — list all entries, long format (what is here?)
ls -la

# wc -l sample.log — count lines in the sample log
wc -l sample.log

# tail -5 sample.log — show the last five lines (how did it end?)
tail -5 sample.log

# grep -i error sample.log — find error lines, case-insensitive
grep -i error sample.log

# grep -i warn sample.log — find warn lines, case-insensitive
grep -i warn sample.log

# grep -n ERROR sample.log — ERROR matches with line numbers
grep -n ERROR sample.log
```

## Slide 5 — Pitfalls to watch

Do not rewrite RTL when the log says command not found. Do not ignore warn lines that foreshadow a timeout. And remember: the browser lab trains classification; lasting skill means tail and grep on real logs before you change design.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, classify a few fail, env, and flake cases after the starter. On the real shell, triage the sample log with tail and grep. When you are ready, take the short quiz, then continue to env-file literacy.
