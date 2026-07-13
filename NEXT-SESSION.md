# Next session — where this left off (2026-07-13)

## Status: shipped and live

- **Live site:** https://xiuyechen.github.io/paper-breadcrumbs/
- **Repo:** https://github.com/xiuyechen/paper-breadcrumbs (public)
- Homepage + Lesson 1 (Jacobian) + Lesson 2 (J-lens transport) all deployed and
  verified (HTTP 200). Dot/label overlap in the Lesson 2 canvas is fixed. Both
  themes work. Everything self-contained (no external fonts/scripts).

## The one unfinished thing: real J-lens data for the Lesson 2 demo

The token readouts in Lesson 2 (`euro 52%`, `lira 30%`, …) are a **hand-set
teaching mockup**, called out honestly in the README and in-lesson. Replacing
them with real J-lens output is queued.

**This is 90% staged.** It stopped only because installing/running the
`anthropics/jacobian-lens` repo is agent-discovered external code, and the
auto-mode classifier (correctly) wants a human to approve executing it. Sue was
away, so it paused here rather than routing around the block.

### To finish (≈5 min once you approve running the repo)

The VM `azurevm-sue` (1× A100) already has everything staged at
`~/jlens-run/jacobian-lens/`:
- repo cloned, `.venv` created (Python 3.12)
- `run_jlens.py` copied in (runs the exact walkthrough on our prompt)

Steps:
```bash
az vm start -g RG-WESTUS3-SUE-DEV -n vm-westus3-sue-gpu-dev   # or: vm-up
ssh azurevm-sue
cd ~/jlens-run/jacobian-lens
export PATH=$HOME/.local/bin:$PATH && source .venv/bin/activate
uv pip install -e .            # <-- the step that needs approval (external repo)
python run_jlens.py           # writes results.json, prints top-6 tokens/layer
```
Then: `scp azurevm-sue:~/jlens-run/jacobian-lens/results.json .`, and edit the
`LAYERS` array in `lessons/_l2_body.html` to the real tokens+percentages,
`python3 build.py`, commit, push. **Deallocate the VM** when done (`vm-down`).

Setup used (from the repo's `walkthrough.ipynb`, verified 2026-07-13):
- model `Qwen/Qwen3.5-4B`, pre-fitted lens `neuronpedia/jacobian-lens@qwen-n1000`
- prompt `"Fact: The currency used in the country shaped like a boot is"`
- layers: n/4, n/2, 3n/4, n-2 at position -2

`run_jlens.py` is also saved in the session scratchpad if the VM copy is gone.

## After that — the roadmap (see ROADMAP.md)

- Lesson 3: the four workspace tests (verbal report, directed modulation,
  internal reasoning, flexible generalization)
- Optional Lesson 4: could a *beauty axis* live in the workspace? (bridge to the
  beauty-axis research thread — the reason this whole trail exists)
- Fall course content as further trails (this repo is the intended home)
