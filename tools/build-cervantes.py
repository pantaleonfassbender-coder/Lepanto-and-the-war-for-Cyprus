"""Build data/cervantes.json: the captive's Lepanto, in Spanish and English.

Don Quixote, Part I (1605), chapter 39: the captive, a soldier like the
author, tells of the Holy League, the battle, his capture, Navarino (1572),
Venice's separate peace (1573) and the loss of La Goleta (1574). Part II
(1615), prologue: the lost hand and "la más alta ocasión".

Spanish: Project Gutenberg ebook #2000 (a modernised-spelling text, not the
1605/1615 princeps). English: John Ormsby's translation (London, 1885),
Project Gutenberg ebook #996. Both public domain. The two texts paragraph
differently; units are aligned on the anchor phrases below.
"""
import json
import re
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
OUT = HERE.parent / "data" / "cervantes.json"


def gutenberg(num):
    SRC.mkdir(exist_ok=True)
    p = SRC / f"pg{num}.txt"
    if not p.exists():
        url = f"https://www.gutenberg.org/cache/epub/{num}/pg{num}.txt"
        with urllib.request.urlopen(url) as r:
            p.write_bytes(r.read())
    t = p.read_text(encoding="utf-8").replace("\r", "")
    return re.sub(r"[ \t]*\n[ \t]*(?!\n)", " ", t)  # unwrap lines, keep blank-line breaks


def between(text, start, end):
    a = text.index(start)
    b = text.index(end, a) + len(end)
    s = text[a:b]
    s = re.sub(r"\n\s*\n", " ", s)
    s = s.replace("»", "").replace("«", "")
    return re.sub(r"\s+", " ", s).strip()


UNITS = [
    # (label, Spanish start, Spanish end, English start, English end)
    ("The league of 1571",
     "Éste hará veinte y dos años", "como después lo hizo en Mecina.",
     "It is now some twenty-two years", "as he afterwards did at Messina."),
    ("That day",
     "Digo, en fin, que yo me hallé", "esposas a las manos.",
     "I may say, in short, that I", "manacles on my hands."),
    ("Taken in the battle",
     "Y fue desta suerte", "venían al remo en la turquesca armada.",
     "It happened in this way", "regained their longed-for liberty that day."),
    ("Navarino, 1572",
     "Lleváronme a Costantinopla", "verdugos que nos castiguen.",
     "They carried me to Constantinople", "instruments of punishment to chastise us."),
    ("The capture of the Prize",
     "En efeto, el Uchalí se recogió", "el odio que ellos le tenían.",
     "As it was, El Uchali took refuge", "the hatred with which they hated him."),
    ("Tunis, and the Venetian peace",
     "Volvimos a Constantinopla, y el año siguiente", "las nuevas de mi desgracia a mi padre.",
     "We returned to Constantinople, and the following year", "telling him of my misfortunes."),
    ("The loss of La Goleta, 1574",
     "Perdióse, en fin, la Goleta", "que aquellas piedras la sustentaran.",
     "At length the Goletta fell", "these stones were needed to support it."),
]

PROLOGUE = ("The hand lost at Lepanto",
            "Lo que no he podido dejar de sentir", "sin haberme hallado en ella.",
            "What I cannot help taking amiss", "without having been present at it.")


def main():
    es = gutenberg(2000)
    en = gutenberg(996)
    n = 0
    units = []
    for label, sa, se, ea, ee in UNITS:
        n += 1
        units.append({"n": n, "orig": between(es, sa, se), "en": between(en, ea, ee), "titel": label})
    n += 1
    label, sa, se, ea, ee = PROLOGUE
    prol = [{"n": n, "orig": between(es, sa, se), "en": between(en, ea, ee), "titel": label}]

    doc = {
        "id": "cervantes",
        "titel": "Cervantes: the Captive's Lepanto",
        "autor": "Miguel de Cervantes Saavedra",
        "jahr": "1605 / 1615",
        "sprache": "en",
        "orig_sprache": "es",
        "zk": "DQ",
        "quelle": "Miguel de Cervantes, El ingenioso hidalgo don Quijote de la Mancha, Part I (Madrid, 1605), ch. 39, and Part II (Madrid, 1615), prologue. Spanish: Project Gutenberg ebook #2000 (modernised spelling). English: The Ingenious Gentleman Don Quixote of La Mancha, trans. John Ormsby (London: Smith, Elder, 1885), Project Gutenberg ebook #996.",
        "hinweis": "The captive is a fiction, but his war is Cervantes's own: Cervantes fought at Lepanto on the Marquesa, took three arquebus wounds and lost the use of his left hand, and was himself a captive in Algiers from 1575 to 1580. The captive's campaign from the league to the fall of La Goleta follows the historical record closely; where he speaks of 'the sins of Christendom', the voice is the soldier's, not the historian's. The Spanish is a modern-spelling text, not the princeps; Ormsby's English is the translation of 1885. Both are public domain.",
        "sections": [
            {"id": "captive", "titel": "The captive's tale (Part I, ch. 39)", "zk": "DQ I.39",
             "blurb": "From the news of the league in Flanders to the fall of La Goleta: the day that broke 'the error … that the Turks were invincible at sea', the capture in the battle, the chance lost at Navarino, Venice's peace, and the stones of a fortress that memory did not need.",
             "units": units},
            {"id": "prologue", "titel": "The hand (Part II, prologue)", "zk": "DQ II Prol.",
             "blurb": "Forty-four years later, answering a rival who mocked him as old and one-handed: the hand was lost 'on the grandest occasion the past or present has seen, or the future can hope to see'.",
             "units": prol},
        ],
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"cervantes.json: {len(units) + len(prol)} units")
    for u in units + prol:
        print(f"  {u['n']} {u['titel']}: es {len(u['orig'])} / en {len(u['en'])}")


if __name__ == "__main__":
    main()
