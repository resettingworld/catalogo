# Contributing to `catalogo`

We welcome researchers, librarians, educators, and technical curators to expand and refine Resetting World's open knowledge index.

## How to Submit a New Capsule Catalog

1. Verify source documents are **open-access / public domain / Creative Commons** and contain zero fiction.
2. Keep capsule size **`<= 50` books** to ensure fast ARM64 / Raspberry Pi 5 search latency.
3. Generate `catalog.json`, `metadata.json`, `manifest.json`, and Collage Punk covers using [`rw-knowledge`](https://github.com/resettingworld/rw-knowledge).
4. Add the lightweight folder under `catalogs/<capsule-id>/` and update `marketplace_catalog.json` (do NOT commit large `.zip` or `.db` files directly to Git).
5. Run `python3 scripts/verify_catalog.py` before opening a Pull Request.
