# Module 05 — File types & links

**Module id:** module05-file-types-lab  
**Lab:** file-types-lab  
**Tracks:** A · B

## Slide 1 — File types & links

Not every name in a directory is the same kind of thing. Some are ordinary files, some are folders, and some are symbolic links that point elsewhere. In design trees you meet all three—source files, directories, and shortcuts into toolchains or shared IP. This module teaches you to read the long listing and follow a link safely.

## Slide 2 — Dash, dee, and ell

In a long listing, the first character is the type. A dash means a regular file. The letter d means a directory. The letter l means a symbolic link—and the listing often shows an arrow to the target. Soft links are names that point at another path; if that path is missing, the link is broken, but you can still read the intended target with readlink.

## Slide 3 — Browser lab

![File types and links lab](assets/lab-starter.png)

In the browser lab, load the starter example. Study the long listing: directories, files, and symlinks. Notice which link is broken. Use the mini terminal for list, make-link, and readlink when you are ready. Orient yourself, try a few challenges, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — file types and links](assets/real-shell.png)

In the real Unix track, open this module’s file-types example folder. List in long format and read the first character of each line. Inspect the working symlink—list it, then print its target with readlink. Ask the file command what sample text and the symlink look like. Finally, readlink the broken link and list it: the target string is still there even though the file does not exist.

```bash
# ls -l — long listing; first character is the type (-, d, or l)
ls -l

# ls -l my_symlink — inspect the working symlink line (arrow to target)
ls -l my_symlink

# readlink my_symlink — print the path the symlink points to
readlink my_symlink

# file sample.txt — classify the regular file
file sample.txt

# file my_symlink — classify the symlink (follows or reports the link)
file my_symlink

# readlink broken_link — target path even when the target is missing
readlink broken_link

# ls -l broken_link — see the broken symlink in the long listing
ls -l broken_link
```

## Slide 5 — Pitfalls to watch

Removing a symlink with remove deletes the link name, not the target file—unless you remove the target itself. Do not confuse a broken link with “nothing there”: readlink still prints a path. And remember: the browser lab shows the idea; real projects still need you to read listings and links on a real shell.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On the real shell, practice long listing, readlink, and spotting a broken link. When you are ready, take the short quiz, then continue to realpath and resolving paths.
