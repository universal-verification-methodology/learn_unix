#!/usr/bin/env bash
# Track A demo for module20 — tar.gz and zip create + list
set -e

echo "# real shell session (Track A)"
echo

printf '%s\n' "$ ls demo_dir/"
ls demo_dir/
echo

printf '%s\n' "$ tar czf /tmp/m20_demo.tar.gz demo_dir/"
tar czf /tmp/m20_demo.tar.gz demo_dir/
echo

printf '%s\n' "$ tar tzf /tmp/m20_demo.tar.gz"
tar tzf /tmp/m20_demo.tar.gz
echo

printf '%s\n' "$ cd ../zip_archives"
cd ../zip_archives
echo

printf '%s\n' "$ zip -r /tmp/m20_demo.zip demo_dir/"
zip -r /tmp/m20_demo.zip demo_dir/
echo

printf '%s\n' "$ unzip -l /tmp/m20_demo.zip"
unzip -l /tmp/m20_demo.zip
echo
