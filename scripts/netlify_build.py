#!/usr/bin/env python3
"""Build the static Netlify site from the canonical story data."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from web.main import api_export


def main() -> None:
    result = api_export()
    print(result["dist"])


if __name__ == "__main__":
    main()
