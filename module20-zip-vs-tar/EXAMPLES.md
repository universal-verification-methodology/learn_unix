# Module 20 examples — tar vs zip

Track A (real Unix). Each folder was adapted from `learn_unix / learn_git (legacy archive ignored)`.

## `tar_archives/`

See [`examples/tar_archives/README.md`](examples/tar_archives/README.md).

```bash
cd module20-zip-vs-tar/examples/tar_archives

# Create / list / extract
tar czf demo.tar.gz demo_dir/
tar tzf demo.tar.gz
mkdir -p /tmp/tar_extract && tar xzf demo.tar.gz -C /tmp/tar_extract
ls /tmp/tar_extract/demo_dir/
```

## `zip_archives/`

See [`examples/zip_archives/README.md`](examples/zip_archives/README.md).

```bash
cd module20-zip-vs-tar/examples/zip_archives

# Create / list / extract
zip -r demo.zip demo_dir/
unzip -l demo.zip
mkdir -p /tmp/zip_extract && unzip -o demo.zip -d /tmp/zip_extract
ls /tmp/zip_extract/demo_dir/
```
