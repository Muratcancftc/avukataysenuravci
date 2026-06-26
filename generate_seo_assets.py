#!/usr/bin/env python3
"""Sync sitemap.xml, robots.txt, canonical and meta descriptions for all pages."""

from __future__ import annotations

import html
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

SITE_URL = "https://avukataysenuravci.com"
ROOT = Path(__file__).resolve().parent
EXCLUDED_DIRS = {".git", "node_modules", ".cursor", "__pycache__"}


def iter_html_files() -> list[Path]:
    files: list[Path] = []
    for file_path in ROOT.rglob("*.html"):
        if any(part in EXCLUDED_DIRS for part in file_path.parts):
            continue
        files.append(file_path)
    return sorted(files)


def public_path(file_path: Path) -> str:
    rel = file_path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    return f"/{rel}"


def absolute_url(file_path: Path) -> str:
    p = public_path(file_path)
    if p == "/":
        return SITE_URL + "/"
    encoded = quote(p, safe="/-._~")
    return SITE_URL + encoded


def squeeze_spaces(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def trim_to_limit(text: str, limit: int = 155) -> str:
    text = squeeze_spaces(text)
    if len(text) <= limit:
        return text
    clipped = text[: limit - 1]
    if " " in clipped:
        clipped = clipped.rsplit(" ", 1)[0]
    return clipped.rstrip(" ,;:-") + "."


def title_from_html(doc: str) -> str:
    title_match = re.search(r"<title>(.*?)</title>", doc, flags=re.IGNORECASE | re.DOTALL)
    if not title_match:
        return "Gebze Avukatlik Hizmetleri"
    title = re.sub(r"\s+", " ", title_match.group(1)).strip()
    title = re.sub(
        r"\s*\|\s*(AV. AYŞENUR AVCI Hukuk(?: Bürosu)?)\s*$",
        "",
        title,
        flags=re.IGNORECASE,
    ).strip()
    return title or "Gebze Avukatlik Hizmetleri"


def slug_label(file_path: Path) -> str:
    rel = file_path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "anasayfa"
    base = file_path.stem.replace("-", " ").replace("_", " ")
    return squeeze_spaces(base.lower())


def build_default_description(file_path: Path, title: str) -> str:
    path = file_path.relative_to(ROOT).as_posix()
    if path.startswith("blog/"):
        text = f"{title}: Gebze ve Kocaeli odakli guncel hukuki rehber ve uygulama bilgileri."
    elif path.startswith("faaliyet-alanlari/"):
        text = (
            f"{title}: Gebze merkezli avukatlik destegi, dava sureci yonetimi ve "
            "hukuki danismanlik hizmetleri."
        )
    elif path == "iletisim.html":
        text = "Gebze avukat iletisim: AV. AYŞENUR AVCI Hukuk Burosu adres, telefon ve randevu bilgileri."
    elif path == "makaleler.html":
        text = "Gebze avukatlik blogu: bosanma, is hukuku, kira ve tazminat konularinda guncel makaleler."
    else:
        text = f"{title}: Gebze ve Kocaeli bolgesinde hukuki danismanlik ve dava sureci destegi."
    return trim_to_limit(text, 155)


def upsert_canonical(doc: str, canonical_url: str) -> str:
    canonical_tag = f'<link rel="canonical" href="{canonical_url}">'
    if re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*>', doc, flags=re.IGNORECASE):
        return re.sub(
            r'<link[^>]+rel=["\']canonical["\'][^>]*>',
            canonical_tag,
            doc,
            count=1,
            flags=re.IGNORECASE,
        )
    return re.sub(r"</head>", f"    {canonical_tag}\n</head>", doc, count=1, flags=re.IGNORECASE)


def upsert_meta_description(doc: str, description: str) -> str:
    escaped = html.escape(description, quote=True)
    meta_tag = f'<meta name="description" content="{escaped}">'
    if re.search(r'<meta[^>]+name=["\']description["\'][^>]*>', doc, flags=re.IGNORECASE):
        return re.sub(
            r'<meta[^>]+name=["\']description["\'][^>]*>',
            meta_tag,
            doc,
            count=1,
            flags=re.IGNORECASE,
        )
    return re.sub(r"</head>", f"    {meta_tag}\n</head>", doc, count=1, flags=re.IGNORECASE)


def priority_and_changefreq(file_path: Path) -> tuple[str, str]:
    rel = file_path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "1.0", "weekly"
    if rel.startswith("blog/"):
        return "0.7", "monthly"
    if rel in {"makaleler.html", "hizmet-bolgelerimiz.html"}:
        return "0.9", "weekly"
    if rel.startswith("faaliyet-alanlari/"):
        return "0.8", "monthly"
    return "0.9", "monthly"


def write_sitemap(html_files: list[Path]) -> None:
    rows: list[str] = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for file_path in html_files:
        lastmod = file_path.stat().st_mtime
        lastmod_iso = datetime.fromtimestamp(lastmod).strftime("%Y-%m-%d")
        priority, changefreq = priority_and_changefreq(file_path)
        rows.append("  <url>")
        rows.append(f"    <loc>{absolute_url(file_path)}</loc>")
        rows.append(f"    <lastmod>{lastmod_iso}</lastmod>")
        rows.append(f"    <changefreq>{changefreq}</changefreq>")
        rows.append(f"    <priority>{priority}</priority>")
        rows.append("  </url>")
    rows.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(rows) + "\n", encoding="utf-8")


def write_robots() -> None:
    robots = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /node_modules/\n"
        "Disallow: /.git/\n"
        "\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n"
    )
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")


def sync_meta_and_canonical(html_files: list[Path]) -> None:
    used_descriptions: dict[str, int] = {}
    for file_path in html_files:
        original = file_path.read_text(encoding="utf-8")
        doc = original
        title = title_from_html(doc)

        existing_meta = re.search(
            r'<meta[^>]+name=["\']description["\'][^>]+content=(["\'])(.*?)\1',
            doc,
            flags=re.IGNORECASE | re.DOTALL,
        )
        description = squeeze_spaces(existing_meta.group(2)) if existing_meta else ""
        if not description or len(description) < 60:
            description = build_default_description(file_path, title)
        description = trim_to_limit(description, 155)

        key = description.lower()
        if key in used_descriptions:
            unique_suffix = f" ({slug_label(file_path)})"
            description = trim_to_limit(description[: 155 - len(unique_suffix)] + unique_suffix, 155)
            key = description.lower()
        used_descriptions[key] = used_descriptions.get(key, 0) + 1

        doc = upsert_meta_description(doc, description)
        doc = upsert_canonical(doc, absolute_url(file_path))

        if doc != original:
            file_path.write_text(doc, encoding="utf-8")


def main() -> None:
    html_files = iter_html_files()
    if not html_files:
        print("No HTML files found.")
        return
    sync_meta_and_canonical(html_files)
    write_sitemap(html_files)
    write_robots()
    print(f"Synced SEO assets for {len(html_files)} HTML files.")


if __name__ == "__main__":
    main()
