#!/usr/bin/env python3
"""Run all DSA Visualization code blocks and report errors.

This uses a headless matplotlib backend to avoid opening windows
and focuses on execution correctness.
"""

from __future__ import annotations

import os
import re
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DSA_DIRS = [ROOT / "04_DSA_Linear", ROOT / "05_DSA_NonLinear"]

PATTERN = re.compile(
    r"## 🎨 Visualization \(Optional\)[\s\S]*?```python\n([\s\S]*?)\n```",
    re.MULTILINE,
)


def extract_visual_snippets(md_path: Path) -> list[str]:
    text = md_path.read_text(encoding="utf-8")
    return [m.group(1) for m in PATTERN.finditer(text)]


def run_snippet(snippet: str) -> tuple[bool, str]:
    try:
        exec(snippet, {})
        return True, ""
    except Exception:
        return False, traceback.format_exc()


def main() -> int:
    # Ensure repo root is on sys.path for DSA_Utils imports.
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    os.environ.setdefault("DSA_FORCE_GUI", "0")
    # Use a writable Matplotlib config dir to avoid cache issues.
    os.environ.setdefault("MPLCONFIGDIR", str(Path("/tmp") / "mplconfig"))
    os.environ.setdefault("MPLBACKEND", "Agg")

    import warnings
    warnings.filterwarnings("ignore", message="FigureCanvasAgg is non-interactive")

    import matplotlib
    matplotlib.use("Agg", force=True)
    import matplotlib.pyplot as plt
    plt.show = lambda *args, **kwargs: None

    files = []
    for d in DSA_DIRS:
        files.extend(sorted(d.glob("*.md")))

    total = 0
    failures = []

    for md in files:
        snippets = extract_visual_snippets(md)
        if not snippets:
            continue
        for idx, snippet in enumerate(snippets, start=1):
            total += 1
            ok, output = run_snippet(snippet)
            if not ok:
                failures.append((md, idx, output))
                print(f"FAIL: {md} (snippet {idx})")
                if output:
                    print(output)
                print("-" * 60)
            else:
                print(f"OK:   {md} (snippet {idx})")

    print("\nSummary")
    print(f"  Total snippets: {total}")
    print(f"  Failures: {len(failures)}")

    if failures:
        print("\nFailed snippets:")
        for md, idx, output in failures:
            print(f"- {md} (snippet {idx})")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
