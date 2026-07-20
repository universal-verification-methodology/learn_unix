# Module 06 — realpath / readlink

**Module id:** module06-realpath-resolve  
**Lab:** realpath-resolve  
**Tracks:** A · B

## Slide 1 — realpath / readlink

Relative paths and symlinks are handy—until a script needs one clear absolute location. realpath and readlink help you resolve a path to a canonical form: no dots, no parent hops left in the string, and symlinks followed to the real file. This module shows when the stored link string is enough and when you need the full resolve.

## Slide 2 — Stored target vs canonical path

readlink on a symlink prints the stored target string—often a short relative path. realpath (and readlink with a force-style flag on Linux) cleans dots and parent segments and follows links until you get one absolute path. That difference matters in build scripts: you may store a relative link for portability, then resolve it when you need the real file on disk.

## Slide 3 — Browser lab

![realpath resolve lab](assets/lab-starter.png)

In the browser lab, load the starter example. Compare readlink on a project link—you see the short stored target—with realpath on the same name—you see the canonical absolute path. Try a chain of links if the lab offers one. Orient yourself with the side-by-side results, try a few challenges, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — realpath and readlink](assets/real-shell.png)

In the real Unix track, open this module’s realpath example folder. Print the working directory, then ask realpath for the current directory and for the sample file—both become absolute. List the symlink that points at the file. Use readlink to see the short stored target, then realpath and readlink with the force flag so you see the same canonical file path. You will reuse this when scripts need “where am I really?”

```bash
# pwd — where you are before resolving
pwd

# realpath . — absolute canonical path of the current directory
realpath .

# realpath a_file.txt — absolute path of the sample file
realpath a_file.txt

# ls -l link_to_file — see the symlink arrow to the file
ls -l link_to_file

# readlink link_to_file — stored target string (often relative)
readlink link_to_file

# realpath link_to_file — follow the link to a canonical absolute path
realpath link_to_file

# readlink -f link_to_file — Linux-style canonical path (same idea as realpath)
readlink -f link_to_file
```

## Slide 5 — Pitfalls to watch

A broken link still has a stored string—readlink can print it—but realpath typically fails because the final file is missing. Do not assume every system has the same readlink flags; realpath from coreutils is often the clearer choice in scripts. And remember: the browser lab shows the idea; real projects still resolve paths on a real shell.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On the real shell, compare readlink’s stored target with realpath’s canonical path. When you are ready, take the short quiz, then continue to permissions, umask, and PATH.
