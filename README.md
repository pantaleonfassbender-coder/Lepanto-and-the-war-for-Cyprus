# Lepanto and the War for Cyprus

A documentary apparatus for the war for Cyprus and the Holy League, 1570–1573: public-domain sources from the siege of Famagusta to the battle of Lepanto and its afterlife, with readers (original beside English), a timeline linked into the texts, and plates from the prints of the time.

Stage 1 (September 2026) carries four modules:

- **The capitulations of the Holy League** (Rome, May 1571) — the treaty in a Spanish copy printed by Dumont (1728), transcribed from the page images, with a working translation.
- **The loss of Famagusta** — Nestore Martinengo's report in William Malim's English (1572), with Malim's dedication, his description of Cyprus and his Latin prayer (transcribed from the page, with a working translation), from Hakluyt vol. V (1904).
- **Cervantes: the captive's Lepanto** — *Don Quixote* I.39 and the prologue to Part II, Spanish and Ormsby's English (1885).
- **Chesterton: Lepanto** (1911), as reception.

Planned modules and their sources are listed on the Texts page (`data/modules.json`).

## Building the data

```
python tools/build-liga.py
python tools/build-famagusta.py
python tools/build-cervantes.py
python tools/build-chesterton.py
```

The scripts download their sources (Internet Archive OCR, Project Gutenberg texts) into `tools/src/` and record every repair.

## Running locally

Any static server, e.g. `python -m http.server 8133`.

Licences: see `LICENSES.md`.
