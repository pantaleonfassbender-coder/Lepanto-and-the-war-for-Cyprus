"""Build data/famagusta.json: the loss of Famagusta, 1571.

Source: Nestore Martinengo's report to the Doge, in William Malim's English
(London, 1572), with Malim's dedication, his description of Cyprus, his
address to the reader and his Latin prayer "In Turchas precatio", as
reprinted in Hakluyt, Principal Navigations, vol. V (Glasgow: MacLehose,
1904), pp. 117-152. Public domain.

Text: the Internet Archive OCR of copy `principalnavigat0005unse`, which
keeps the side notes apart from the body; the report's first page is taken
from copy `principalnavigat05hakl`, where the other copy runs the notes into
the text. The Latin prayer was transcribed by eye from the page image
(leaf 158 of the first copy), keeping the printer's ligatures and accents.
Spelling is the 1599 text as MacLehose reprinted it; the English working
translation of the Latin is this site's own (CC0).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hakluyt as H

OUT = Path(__file__).resolve().parent.parent / "data" / "famagusta.json"

HEADS = [
    "To the Reader.", "In Turchas precatio.", "Gulielmus Malim.",
    "The first assault.", "The second assault.", "The third assault.",
    "The fourth assault.", "The fift assault.", "The sixt and last assault.",
    "The Fortifiers.", "Turkish Captaines at Famagusta.",
    "The names of Christians made slaves.",
    "The Captains of the Christians slaine in Famagusta.",
]

# Decorated initials the OCR lost or mangled, and single misreadings.
FIXES = [
    (r"^<@\]i hath bene", "It hath bene"),
    (r"^He Mand of Cyprus", "The Iland of Cyprus"),
    (r"^Am not ignorant \(gentle Reader\) how hard a matter it is for any one man to write that, which should please and -~§\|\| satishe all persons, we being commonly \| of so divers opinions and contrary judges@p\|\} ments: againe Tully affrmeth it to be =a very",
     "I Am not ignorant (gentle Reader) how hard a matter it is for any one man to write that, which should please and satisfie all persons, we being commonly of so divers opinions and contrary judgements: againe Tully affirmeth it to be a very"),
    (r"^r / ‘He one and twentieth", "THe one and twentieth"),
    (r"^, i ‘He nine and twentieth", "THe nine and twentieth"),
    (r"^= the said Brey", "TO the said Brey"),
    (r"^\\ A THerefore they came", "WHerefore they came"),
    (r"^He enemies travelled", "THe enemies travelled"),
    (r"^ok \(aS next morning", "THe next morning"),
    (r"\bHand\b", "Iland"), (r"\bHands\b", "Ilands"),
    (r"behaviour \| partly", "behaviour I partly"),
    (r"From whence \| shortly", "From whence I shortly"),
    (r"Aégypt", "Ægypt"), (r"newé", "newe"), (r"perSorm", "perform"),
    (r"y‘ he had", "yt he had"), (r"d’Ascolt", "d'Ascoli"), (r"d’I", "d'I"),
    (r"Signiour -Baglione", "Signiour Baglione"),
    (r"with the sonne also of Mustafa in person, the Turkes gard\.",
     "with the sonne also of Mustafa in person, who made very much of them."),
    (r" The Vv 145 K The propertie of true fortitude is, not to be broken with sudden terrors\.$", " The"),
    (r"Cilictum", "Cilicium"), (r"it,; but", "it, but"),
    (r"for ever\) I, craving", "for ever) craving"),
]

# The report's first page, from the second copy (see above).
FIRST_PAGE = (
    "THe sixteenth day of February, * 1571, the fleet which had brought the ayde "
    "unto Famagusta, departed from thence, whereas were found in all the army, but "
    "foure thousand footmen, eight hundred of them chosen souldiers, and three "
    "thousand (accounting the Citizens and other of the Villages) the rest two "
    "hundred in number were souldiers of Albania. After the arrivall of the which "
    "succour, the fortification of the City went more diligently forward of all "
    "hands, then it did before, the whole garison, the Grecian Citizens inhabiting "
    "the Towne, the Governours and Captaines not withdrawing themselves from any "
    "kinde of labour, for the better incouragement and good example of others, both "
    "night and day searching the watch, to the intent with more carefull heed taking "
    "they might beware of their enemies, against whom they made no sally out of the "
    "City to skirmish but very seldome, especially to understand when they might "
    "learne the intent of the enemies. Whilest we made this diligent provision "
    "within the Citie, the Turks without made no lesse preparation of all things "
    "necessary, fit to batter the fortresse withall, as in bringing out of Caramania "
    "and Syria with all speed by the Sea, many woollpacks, a great quantitie of wood "
    "and timber, divers pieces of artillery, engins, and other things expedient for "
    "their purpose."
)

# Where one printed paragraph was run into the next (a full-width last line).
SPLITS = [
    "Since the which time, an easier, readier",
    "Many other like examples I could alledge",
    "But whosoever they be, that in all their life time",
    "For the which cause I have enterprised",
    "Certeinly it mooveth me much",
    "Thus nothing doubting of your ready ayd",
    "It hath bene, as Plinie writeth",
    "And last of all, the Venetians have enjoyed it",
    "Now this great Turke called Sultan Selim",
    "The Turkes in processe of time",
    "The nine and twentieth day of May",
    "Our enemies understanding how great",
    "So I speedily returning made true report",
    "It seemeth also a thing not impertinent",
    "At the same time, when the battery began",
]

# Malim's side notes, attached to the paragraph they stand beside.
NOTES = {
    "THe sixteenth day of February": "In Italy and other places the date of the yere of ye Lord is alwayes changed the first of January, or on New yeres day, and from that day reckoned upon: although wee heere in England, especially the temporall lawyers for certaine causes are not woont to alter the same untill the Annunciation of our Ladie.",
    "At the beginning of April Halli Basha": "Carumusalini be vessels like unto ye French Gabards, sailing daily upon the river of Bordeaux, which saile wt a misen or triangle saile. — Maone be vessels like unto ye great hulks, which come hither from Denmarke, some of the which cary 7 or 8 hundred tunnes a piece, flat and broad, which saile some of them with seven misens a piece. — Palandrie be great flat vessels made like Feriboats to transport horse.",
    "The Lord Baglione imparld": "Just Turkish dealing, to speake and not to meane: sodainly to promise, and never to perform the same.",
    "which thing was most false": "The propertie of true fortitude is, not to be broken with sudden terrors. — Mustafa, cosin germaine to ye thiefe, which hong on the left side of our Saviour at his Passion.",
    "This is now so much as I am able": "Begliarbei signifieth lord Admirall. — Sangiaccho, is that person wt the Turkes, that governeth a province or countrey.",
}

# In Turchas precatio, by eye from the page, with a working translation.
PRECATIO = [
    ("Summe Deus, succurre tuis, miseresce tuorum,\nEt subeat gentis te nova cura tuæ.",
     "Highest God, help your own, have pity on those who are yours,\nand let a new care for your people come upon you."),
    ("Quem das tantorum finem, Rex magne, laborum?\nIn nos vibrabit tela quoúsque Sathan?",
     "What end do you set, great King, to such labours?\nHow long will Satan hurl his spears at us?"),
    ("Antè Rhodum, mox indè Chium, nunc denique Cyprum,\nTurcharum cepit sanguinolenta manus.",
     "First Rhodes, then Chios, and now at last Cyprus\nhas the bloodstained hand of the Turks taken."),
    ("Mustafa fœdifragus partes grassatur in omnes,\nEt Veneta Cypriam strage cruentat humum.",
     "Mustafa, the breaker of treaties, rages through every quarter,\nand stains the soil of Cyprus with Venetian slaughter."),
    ("Nec finem imponit sceleri, mollitùe furorem,\nNec nisi potato sanguine pastus abit.",
     "He sets no end to crime, nor softens his fury,\nnor goes away fed until he has drunk blood,"),
    ("Qualis, quæ nunquam nisi plena tuménsque cruore\nSanguisuga obsessam mittit hirudo cutem.",
     "like the bloodsucking leech, which never lets go the skin it has seized\nuntil it is full and swollen with gore."),
    ("Torturam sequitur tortura, cruorque cruorem,\nEt cædem admissam cædis alîus amor.",
     "Torture follows torture, and blood follows blood,\nand after one slaughter done comes the lust for another."),
    ("Sævit inops animi, nec vel se temperat ipse,\nVel manus indomitum nostra domare potest.",
     "He rages, master of nothing in his mind; he does not restrain himself,\nnor can our hand tame the untamed."),
    ("At tu, magne Pater, tumidum disperde Tyrannum,\nNec sine mactari semper ovile tuum.",
     "But you, great Father, destroy the swollen tyrant,\nand do not let your fold be slaughtered for ever."),
    ("Exulet hoc monstrum, ne sanguine terra redundet.\nExcutiántque novum Cypria regna jugum.",
     "Let this monster be driven out, lest the earth overflow with blood,\nand let the realm of Cyprus shake off the new yoke."),
    ("Et quod Christicolæ fœdus pepigere Monarchæ,\nId faustum nobis omnibus esse velis.",
     "And the covenant the Christian monarchs have struck —\nmay you will it to be of good fortune to us all."),
    ("Tu pugna illorum pugnas, & bella secundes.\nCaptivósque tibi subde per arma Scythas.",
     "Fight their fights, and prosper their wars,\nand by arms bring the Scythians captive under you."),
    ("Sic tua per totum fundetur gloria mundum,\nUnus sic Christus fiet, & una fides.",
     "So shall your glory be poured out over all the world;\nso there shall be one Christ, and one faith."),
]


def load():
    L = H.fetch("principalnavigat0005unse")
    N = [H.norm(l) for l in L]
    s = next(i for i, l in enumerate(N) if l.startswith("The true report of the siege and taking of Fama"))
    e = next(i for i, l in enumerate(N) if "THE ENTERPRISE OF JOHN FOX" in l)
    P = H.paragraphs(H.body_lines(L[s:e]), HEADS)
    out = []
    for p in P:
        for pat, rep in FIXES:
            p = re.sub(pat, rep, p)
        out.append(p)
    return out


def split(paras):
    out = []
    for p in paras:
        parts = [p]
        for phrase in SPLITS:
            nxt = []
            for q in parts:
                k = q.find(phrase)
                if k > 0:
                    nxt += [q[:k].strip(), q[k:].strip()]
                else:
                    nxt.append(q)
            parts = nxt
        out += parts
    return out


def main():
    P = load()
    # repairs by position: the report's first page; notes that ran inline
    i = next(i for i, p in enumerate(P) if p.startswith("AN] He sixteenth"))
    P[i] = FIRST_PAGE
    P = [p for p in P if not p.startswith(("Just Turkish dealing", "who made very much of them.",
                                           "Mustafa, cosin germaine", "Ann. Dom. 1572.", "[In Turchas"))]
    j = next(i for i, p in enumerate(P) if p.endswith(" The") and "put to death" in p)
    P[j] = P[j] + " " + P[j + 1]
    del P[j + 1]
    P = split(P)

    idx = {name: next(i for i, p in enumerate(P) if p.startswith(start)) for name, start in [
        ("ded", "To the right honourable"), ("cyp", "A briefe description of the Iland"),
        ("rdr", "To the Reader."), ("pre", "In Turchas precatio."),
        ("rep", "The true report of all the successe"), ("rolls", "The Captains of the Christians slaine"),
    ]}

    n = 0
    def unit(text, **kw):
        nonlocal n
        n += 1
        u = {"n": n, "en": text}
        for key, prefix in NOTES.items():
            if text.startswith(key) or (key.startswith("which thing") and key in text):
                u["note"] = "Malim's side note: " + NOTES[key]
        u.update(kw)
        return u

    def prose(a, b, skip_first=True):
        units = []
        for p in P[a + (1 if skip_first else 0):b]:
            if p in HEADS:
                units.append(unit(p.rstrip("."), label=True))
            else:
                units.append(unit(p))
        return units

    title = unit(P[0], label=True)
    ded = [unit("To the right honourable and his singular good Lord, and onely Patron the Earle of Leicester, Baron of Denbigh, Knight of the honourable order of the Garter, one of the Queenes Majesties most honourable privy Councell &c. William Malim wisheth long health with increase of honour.", label=True)]
    ded += [unit(p) for p in P[idx["ded"] + 2:idx["cyp"]]]
    cyp = [unit(P[idx["cyp"]], label=True)] + [unit(p) for p in P[idx["cyp"] + 1:idx["rdr"]]]
    rdr = [unit(p) for p in P[idx["rdr"] + 1:idx["pre"]]]
    pre = [unit(en, orig=la) for la, en in PRECATIO] + [unit("Gulielmus Malim.", label=True)]

    rep_paras = P[idx["rep"]:idx["rolls"]]
    rep = [unit(rep_paras[0], label=True)]
    for p in rep_paras[1:]:
        rep.append(unit(p.rstrip(".") if p in HEADS else p, **({"label": True} if p in HEADS else {})))

    rolls_raw = P[idx["rolls"]:]
    rolls, cur = [], None
    for p in rolls_raw:
        if p in HEADS:
            cur = {"head": p.rstrip("."), "items": []}
            rolls.append(cur)
            continue
        for item in re.split(r"(?<=\.) (?=The |John |Three |Mustafa |Fergat|Soliman|Giambelat|Musafer|Ferca)", p):
            item = item.strip()
            if not item:
                continue
            item = re.sub(r"^Te lord", "The lord", item)
            item = re.sub(r"^cle Earle", "The Earle", item)
            if item[0].islower():
                item = "The " + item
            item = re.sub(r"^Ustafa", "Mustafa", item)
            item = re.sub(r" \[David Noce\.$", "", item)
            item = re.sub(r"successour to the captaine The captaine Tiberio",
                          "successour to the captaine David Noce.\nThe captaine Tiberio", item)
            cur["items"].append(item)
    roll_units = [unit(r["head"] + "\n" + "\n".join(r["items"]), list=True) for r in rolls]

    sections = [
        {"id": "dedication", "titel": "Malim to the Earl of Leicester", "zk": "Fam. Ded.",
         "blurb": "The translator's dedication, London, March 1572: monuments of stone decay, but letters committed to the printing press let men live for ever. Then the losses: Rhodes, Chios, and now Famagusta.",
         "units": [title] + ded},
        {"id": "cyprus", "titel": "A briefe description of the Iland of Cyprus", "zk": "Fam. Cyp.",
         "blurb": "Malim's own sketch of the island and of the titles to it: Lusignan, Venice by the adoption of Caterina Cornaro, and Selim's claim through the conquered Sultan of Egypt.",
         "units": cyp},
        {"id": "reader", "titel": "To the Reader", "zk": "Fam. Rdr.",
         "blurb": "The translator on the difficulty of turning Italian into English, with his translation 'precisely tied to mine authours meaning'.",
         "units": rdr},
        {"id": "precatio", "titel": "In Turchas precatio", "zk": "Fam. Prec.",
         "blurb": "Malim's Latin prayer against the Turks, in thirteen couplets, with a working translation. Written in March 1572, it already prays for the covenant the Christian monarchs have struck: the Holy League.",
         "units": pre},
        {"id": "report", "titel": "The true report of all the successe of Famagusta", "zk": "Fam. Rep.",
         "blurb": "Nestore Martinengo's report to the Doge: the siege from February to August 1571, the six assaults, the surrender on terms, the killing of the commanders in Mustafa's tent, the flaying of Bragadin, and the author's own escape from slavery in a fishing boat.",
         "units": rep},
        {"id": "rolls", "titel": "The rolls of the dead and the enslaved", "zk": "Fam. Rolls",
         "blurb": "The lists that close the report: the Christian captains slain, the captains made slaves, the fortifiers, and the Turkish commanders at Famagusta.",
         "units": roll_units},
    ]

    for s in sections:
        for i, x in enumerate(s["units"]):
            x["n"] = i + 1

    doc = {
        "id": "famagusta",
        "titel": "The Loss of Famagusta, 1571",
        "autor": "Nestore Martinengo; William Malim (translator)",
        "jahr": "1572",
        "sprache": "en",
        "orig_sprache": "la",
        "zk": "Fam.",
        "quelle": "Nestore Martinengo, The true report of all the successe of Famagusta, Englished out of Italian by William Malim (London, 1572), as reprinted in Richard Hakluyt, The Principal Navigations, vol. V (Glasgow: James MacLehose and Sons, 1904), pp. 117–152; Internet Archive principalnavigat0005unse (report's first page collated with principalnavigat05hakl).",
        "hinweis": "Spelling is Hakluyt's of 1599 as MacLehose reprinted it. The Latin prayer is transcribed from the page image; its English is this site's working translation (CC0). Malim's side notes are given as notes to the paragraphs they stand beside; the running heads, dates in the margin and folio references to the 1599 edition are omitted. The rolls are printed as lists. A Venetian officer's report, translated by an English protestant who had been to Constantinople: both the Ottoman and the Venetian side of the siege are seen from inside the walls.",
        "sections": sections,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    total = sum(len(s["units"]) for s in sections)
    print(f"famagusta.json: {len(sections)} sections, {total} units")
    for s in sections:
        print(" ", s["id"], len(s["units"]))


if __name__ == "__main__":
    main()
