# Module 08 — Dotfiles & config homes

**Module id:** module08-dotfiles-lab  
**Lab:** dotfiles-lab  
**Tracks:** A · B

## Slide 1 — Dotfiles & config homes

Names that start with a dot are usually hidden from a plain list—and that is where a lot of your shell and tool configuration lives. Bashrc, gitignore, and the config directory under home shape how your environment behaves. This module teaches you to reveal those names safely and read them before you change anything.

## Slide 2 — Hidden names and home config

A plain list shows only visible names. Add all-files mode and the dots appear: hidden files, hidden directories, and project files like gitignore. Home is full of them—bashrc for interactive Bash, profile for login shells, gitconfig for your identity. Projects add their own, especially the git directory and ignore rules. Listing with all-files is the first habit; editing comes later.

## Slide 3 — Browser lab

![Dotfiles lab](assets/lab-starter.png)

In the browser lab, load the starter example. You start in the lab home. Run a plain list, then list all so dotfiles appear. Open bashrc, then change into the chip project and inspect gitignore. Orient yourself with the listing and the preview panel, try a few challenges, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — dotfiles](assets/real-shell.png)

In the real Unix track, open this module’s dotfiles example folder. List with a plain list—you mostly see the visible files. List all, then list all in long format so hidden names and the hidden directory show up. Read the hidden sample file and the sample rc so you see they are ordinary text. Optionally peek at a few names in your real home with list-all and head—read only; do not edit configs until you know what they do.

```bash
# ls — plain list; dot-names stay hidden
ls

# ls -a — show all names, including those starting with a dot
ls -a

# ls -la — long listing that includes hidden names
ls -la

# cat .hidden_file — read a hidden file (safe inspect)
cat .hidden_file

# cat .sample_rc — read an example config-style dotfile
cat .sample_rc

# ls -a ~ | head -12 — peek at real home dotfiles (read-only)
ls -a ~ | head -12
```

## Slide 5 — Pitfalls to watch

Do not edit bashrc or profile until you understand the change—a typo can break new shells. Prefer read tools first: cat or less. Remember that star globs often skip leading-dot names unless you ask for them. And remember: the browser lab shows the idea; your real home and projects still live on a real shell.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On the real shell, practice plain list versus list-all, and read a couple of sample dotfiles. When you are ready, take the short quiz, then continue to process list and signals.
