#!/usr/bin/env python3
"""Scaffold courses/learn_unix from syllabus (lab-driven + dual tracks)."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # courses/learn_unix
COURSES = ROOT.parent
SRC = COURSES / "learn_unix_git"
DST = ROOT

LAB_BASE_LOCAL = "http://127.0.0.1:8080/tools"
LAB_BASE_LIVE = "https://universal-verification-methodology.github.io/learning/tools"

# (num, slug, kind, title, lab_id|None, status, source_example_dirs relative to learn_unix_git)
MODULES = [
    (0, "intro", "intro", "Welcome to Unix for design", None, None, []),
    (1, "vfs-terminal", "lab", "Virtual filesystem terminal", "vfs-terminal", "S",
     ["module1/examples/navigation", "module1/examples/viewing", "module1/examples/file_operations",
      "module1/examples/touch", "module1/examples/ls_options", "module1/examples/wc_basics",
      "module1/examples/design_files"]),
    (2, "man-help-lab", "lab", "man / --help discoverability", "man-help-lab", "S",
     ["module1/examples/help"]),
    (3, "path-abs-rel", "lab", "Absolute vs relative paths", "path-abs-rel", "S",
     ["module1/examples/paths"]),
    (4, "wildcards-globs", "lab", "Globs & wildcards", "wildcards-globs", "S",
     ["module1/examples/wildcards"]),
    (5, "file-types-lab", "lab", "File types & links", "file-types-lab", "S",
     ["module2/examples/file_types"]),
    (6, "realpath-resolve", "lab", "realpath / readlink", "realpath-resolve", "S",
     ["module2/examples/realpath"]),
    (7, "permissions", "lab", "Permissions, umask, PATH", "permissions", "S",
     ["module2/examples/permissions", "module2/examples/umask", "module2/examples/ownership",
      "module2/examples/groups", "module2/examples/path_and_script", "module2/examples/environment",
      "module2/examples/env_export"]),
    (8, "dotfiles-lab", "lab", "Dotfiles & config homes", "dotfiles-lab", "S",
     ["module2/examples/dotfiles"]),
    (9, "ps-kill-lab", "lab", "Process list & signals", "ps-kill-lab", "S",
     ["module3/examples/processes"]),
    (10, "job-control-lab", "lab", "Job control", "job-control-lab", "S",
     ["module3/examples/background"]),
    (11, "pipes", "lab", "Pipes, redirection, xargs", "pipes", "S",
     ["module3/examples/pipes", "module3/examples/redirection", "module3/examples/xargs",
      "module3/examples/combining", "module3/examples/troubleshooting"]),
    (12, "sort-uniq-cut", "lab", "sort / uniq / cut", "sort-uniq-cut", "S",
     ["module3/examples/sort_uniq", "module3/examples/cut_columns"]),
    (13, "here-doc-lab", "lab", "Here-doc / here-string", "here-doc-lab", "S",
     ["module3/examples/here_doc"]),
    (14, "shell-history", "lab", "Shell history & reverse-search", "shell-history", "S",
     ["module4/examples/history"]),
    (15, "alias-lab", "lab", "Alias & functions", "alias-lab", "S",
     ["module4/examples/aliases", "module4/examples/functions"]),
    (16, "scripting", "lab", "Script control flow", "scripting", "S",
     ["module4/examples/script_basics", "module4/examples/arguments", "module4/examples/control_flow",
      "module4/examples/case_statement", "module4/examples/read_input"]),
    (17, "exit-status-lab", "lab", "Exit status & && / ||", "exit-status-lab", "S",
     ["module4/examples/exit_codes"]),
    (18, "safe-scripting", "lab", "Safe scripting", "safe-scripting", "S",
     ["module4/examples/safe_scripting"]),
    (19, "project-archives", "lab", "Project layout, archives, sed & diff", "project-archives", "S",
     ["module5/examples/project_structure", "module5/examples/find_grep", "module5/examples/sed_basics",
      "module5/examples/diff_patch", "module5/examples/editor"]),
    (20, "zip-vs-tar", "lab", "tar vs zip", "zip-vs-tar", "S",
     ["module5/examples/tar_archives", "module5/examples/zip_archives"]),
    (21, "backup-clean", "lab", "Backup & clean-build", "backup-clean", "S",
     ["module5/examples/backup", "module5/examples/clean_build"]),
    (22, "link-relative", "lab", "Relative symlink pitfalls", "link-relative", "S",
     ["module5/examples/link_relative"]),
    (23, "workflow", "lab", "Pre-push / Make / env checklist", "workflow", "S",
     ["module8/examples/pre_push_checks", "module8/examples/scripts"]),
    (24, "make-basics", "lab", "Makefile basics", "make-basics", "P",
     ["module8/examples/makefile_basics"]),
    (25, "dry-run-lab", "lab", "Dry-run mindset", "dry-run-lab", "P",
     ["module8/examples/dry_run"]),
    (26, "log-triage", "lab", "Log / failure triage", "log-triage", "P",
     ["module8/examples/logs"]),
    (27, "env-file-lab", "lab", ".env literacy", "env-file-lab", "P",
     ["module8/examples/env_file"]),
    (28, "wrap", "wrap", "Unix path complete → Git", None, None, []),
]


def mod_dir(num: int, slug: str) -> Path:
    return DST / f"module{num:02d}-{slug}"


def lab_urls(lab_id: str) -> tuple[str, str]:
    return (f"{LAB_BASE_LOCAL}/{lab_id}/index.html", f"{LAB_BASE_LIVE}/{lab_id}/")


def write_module_readme(num: int, slug: str, kind: str, title: str, lab_id: str | None, status: str | None) -> None:
    d = mod_dir(num, slug)
    d.mkdir(parents=True, exist_ok=True)
    nn = f"{num:02d}"
    prev_n = num - 1
    next_n = num + 1
    prev = next((m for m in MODULES if m[0] == prev_n), None)
    nxt = next((m for m in MODULES if m[0] == next_n), None)

    nav = []
    if prev:
        nav.append(f"[← {prev[3]}](../module{prev[0]:02d}-{prev[1]}/README.md)")
    else:
        nav.append("← Start")
    nav.append(f"[Course README](../README.md)")
    if nxt:
        nav.append(f"[{nxt[3]} →](../module{nxt[0]:02d}-{nxt[1]}/README.md)")
    else:
        nav.append("End →")
    nav_line = " · ".join(nav)

    if kind == "intro":
        body = f"""# Module {nn}: {title}

**Kind:** `intro` · Dual-track course welcome

{nav_line}

## What this course is

**learn_unix** teaches shell fluency for digital design students using **two learning modes** on every lab module:

| Track | Where you practice | Best for |
|-------|--------------------|----------|
| **A — Real Unix** | Your local terminal (Linux, macOS, or WSL2) | Muscle memory, real paths, scripts you keep |
| **B — Browser lab** | Interactive lab on the learning platform | Concept literacy, no install, quick feedback |

You can do **A only**, **B only**, or **both** (recommended: B for intuition, then A for fidelity).

## Setup (Track A)

1. Open a terminal (WSL2 recommended on Windows).
2. Clone or open this repo and `cd` into `courses/learn_unix`.
3. Run: `./scripts/scaffold.sh` to create `~/unix_practice/`.

## Setup (Track B)

1. Serve the platform: `python -m http.server 8080 --directory platform` (from monorepo root).
2. Open http://127.0.0.1:8080/tools/index.html
3. Or use the live site: {LAB_BASE_LIVE}/

## How to move through modules

1. Read the module **README** (outcomes).
2. Pick a track (or both).
3. Check off **CHECKLIST.md**.
4. Optional: skim `outline.yaml` / `transcript.md` for upcoming slides & clips.

## Next

→ [Module 01: Virtual filesystem terminal](../module01-vfs-terminal/README.md)
"""
    elif kind == "wrap":
        body = f"""# Module {nn}: {title}

**Kind:** `wrap`

{nav_line}

## You can now

- Navigate, inspect, and edit files from a shell
- Use pipes, jobs, and basic scripts safely
- Organize a small design-style project (`src/`, `tb/`, archives, Make hygiene)

## Dual-track recap

If you mainly used **browser labs**, spend a short session on Track A for modules 01, 07, 11, and 16–18 so real paths and scripts feel natural.  
If you mainly used **real Unix**, skim any skipped browser labs for visual challenges.

## Next course

→ **learn_git** (syllabus: [../../syllabus.md](../../syllabus.md#2-learn_git))  
Legacy combined path still lives in [`../learn_unix_git/`](../learn_unix_git/).

## Checklist

- [ ] I completed Track A and/or Track B for the lab modules I care about
- [ ] I can explain abs vs rel paths and why globs expand before the command runs
- [ ] I have a `~/unix_practice` (or similar) tree I can reuse in Git
"""
    else:
        assert lab_id and status
        local, live = lab_urls(lab_id)
        status_note = "Shipped" if status == "S" else "Planned (Coming soon on tools index — use Track A until it ships)"
        body = f"""# Module {nn}: {title}

**Kind:** `lab` · Primary lab: `{lab_id}` · **{status_note}**

{nav_line}

## Outcomes

After this module you can explain and practice the ideas taught by **`{lab_id}`**, in the browser and/or on a real shell.

## Two tracks (pick one or both)

### Track A — Real Unix (hands-on)

Work in your local terminal using this module’s `examples/` (copied from the proven `learn_unix_git` trees).

1. Open [EXAMPLES.md](EXAMPLES.md) and run the “Try these” commands.
2. Complete [CHECKLIST.md](CHECKLIST.md) on a real filesystem (`~/unix_practice` recommended).
3. Optional self-check: `./scripts/module.sh {nn} --check` (from course root).

### Track B — Browser lab (online)

1. Local: [{local}]({local})
2. Live: [{live}]({live})
3. Load the **starter example**, then work challenges.
4. Check off the Track B items in [CHECKLIST.md](CHECKLIST.md).

> Concept labs are literacy tools — they do not replace a real shell for scripts you will keep in a design project.

## Media (planned)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript stub | [transcript.md](transcript.md) |
| Slides / video | `media/module{nn}/` (generate later) |

## Files

```
module{nn}-{slug}/
├── README.md       # this file
├── CHECKLIST.md    # Track A + Track B checkboxes
├── EXAMPLES.md     # real-Unix example index
├── outline.yaml    # slide / clip outline
├── transcript.md   # speakable stub
└── examples/       # hands-on trees (Track A)
```
"""
    (d / "README.md").write_text(body, encoding="utf-8")


def write_checklist(num: int, slug: str, kind: str, title: str, lab_id: str | None) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind == "intro":
        text = f"""# Module {nn} checklist — {title}

## Setup

- [ ] Terminal available (Linux / macOS / WSL2)
- [ ] Opened this repo at `courses/learn_unix`
- [ ] Ran `./scripts/scaffold.sh` (or created `~/unix_practice` yourself)
- [ ] Opened the [tools index]({LAB_BASE_LOCAL}/index.html) once (or live site)

## Mindset

- [ ] I understand Track A = real Unix, Track B = browser lab
- [ ] I know I can do either track, or both
"""
    elif kind == "wrap":
        text = f"""# Module {nn} checklist — {title}

- [ ] Reviewed outcomes in [README.md](README.md)
- [ ] Ready to start **learn_git** (or continue practicing weak modules)
"""
    else:
        text = f"""# Module {nn} checklist — {title}

## Track A — Real Unix

- [ ] Worked through at least one example under `examples/` (see [EXAMPLES.md](EXAMPLES.md))
- [ ] Repeated the key commands in `~/unix_practice` (or another writable tree)
- [ ] Can explain the outcome in my own words

## Track B — Browser lab (`{lab_id}`)

- [ ] Opened the lab (local or live)
- [ ] Loaded the starter example
- [ ] Completed a few challenges (or noted the lab is still Coming soon)

## Done when

- [ ] I can do the task on a real shell **or** I finished the browser challenges (preferably both)
"""
    (d / "CHECKLIST.md").write_text(text, encoding="utf-8")


def write_examples_md(num: int, slug: str, kind: str, title: str, copied: list[str]) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind != "lab":
        (d / "EXAMPLES.md").write_text(
            f"# Module {nn} — no Track A example trees\n\nThis is an `{kind}` module. See [README.md](README.md).\n",
            encoding="utf-8",
        )
        return
    lines = [
        f"# Module {nn} examples — {title}",
        "",
        "Track A (real Unix). Each folder was adapted from `learn_unix_git`.",
        "",
    ]
    if not copied:
        lines.append("_No example trees copied yet — use the browser lab and your own `~/unix_practice`._")
    else:
        for name in copied:
            lines += [
                f"## `{name}/`",
                "",
                f"See [`examples/{name}/README.md`](examples/{name}/README.md) if present.",
                "",
                "**Try:**",
                "",
                "```bash",
                f"cd module{nn}-{slug}/examples/{name}",
                "ls -la",
                "```",
                "",
            ]
    (d / "EXAMPLES.md").write_text("\n".join(lines), encoding="utf-8")


def write_outline_transcript(num: int, slug: str, kind: str, title: str, lab_id: str | None) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    outline = f"""# Module {nn} outline
title: "{title}"
kind: {kind}
lab: {lab_id or "null"}
slides:
  - Course context / why this matters for digital design
  - Core idea (1 concept)
  - Track B: show lab starter (if lab module)
  - Track A: one real-shell demo
  - Common pitfalls
  - Your turn + quiz prompt
duration_minutes: 8
"""
    (d / "outline.yaml").write_text(outline, encoding="utf-8")
    transcript = f"""# Module {nn} transcript — {title}

> Stub for voiceover / clip. Expand when recording.

## Hook

In digital design work you will live in a shell. This module: **{title}**.

## Teach

(3–5 sentences on the concept.)

## Show Track B

Open the browser lab{", `" + lab_id + "`" if lab_id else ""}. Load the starter. Point at the UI.

## Show Track A

In a real terminal, demonstrate one command sequence from `examples/`.

## Your turn

Complete the checklist for at least one track. Then take the short quiz.
"""
    (d / "transcript.md").write_text(transcript, encoding="utf-8")


def copy_examples(num: int, slug: str, sources: list[str]) -> list[str]:
    if not sources:
        return []
    dest_ex = mod_dir(num, slug) / "examples"
    dest_ex.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for rel in sources:
        src = SRC / rel
        if not src.exists():
            print(f"  skip missing {rel}")
            continue
        name = src.name
        dst = dest_ex / name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        copied.append(name)
    readme = dest_ex / "README.md"
    readme.write_text(
        "# Examples\n\nTrack A trees for this module. See ../EXAMPLES.md.\n",
        encoding="utf-8",
    )
    return copied


def write_docs_index() -> None:
    docs = DST / "docs"
    docs.mkdir(exist_ok=True)
    rows = []
    for num, slug, kind, title, lab_id, status, _ in MODULES:
        lab = f"`{lab_id}`" if lab_id else "—"
        st = status or "—"
        rows.append(
            f"| {num:02d} | `{kind}` | [{title}](../module{num:02d}-{slug}/README.md) | {lab} | {st} |"
        )
    text = f"""# learn_unix — module index

Lab-driven syllabus (pass 3). Full product syllabus: [../../syllabus.md](../../syllabus.md#1-learn_unix).

| # | Kind | Module | Lab | Status |
|---|------|--------|-----|--------|
{chr(10).join(rows)}

## Dual tracks

See [TWO_TRACKS.md](TWO_TRACKS.md).
"""
    (docs / "MODULES.md").write_text(text, encoding="utf-8")
    (docs / "TWO_TRACKS.md").write_text(
        f"""# Two learning tracks

## Track A — Real Unix

Practice on a real shell (Linux, macOS, or **WSL2** on Windows).

- Examples live under each `moduleNN-*/examples/`
- Scaffold: `./scripts/scaffold.sh` → `~/unix_practice/`
- Self-check: `./scripts/module.sh NN --check`

Use this track when you need **fidelity**: real paths, permissions, jobs, scripts you will commit.

## Track B — Browser lab

Practice in the learning platform concept labs (no install).

- Local tools: {LAB_BASE_LOCAL}/
- Live: {LAB_BASE_LIVE}/
- Each lab module README links its primary lab id

Use this track for **intuition** and quick challenges. Planned labs show “Coming soon”; use Track A until they ship.

## Recommended path

1. **Track B** starter + a few challenges (5–10 min)
2. **Track A** examples + checklist (10–20 min)
3. Optional quiz / transcript review

Doing only one track is OK for self-study; courses that assume Unix later (Git, Make, simulators) expect Track A comfort.
""",
        encoding="utf-8",
    )


def write_course_readme() -> None:
    lines = [
        "# Learn Unix",
        "",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](https://creativecommons.org/licenses/by/4.0/)",
        "[![Modules](https://img.shields.io/badge/modules-lab--driven-0A9EDC)](docs/MODULES.md)",
        "[![Tracks](https://img.shields.io/badge/tracks-Real%20Unix%20%7C%20Browser%20lab-blue)](docs/TWO_TRACKS.md)",
        "",
        "**learn_unix** is the Unix/shell path split from [`learn_unix_git`](../learn_unix_git/).",
        "Modules follow the lab-driven syllabus ([../../syllabus.md](../../syllabus.md#1-learn_unix)).",
        "",
        "## Two learning modes",
        "",
        "| Track | Practice surface | Start here |",
        "|-------|------------------|------------|",
        "| **A — Real Unix** | Local terminal + `examples/` | [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) · `./scripts/scaffold.sh` |",
        f"| **B — Browser lab** | Platform tools | [{LAB_BASE_LOCAL}/]({LAB_BASE_LOCAL}/) · [live]({LAB_BASE_LIVE}/) |",
        "",
        "Every **lab** module documents both tracks. Intro/wrap modules have no lab.",
        "",
        "## Quick start",
        "",
        "```bash",
        "cd courses/learn_unix",
        "chmod +x scripts/*.sh",
        "./scripts/scaffold.sh          # Track A home practice tree",
        "./scripts/module.sh 01 --check # optional env check for module 01",
        "```",
        "",
        "Then open [module00-intro/README.md](module00-intro/README.md).",
        "",
        "## Module map",
        "",
        "See **[docs/MODULES.md](docs/MODULES.md)** for the full table (00–28).",
        "",
        "### Clusters",
        "",
        "| Modules | Theme |",
        "|---------|--------|",
        "| 00 | Intro / dual-track setup |",
        "| 01–04 | Shell navigation, help, paths, globs |",
        "| 05–08 | Types, links, permissions, dotfiles |",
        "| 09–13 | Processes, jobs, pipes, text, here-docs |",
        "| 14–18 | History, aliases, scripting, safety |",
        "| 19–22 | Projects, archives, backup, symlinks |",
        "| 23–27 | Workflow, Make, dry-run, logs, `.env` |",
        "| 28 | Wrap → learn_git |",
        "",
        "## Layout",
        "",
        "```",
        "learn_unix/",
        "├── README.md",
        "├── docs/MODULES.md",
        "├── docs/TWO_TRACKS.md",
        "├── scripts/scaffold.sh",
        "├── scripts/module.sh",
        "├── module00-intro/",
        "├── module01-vfs-terminal/",
        "│   ├── README.md",
        "│   ├── CHECKLIST.md",
        "│   ├── EXAMPLES.md",
        "│   ├── outline.yaml",
        "│   ├── transcript.md",
        "│   └── examples/          # Track A",
        "├── …",
        "└── module28-wrap/",
        "```",
        "",
        "## Relationship to learn_unix_git",
        "",
        "Example trees were copied from `learn_unix_git` modules 1–5 and 8.",
        "Git content stays in `learn_unix_git` until `learn_git` is scaffolded.",
        "",
        "## License",
        "",
        "CC BY 4.0 — see upstream course materials.",
        "",
    ]
    (DST / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_scripts() -> None:
    scripts = DST / "scripts"
    scripts.mkdir(exist_ok=True)
    scaffold = r"""#!/usr/bin/env bash
# Create ~/unix_practice for Track A exercises.
set -euo pipefail
TARGET="${HOME}/unix_practice"
mkdir -p "$TARGET"/{notes,projects,src,tb,scripts,logs,build}
if [[ ! -f "$TARGET/notes/readme.txt" ]]; then
  cat > "$TARGET/notes/readme.txt" << 'EOF'
learn_unix Track A practice tree
Use this directory for checklist exercises.
EOF
fi
echo "Created/updated: $TARGET"
ls -la "$TARGET"
"""
    (scripts / "scaffold.sh").write_text(scaffold, encoding="utf-8")

    module_sh = r"""#!/usr/bin/env bash
# Generic module helper: ./scripts/module.sh NN [--check|--demo|--help]
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NN="${1:-}"
shift || true
if [[ -z "$NN" || "$NN" == "--help" ]]; then
  echo "Usage: $0 NN [--check|--demo|--help]"
  echo "  NN = module number, e.g. 01 or 1"
  exit 0
fi
NN="$(printf '%02d' "$((10#$NN))")"
MOD_DIR="$(find "$ROOT" -maxdepth 1 -type d -name "module${NN}-*" | head -1)"
if [[ -z "$MOD_DIR" ]]; then
  echo "No module directory for $NN"
  exit 1
fi
ACTION="${1:---check}"
case "$ACTION" in
  --check)
    echo "Module $NN self-check (Track A environment)"
    echo "Module dir: $MOD_DIR"
    command -v bash >/dev/null && echo "[OK] bash"
    command -v ls >/dev/null && echo "[OK] ls"
    command -v pwd >/dev/null && echo "[OK] pwd: $(pwd)"
    if [[ -d "$MOD_DIR/examples" ]]; then
      echo "[OK] examples present:"
      ls "$MOD_DIR/examples"
    else
      echo "[INFO] no examples/ (intro/wrap or pending)"
    fi
    if [[ -d "${HOME}/unix_practice" ]]; then
      echo "[OK] ~/unix_practice exists"
    else
      echo "[INFO] run ./scripts/scaffold.sh to create ~/unix_practice"
    fi
    ;;
  --demo)
    echo "Demo: open $MOD_DIR/EXAMPLES.md and README.md"
    echo "Browser lab link is in README (Track B)."
    ;;
  *)
    echo "Unknown option: $ACTION"
    exit 1
    ;;
esac
"""
    (scripts / "module.sh").write_text(module_sh, encoding="utf-8")
    (scripts / "README.md").write_text(
        """# Scripts

| Script | Purpose |
|--------|---------|
| `scaffold.sh` | Create `~/unix_practice` for Track A |
| `module.sh NN` | `--check` / `--demo` for module number `NN` |

```bash
chmod +x scripts/*.sh
./scripts/scaffold.sh
./scripts/module.sh 01 --check
```
""",
        encoding="utf-8",
    )


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    write_course_readme()
    write_docs_index()
    write_scripts()
    for num, slug, kind, title, lab_id, status, sources in MODULES:
        print(f"module{num:02d}-{slug} …")
        write_module_readme(num, slug, kind, title, lab_id, status)
        write_checklist(num, slug, kind, title, lab_id)
        copied = copy_examples(num, slug, sources) if kind == "lab" else []
        write_examples_md(num, slug, kind, title, copied)
        write_outline_transcript(num, slug, kind, title, lab_id)
    print("Done:", DST)


if __name__ == "__main__":
    main()
