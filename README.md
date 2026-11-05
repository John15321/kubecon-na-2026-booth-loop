# KubeCon NA 2026 Booth Loop

Looping slide deck for the Flatcar kiosk at KubeCon + CloudNativeCon North
America 2026 (Project Pavilion, kiosk P-8A). Rebuilt from the original
PowerPoint (`reference/original-powerpoint.pdf`) on the Flatcar Marp theme.

Slides: a title slide, secure minimal Linux (with the CNCF banner), designed
for, runs everywhere, and a closing community slide that carries four QR codes
(`assets/qr/`: website, GitHub, Discord, learning series) plus the booth
location and meeting times. The loop wraps from the community slide back to
the title.

## Run it on a loop

```sh
make loop         # -> build/booth-loop/index.html (self-contained folder)
chromium --kiosk "file://$PWD/build/booth-loop/index.html?interval=10"
```

`?interval=SECONDS` sets the time per slide (default 10). Click or press Space
to pause and resume. The deck wraps from the last slide back to the first.

## Export for PowerPoint

```sh
make export       # -> build/png/slide.NNN.png (2560x1440)
```

Use the PNGs to paste slides into another deck.

For a native, editable PowerPoint (real text boxes, cards and pictures), run:

```sh
make pptx         # -> build/slides-native.pptx (needs uv and rsvg-convert)
```

It is built by `scripts/build-pptx.py` and mirrors the Marp slides by hand, so
keep the two in sync when you change content.

To skip that, `make pptx-auto` converts `slides.md` automatically with Marp's
experimental editable export (needs LibreOffice) into `build/slides-auto.pptx`.
It is good but not perfect: expect small glitches such as card shadows.

## Build

The recommended path is Podman + `make`. Everything runs inside a small container image so the host only needs `podman` and `make`.

```sh
make setup        # first-time: build the slides-builder container image
make build        # -> build/slides.pdf
make clean        # remove build artifacts
make shell        # interactive shell inside the container
```

Native (no container) — requires Node.js on the host:

```sh
npm ci            # or npm install
make native-build # -> build/slides.pdf
```

Author-time preview with live reload:

```sh
make watch        # rebuilds on save
make preview      # live browser preview
```

See `make help` for the full target list.

## Layout

```
slides.md                  # slide content (Markdown)
themes/
  flatcar.css              # theme entry point
  flatcar/{base,dark,sidebar}.css   # partials
assets/
  backgrounds/             # theme backgrounds (staircase, etc.)
  diagrams/                # D2 sources + generated .svg diagrams
  logos/                   # brand + third-party logos
  photo/                   # individual + group photos
  qr-code.png              # closing-slide QR
scripts/                   # build / clean / gather-artifacts
Containerfile              # Podman image (Marp CLI + bash + make)
compose.yaml               # slides-builder service definition
Makefile                   # top-level workflow
.github/workflows/         # CI: builds PDF on push, releases on tag
```

## Slide layouts & utility classes

See [MANUAL.md](MANUAL.md) for the full authoring reference — slide
layouts (`cover`, `sidebar`, `agenda`, etc.), utility classes
(`img-*`, `pin-*`, `pane-*`, `row`, `cols-*`, `callout`, …) and both
the HTML-class and markdown-alt-text ways to apply them.

## Diagrams

[D2](https://d2lang.com) is the default diagramming tool. Put sources
in `assets/diagrams/*.d2` and reference the generated `.svg` from your
slides — `make build` re-renders them when `d2` is on `PATH` and falls
back to the committed SVGs otherwise. Other tools (Mermaid, Excalidraw,
draw.io, plain PNGs / screenshots) work too: just drop the exported
image under `assets/` and `<img>` it in. See [MANUAL.md](MANUAL.md#diagrams-d2)
for details.

## Releases

Pushing a tag `v*` triggers the CI workflow to attach `slides.pdf` to a GitHub Release.

---

Generated from [cookiecutter-marp-flatcar](https://github.com/John15321/cookiecutter-marp-flatcar) by **Jan Bronicki**.
