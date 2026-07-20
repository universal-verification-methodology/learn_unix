---
marp: true
title: tar versus zip
paginate: true
---

# tar versus zip

You will ship trees as archives, homework drops, IP handoffs, backup snapshots

---

## Create, list, extract
- Tar create with gzip is tar c-z-f, then the archive name, then the directory
- List with t-z-f; extract with x-z-f
- Zip uses zip dash-r to recurse, unzip dash-l to list, and unzip to extract
- Remember: c create, x extract, t list, z gzip, f file
- Exclude build and logs when packing a project so the archive stays small

---

## Browser lab
![Zip versus tar lab](assets/lab-starter.png)

---

## Real shell practice
![Real shell — tar and zip](assets/real-shell.png)

---

## Real shell practice — try these

```
# ls demo_dir/ — see the sample tree to pack (tar_archives/)
ls demo_dir/

# tar czf … — create a gzip-compressed tar of demo_dir
tar czf /tmp/m20_demo.tar.gz demo_dir/

# tar tzf … — list archive contents without extracting
tar tzf /tmp/m20_demo.tar.gz

# cd ../zip_archives — switch to the zip example tree
cd ../zip_archives

# zip -r … — create a recursive zip of demo_dir
zip -r /tmp/m20_demo.zip demo_dir/

# unzip -l … — list zip contents without extracting
unzip -l /tmp/m20_demo.zip

```

---

## Pitfalls to watch
- The f flag’s next argument is the archive filename, put options before the name carefully
- Prefer listing before extract so you know what will unpack
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish a few challenges after the starter
- On the real shell, create and list both a tar.gz and a zip
- When you are ready, take the short quiz, then continue to backup and clean-build

