# Module 00 — Welcome to Unix for design

**Module id:** module00-intro  
**Lab:** none (intro)  
**Tracks:** A · B (course setup)

## Slide 1 — Welcome to Unix for design

If you work in digital design or verification, you will live in a shell. You will open projects, run simulators, skim logs, and move files—all from a terminal. This short clip welcomes you to learn Unix, and shows how the course is meant to be used.

## Slide 2 — Why the shell matters

Chip and verification work sits on real files and real tools. A graphical editor helps you write RTL, but Make, Git, Icarus, Verilator, and log triage all assume you can navigate a tree, run a command, and read what came back. Getting comfortable here pays off in every later course.

## Slide 3 — Two tracks, one idea

Every lab module offers two ways to practice. The real Unix track uses your own terminal—Linux, macOS, or WSL on Windows—so paths, permissions, and scripts feel real. The browser lab track uses interactive tools on the learning platform, so you can build intuition without installing anything. You may do either track, or both. The usual rhythm is browser first for the idea, then the real shell for muscle memory.

## Slide 4 — Set up the real Unix track

Open a terminal. On Windows, prefer WSL—Windows Subsystem for Linux—so you get a real Unix shell. From the learn Unix course folder, run the scaffold script once. That script only creates a small practice tree under your home directory where checklist exercises can live safely; it does not install course tools. You will come back to that tree throughout the course.

## Slide 5 — Set up the browser lab track

From the monorepo, serve the platform folder with a simple local web server, then open the tools index in your browser. Serving the folder means your browser can load the interactive labs as ordinary web pages. If you prefer, use the published tools site instead. Either way, you only need to confirm you can reach the labs—the next module will send you into a specific one.

## Slide 6 — How to move through modules

For each module, read the README for the outcome, pick a track—or both—then work the checklist. When you finish this intro checklist, continue to the first lab module: the virtual filesystem terminal.
