# Roadmap

## Trail 01 — global workspace

- [x] Lesson 1 — What a Jacobian actually is
- [x] Lesson 2 — Transport a hidden activation into the final-layer basis via J
- [x] Homepage — learning path with nodes + paper destination
- [ ] **Lesson 2 demo: swap in real J-lens output.** The token readouts in
      Lesson 2 (`euro 52%`, `lira 30%`, …) are currently a hand-set teaching
      mockup. Run the actual [J-lens code](https://github.com/anthropics/jacobian-lens)
      on an open-weights model (Qwen) for the prompt *"The currency used in the
      country shaped like a boot is"*, capture the real lens readouts at a few
      layers, and replace the `LAYERS` array in `lessons/_l2_body.html` with the
      real tokens + percentages. Then rebuild. Keeps the lesson honest and makes
      it a genuine artifact of the method.
- [ ] Lesson 3 — The four tests that make it a "workspace" (verbal report,
      directed modulation, internal reasoning, flexible generalization)
- [ ] Optional Lesson 4 — Could a *beauty axis* live in the workspace? (bridge
      to the beauty-axis research thread)

## Beyond trail 01

- [ ] Fall course content as additional trails (this repo is the home for it).
- [ ] Consider a shared design-tokens file if the CSS starts to drift between
      lessons (right now each lesson re-declares the palette — fine for two, may
      want to factor out at ~5+).
