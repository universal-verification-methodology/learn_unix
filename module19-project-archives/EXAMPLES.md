# Module 19 examples — Project layout, archives, sed & diff

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `project_structure/`

See [`examples/project_structure/README.md`](examples/project_structure/README.md).

```bash
cd module19-project-archives/examples/project_structure/sample_project
ls -la
ls src tb docs scripts build
find . -type f
# tree .   # if installed
```

## `find_grep/`

See [`examples/find_grep/README.md`](examples/find_grep/README.md).

```bash
cd module19-project-archives/examples/find_grep
find . -name "*.v"
grep -Rn "CLOCK_SIGNAL" .
grep -Rl "CLOCK_SIGNAL" .
```

## `sed_basics/`

See [`examples/sed_basics/README.md`](examples/sed_basics/README.md).

```bash
cd module19-project-archives/examples/sed_basics
sed 's/old/new/' sample.txt
sed 's/old/new/g' sample.txt
sed -n '2p' sample.txt
# Test before in-place: cp sample.txt sample.bak && sed -i 's/old/NEW/' sample.txt
```

## `diff_patch/`

See [`examples/diff_patch/README.md`](examples/diff_patch/README.md).

```bash
cd module19-project-archives/examples/diff_patch
diff original.txt modified.txt
diff -u original.txt modified.txt
# Optional: diff -u original.txt modified.txt > change.patch
```

## `editor/`

See [`examples/editor/README.md`](examples/editor/README.md).

```bash
cd module19-project-archives/examples/editor
ls -la
# Open sample.txt / sample.v in your preferred editor
```
