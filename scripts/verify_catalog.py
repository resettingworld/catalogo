"""Verify structural integrity and schema compliance of Resetting World catalogo."""

import json
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    market_path = root / "marketplace_catalog.json"
    if not market_path.exists():
        print("ERROR: marketplace_catalog.json missing")
        return 1

    market = json.loads(market_path.read_text(encoding="utf-8"))
    catalogs_dir = root / "catalogs"
    errors = 0

    for entry in market:
        cid = entry["id"]
        cdir = catalogs_dir / cid
        if not cdir.exists():
            print(f"ERROR: Missing catalog folder for {cid}")
            errors += 1
            continue
        for req_file in ("metadata.json", "manifest.json"):
            fpath = cdir / req_file
            if not fpath.exists():
                print(f"ERROR: {cid} missing {req_file}")
                errors += 1
                continue
            try:
                json.loads(fpath.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                print(f"ERROR: Invalid JSON in {fpath}: {exc}")
                errors += 1

        cat_file = cdir / "catalog.json"
        if cat_file.exists():
            try:
                json.loads(cat_file.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                print(f"ERROR: Invalid JSON in {cat_file}: {exc}")
                errors += 1

    print(f"Verified {len(market)} marketplace entries with {errors} errors.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
