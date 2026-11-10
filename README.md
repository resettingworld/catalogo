# Resetting World — Open Knowledge Catalog (`catalogo`)

> **Public Data Repository of Resetting World**: Curated metadata, academic classifications, Collage Punk visual assets, and downloadable RAG capsule releases ($\le 50$ books/capsule).

[![License: CC-BY-4.0 / MIT](https://img.shields.io/badge/Data%20License-CC--BY--4.0%20%7C%20MIT-blue.svg)](./LICENSE)
[![Capsules: 50](https://img.shields.io/badge/Knowledge%20Capsules-50-39ff14.svg)]()
[![Release: v1.0.0](https://img.shields.io/badge/Packs-GitHub%20Releases-ff007f.svg)](https://github.com/resettingworld/catalogo/releases)

---

## 🌍 Overview / Visió General / Visión General

**EN**: `catalogo` stores the open-access structural metadata (`marketplace_catalog.json`, `metadata.json`, `manifest.json`, `catalog.json`) and Collage Punk visual covers for all **50 Resetting World RAG Capsules**, while full vectorized `.zip` capsules (4.6 GB total, containing preserved original PDFs and SQLite FTS5 + EmbeddingGemma 2 vector databases) are published under [**GitHub Releases (`v1.0.0`)**](https://github.com/resettingworld/catalogo/releases/tag/v1.0.0).

**CA**: `catalogo` emmagatzema les metadades estructurals obertes (`marketplace_catalog.json`, `metadata.json`, `manifest.json`, `catalog.json`) i les portades visuals Collage Punk de les **50 Càpsules RAG de Resetting World**. Els arxius `.zip` complets vectoritzats (4.6 GB totals amb PDFs preservats i bases SQLite) es distribueixen directament a [**GitHub Releases (`v1.0.0`)**](https://github.com/resettingworld/catalogo/releases/tag/v1.0.0).

**ES**: `catalogo` almacena los metadatos estructurales abiertos (`marketplace_catalog.json`, `metadata.json`, `manifest.json`, `catalog.json`) y las portadas visuales Collage Punk de las **50 Cápsulas RAG de Resetting World**, mientras que los paquetes `.zip` vectorizados completos (4.6 GB totales con PDFs preservados e índices SQLite) se publican en [**GitHub Releases (`v1.0.0`)**](https://github.com/resettingworld/catalogo/releases/tag/v1.0.0).

---

## 📂 Repository Layout

```text
catalogo/
├── marketplace_catalog.json       # Unified index of all 50 RAG capsules & download URLs
├── catalogs/
│   └── <capsule-id>/
│       ├── catalog.json           # Front-matter summaries, region, normatives & Collage Punk style
│       ├── metadata.json          # KnowledgeAreaMeta schema & BookMeta SHA-256 registry
│       ├── manifest.json          # Vector chunks, modalities & pack integrity manifest
│       └── images/
│           ├── banner.png|jpg     # 16:9 Collage Punk capsule banner
│           └── covers/*.png       # Per-book Collage Punk covers
├── scripts/
│   └── verify_catalog.py          # Automated catalog integrity & policy validator
├── AGENTS.md                      # AI agent cataloging rules & invariants
├── CONTRIBUTING.md                # How to curate & submit new technical capsules
└── LICENSE                        # CC-BY-4.0 (metadata) + MIT (scripts)
```

---

## 🚀 Usage with `rw-knowledge` (`smart-local`)

```bash
# Download any capsule from Releases, e.g. survival basics:
curl -LO https://github.com/resettingworld/catalogo/releases/download/v1.0.0/supervivencia-es-v1.0.0.zip

# Install into your local offline RAG node:
smart-local import-pack supervivencia-es-v1.0.0.zip
```

Verify catalog integrity locally:
```bash
python3 scripts/verify_catalog.py
```
