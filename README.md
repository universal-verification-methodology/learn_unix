# learn_unix

[![GitHub](https://img.shields.io/badge/GitHub-learn__unix-181717?logo=github)](https://github.com/universal-verification-methodology/learn_unix)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)
[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)
[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)
[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)
[![Domain](https://img.shields.io/badge/domain-Unix%20%7C%20shell%20%7C%20digital%20design-purple)](https://github.com/universal-verification-methodology/learn_unix)

**learn_unix** is the open learning path for *Unix / shell fluency for digital design students*. 

Readers and students usually **open a module README** (or the live tools) or clone this public repo. Authors edit content here (or via the parent monorepo checkout), rebuild slides/audio with **module-slides** in the parent, and push; the parent repo only stores a pinned submodule commit.


## Table of contents

- [Contents](#contents)
- [Browse or clone](#browse-or-clone)
- [Consume from the parent](#consume-from-the-parent)
- [Author: publish or update](#author-publish-or-update)
- [Two learning tracks](#two-learning-tracks)
- [Module landings](#module-landings)
- [Browser labs](#browser-labs)
- [License](#license)

## Contents

```text
learn_unix/
├── README.md
├── LICENSE              # CC BY 4.0
├── docs/
│   ├── MODULES.md       # full module index (00–28)
│   └── TWO_TRACKS.md    # Track A (real Unix) vs Track B (browser)
├── scripts/
│   ├── scaffold.sh      # Track A practice tree
│   └── module.sh        # per-module --check helpers
├── module00-intro/
├── module01-vfs-terminal/
│   ├── README.md
│   ├── CHECKLIST.md
│   ├── EXAMPLES.md
│   ├── outline.yaml
│   ├── transcript.md
│   ├── examples/        # Track A
│   └── (optional) slides.pptx / slides.pdf / video.mp4 / assets/
├── …
└── module28-wrap/
```

Videos and decks are optional per module. Generate with the **module-slides** skill (`.cursor/skills/module-slides/`) in the parent monorepo when ready.

## Browse or clone

- **Browser labs:** [https://universal-verification-methodology.github.io/learning/tools/](https://universal-verification-methodology.github.io/learning/tools/)
- **Syllabus (parent):** [`syllabus.md` § learn_unix](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#1-learn_unix)
- **Clone this repo alone:**

```bash
git clone https://github.com/universal-verification-methodology/learn_unix.git
cd learn_unix
chmod +x scripts/*.sh
./scripts/scaffold.sh          # Track A home practice tree
./scripts/module.sh 01 --check # optional env check for module 01
```

Then open [module00-intro/README.md](module00-intro/README.md).

## Consume from the parent

From a clone of the **learning** monorepo (lists this repo in `.gitmodules` when registered):

```bash
git clone --recurse-submodules \
  git@github.com:universal-verification-methodology/learning.git
# or, if already cloned without submodules:
git submodule update --init --recursive

ls courses/learn_unix
```

Working tree path in the parent: `courses/learn_unix/` → this repository at a pinned commit.

## Author: publish or update

Edit inside the parent monorepo (recommended) or in a standalone clone of this repo.

```bash
# from the learning monorepo checkout
cd courses/learn_unix
# … edit module README / CHECKLIST / EXAMPLES / transcript …

# rebuild media from the parent (one module at a time):
cd ../..
# revise transcript.md, then:
python .cursor/skills/module-slides/scripts/transcript_to_outline.py \
  courses/learn_unix/moduleNN-slug
bash .cursor/skills/module-slides/scripts/narrate_clips.sh \
  courses/learn_unix/moduleNN-slug

cd courses/learn_unix
git add -A
git commit -m "Update learn_unix modules"
git push origin main
```

Then bump the pin in the **parent**:

```bash
cd /path/to/learning
git add courses/learn_unix
git commit -m "Bump learn_unix submodule"
git push
```

See the skill `SKILL.md` for dual-track narration rules and the full PPTX → PDF → TTS → MP4 pipeline.

## Two learning tracks

Every **lab** module documents both tracks. Intro/wrap modules have no lab. Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).

| Track | Practice surface | Start here |
|-------|------------------|------------|
| **A — Real Unix** | Local terminal + `examples/` | `./scripts/scaffold.sh` · [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) |
| **B — Browser lab** | Platform tools | [local tools](http://127.0.0.1:8080/tools/) · [live](https://universal-verification-methodology.github.io/learning/tools/) |

Recommended path: short Track B starter → Track A examples + checklist → optional quiz / transcript review.

## Module landings

Full status table: **[docs/MODULES.md](docs/MODULES.md)**. Clusters: 00 intro · 01–04 navigation · 05–08 types/links/perms · 09–13 processes/pipes/text · 14–18 history/scripting · 19–22 projects/archives · 23–27 workflow · 28 wrap → Git.

| Module | Landing |
|--------|---------|
| 00 — Welcome to Unix for design | [module00-intro](module00-intro/README.md) |
| 01 — Virtual filesystem terminal | [module01-vfs-terminal](module01-vfs-terminal/README.md) |
| 02 — man / --help discoverability | [module02-man-help-lab](module02-man-help-lab/README.md) |
| 03 — Absolute vs relative paths | [module03-path-abs-rel](module03-path-abs-rel/README.md) |
| 04 — Globs & wildcards | [module04-wildcards-globs](module04-wildcards-globs/README.md) |
| 05 — File types & links | [module05-file-types-lab](module05-file-types-lab/README.md) |
| 06 — realpath / readlink | [module06-realpath-resolve](module06-realpath-resolve/README.md) |
| 07 — Permissions, umask, PATH | [module07-permissions](module07-permissions/README.md) |
| 08 — Dotfiles & config homes | [module08-dotfiles-lab](module08-dotfiles-lab/README.md) |
| 09 — Process list & signals | [module09-ps-kill-lab](module09-ps-kill-lab/README.md) |
| 10 — Job control | [module10-job-control-lab](module10-job-control-lab/README.md) |
| 11 — Pipes, redirection, xargs | [module11-pipes](module11-pipes/README.md) |
| 12 — sort / uniq / cut | [module12-sort-uniq-cut](module12-sort-uniq-cut/README.md) |
| 13 — Here-doc / here-string | [module13-here-doc-lab](module13-here-doc-lab/README.md) |
| 14 — Shell history & reverse-search | [module14-shell-history](module14-shell-history/README.md) |
| 15 — Alias & functions | [module15-alias-lab](module15-alias-lab/README.md) |
| 16 — Script control flow | [module16-scripting](module16-scripting/README.md) |
| 17 — Exit status & && / \|\| | [module17-exit-status-lab](module17-exit-status-lab/README.md) |
| 18 — Safe scripting | [module18-safe-scripting](module18-safe-scripting/README.md) |
| 19 — Project layout, archives, sed & diff | [module19-project-archives](module19-project-archives/README.md) |
| 20 — tar vs zip | [module20-zip-vs-tar](module20-zip-vs-tar/README.md) |
| 21 — Backup & clean-build | [module21-backup-clean](module21-backup-clean/README.md) |
| 22 — Relative symlink pitfalls | [module22-link-relative](module22-link-relative/README.md) |
| 23 — Pre-push / Make / env checklist | [module23-workflow](module23-workflow/README.md) |
| 24 — Makefile basics | [module24-make-basics](module24-make-basics/README.md) |
| 25 — Dry-run mindset | [module25-dry-run-lab](module25-dry-run-lab/README.md) |
| 26 — Log / failure triage | [module26-log-triage](module26-log-triage/README.md) |
| 27 — .env literacy | [module27-env-file-lab](module27-env-file-lab/README.md) |
| 28 — Unix path complete → Git | [module28-wrap](module28-wrap/README.md) |

## Browser labs

By workflow (Track B): [vfs-terminal](https://universal-verification-methodology.github.io/learning/tools/vfs-terminal/) → [man-help-lab](https://universal-verification-methodology.github.io/learning/tools/man-help-lab/) → [path-abs-rel](https://universal-verification-methodology.github.io/learning/tools/path-abs-rel/) · [wildcards-globs](https://universal-verification-methodology.github.io/learning/tools/wildcards-globs/) → [file-types-lab](https://universal-verification-methodology.github.io/learning/tools/file-types-lab/) · [permissions](https://universal-verification-methodology.github.io/learning/tools/permissions/) · [pipes](https://universal-verification-methodology.github.io/learning/tools/pipes/) · [scripting](https://universal-verification-methodology.github.io/learning/tools/scripting/) → later workflow / Make / env labs. See [all tools](https://universal-verification-methodology.github.io/learning/tools/) and each module README for its primary lab id.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).

Example trees for early modules were adapted from [`learn_unix_git`](https://github.com/universal-verification-methodology/learn_unix_git). Platform tools and the parent monorepo may carry additional notices.
