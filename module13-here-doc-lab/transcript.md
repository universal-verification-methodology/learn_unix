# Module 13 — Here-doc / here-string

**Module id:** module13-here-doc-lab  
**Lab:** here-doc-lab  
**Tracks:** A · B

## Slide 1 — Here-doc / here-string

Sometimes you need to feed a command several lines of input without creating a temp file. A here-document does that: you open with a delimiter, type the body, and close with the same word. A here-string is the one-line cousin—handy for a short phrase. This module makes both feel natural in scripts and one-off shell work.

## Slide 2 — Multi-line stdin vs one string

Less-than less-than EOF starts a here-doc: everything until a line that is exactly EOF becomes the command’s standard input. Leave the delimiter unquoted if you want variables expanded; quote it if you want literal dollars. Three less-thans with a string is a here-string—one chunk of text as stdin. Prefer these over awkward echo pipes when the reader must run in the current shell.

## Slide 3 — Browser lab

![Here-doc lab](assets/lab-starter.png)

In the browser lab, load the starter example. Run cat with a three-line here-doc and watch the body become stdin. Toggle the quoted delimiter so variables stay literal. Try a here-string preset. Orient yourself with the body editor and the contrast cards, try a few challenges, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — here-doc and here-string](assets/real-shell.png)

In the real Unix track, open this module’s here-doc example. Make the reader script executable. Feed cat a two-line here-doc so you see the body printed. Grep inside a here-doc for a matching word. Feed the reader script with a here-doc so it echoes each line. Finish with a here-string into grep—one short string as stdin. You will reuse this when scripts need inline config blocks.

```bash
# chmod u+x read_stdin.sh — make the stdin reader executable
chmod u+x read_stdin.sh

# cat <<EOF … EOF — here-doc: multi-line body becomes cat’s stdin
cat <<EOF
line one
line two
EOF

# grep two <<EOF … EOF — search inside a here-doc body
grep two <<EOF
one
two
three
EOF

# ./read_stdin.sh <<EOF … EOF — feed the script via here-doc
./read_stdin.sh <<EOF
fed via here-doc
EOF

# grep hi <<< "…" — here-string: one string as stdin
grep hi <<< "hi from here-string"
```

## Slide 5 — Pitfalls to watch

The closing delimiter must be alone on its line—no spaces—or the here-doc never ends. Unquoted EOF expands variables; quoted EOF does not—pick deliberately. And remember: the browser lab shows the idea; real scripts still use here-docs on a real shell.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On the real shell, practice a here-doc into cat and the reader script, plus a here-string. When you are ready, take the short quiz, then continue to shell history and reverse-search.
