# AGENTS.md — `catalogo`

Instructions for AI curation and validation agents working in **`resettingworld/catalogo`**.

---

## 1. Repository Purpose
`catalogo` holds the open structured index (`marketplace_catalog.json`, per-capsule `catalog.json`, `metadata.json`, `manifest.json`, and Collage Punk cover imagery) for Resetting World's off-grid knowledge packages. Full `.zip` archives live in GitHub Releases (`v1.0.0`) because individual capsules exceed Git's 100 MB blob limit.

---

## 2. Hard Invariants
1. **No Raw Large Binaries in Git**: Never commit `.zip`, `.gpk`, `.db`, or large `.pdf` files directly to git history (`<= 100 MB` GitHub limit). Store release `.zip` packs as GitHub Release assets.
2. **Capsule Book Cap (`<= 50`)**: New or updated capsules must contain at most 50 books (one legacy capsule `cloud-computing` has 70 and should be split in future v1.1.0 releases).
3. **Strict Fiction Exclusion**: Novels, poetry, drama, and commercial fiction are prohibited. Focus strictly on survival, medicine, agriculture, engineering, physics, computing, and philosophy.
4. **Canonical Visual Identity (`collage-punk-v1`)**: All `catalog.json` entries and generated covers/banners must match `collage-punk-v1`.
5. **License Respect**: Preserve original institutional/public-domain attributions (`source_portal`, `author`, `sha256`) in `metadata.json` and `catalog.json`.

---

## 3. Verification Command
```bash
python3 scripts/verify_catalog.py
```
Always run `verify_catalog.py` after modifying any JSON file in `catalogs/` or `marketplace_catalog.json`.
