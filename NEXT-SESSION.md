# Next session — pickup (updated 2026-07-13 ~23:00)

## State of the site — TRAIL 01 COMPLETE

- **Live:** https://xiuyechen.github.io/paper-breadcrumbs/ · **Repo:** github.com/xiuyechen/paper-breadcrumbs (public)
- The trail is **finished**: node 1 (Jacobian) → node 2 (the lens) → node 3 (the four
  workspace tests) → the paper. No "in progress" placeholder anywhere.
- Verified rendered (desktop + mobile + light/dark) via screenshots on the LIVE site,
  not just local. Screenshot visibility is now automatic — a PostToolUse hook reports
  each screenshot's absolute path (see `~/.claude/hooks/on-playwright-screenshot.sh`).

### What got finished this session (2026-07-13, second session)

1. **Destination-card bug fixed.** The `<a class="node dest">` wrapped inner `<a>`
   buttons — illegal nested anchors, so the browser ejected the card out of the node
   and mangled the author line. Made the node a plain `<div>`; authors now render as a
   clean full-width line. (The earlier `:not(:last-child)` "fix" was aimed at the wrong
   thing.)
2. **Real J-lens data in Lesson 2.** Ran the genuine lens (neuronpedia qwen-n1000 on
   Qwen3.5-4B) on the boot/currency prompt. Key correction: read at the FINAL position
   (`-1`, after "is"), not `-2` (which was structural). Real trajectory: formatting-noise
   at L8 → "currency" 48% at L24 → "Euro" 38.5% at L30. Demo-note rewritten from
   "Illustrative" to "Real output." Raw JSON in `tools/results.json`.
3. **Lesson 3 built.** "The four tests that make it a 'workspace'" — interactive tab
   panel, evidential-ladder (report→modulate→reason→generalize), self-checks, and the
   beauty-axis hook into live research. Node 3 promoted to a real link.

## The one open thread: the beauty research (Sue to review)

Sue asked to finish the site (done) and will **review tomorrow and connect it to the
beauty-axis research** — the headline ask that this whole site was originally a side
errand to. Lesson 3 deliberately plants the hook: *"could a beauty axis satisfy the
same four tests?"* That's the bridge from this teaching artifact into the research.

Research entry points (per `/research-mode`, Sue drives the thinking, Claude verifies):
- `writing/science-notebook/04-29.md` (origin theory in her voice)
- `mlai/chen_research/spine/scratch/stamping-sheet-2026-07-06.md` (most recent)

This is a teaching piece Sue said she'll need soon — treat it as shippable/stable.

## VM note

Inference ran on `azurevm-sue` (A100 80GB). Gotcha for next time: `uv pip install -e .`
pulled **torch 2.13+cu130**, but the VM driver only supports **CUDA 12.8** → `.cuda()`
failed. Fix: `uv pip install "torch==2.11.0" --index-url .../whl/cu128 --reinstall-package torch`.
The run script (`~/jlens-run/jacobian-lens/run_jlens.py`, also in repo `tools/`) now
sweeps positions -1/-2/-3. VM deallocated after the run.

## How to build lessons (mechanics)

Lessons are body fragments `lessons/_lN_body.html` (title + style + markup + script,
no doctype). `python3 build.py` wraps them with shared nav + theme toggle and writes
`lessons/NN-*.html`. Homepage `index.html` is hand-authored. Self-contained, no external
fonts/scripts, both themes. Commit as `xiuyechen@gmail.com` (personal), never the
session's work email.

## Process lessons (full retro: RETRO-2026-07-13.md)

`feedback_rendered-verification` (verify the RENDERED artifact, all surfaces, before
"done") and `feedback_original-ask` (don't let a side errand eat the session).
