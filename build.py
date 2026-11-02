"""Compute popularity scores and generate README.md + docs/books.json from data/books.json.

Score (the "Translation Popularity Index", TPI):

    TPI = (L + W * sum(log2(k) for every target language with k translations)) * R

  L  - number of languages the book has been translated into
  k  - number of *distinct* translations into one language
  W  - weight of retranslations (default 25)
  R  - recency boost: 1 + B for books first published in 1950 or later (B = 0.5), else 1

A single translation into a language adds 1 point (via L). Each *doubling* of
the number of translations into the same language adds W more points, so
retranslations dominate: 2 English translations = +25, 4 = +50, 8 = +75 ...
"""
import json
import math
import urllib.parse
from collections import defaultdict
from pathlib import Path

W = 25
BOOST = 1.0
MODERN = 1950
ROOT = Path(__file__).parent


def score(book, w=W, boost=BOOST):
    base = book["langs"] + w * sum(math.log2(k) for k in book["multi"].values() if k > 1)
    return round(base * (1 + boost if book["year"] >= MODERN else 1))


def load_links():
    """Merge data/links.json (found by links.py) with hand-made data/links_overrides.json."""
    links = {}
    for name in ("links.json", "links_overrides.json"):
        f = ROOT / "data" / name
        if f.exists():
            for title, d in json.loads(f.read_text(encoding="utf-8")).items():
                links.setdefault(title, {}).update(d)
    return links


def free_links(found):
    """Turn cached source matches into download links: [{lang, fmt, src, url}]."""
    out = []
    for lang in ("en", "ru"):
        g = found.get(f"gutenberg_{lang}")
        if g:
            out.append({"lang": lang, "fmt": "EPUB", "src": "Project Gutenberg",
                        "url": f"https://www.gutenberg.org/ebooks/{g['id']}.epub3.images"})
            out.append({"lang": lang, "fmt": "Read", "src": "Project Gutenberg",
                        "url": f"https://www.gutenberg.org/ebooks/{g['id']}"})
        w = found.get(f"wikisource_{lang}")
        if w:
            page = urllib.parse.quote(w.replace(" ", "_"))
            for fmt, ws_fmt in (("EPUB", "epub-3"), ("PDF", "pdf-a4")):
                out.append({"lang": lang, "fmt": fmt, "src": "Wikisource",
                            "url": f"https://ws-export.wmcloud.org/?lang={lang}&page={page}&format={ws_fmt}"})
            out.append({"lang": lang, "fmt": "Read", "src": "Wikisource",
                        "url": f"https://{lang}.wikisource.org/wiki/{page}"})
    # keep the first link per (lang, fmt): Gutenberg wins over Wikisource
    seen, uniq = set(), []
    for l in out:
        if (l["lang"], l["fmt"]) not in seen:
            seen.add((l["lang"], l["fmt"]))
            uniq.append(l)
    return uniq


def md_links(links):
    return " ".join(f"[{l['lang'].upper()}·{l['fmt']}]({l['url']})" for l in links if l["fmt"] != "Read") or "—"


def fmt_year(y):
    return f"{-y} BC" if y < 0 else str(y)


def fmt_multi(multi):
    items = sorted(multi.items(), key=lambda kv: -kv[1])
    return ", ".join(f"{lang} ×{k}" for lang, k in items if k > 1) or "—"


def main():
    books = json.loads((ROOT / "data" / "books.json").read_text(encoding="utf-8"))
    links = load_links()
    for b in books:
        b["score"] = score(b)
        b["free"] = free_links(links.get(b["title"], {}))
        b["retranslations"] = sum(k - 1 for k in b["multi"].values() if k > 1)
    books.sort(key=lambda b: -b["score"])
    for i, b in enumerate(books, 1):
        b["rank"] = i

    (ROOT / "docs" / "books.json").write_text(
        json.dumps({"weight": W, "boost": BOOST, "modern": MODERN, "books": books}, ensure_ascii=False, indent=1), encoding="utf-8")

    by_genre = defaultdict(list)
    for b in books:
        by_genre[b["genre"]].append(b)
    genres = sorted(by_genre, key=lambda g: -max(b["score"] for b in by_genre[g]))

    out = [
        "# Translated Audiobooks",
        "",
        "Books that (1) have an **audiobook** edition, (2) have an **English** edition, and "
        "(3) are translated into **at least 3 languages** — grouped by genre and ranked by an invented "
        "popularity counter.",
        "",
        "**Interactive site:** https://levnach.github.io/books/ (filter, search, sort, tune the score, free e-book links)",
        "",
        "## The score — Translation Popularity Index (TPI)",
        "",
        "```",
        f"TPI = (L + {W} × Σ log2(k)) × R",
        "```",
        "",
        "* **L** — number of languages the book is translated into.",
        "* **k** — number of distinct translations into the same language (summed over every language with k ≥ 2).",
        f"* **R** — recency boost: ×{1 + BOOST:g} for books first published in {MODERN} or later, ×1 otherwise. "
        "Newer books have had less time to be retranslated, so they get a head start.",
        "",
        f"Multiple translations into the same language count very high: every *doubling* of translations "
        f"in one language is worth {W} extra languages. Two English translations add {W}; four add {2*W}; eight add {3*W}.",
        "",
        "> Counts are curated, rounded estimates (from publishers, Index Translationum, Wikipedia and "
        "translation bibliographies). They are meant for ranking, not as exact bibliographic data. "
        "Corrections are welcome — edit `data/books.json` and run `python build.py`.",
        "",
        "## Free e-books",
        "",
        "The **Free** column links to legal, public-domain copies only: "
        "[Project Gutenberg](https://www.gutenberg.org) (EPUB) and [Wikisource](https://wikisource.org) "
        "(EPUB / PDF generated by [WS Export](https://ws-export.wmcloud.org)), in English (EN) and Russian (RU). "
        "Books still under copyright have no free links. "
        f"{sum(1 for b in books if b['free'])} of {len(books)} books have at least one link "
        f"({sum(1 for b in books if any(l['lang'] == 'ru' for l in b['free']))} in Russian).",
        "",
        "## Top 20 overall",
        "",
        "| # | Book | Author | Genre | Languages | Retranslations | TPI | Free |",
        "|---|------|--------|-------|----------:|----------------|----:|------|",
    ]
    for b in books[:20]:
        out.append(f"| {b['rank']} | {b['title']} | {b['author']} | {b['genre']} | {b['langs']} | "
                   f"{fmt_multi(b['multi'])} | **{b['score']}** | {md_links(b['free'])} |")
    out += ["", "## By genre", ""]
    out += [f"* [{g}](#{g.lower().replace(' & ', '--').replace(' ', '-').replace(chr(39), '')}) ({len(by_genre[g])})"
            for g in genres]
    for g in genres:
        out += ["", f"### {g}", "",
                "| # | Book | Russian title | Author | Year | Original | Languages | Retranslations | TPI | Free |",
                "|---|------|---------------|--------|------|----------|----------:|----------------|----:|------|"]
        for b in by_genre[g]:
            out.append(f"| {b['rank']} | {b['title']} | {b['ru']} | {b['author']} | {fmt_year(b['year'])} | {b['orig']} | "
                       f"{b['langs']} | {fmt_multi(b['multi'])} | **{b['score']}** | {md_links(b['free'])} |")
    out += ["", "## Rebuild", "", "```", "python links.py   # find free e-book links (cached in data/links.json)",
            "python build.py   # scores, README, site data", "```", ""]
    (ROOT / "README.md").write_text("\n".join(out), encoding="utf-8")
    print(f"{len(books)} books, {len(genres)} genres")


if __name__ == "__main__":
    main()
