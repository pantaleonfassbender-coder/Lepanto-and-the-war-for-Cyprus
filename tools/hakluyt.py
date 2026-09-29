"""Shared reader for the MacLehose edition of Hakluyt's Principal Navigations
(Glasgow 1903-05), from the Internet Archive's OCR text.

The OCR runs page by page: body lines, the page number at the foot, the
running head ("THE ENGLISH VOYAGES" / a section title), the year in the outer
margin, folio references to the 1599 edition ("[II. i. 118.]"), and the side
notes as a block of narrow lines. Blank lines are unreliable: they appear
inside paragraphs as well as between them.
"""
import re
import urllib.request
from pathlib import Path

SRC = Path(__file__).resolve().parent / "src"


def fetch(ident):
    SRC.mkdir(exist_ok=True)
    p = SRC / f"{ident}_djvu.txt"
    if not p.exists():
        url = f"https://archive.org/download/{ident}/{ident}_djvu.txt"
        with urllib.request.urlopen(url) as r:
            p.write_bytes(r.read())
    return p.read_text(encoding="utf-8").split("\n")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


FOLIO = re.compile(r"[\[(]\s*I[IlL1r]+\.?\s*[i1]\.?\s*[\dIl]{2,3}[\s.;:,]*[\])]")
PAGENO = re.compile(r"^\s*[vV]?\s*[\dIl]{3}\s*[;:,.]?\s*[A-Z]?\s*$")
HEAD = re.compile(r"^\s*(A\.?\s*D[\.,]?\s*)?THE\s+(ENGLISH\s+V\^?OYAGES|LOSS\s+OF\s+FAMAGUSTA)\b.{0,8}$", re.I)
YEARISH = re.compile(r"^\s*(A\.?\s*D[\.,]?|[I1l]\s*5\s*[7I4]\s*[I1l][\.,]?|1571[\.,-]?)\s*$")
BODY_MIN = 38


def body_lines(lines):
    """Body lines with page furniture removed. After a page number the side
    notes follow; they are skipped until the running head, or until a line
    long enough to be body text (a misread head must not swallow a page)."""
    skipping = False
    for raw in lines:
        s = norm(raw)
        if not s:
            continue
        if PAGENO.match(s):
            skipping = True
            continue
        if HEAD.match(s):
            skipping = False
            continue
        if skipping and len(s) < BODY_MIN:
            continue
        skipping = False
        if YEARISH.match(s):
            continue
        s = norm(FOLIO.sub("", s))
        if s:
            yield s


def paragraphs(lines, headings=(), full=46):
    """Join lines into paragraphs. A paragraph ends where a line closes a
    sentence and falls short of the full measure, or at a known heading."""
    paras, cur = [], ""
    heads = set(headings)

    def flush():
        nonlocal cur
        if cur:
            paras.append(re.sub(r"\s+([,;:.!?)])", r"\1", cur))
        cur = ""

    for s in lines:
        if s in heads:
            flush()
            paras.append(s)
            continue
        if cur.endswith("-") and not cur.endswith("--"):
            cur = cur[:-1] + s
        else:
            cur = (cur + " " + s).strip()
        if re.search(r"[.:?!]\)?$", s) and len(s) < full:
            flush()
    flush()
    return paras
