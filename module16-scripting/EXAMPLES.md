# Module 16 examples — Script control flow

Track A (real Unix). Each folder ships under this module’s `examples/`.

## `script_basics/`

See [`examples/script_basics/README.md`](examples/script_basics/README.md).

```bash
cd module16-scripting/examples/script_basics
chmod u+x say_hello.sh
./say_hello.sh
bash say_hello.sh
```

## `arguments/`

See [`examples/arguments/README.md`](examples/arguments/README.md).

```bash
cd module16-scripting/examples/arguments
chmod u+x greet.sh
./greet.sh Alice
./greet.sh "Bob Smith"
./greet.sh
```

## `control_flow/`

See [`examples/control_flow/README.md`](examples/control_flow/README.md).

```bash
cd module16-scripting/examples/control_flow
chmod u+x count_lines.sh
./count_lines.sh
wc -l *.log
```

## `case_statement/`

See [`examples/case_statement/README.md`](examples/case_statement/README.md).

```bash
cd module16-scripting/examples/case_statement
chmod u+x greet.sh
./greet.sh hello
./greet.sh bye
./greet.sh other
```

## `read_input/`

See [`examples/read_input/README.md`](examples/read_input/README.md).

```bash
cd module16-scripting/examples/read_input
chmod u+x prompt_name.sh confirm.sh
# interactive: follow the prompts
./prompt_name.sh
```
