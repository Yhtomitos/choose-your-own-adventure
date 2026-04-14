#!/usr/bin/env python3
"""Build the static Netlify site from the canonical story data."""

from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from web.main import api_export


def main() -> None:
    result = api_export()
    dist_dir = Path(result["dist"])
    api_base = os.environ.get("CYOA_API_BASE", "").rstrip("/")
    config_js = (
        "// Generated at build time for Netlify static deployment.\n"
        f"window.CYOA_API_BASE = {api_base!r};\n"
    )
    (dist_dir / "config.js").write_text(config_js, encoding="utf-8")
    print(result["dist"])


if __name__ == "__main__":
    main()
