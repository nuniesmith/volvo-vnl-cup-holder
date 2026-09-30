# Tasks

Updated 2026-09-29. [v0.1 gauges](../src/stl/v0.1/README.md) · [Measurements](measurements.md) · [Photo review](photo-review.md)

## Decided

- [x] Goal: clone the stock VNL cup holder (84752175) for the ribbed dash shelf (four fit side by side).
- [x] Enlarge the cup so the **YETI Rambler 36 oz** (3.75 in / 95.3 mm) fits; the stock holder is too small.
- [x] Print in **two parts**, the main body and the clip, like the original.
- [x] Use the 304 stainless compression spring kit (0.5 × 6 × 25 mm, or × 30 mm for more preload).

## Done

- [x] Review all 13 photos; record markings, material (PC/ABS) and approximate tape readings.
- [x] Export v0.1 bottle rings and the stock-cup step gauge.
- [x] Resize the bottle rings to 96.0 / 97.5 / 99.0 mm for the 95.3 mm Rambler 36 oz.
- [x] Record the mount width, box length, floor size and torsion spring from the second photo set.

## Next

- [ ] Print the bottle rings; record the smallest ring that slides freely along the lower bottle (Y4).
- [ ] Print the step gauge; record the stock cup taper (B6).
- [ ] Take the caliper measurements in [measurements.md](measurements.md), especially the mount (B1–B3), pivots (B8, C2) and springs (S2–S4).
- [x] Mounting: holders clip onto any notch of the ribbed shelf lip and can be moved; four fit side by side (owner).
- [x] Read the rib pitch from the photo: ~39.5 mm (1.55 in).
- [x] Mount identified: two split posts snap into round holes under the upper ledge.
- [x] Spring kit: 304 stainless, largest 0.5 × 6 mm in 25/30 mm; roughly 2–4× weaker than stock.
- [x] Caliper the ledge holes and clip posts: 11.5 mm hole, 75.5 mm post spacing, 20 mm ledge, 17.5 / 24 mm on the post (owner).
- [x] 17.6 / 23.9 mm identified as orange clip dimensions (end tab, socket-end width), not post dimensions.
- [ ] Measure the stock post height (flange to tip), shank diameter and barb diameter; then fix `post_h` and re-export v0.2.
- [x] Neighbouring ledge holes are 75.5 mm apart (owner), the same as the post spacing. Holders sit at least 2 holes (151 mm) apart center to center.
- [x] Side-by-side clearance: at 151 mm minimum center spacing, the ~103 mm Yeti cup clears its neighbours.
- [ ] Confirm how the bottom of the holder grips the lip (T4).
- [ ] Decide on the grey tongue: reuse a torsion spring, or a printed flex finger (B11).
- [ ] Pick a filament: PETG or ASA suggested for cab heat.

## v0.2 (after measurements)

- [x] Export v0.2 mount tests: `post_fit.stl` (barbs 11.8 / 12.2 / 12.6 mm) and `pitch_strip.stl` (75.5 mm).
- [ ] Print the v0.2 mount tests **after** `post_h` is corrected; pick the barb size and confirm the pitch in the truck.
- [ ] Model the clip with a pocket for the 6 mm OD kit spring (~6.6 mm bore, ~18–20 mm installed); test pivot and return.
- [ ] Model the full body with the enlarged, tapered cup; decide the print orientation and supports.
- [ ] Assemble the body, clip and spring; test the Yeti fit, clip action and rattles in the truck.
- [ ] Print the second set once the first one fits.
