# Module 03 — Absolute vs relative paths

**Module id:** module03-path-abs-rel  
**Lab:** path-abs-rel  
**Tracks:** A · B

## Slide 1 — Absolute vs relative paths

Paths are how you tell the shell where to go. In design work you jump between source, testbench, and build folders constantly—and a relative path that worked a moment ago can break after you change directories. This module makes absolute and relative paths feel obvious.

## Slide 2 — Absolute vs relative

An absolute path starts from the filesystem root—usually with a leading slash—or from home with a tilde. A relative path is resolved against your current working directory: a plain folder name, a single dot for “here,” or two dots for “up one level.” After you change directory, every relative path is re-aimed at the new place.

## Slide 3 — Browser lab

![Absolute vs relative paths lab](assets/lab-starter.png)

In the browser lab, load the starter example. Watch the current directory, resolve a relative path like going up and into another project folder, then try an absolute or home-based path. Change directory and resolve again—you will see when a relative path breaks. Orient yourself, try a few challenges, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — absolute and relative paths](assets/real-shell.png)

In the real Unix track, open this module’s paths example folder. Print the working directory so you see the absolute path of where you are. List what is here. Change up one level with two dots—that is a relative move—then print the directory again. Change back into paths with a relative name. Finally, jump home with a tilde and print once more: tilde expands to your home directory, which is absolute in effect. You will reuse this when scripts and simulators expect the right path.

```bash
# pwd — print working directory (absolute path of “here”)
pwd

# ls -la — list this folder so you see what relative names refer to
ls -la

# cd .. — relative: move up one directory
cd ..

# pwd — confirm where you landed after the relative move
pwd

# cd paths — relative: enter this folder by name from here
cd paths

# cd ~ — go to your home directory (tilde expands to home)
cd ~

# pwd — home’s absolute path
pwd
```

## Slide 5 — Pitfalls to watch

A relative path is not “wrong”—it is just tied to where you are now. After change-directory, the same short path may fail. Leading slash means from the root; tilde means home. And remember: the browser lab shows the idea; real projects and tools like Icarus and Verilator still need correct paths on a real shell.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On the real shell, practice relative moves with two dots and absolute jumps with slash or tilde. When you are ready, take the short quiz, then continue to globs and wildcards.
