"""Compute popularity scores and generate README.md + docs/books.json from data/books.json.

Score (the "Translation Popularity Index", TPI):

    TPI = L + W * sum(log2(k) for every target language with k translations)

  L  - number of languages the book has been translated into
  k  - number of *distinct* translations into one language
  W  - weight of retranslations (default 25)

A single translation into a language adds 1 point (via L). Each *doubling* of
the number of translations into the same language adds W more points, so
retranslations dominate: 2 English translations = +25, 4 = +50, 8 = +75 ...
"""
import json
import math
from collections import defaultdict
from pathlib import Path

W = 25
ROOT = Path(__file__).parent


def score(book, w=W):
    return round(book["langs"] + w * sum(math.log2(k) for k in book["multi"].values() if k > 1))


def fmt_year(y):
    return f"{-y} BC" if y < 0 else str(y)


def fmt_multi(multi):
    items = sorted(multi.items(), key=lambda kv: -kv[1])
    return ", ".join(f"{lang} ×{k}" for lang, k in items if k > 1) or "—"


def main():
    books = json.loads((ROOT / "data" / "books.json").read_text(encoding="utf-8"))
    for b in books:
        b["score"] = score(b)
        b["retranslations"] = sum(k - 1 for k in b["multi"].values() if k > 1)
    books.sort(key=lambda b: -b["score"])
    for i, b in enumerate(books, 1):
        b["rank"] = i

    (ROOT / "docs" / "books.json").write_text(
        json.dumps({"weight": W, "books": books}, ensure_ascii=False, indent=1), encoding="utf-8")

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
        "**Interactive site:** https://levnach.github.io/books/ (filter, search, sort, tune the score weight)",
        "",
        "## The score — Translation Popularity Index (TPI)",
        "",
        "```",
        f"TPI = L + {W} × Σ log2(k)",
        "```",
        "",
        "* **L** — number of languages the book is translated into.",
        "* **k** — number of distinct translations into the same language (summed over every language with k ≥ 2).",
        "",
        f"Multiple translations into the same language count very high: every *doubling* of translations "
        f"in one language is worth {W} extra languages. Two English translations add {W}; four add {2*W}; eight add {3*W}.",
        "",
        "> Counts are curated, rounded estimates (from publishers, Index Translationum, Wikipedia and "
        "translation bibliographies). They are meant for ranking, not as exact bibliographic data. "
        "Corrections are welcome — edit `data/books.json` and run `python build.py`.",
        "",
        "## Top 20 overall",
        "",
        "| # | Book | Author | Genre | Languages | Retranslations | TPI |",
        "|---|------|--------|-------|----------:|----------------|----:|",
    ]
    for b in books[:20]:
        out.append(f"| {b['rank']} | {b['title']} | {b['author']} | {b['genre']} | {b['langs']} | "
                   f"{fmt_multi(b['multi'])} | **{b['score']}** |")
    out += ["", "## By genre", ""]
    out += [f"* [{g}](#{g.lower().replace(' & ', '--').replace(' ', '-').replace(chr(39), '')}) ({len(by_genre[g])})"
            for g in genres]
    for g in genres:
        out += ["", f"### {g}", "",
                "| # | Book | Author | Year | Original | Languages | Retranslations | TPI |",
                "|---|------|--------|------|----------|----------:|----------------|----:|"]
        for b in by_genre[g]:
            out.append(f"| {b['rank']} | {b['title']} | {b['author']} | {fmt_year(b['year'])} | {b['orig']} | "
                       f"{b['langs']} | {fmt_multi(b['multi'])} | **{b['score']}** |")
    out += ["", "## Rebuild", "", "```", "python build.py", "```", ""]
    (ROOT / "README.md").write_text("\n".join(out), encoding="utf-8")
    print(f"{len(books)} books, {len(genres)} genres")


if __name__ == "__main__":
    main()
