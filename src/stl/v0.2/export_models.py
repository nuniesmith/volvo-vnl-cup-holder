"""Export the v0.2 mount test pieces; requires OpenSCAD."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parent
for part in ("post_fit", "pitch_strip"):
    result=subprocess.run(["openscad", "--export-format", "binstl", "-D", f'part="{part}"',
                           "-o", str(ROOT / f"{part}.stl"), str(ROOT / "mount_test.scad")],
                          capture_output=True, text=True)
    if result.returncode or "WARNING:" in result.stderr or "ERROR:" in result.stderr:
        raise RuntimeError(f"{part}: {result.stderr}")
    print(f"Exported {part}.stl", flush=True)
