# Work Item 22 — Citation & Uncertainty Pass: Kickoff (Headline Numbers)
### Magnetic Matter Movers · compiled July 20, 2026
*Scope of this kickoff: the cheat-sheet headline figures and the claims most likely to be challenged in review. Each row: study claim → best public source found → verdict and band. Remaining scope at the end. This does not close item 22; it establishes the method and clears the highest-visibility rows.*

---

## Verified rows

| # | Study claim | Public source & figure | Verdict |
|---|---|---|---|
| 1 | Chemical comparison: "$5–10k/kg chemical" and 2% payload fraction | Falcon 9 list price raised to **$74M in 2026**; rideshare **$7,000/kg**; dedicated F9 ≈ $3.2–4.3k/kg LEO at 17–23 t; SpaceX *internal* cost reported ≈ $660/kg | **Revise band.** "$5–10k/kg" is right for escape-class and rideshare, high for dedicated LEO. Recommended language: "LEO $3–7k/kg published prices; escape-class $5–10k/kg" → [E] with citation |
| 2 | Laser-thermal Isp 900 (solid HX ceiling) | Kare's HX thruster program (AIP Conf. Proc. 664, 442, 2003; OSTI 20632945): solid-HX laser launch at **Isp 600–800 s**; Duplay et al. 2022 (Acta Astronautica / arXiv 2201.00244) laser-*plasma* hydrogen: **Isp ~3,000 s** | **Consistent but at the edge.** 900 s sits above published solid-HX demos, below plasma — matches the study's own "solid-HX ceiling" framing and its Isp-850 de-rate check. Label [I]; cite Kare as floor, Duplay as the block-upgrade ceiling |
| 3 | "2,800× the largest EM launcher built" (gun extrapolation) | Largest EM launchers: Navy/General Atomics railgun **world-record ~33 MJ** muzzle-energy class (ONR, 2010–2012 32 MJ prototypes) | **Confirmed order.** 85 GJ / 32 MJ ≈ 2,650×; 48 GJ variant ≈ 1,500×. Recommended: "~1,500–2,700×" → [E] for the record, [I] for the extrapolation claim |
| 4 | Black carbon "≈500× surface warming potency"; "~1 t BC per launch" | Ryan et al. 2022, *Earth's Future* (10.1029/2021EF002612): BC at stratospheric injection ~**500× more warming-efficient** than surface/aviation BC — confirmed. Per-launch BC for kerolox: literature range ~0.3–3 t depending on engine/cycle | **500× confirmed [E] with citation. Per-launch tonnage: widen to 0.3–3 t [I]** pending engine-specific sourcing |
| 5 | "~25–30 t CO₂ per t payload, chemical" | Order-of-magnitude check: F9 ≈ 490 t propellant burn ≈ ~500 t CO₂-class combustion products / ~17 t payload ≈ 29 t/t | **Consistent [I]** — replace with sourced per-vehicle emissions inventory in full pass |
| 6 | Laser capex "$5–20/W" (dominant System B capex) | Industrial fiber-laser market 2026: complete multi-kW cutting systems now ≈ $5–15/W all-in; bare high-power sources lower and falling; Duplay et al. use ~$10/W near-term with $1/W far-term projections | **Band confirmed [I]**, well-positioned on the curve; cite Duplay's cost-curve discussion + market pricing snapshot |
| 7 | Myrabo lightcraft: "50 g to 71 m, 2000" (Phase 1 anchor) | Lightcraft Technology Demonstrator, White Sands/HELSTF, Oct 2000: 10 kW pulsed CO₂ laser, ~50 g craft, **71–72 m altitude** | **Confirmed [E]** |
| 8 | HX flux "48 MW/m² = 3× fusion divertor" | ITER divertor steady-state design target ~10 MW/m², transient/slow-transient 20 MW/m² | **Confirmed as 2.4–5×** depending on reference point; keep "3×" with the 10–20 MW/m² citation → [E] |
| 9 | Tracking collapse "60.1% → 0.43%" (relay justification) | Shimamura group 28 GHz program, J. Spacecraft & Rockets + Sci. Rep. 2025 (already cited in study) | **Already sourced [E]** — carry citation into white paper reference list |
| 10 | Provisional filing "$65" | USPTO current fee schedule: micro entity provisional = **$65.00** (code 1005/2005/3005) | **Confirmed [E]** |
| 11 | NM sky statistics (new, item 21) | ABQ 167 clear/111 partly cloudy days, 76% possible sunshine | **Sourced [E]** — see item 21 memo |

## Corrections to apply to the architecture study (forward-dated commit, per repo convention)

1. **Row 1:** re-band the chemical $/kg comparison and add the 2026 price citations — the current "2%/$5–10k" framing is attackable as stale in review.
2. **Row 3:** replace "2,800×" with "~1,500–2,700× (variant-dependent)".
3. **Row 4:** widen per-launch BC to 0.3–3 t; keep the 500× with the Ryan et al. DOI.
4. **General:** rows 2, 5, 6 keep [I] labels but now carry citations — upgrade their footnotes from "memory-sourced" to "sourced, first-cut."

## Remaining item-22 scope (unchanged priority order)

Full $/kg inference chains (payload × capex × rate × amortization) with propagated uncertainty bands; capex curves ($0.1B/$4–12B/$23–84B) against published megaproject analogs; tug/depot trade table sources (electrolysis yield 0.78, steam Isp 400); aerocapture entry-speed heritage (MSL 5.8 km/s etc.); pulsed-power farm cost basis; Inductrack L/D and Halbach field claims to Post/Lawrence Livermore primary papers; line-by-line [E]/[I]/[S] sweep of the full study.

---
*Sources: [SatBase: F9 price 2026](https://satbase.com/articles/spacex-falcon-9-price-increase-2026) · [NextBigFuture: F9 internal cost](https://www.nextbigfuture.com/2026/02/spacex-falcon-9-true-cost-to-launch-is-about-300-per-pound-which-is-25-of-selling-price-to-customers.html) · [NASA NTRS: launch cost reduction](https://ntrs.nasa.gov/citations/20200001093) · [Kare HX thruster (ADS)](https://ui.adsabs.harvard.edu/abs/2003AIPC..664..442K/abstract) · [Kare HX development (OSTI)](https://www.osti.gov/biblio/20632945) · [Duplay et al. laser-thermal Mars (arXiv)](https://ar5iv.labs.arxiv.org/html/2201.00244) · [ONR railgun record](https://www.onr.navy.mil/media-center/news-releases/navy-targets-new-world-record-electromagnetic-railgun-demonstration) · [GA railgun record](https://www.ga.com/general-atomics-team-powers-navy-rail-gun-to-new-world-record) · [Ryan et al. 2022, Earth's Future](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2021EF002612) · [NOAA BC rocket climate report](https://repository.library.noaa.gov/view/noaa/53971) · [USPTO fee schedule](https://www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule) · [Laser propulsion overview (Wikipedia, for chain-citations only)](https://en.wikipedia.org/wiki/Laser_propulsion) · [2026 fiber laser pricing guide](https://www.superstarlaser.com/how-much-is-a-fiber-laser-2026-guide/)*
