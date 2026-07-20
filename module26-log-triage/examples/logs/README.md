# Logs and outputs example

Practice **inspecting** log directories and **searching** logs with `tail`, `less`, and `grep`.

## Layout

```
logs/
├── README.md           # this file
├── sample.log          # sample log for grep/tail/less practice
└── commands_to_try.txt  # copy-paste commands
```

## Try these (from this directory)

```bash
cd module26-log-triage/examples/logs
wc -l sample.log
tail -5 sample.log
grep -i error sample.log
grep -i warn sample.log
grep -n ERROR sample.log
# less sample.log   # interactive: /error to search
```

## Analyzing logs

- **tail** — last N lines: `tail -50 sample.log`
- **less** — scroll and search: `less sample.log` then `/error`
- **grep** — filter by keyword: `grep -i error sample.log`, `grep -i warn sample.log`

## Triage classes

| Class | Typical cues |
|-------|----------------|
| **fail** | expect/got, assertion, syntax error, X-prop |
| **env** | command not found, license, no space left |
| **flake** | timeout + prior pass, fails under `-j`, alone PASS |

See `commands_to_try.txt` and use `sample.log` for practice.
