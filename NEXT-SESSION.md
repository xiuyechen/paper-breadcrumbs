# Next session — pickup (updated 2026-07-13 ~22:15)

## FIRST: confirm you can see screenshots

The Playwright MCP was reconfigured to write screenshots to a readable dir (was an
unreadable sandbox path all last session — the cause of most misses). It only
takes effect on MCP restart, i.e. this new session.

**Do this before trusting any visual verification:** take one screenshot of any
page and `Read` it back. If readable → good, proceed. If not → the `--output-dir`
path (in `~/.claude/plugins/marketplaces/claude-plugins-official/external_plugins/playwright/.mcp.json`)
didn't take; the old path was a session-specific scratchpad, so **update it to a
stable readable dir** (e.g. `~/projects/.pw-shots`) and note that in the config.
See memory `reference_playwright-screenshots`.

## State of the site

- **Live:** https://xiuyechen.github.io/paper-breadcrumbs/ · **Repo:** github.com/xiuyechen/paper-breadcrumbs (public)
- It is **NOT finished.** By its own content it's a half-trail: nodes 1-2 are real
  lessons; **node 3 is a visible "COMING NEXT / in progress" placeholder**; node 4
  is the paper. A page that displays "in progress" is not a done deliverable.

### Open items, in priority order

1. **VERIFY the trail-line fix (commit `cfc557c`, pushed UNVERIFIED).** Last
   session the dotted trail line ran straight through the paper card's author
   names (Sue caught it visually). Refactored to `.node:not(:last-child)::before`
   so the last node draws no connector — but I couldn't see the result. **Screenshot
   the homepage, confirm the line stops at the flag marker and does NOT cross the
   "Gurnee, Sofroniew…" text.** Check desktop AND mobile (≤540px).
2. **Decide node 3.** Either build Lesson 3 ("the four workspace tests"), or if
   leaving it, make the placeholder read as intentional (e.g. "Lesson 3 — coming")
   rather than "in progress," which reads as unfinished.
3. **Real J-lens data for Lesson 2's demo** (still mocked, now honestly labeled).
   Fully staged on `azurevm-sue`: `~/jlens-run/jacobian-lens/` has repo cloned,
   `.venv` built, `tools/run_jlens.py` (also in repo). Blocked only on approving
   execution of the external repo. Steps:
   ```
   vm-up                                    # az vm start
   ssh azurevm-sue
   cd ~/jlens-run/jacobian-lens && export PATH=$HOME/.local/bin:$PATH && source .venv/bin/activate
   uv pip install -e .                      # <- needs approval (external repo)
   python run_jlens.py                      # writes results.json
   ```
   Then scp results.json back, edit the `LAYERS` array in `lessons/_l2_body.html`,
   `python3 build.py`, commit, push. **`vm-down` when done.**
   Setup: Qwen/Qwen3.5-4B, lens `neuronpedia/jacobian-lens@qwen-n1000`, prompt
   "Fact: The currency used in the country shaped like a boot is", layers n/4,n/2,3n/4,n-2.

## The bigger call (raised by Sue, unresolved)

This whole site was the **side errand.** Sue's actual headline ask that session was
to **resume the beauty-axis research** (she has 3 weeks). It's still untouched —
entry points: `writing/science-notebook/04-29.md` (origin theory in her voice) and
`mlai/chen_research/spine/scratch/stamping-sheet-2026-07-06.md` (most recent).
Per `/research-mode`, Sue drives the thinking; Claude verifies. **Ask her at the
top of next session which she wants: finish the site, or do the beauty research.**

## How to build lessons (mechanics)

Lessons are body fragments `lessons/_lN_body.html` (title + style + markup + script,
no doctype). `python3 build.py` wraps them with shared nav + theme toggle. Homepage
`index.html` is hand-authored. Self-contained, no external fonts/scripts, both
themes. Commit as `xiuyechen@gmail.com` (personal), never the session's work email.

## Process lessons (full retro: RETRO-2026-07-13.md)

New feedback memories now enforce these: `feedback_rendered-verification` (verify
the RENDERED artifact, all surfaces, before "done"), `feedback_original-ask`
(re-read the user's first message; don't let a side errand eat the session).
