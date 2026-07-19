# Learn Unix

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](https://creativecommons.org/licenses/by/4.0/)
[![Modules](https://img.shields.io/badge/modules-lab--driven-0A9EDC)](docs/MODULES.md)
[![Tracks](https://img.shields.io/badge/tracks-Real%20Unix%20%7C%20Browser%20lab-blue)](docs/TWO_TRACKS.md)

**learn_unix** is the Unix/shell path split from [`learn_unix_git`](../learn_unix_git/).
Modules follow the lab-driven syllabus ([../../syllabus.md](../../syllabus.md#1-learn_unix)).

## Two learning modes

| Track | Practice surface | Start here |
|-------|------------------|------------|
| **A — Real Unix** | Local terminal + `examples/` | [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) · `./scripts/scaffold.sh` |
| **B — Browser lab** | Platform tools | [http://127.0.0.1:8080/tools/](http://127.0.0.1:8080/tools/) · [live](https://universal-verification-methodology.github.io/learning/tools/) |

Every **lab** module documents both tracks. Intro/wrap modules have no lab.

## Media (PPT / PDF / video)

Use the **module-slides** skill (`.cursor/skills/module-slides/`) per module:

1. Revise `transcript.md` for natural speech (`## Slide N — Title` blocks)
2. Sync + build: `python .cursor/skills/module-slides/scripts/transcript_to_outline.py …`
3. Narrate: `bash .cursor/skills/module-slides/scripts/narrate_clips.sh courses/learn_unix/moduleNN-slug`

See the skill `SKILL.md` for the full pipeline and dual-track narration rules.

## Quick start

```bash
cd courses/learn_unix
chmod +x scripts/*.sh
./scripts/scaffold.sh          # Track A home practice tree
./scripts/module.sh 01 --check # optional env check for module 01
```

Then open [module00-intro/README.md](module00-intro/README.md).

## Module map

See **[docs/MODULES.md](docs/MODULES.md)** for the full table (00–28).

### Clusters

| Modules | Theme |
|---------|--------|
| 00 | Intro / dual-track setup |
| 01–04 | Shell navigation, help, paths, globs |
| 05–08 | Types, links, permissions, dotfiles |
| 09–13 | Processes, jobs, pipes, text, here-docs |
| 14–18 | History, aliases, scripting, safety |
| 19–22 | Projects, archives, backup, symlinks |
| 23–27 | Workflow, Make, dry-run, logs, `.env` |
| 28 | Wrap → learn_git |

## Layout

```
learn_unix/
├── README.md
├── docs/MODULES.md
├── docs/TWO_TRACKS.md
├── scripts/scaffold.sh
├── scripts/module.sh
├── module00-intro/
├── module01-vfs-terminal/
│   ├── README.md
│   ├── CHECKLIST.md
│   ├── EXAMPLES.md
│   ├── outline.yaml
│   ├── transcript.md
│   └── examples/          # Track A
├── …
└── module28-wrap/
```

## Relationship to learn_unix_git

Example trees were copied from `learn_unix_git` modules 1–5 and 8.
Git content stays in `learn_unix_git` until `learn_git` is scaffolded.

## License

CC BY 4.0 — see upstream course materials.
