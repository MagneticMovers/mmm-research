# mmm-research

Research repository and website source for **Magnetic Matter Movers** — magnetic machines, beamed-energy propulsion, and minimum-chemical space transportation architecture. Served via GitHub Pages at **magneticmattermovers.com**.

## What this is

The primary, version-controlled record of an independent research program. The commit history is the lab notebook's timestamp authority: analyses, build sheets, and measured results are dated by their commits, and documents are corrected forward (new commits), never silently rewritten.

## Repository structure

```
index.md                  — site landing page
/architecture/            — the space transportation study + program gate plan
/build-sheets/            — numbered, buildable hardware documents (001, 002, ...)
/checklists/              — execution checklists with actual-vs-predicted tables and gate criteria
/lab-notes/               — measured results and gate evidence (photos, filled tables, data)
/sis/                     — Slug Interface Standard drafts (reserved)
/assets/                  — figures, photos, data files
```

## Document conventions

- Epistemic tiers: **[E] established / [I] inference / [S] speculation** per the convention in the architecture study; unlabeled dollar figures are [I]-grade approximations pending the citation/uncertainty pass (work item 22)

- Every document exists as `.md` (canonical, diffable) and `.pdf` (print/citation copy)
- Build sheets carry predicted performance tables; lab notes carry the actuals — both are published, including misses
- Gate criteria and kill criteria are written **before** data collection and are immutable once a gate review begins
- Phase numbering follows the Program Gate Plan (Phase 0 = benchtop, currently active)

## Licensing

Licensing is split by the strategic function of each document class:

- **White papers, architecture studies, and analyses: CC BY 4.0** — cite, reuse, and build on freely with attribution. Their job is to spread.
- **The Slug Interface Standard (when published): CC BY 4.0**, explicitly free to implement commercially — an interface standard only creates demand if anyone can design to it without asking.
- **Build sheets, product designs, checklists, and manufacturing packs: CC BY-NC 4.0** — free for personal, educational, and research use with attribution. **Commercial use (selling kits, products, or services derived from these designs) requires a license — contact via the repository or site.** Reasonable terms; the goal is participation, not gatekeeping.
- **Code (when it appears — choreography engine, wave-optics sim): MIT**

Patent notice: certain apparatus and methods described in these documents may be the subject of pending patent applications. The CC BY-NC license grants copyright permissions only and conveys no patent license for commercial use.

## Status

Phase 0 active: Build Sheets 001 (Inductrack) and 002 (droplet thruster) released; hardware purchasing underway. Next milestones: Phase 0 gate review → Lab Note 001 → wave-optics propagation study.

## Feedback

Technical critique is welcome and useful — open an issue. Errors that survive review get corrected in a dated commit with the correction noted in the document.

## Disclaimer

Independent research. Nothing here is professional engineering certification, legal advice, or an offer of securities. Build sheets involve real hazards (magnets, lasers, high current, spinning machinery); their safety sections are load-bearing.
