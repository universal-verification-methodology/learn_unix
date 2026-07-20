# Module 13 examples — Here-doc / here-string

Track A (real Unix). Each folder was adapted from `learn_unix_git`.

## `here_doc/`

See [`examples/here_doc/README.md`](examples/here_doc/README.md) if present.

**Try these** (from `examples/here_doc`):

```bash
# chmod u+x read_stdin.sh — make the stdin reader executable
chmod u+x read_stdin.sh

# cat <<EOF … EOF — multi-line body → cat’s stdin
cat <<EOF
line one
line two
EOF

# grep two <<EOF … EOF — search inside a here-doc
grep two <<EOF
one
two
three
EOF

# ./read_stdin.sh <<EOF … EOF — feed the script via here-doc
./read_stdin.sh <<EOF
fed via here-doc
EOF

# grep hi <<< "…" — here-string (one string as stdin)
grep hi <<< "hi from here-string"
```
