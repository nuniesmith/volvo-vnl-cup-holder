"""Export the v0.1 measurement gauges; requires OpenSCAD."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parent
JOBS=[(f"bottle_ring_{d}", {"part": '"bottle_ring"', "ring_id": d}) for d in ("92.0", "93.5", "95.0")]
JOBS.append(("cup_step_gauge", {"part": '"cup_step_gauge"'}))
for name, params in JOBS:
    args=[a for k, v in params.items() for a in ("-D", f"{k}={v}")]
    result=subprocess.run(["openscad", "--export-format", "binstl", *args,
                           "-o", str(ROOT / f"{name}.stl"), str(ROOT / "measure_gauges.scad")],
                          capture_output=True, text=True)
    if result.returncode or "WARNING:" in result.stderr or "ERROR:" in result.stderr:
        raise RuntimeError(f"{name}: {result.stderr}")
    print(f"Exported {name}.stl", flush=True)
