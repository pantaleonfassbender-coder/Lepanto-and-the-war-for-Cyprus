# Lepanto and the War for Cyprus

A documentary apparatus for the war for Cyprus and the Holy League, 1570–1573: public-domain sources from the siege of Famagusta to the battle of Lepanto and its afterlife, with readers (original beside English), a timeline linked into the texts, and plates from the prints of the time.

Stage 1 (September 2026) carries eight modules:

- **The capitulations of the Holy League** (Rome, May 1571) — the treaty in a Spanish copy printed by Dumont (1728), transcribed from the page images, with a working translation.
- **The loss of Famagusta** — Nestore Martinengo's report in William Malim's English (1572), with Malim's dedication, his description of Cyprus and his Latin prayer (transcribed from the page, with a working translation), from Hakluyt vol. V (1904).
- **Contarini: the councils and the battle** — Giovanni Pietro Contarini's *Historia delle cose successe* (Venice 1572), ff. 40r–56r, the Ottoman council of war, the battle and the news in Venice, from the Munich copy (MDZ full text, corrected against the page images), with a working translation; its map of the bay is a plate.
- **Herrera: the battle, and a song of victory** — Fernando de Herrera's *Relación de la guerra de Cipre* (Seville 1572), chapters XXIV–XXVIII and the *Canción*, from the reprint in the *Colección de documentos inéditos* XXI (1852), with a working translation.
- **Peçevî: Cyprus, Lepanto and the new fleet** — the Ottoman historian's chapters on the conquest of Cyprus (with Ebussuud's fetva and the surrender of Famagusta) and on the battle and the new fleet, *Tarih-i Peçevî* vol. I (Istanbul 1866), pp. 486–491 and 495–499, transcribed by eye from the printed Ottoman text, with a transliteration and a working translation.
- **Kâtip Çelebi: the broken fleet** — the Ottoman naval history *Tuhfetü'l-kibâr* (1656; Istanbul: Müteferrika, 1729), on Lepanto, the new fleet, Modon (1572), Venice's peace (1573) and the fall of La Goleta and Tunis (1574), ff. 42r–45v, transcribed by eye with a transliteration and a working translation.
- **Cervantes: the captive's Lepanto** — *Don Quixote* I.39 and the prologue to Part II, Spanish and Ormsby's English (1885).
- **Chesterton: Lepanto** (1911), as reception.

Planned modules and their sources are listed on the Texts page (`data/modules.json`).

## Building the data

```
python tools/build-liga.py
python tools/build-famagusta.py
python tools/build-contarini.py
python tools/build-herrera.py
python tools/build-pecevi.py
python tools/build-katib.py
python tools/build-cervantes.py
python tools/build-chesterton.py
```

The scripts download their sources (Internet Archive OCR, Project Gutenberg texts) into `tools/src/` and record every repair; the Liga, Peçevî and Kâtip Çelebi texts are transcribed by eye and embedded in their scripts.

## Running locally

Any static server, e.g. `python -m http.server 8133`.

Licences: see `LICENSES.md`.
