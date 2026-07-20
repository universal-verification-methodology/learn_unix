# Module 17 — Exit status & conditional chaining

**Module id:** module17-exit-status-lab  
**Lab:** exit-status-lab  
**Tracks:** A · B

## Slide 1 — Exit status and conditional chaining

Every command leaves an exit status. Zero means success; anything else means failure. Scripts set that with exit. You read the last status with dollar-question-mark—check it right away before the next command overwrites it. Double ampersand runs the next command only on success; double pipe runs the next only on failure. This module makes those conventions feel automatic.

## Slide 2 — Zero, non-zero, and short-circuit

Exit zero is the success convention Make, CI, and other scripts rely on. Non-zero signals an error—often one for a generic fail, two for bad usage. Dollar-question-mark is the last command’s code. True and false are tiny commands that exit zero or one so you can practice chaining. Prefer if for real branches; remember that mixing ampersand-ampersand with pipe-pipe on one line is not a clean if-else.

## Slide 3 — Browser lab

![Exit status lab](assets/lab-starter.png)

In the browser lab, load the starter example. Run true and print the status, try false with double ampersand so the echo is skipped, then false with double pipe so a fallback runs. Orient yourself with the terminal, the chain trace, and the and-versus-or cards, try a few challenges, then practice on a real shell.

## Slide 4 — Real shell practice

![Real shell — exit codes](assets/real-shell.png)

In the real Unix track, open this module’s exit-codes example. Make the three scripts executable. Run the success script and print dollar-question-mark—you should see zero. Run the failure script and print the status—you should see one. Check a file that exists, then a missing path, and watch the status flip. Finish with true double-ampersand echo, and false double-pipe echo, to feel short-circuit chaining. You will reuse this whenever a build step must stop or fall back.

```bash
# chmod u+x … — make the demo scripts executable
chmod u+x success.sh failure.sh check_file.sh

# ./success.sh — script exits 0 (success)
./success.sh

# echo $? — print exit status of the last command (expect 0)
echo $?

# ./failure.sh — script exits 1 (failure); status still printable after
./failure.sh
echo $?

# ./check_file.sh README.md — exit 0 if the file exists
./check_file.sh README.md
echo $?

# ./check_file.sh missing.txt — exit 1 when the file is absent
./check_file.sh missing.txt
echo $?

# true && echo ok — run echo only if true succeeded
true && echo ok

# false || echo fallback — run echo only if false failed
false || echo fallback
```

## Slide 5 — Pitfalls to watch

Check dollar-question-mark immediately—any command, even echo, replaces it. Do not treat ampersand-ampersand pipe-pipe as a full if-else. And remember: the browser lab shows the idea; real scripts and Make still key off exit status on a real shell.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, finish a few challenges after the starter. On the real shell, run success and failure scripts and practice double ampersand and double pipe. When you are ready, take the short quiz, then continue to safe scripting.
