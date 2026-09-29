# Volvo VNL cup holder clone

A 3D-printed clone of the stock **Volvo VNL dash cup holder (Volvo 84752175 REV P02)** for the **two empty spots** in the truck. The cup is **enlarged to fit the owner's Yeti bottle**, which does not fit the stock holder. It is printed on an **Ender 3 Neo (220 × 220 × 250 mm)**.

The clone is printed in **two parts, like the original**:

- **Main body:** the cup, mounting flange and clip posts (grey on the stock part)
- **Clip:** the spring-loaded arm on the underside (orange on the stock part), returned by a **25 mm compression spring** (ordered)

**Current print checkpoint: [v0.1 measurement gauges](src/stl/v0.1/README.md).** No cup holder body or clip is modeled yet. These gauges set the enlarged cup size and record the stock cup's shape. Caliper measurements of the mount and clip come next ([measurement sheet](docs/measurements.md)).

![v0.1 gauges](src/stl/v0.1/preview.png)

## Start here

- [v0.1 gauges: what to print and how to read them](src/stl/v0.1/README.md)
- [Photo review of the stock part](docs/photo-review.md)
- [Caliper measurements needed for the clone](docs/measurements.md)
- [Current tasks](docs/todo.md)

## What we know so far

These are approximate tape readings from the photos, not caliper values.

| Feature | Photo reading | Source |
|---|---:|---|
| Stock cup opening, inside at the rim | ~4.0 in (~101 mm) | [IMG_0159](pictures/IMG_0159.JPEG) |
| Overall length, mount flange to far rim | ~6.6 in (~168 mm) | [IMG_0158](pictures/IMG_0158.JPEG) |
| Overall width across the underside | ~5.1 in (~130 mm) | [IMG_0160](pictures/IMG_0160.JPEG) |
| Orange clip length | ~5.1 in (~129 mm) | [IMG_0156](pictures/IMG_0156.JPEG) |
| Stock spring free length | ~1.05 in (~27 mm) | [IMG_0157](pictures/IMG_0157.JPEG) |
| Yeti bottle base diameter | ~3.6 in (~91 mm) | [IMG_0161](pictures/IMG_0161.JPEG) |

The stock rim is wider than the bottle base, so the tight spot is lower down: the cup tapers
toward its floor, and the grey spring tongue pushes into the cup. The step gauge records that taper.

## What has been checked

Only CAD checks. The v0.1 gauge STLs are closed, single-body meshes within the printer's build
volume ([mesh_checks.json](src/stl/v0.1/mesh_checks.json)). Nothing has been printed or fitted.

## Revision history

| Directory | Role |
|---|---|
| [v0.1](src/stl/v0.1) | Bottle-fit rings and a stock-cup step gauge; no body or clip yet |

## Layout

```
pictures/   reference photos of the stock part and bottle
docs/       photo review, measurement sheet, tasks
src/stl/    one folder per CAD revision (OpenSCAD source, STLs, scripts, preview)
```

Repository: [nuniesmith/volvo-vnl-cup-holder](https://github.com/nuniesmith/volvo-vnl-cup-holder).
