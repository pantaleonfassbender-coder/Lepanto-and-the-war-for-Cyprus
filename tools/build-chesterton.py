"""Build data/chesterton.json: G. K. Chesterton, "Lepanto" (1911).

Text: Project Gutenberg ebook #31184 (Chesterton, Poems), corrected against
the print of Poems (London: Burns & Oates, 1917; Internet Archive
poemsche00chesuoft) wherever the ebook drops or misreads a word. Public
domain (published before 1930; Chesterton died in 1936).
"""
import json
import re
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
OUT = HERE.parent / "data" / "chesterton.json"

# ebook reading -> the 1917 print
COLLATION = [
    ("is shake with his ships", "is shaken with his ships"),
    ("up the cape of Italy", "up the capes of Italy"),
    ("in the brave beard curled.", "in the brave beard curled,"),
    ("Spuming of his stirrups", "Spurning of his stirrups"),
    ("in 'the mountains", "in the mountains"),
    ("in a narrow dusty\n", "in a narrow dusty room,\n"),
    ("he trembles very\n", "he trembles very soon\n"),
    ("shuttered from the day.", "shuttered from the day,"),
    ("his hounds have bayed--Booms\naway past Italy", "his hounds have bayed—\nBooms away past Italy"),
    ("he seeks no more a sign_(But\nDon John of Austria has burst the battle-line!)_",
     "he seeks no more a sign—\n(But Don John of Austria has burst the battle-line!)"),
    ("labour under sex", "labour under sea"),
    ("rides home from the Crusade_.)", "rides home from the Crusade.)"),
]


def main():
    SRC.mkdir(exist_ok=True)
    p = SRC / "pg31184.txt"
    if not p.exists():
        with urllib.request.urlopen("https://www.gutenberg.org/cache/epub/31184/pg31184.txt") as r:
            p.write_bytes(r.read())
    t = p.read_text(encoding="utf-8").replace("\r", "")
    a = t.index("     LEPANTO\n", t.index("WAR POEMS"))
    b = t.index("THE MARCH OF THE BLACK MOUNTAIN", a)
    poem = "\n".join(l.strip() for l in t[a:b].split("\n")[1:]).strip()
    for old, new in COLLATION:
        assert old in poem, old
        poem = poem.replace(old, new)
    poem = poem.replace("--", "—").replace("_", "")
    stanzas = [s.strip() for s in re.split(r"\n\s*\n", poem) if s.strip()]
    units = [{"n": i + 1, "en": s} for i, s in enumerate(stanzas)]
    doc = {
        "id": "chesterton",
        "titel": "Chesterton: Lepanto",
        "autor": "G. K. Chesterton",
        "jahr": "1911",
        "sprache": "en",
        "zk": "Chest.",
        "quelle": "G. K. Chesterton, \"Lepanto\", first printed in 1911; text from Project Gutenberg ebook #31184 (Poems), collated with Poems (London: Burns & Oates, 1917), Internet Archive poemsche00chesuoft.",
        "hinweis": "Three hundred and forty years after the battle, and a year before the Balkan wars: the most read English account of Lepanto is a crusading ballad. It is carried here as reception, not as evidence. Its Sultan, its Mahound and its 'yellow' faces are the Edwardian imagination's, and its closing image, Cervantes sheathing his sword and seeing Don Quixote on the road, is a poet's gift, not a fact. Where the ebook and the 1917 print differ, the print is followed; 'slaves that swat' is the print's reading.",
        "verse": True,
        "sections": [{
            "id": "poem", "titel": "Lepanto", "zk": "Chest.",
            "blurb": "The ballad in the nine stanzas of the 1917 print: the Soldan smiling, the kings of Christendom looking away, Don John riding to the sea, the captives in the galleys' holds, and Cervantes sheathing the sword.",
            "units": units,
        }],
    }
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"chesterton.json: {len(units)} stanzas")


if __name__ == "__main__":
    main()
