"""Find free, legal (public-domain) e-book sources for every book and cache them in data/links.json.

Sources:
  * Project Gutenberg (offline catalog, cached in .cache/) - EPUB, mostly English
  * Wikisource (en, ru)                                    - EPUB / PDF through the WS Export tool

Only books old enough to be in the public domain somewhere are searched (year < 1930,
or Russian originals before 1960). Results are heuristic matches; fix wrong ones in
data/links_overrides.json (same shape as links.json, a null value removes a link).

Usage:  python links.py            # search books missing from the cache
        python links.py --refresh  # search everything again
"""
import csv
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
CACHE = ROOT / "data" / "links.json"
UA = "levnach-books/1.0 (https://github.com/levnach/books)"
CATALOG = ROOT / ".cache" / "pg_catalog.csv"
CATALOG_URL = "https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv"


def get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.loads(r.read().decode("utf-8"))
            if "error" in data and "busy" in str(data["error"]):
                raise RuntimeError("busy")
            return data
        except Exception as e:  # noqa: BLE001 - network is flaky, retry anything
            if i == tries - 1:
                print("   !", url, e)
                return {}
            time.sleep(3 * (i + 1))


def norm(s):
    s = unicodedata.normalize("NFKD", s.lower()).replace("ё", "е")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"^(the|a|an)\s+", "", s.strip())
    return " ".join(s.split())


def surname(author):
    a = re.sub(r"\(.*?\)", "", author).split("&")[0].strip()
    return "" if a in ("Various", "—", "Anonymous", "Buddhist canon") else a.split()[-1]


def load_catalog():
    if not CATALOG.exists():
        CATALOG.parent.mkdir(exist_ok=True)
        req = urllib.request.Request(CATALOG_URL, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=300) as r:
            CATALOG.write_bytes(r.read())
    with CATALOG.open(encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r["Type"] == "Text"]


def gutenberg(catalog, title, author, lang):
    """Lowest-numbered (usually the canonical) Gutenberg text whose title starts with `title` by `author`."""
    nt, na = norm(title), norm(author)[:5]  # surname prefix tolerates Dostoevsky / Dostoyevsky
    hits = [r for r in catalog if r["Language"] == lang and norm(re.split(r"[:;\n]", r["Title"])[0]) == nt
            and (not na or na in norm(r["Authors"]))]
    if not hits:  # allow subtitles / "Complete" etc.
        hits = [r for r in catalog if r["Language"] == lang and norm(r["Title"]).startswith(nt)
                and (not na or na in norm(r["Authors"]))]
    if not hits:
        return None
    r = min(hits, key=lambda r: int(r["Text#"]))
    return {"id": int(r["Text#"]), "title": r["Title"][:80]}


def wikisource(lang, title, author):
    """Wikisource page whose base title (before the parenthetical) equals `title`.

    Russian pages are named "Title (Author; Translator)", so the author must appear in the
    parenthetical - this skips reviews such as "Герой нашего времени (Белинский)".
    English pages may also be "Title (1st edition)" etc.; film pages are skipped.
    """
    nt = norm(title)
    variants = {title, title.replace("ё", "е"), title.replace("е", "ё") if "ё" in title else title}
    pages = []
    for v in variants:
        data = get(f"https://{lang}.wikisource.org/w/api.php?" + urllib.parse.urlencode({
            "action": "query", "format": "json", "generator": "allpages", "gapprefix": v, "gapnamespace": 0,
            "gaplimit": 500, "gapfilterredir": "nonredirects", "prop": "pageprops|info", "ppprop": "disambiguation"}))
        pages += data.get("query", {}).get("pages", {}).values()
        time.sleep(1)
    best = None
    for p in pages:
        t = p["title"]
        if "/" in t or "disambiguation" in p.get("pageprops", {}) or re.search(r"film|Лэм|Lamb", t):
            continue
        base, _, paren = t.partition("(")
        if norm(base) != nt:
            continue
        has_author = bool(author) and author.lower().replace("ё", "е")[:5] in paren.lower().replace("ё", "е")
        if lang == "ru" and author and not has_author:
            continue
        if lang == "en" and paren and not has_author and not re.search(r"\d|edition|translation|version", paren, re.I):
            continue
        key = (has_author, p.get("length", 0))
        if best is None or key > best[0]:
            best = (key, t)
    return best[1] if best else None


def eligible(b):
    return b["year"] < 1930 or (b["orig"] == "Russian" and b["year"] < 1960)


def main():
    books = json.loads((ROOT / "data" / "books.json").read_text(encoding="utf-8"))
    cache = {} if "--refresh" in sys.argv or not CACHE.exists() else json.loads(CACHE.read_text(encoding="utf-8"))
    todo = [b for b in books if eligible(b) and b["title"] not in cache]
    catalog = load_catalog() if todo else []
    for i, b in enumerate(todo, 1):
        en_title = re.sub(r"\(.*?\)", "", b["title"]).strip()
        res = {
            "gutenberg_en": gutenberg(catalog, en_title, surname(b["author"]), "en"),
            "gutenberg_ru": gutenberg(catalog, b["ru"], "", "ru"),
            "wikisource_en": wikisource("en", en_title, surname(b["author"])),
            "wikisource_ru": wikisource("ru", b["ru"], b["ru_author"]),
        }
        cache[b["title"]] = res
        print(f"[{i}/{len(todo)}] {b['title']}: " + ", ".join(
            f"{k}={v['id'] if isinstance(v, dict) else v}" for k, v in res.items() if v), flush=True)
        CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")


if __name__ == "__main__":
    main()
