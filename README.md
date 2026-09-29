# Volvo VNL cup holder clone

A 3D-printed clone of the stock **Volvo VNL dash cup holder (Volvo 84752175 REV P02)** for the ribbed dash shelf, where holders clip onto **any notch** and four fit side by side. The cup is **enlarged to fit the owner's YETI Rambler 36 oz bottle** (listed 3.75 in / 95.3 mm across), which does not fit the stock holder. It is printed on an **Ender 3 Neo (220 × 220 × 250 mm)**.

The clone is printed in **two parts, like the original**:

- **Main body:** the cup, mounting flange and clip posts (grey on the stock part)
- **Clip:** the spring-loaded arm on the underside (orange on the stock part), returned by a **25 mm compression spring** (a spring kit is on order)

The stock part also has a **torsion spring on a metal pin** inside the box, which loads the grey tongue ([photo](pictures/box_inside_torsion_spring.jpg)). The clone needs that one too, or a printed flex tongue instead.

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
| Stock cup floor, inside | ~3.3–3.4 in (~85 mm), scaled from the photo | [underside_floor](pictures/underside_floor.jpg) |
| Mount end (box) width | ~3.9 in (~99 mm) | [mount_end_width](pictures/mount_end_width.jpg) |
| Box length along the side | ~4.1 in (~104 mm) | [box_inside_torsion_spring](pictures/box_inside_torsion_spring.jpg) |
| Clip-post edge to where the cup curve starts | ~2.2 in (~56 mm) | [clip_post_flange](pictures/clip_post_flange.jpg) |
| Overall length, mount flange to far rim | ~6.6 in (~168 mm) | [IMG_0158](pictures/IMG_0158.JPEG) |
| Overall width across the underside | ~5.1 in (~130 mm) | [IMG_0160](pictures/IMG_0160.JPEG) |
| Orange clip length | ~5.1 in (~129 mm) | [IMG_0156](pictures/IMG_0156.JPEG) |
| Stock spring free length | ~1.05 in (~27 mm) | [IMG_0157](pictures/IMG_0157.JPEG) |
| YETI Rambler 36 oz diameter | **3.75 in (95.3 mm)**, listed spec; base read ~3.6 in | [IMG_0161](pictures/IMG_0161.JPEG) |

The stock rim (~101 mm) is wider than the bottle (95.3 mm), but the cup tapers to about 85 mm at the floor,
so the bottle jams partway down. The grey spring tongue also pushes into the cup. The clone needs a bore of
about 97–98 mm most of the way down; the bottle rings pick the exact size.

## What has been checked

Only CAD checks. The v0.1 gauge STLs are closed, single-body meshes within the printer's build
volume ([mesh_checks.json](src/stl/v0.1/mesh_checks.json)). Nothing has been printed or fitted.

## Revision history

| Directory | Role |
|---|---|
| [v0.1](src/stl/v0.1) | Bottle-fit rings (96.0 / 97.5 / 99.0 mm) and a stock-cup step gauge; no body or clip yet |

## Layout

```
pictures/   reference photos of the stock part and bottle
docs/       photo review, measurement sheet, tasks
src/stl/    one folder per CAD revision (OpenSCAD source, STLs, scripts, preview)
```

Repository: [nuniesmith/volvo-vnl-cup-holder](https://github.com/nuniesmith/volvo-vnl-cup-holder).
