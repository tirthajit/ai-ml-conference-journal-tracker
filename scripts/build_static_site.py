#!/usr/bin/env python3
"""Sanity-check static GitHub Pages assets.

The website is intentionally static. It reads CSV data from the repository's raw
GitHub URLs, so routine data updates only require editing files in data/.
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REQUIRED_FILES = [
    "index.html",
    "calendar.html",
    "conferences.html",
    "journals.html",
    "methodology.html",
    "how-to-use.html",
    "assets/style.css",
    "assets/app.js",
    "assets/logo.svg",
    ".nojekyll",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Check required site files exist.")
    parser.parse_args()

    missing = [rel for rel in REQUIRED_FILES if not (DOCS / rel).exists()]
    if missing:
        print("Missing site files:")
        for item in missing:
            print(f"- docs/{item}")
        return 1

    print("Static site files are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
