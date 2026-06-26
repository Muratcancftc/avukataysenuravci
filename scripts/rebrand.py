#!/usr/bin/env python3
"""Bulk rebrand: Murat Can -> AV. AYŞENUR AVCI HUKUK BÜROSU."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = "https://avukataysenuravci.com"
SITE_HOST = "avukataysenuravci.com"
OLD_HOST = "avukatmuratcan.com.tr"

GLOBS = ("*.html", "*.php", "*.py", "*.js", "*.md", ".htaccess", "robots.txt", "package.json")
SKIP_DIRS = {".git", "node_modules", ".cursor", "__pycache__", "adsız klasör"}

REPLACEMENTS = [
    ("https://www.avukatmuratcan.com.tr", SITE_URL),
    ("http://www.avukatmuratcan.com.tr", SITE_URL),
    ("https://avukatmuratcan.com.tr", SITE_URL),
    ("http://avukatmuratcan.com.tr", SITE_URL),
    ("www.avukatmuratcan.com.tr", f"www.{SITE_HOST}"),
    ("avukatmuratcan.com.tr", SITE_HOST),
    ("MURAT CAN HUKUK BÜROSU", "AV. AYŞENUR AVCI HUKUK BÜROSU"),
    ("Murat Can Hukuk ve Danışmanlık", "AV. AYŞENUR AVCI HUKUK BÜROSU"),
    ("Murat Can Hukuk Bürosu", "AV. AYŞENUR AVCI HUKUK BÜROSU"),
    ("Murat Can Hukuk", "AV. AYŞENUR AVCI Hukuk"),
    ("Murat Can Law Firm", "Ayşenur Avcı Law Firm"),
    ("Kanzlei Murat Can", "Kanzlei Ayşenur Avcı"),
    ("Cabinet d'avocats Murat Can", "Cabinet d'avocats Ayşenur Avcı"),
    ("Юридическая фирма Murat Can", "Юридическая фирма Ayşenur Avcı"),
    ("مكتب مراد كان للمحاماة", "مكتب أيشينور أفجي للمحاماة"),
    ("Murat Can Hukuk Asistanı", "Ayşenur Avcı Hukuk Asistanı"),
    ('Sen "Murat Can Hukuk Asistanı"sın', 'Sen "Ayşenur Avcı Hukuk Asistanı"sın'),
    ("Murat Can", "Av. Ayşenur Avcı"),
]


def iter_files() -> list[Path]:
    files: list[Path] = []
    for pattern in GLOBS:
        for path in ROOT.glob(pattern):
            if path.is_file():
                files.append(path)
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix in {".html", ".php", ".py", ".js", ".md"} or path.name in {".htaccess", "robots.txt", "package.json", "sitemap.xml"}:
            if path not in files:
                files.append(path)
    return sorted(set(files))


def rebrand_text(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text


def main() -> None:
    changed = 0
    for path in iter_files():
        if path.name == "rebrand.py":
            continue
        original = path.read_text(encoding="utf-8", errors="replace")
        updated = rebrand_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"updated: {path.relative_to(ROOT)}")
    print(f"Done. {changed} files updated.")


if __name__ == "__main__":
    main()
