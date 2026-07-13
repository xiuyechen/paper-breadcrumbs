# Paper Breadcrumbs

Short, interactive mini-lessons that lay a trail into a research paper — one
load-bearing idea per step, built up from something you already know, so the
paper itself becomes readable once the trail is behind you.

**Live:** https://xiuyechen.github.io/paper-breadcrumbs/

## Trail 01 — The global workspace inside a language model

A path from plain calculus to the interpretability instrument at the heart of
Anthropic's 2026 paper *[Verbalizable Representations Form a Global Workspace in
Language Models](https://transformer-circuits.pub/2026/workspace/index.html)*.

1. **[What a Jacobian actually is](lessons/01-jacobian.html)** — the ordinary
   derivative generalized to vectors, with a draggable tangent line.
2. **[Why "transport a hidden activation into the final-layer basis via J"](lessons/02-jlens.html)**
   — how the Jacobian becomes the J-lens, with a clickable residual-stream
   diagram.
3. *The four tests that make it a "workspace"* — coming next.

Destination: the [paper](https://transformer-circuits.pub/2026/workspace/index.html)
· [code (J-lens)](https://github.com/anthropics/jacobian-lens).

## Design

Each lesson is a single self-contained HTML file — no build step, no external
fonts or scripts, works offline. Interactive figures are hand-drawn on `<canvas>`.
Both light and dark themes; a per-page toggle persists your choice.

## Building

Lessons are authored as body fragments (`lessons/_lN_body.html`) and wrapped into
standalone pages by `build.py`, which injects the shared nav and theme toggle:

```
python3 build.py
```

The homepage (`index.html`) is hand-authored and needs no build.

## Note on the demos

Interactive figures are illustrative. The J-lens token readouts in Lesson 2 are a
teaching mockup of a thought resolving into words — the mechanism and formula are
faithful, but the specific token percentages are hand-set, not real model output.
Real readouts require running the [J-lens code](https://github.com/anthropics/jacobian-lens).

## Roadmap

See [`ROADMAP.md`](ROADMAP.md).

---

Created by [Xiuye Chen](https://github.com/xiuyechen), built collaboratively with
Claude (Claude Code). Direction, framing, and editorial judgment: Xiuye. Drafting,
interactive figures, and build: Claude. CC BY 4.0.
