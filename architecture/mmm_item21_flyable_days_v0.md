# Work Item 21 — Beamed-Line Availability: Flyable-Days Model v0
### Magnetic Matter Movers · compiled July 20, 2026
*Red-team finding closed to first cut: NM sky statistics × DoD Laser Clearinghouse (LCH) windows → a flyable-days fraction feeding the cadence economics. Epistemic tiers per house convention: climate data and LCH-published statistics **[E]**; every transfer of those numbers to the launch context, and every usability factor, **[I]**. Model is deliberately conservative-simple; refinement paths listed at the end.*

---

## 1. The three gates on a beamed launch day

A System B launch requires, simultaneously: (a) cloud-free line of sight on the vertical beam path for the 462 s burn, (b) winds within track/vehicle limits, (c) an open LCH deconfliction window covering the shot. The gun (System A) faces none of these — the all-weather hedge from the red-team register is quantified below.

## 2. Sky statistics — the geometry is favorable [E→I]

Albuquerque climate normals: **167 clear days + 111 partly-cloudy days = 278 days/yr with sun; 76% of possible sunshine** (Roswell 74%, statewide similar). The vertical beam needs a cloud-free column for only ~8 minutes, not a clear day: on partly-cloudy days (40–70% cover), short launch windows through gaps are largely schedulable against satellite imagery.

Sky-gate model [I]: clear days count 1.0; partly-cloudy days count 0.7 (schedulable-window assumption); overcast days count 0.
**Sky availability ≈ (167 + 0.7 × 111)/365 = 0.67** — band 0.60–0.75 depending on the partly-cloudy usability assumption (0.5–0.9).

## 3. Wind gate [I]

NM spring (Mar–May) brings sustained high-wind days; the constraint binds on vehicle ascent dispersion and track-exit operations, not the beam itself. Placeholder derate ×0.92 (≈30 lost days/yr, concentrated in spring), pending the NWS ABQ high-wind climatology pull in v1. Correlation note: high-wind and overcast days partially overlap (frontal passages), so multiplying is conservative.

## 4. Laser Clearinghouse — the newly quantified gate [E→I]

Process [E]: sky-directed beams above threshold require LCH deconfliction (DoDI 3100.11). Requests go in **3–30 days before laser activity**; LCH returns Program Approval Messages (PAMs) defining open firing windows by pointing direction and time.

Published closure burden (astronomy, the best public dataset) [E]: for a 2025-era analysis of observatory laser operations, median *open* time was **74–90% for 300 s windows**, collapsing to **10–35% for 1,800 s windows**, and **96% for 1 s** — closures are frequent-but-short, so long continuous windows are exponentially harder to find than brief ones. Open time has **declined steadily since ~2016** as constellations grow; a 2022 SpaceX waiver (Starlink tolerates illumination) gave partial relief.

Transfer to the launch case [I], three structural differences, all favorable:

1. **Duration:** the 462 s burn sits between the published 300 s (74–90% open) and 1,800 s (10–35% open) cases → naive interpolation gives ~55–80% per-slot availability.
2. **Pointing:** a launch beam sweeps a *fixed, narrow, pre-declared corridor* (vertical to relay), not arbitrary sky — a single PAM geometry, requested weeks ahead. Astronomy's burden is inflated by full-sky pointing; ours is one repeating corridor.
3. **Schedulability:** cargo launches slide inside a day. If closures are frequent-but-short, the probability that *no* 8-minute open window exists across a whole operating day is small. Day-level model: **P(≥1 usable window/day) ≈ 0.90**, band 0.80–0.95.

Structural risk running the other way: relay-mirror illumination is itself an LCH matter (we are deliberately lasing a spacecraft — ours), and the declining-open-time trend is adverse. Mitigations: negotiated standing PAM for the fixed corridor; operator-waiver agreements with constellation owners (Starlink precedent); Spaceport America/WSMR restricted-airspace umbrella, which the range plan already selects for exactly this reason.

## 5. The model

**Flyable-day fraction = Sky × Wind × LCH-day ≈ 0.67 × 0.92 × 0.90 ≈ 0.55** → **~200 flyable days/yr** (band: 150–250). Per-shot slot availability within a flyable day ≈ 0.55–0.80 (LCH interpolation) — relevant only once daily cadence exceeds ~2–3 shots.

## 6. Feed into cadence economics

| Flight rate target | Required shots per flyable day (200 d/yr) | Verdict |
|---|---|---|
| 100/yr (Falcon-parity $3,800/kg) | 0.5 | Trivial — availability is not the binding constraint |
| 500/yr ($870/kg) | 2.5 | Comfortable; 5 h recharge cycle supports ~3/day |
| 2,000/yr ($323/kg) | 10 | **Binding.** Requires either grid feed >25 MW (recharge), second beam line, or accepting LCH slot losses at ~10 shots/day. The $323/kg figure inherits this availability assumption — flag in item 22's uncertainty pass |

Portfolio consequence (red-team hedge, now numeric): the gun's all-weather cadence backfills every lost beam day for water/bulk manifests — beamed-line availability caps *delicate-cargo* rate, not program mass throughput. The low-demand doctrine (water-slug dummy shots) is unaffected.

## 7. v1 refinement path

Hour-resolved cloud data (NSRDB/ASOS for the actual 2 km site, not ABQ airport) replacing day-counting; NWS high-wind climatology with seasonal correlation; LCH engagement: request an exploratory dialogue on standing-corridor PAMs (cost ≈ $0, information ≈ high); model closure arrival process explicitly (window-length distribution, not day-level probability); couple to the battery-recharge scheduler for >3 shots/day regimes.

---
*Sources: [NM annual sunshine days](https://www.currentresults.com/Weather/New-Mexico/annual-days-of-sunshine.php) · [LCH Reports Handbook](https://www.ucolick.org/~plynam/SHANEAO/DOCS/LCH_Reports_Handbook--2017-06-16.pdf) · [Laser-satellite deconfliction analysis (arXiv 2606.25238)](https://arxiv.org/html/2606.25238) · [DoDI 3100.11](https://irp.fas.org/doddir/dod/i3100_11.pdf) · [JSpOC laser deconfliction](https://www.vandenberg.spaceforce.mil/News/Features/Display/Article/920559/laser-tagged-how-the-jspoc-manages-laser-deconfliction/) · [NWS ABQ high-wind climatology](https://www.weather.gov/abq/features_highwind)*
