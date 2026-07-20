# Module 24 — Makefile basics

**Module id:** module24-make-basics
**Lab:** make-basics
**Tracks:** A · B

## Slide 1 — Makefile basics

Make reads a Makefile and runs named targets—build, run, clean, help—so you do not retype long compile and sim commands. This module covers the basics you will use in every RTL and verification project: default targets, dependencies, and phony names that are not real files.

## Slide 2 — Targets, deps, and .PHONY

A rule is a target, optional dependencies, then a tab-indented recipe. Make rebuilds when the target is missing or older than a dependency. Names like clean are usually marked .PHONY so Make always runs them even if a file with that name exists. Default make often means all or the first target—here, build.

## Slide 3 — Browser lab

![Makefile basics lab](assets/lab-starter.png)

In the browser lab, load the starter example. You will see a tiny chip Makefile, variables like SIM and TB, a file tree, and make buttons. Run make sim, touch RTL, run again, and watch what rebuilds. Orient yourself with the challenge strip and the Makefile panel, then practice the same ideas on a real shell.

## Slide 4 — Real shell practice

![Real shell — make targets](assets/real-shell.png)

In the real Unix track, open the sample project under this module’s examples. Print where you are, then list the tree so you see the Makefile beside src and tb. Ask Make for help, run the default build, run the demo target that writes a log, list build and logs, then clean and list again. You will reuse these targets in every course project that ships a Makefile.

```bash
# pwd — print working directory (where am I?)
pwd

# ls -la — list all entries, long format (what is here?)
ls -la

# make help — list available targets
make help

# make — default target (all → build); creates build/ and logs/
make

# make run — depends on build; appends a line to logs/run.log
make run

# ls -la build logs — confirm generated dirs and the run log
ls -la build logs

# make clean — remove generated files under build/ and logs/
make clean

# ls build logs — verify cleanup left the directories tidy
ls build logs
```

## Slide 5 — Pitfalls to watch

Run make from the project root so paths in the Makefile resolve. Recipes must use a real tab, not spaces. Do not create a file named clean if clean is a phony target—or mark it .PHONY. And remember: the browser lab teaches the ideas; lasting skill means running make on a real shell.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, clear a few challenges after the starter. On the real shell, run help, build, run, and clean in the sample project. When you are ready, take the short quiz, then continue to the dry-run mindset module.
