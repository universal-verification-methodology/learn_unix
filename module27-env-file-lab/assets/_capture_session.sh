#!/usr/bin/env bash
set -e
cd /mnt/d/proj/designs/learning/courses/learn_unix/module27-env-file-lab/examples/env_file
echo '# real shell session (Track A)'
echo
printf '%s\n' '$ pwd'
pwd
echo
printf '%s\n' '$ ls -la'
ls -la
echo
printf '%s\n' '$ cat sample.env'
cat sample.env
echo
printf '%s\n' '$ chmod u+x use_env.sh'
chmod u+x use_env.sh
echo
printf '%s\n' '$ ./use_env.sh'
./use_env.sh
echo
printf '%s\n' '$ source sample.env'
source sample.env
echo
printf '%s\n' '$ echo MY_VAR=$MY_VAR'
echo "MY_VAR=$MY_VAR"
echo
printf '%s\n' '$ echo ANOTHER_VAR=$ANOTHER_VAR'
echo "ANOTHER_VAR=$ANOTHER_VAR"
echo
