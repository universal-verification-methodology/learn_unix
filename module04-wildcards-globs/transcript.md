# Module 04 — Globs & wildcards

**Module id:** module04-wildcards-globs  
**Lab:** wildcards-globs  
**Tracks:** A · B

## Slide 1 — Globs & wildcards

When you work with many Verilog files or log files, you do not want to type every name. Globs—also called wildcards—let the shell expand a pattern into a list of matching filenames before the command runs. This module makes star, question mark, and brackets feel natural.

## Slide 2 — Star, question mark, brackets

Star matches any sequence of characters, including none—so star-dot-txt means every file ending in that extension. Question mark matches exactly one character—handy for data underscore question-mark log. Brackets match one character from a set or a range, like a, b, or c in square brackets. The shell expands these patterns first; the command only sees the resulting names.

## Slide 3 — Browser lab

![Globs and wildcards lab](assets/lab-starter.png)

In the browser lab, load the starter example. The pattern starts as star-dot-txt—watch which names light up. Try a question-mark pattern for the log files, then a star pattern, and notice that hidden names like gitignore are not matched by a bare star. Orient yourself with the pattern box and the file list, try a few challenges, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — globs and wildcards](assets/real-shell.png)

In the real Unix track, open this module’s wildcards example folder. List everything so you see the sample names. Then list only text files with a star pattern. Narrow to reports with a prefix and a star. Use a question mark for the numbered logs. Match the single-letter text files with a character class. You will use the same idea later for source files and build logs.

```bash
# ls — see every name in this folder first
ls

# ls *.txt — star matches any sequence; list all .txt files
ls *.txt

# ls report_*.txt — star after a prefix; only report_… text files
ls report_*.txt

# ls data_?.log — question mark matches exactly one character
ls data_?.log

# ls [abc].txt — brackets: one character from the set a, b, or c
ls [abc].txt
```

## Slide 5 — Pitfalls to watch

The shell expands the pattern before the command runs—so remove-star-dot-log becomes a list of real filenames. If nothing matches, bash may leave the pattern literal. Always list a destructive pattern first. And remember: the browser lab shows the idea; real projects still need globs on a real shell for scripts and simulators.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On the real shell, practice star, question mark, and brackets on this module’s sample files. When you are ready, take the short quiz, then continue to file types and links.
