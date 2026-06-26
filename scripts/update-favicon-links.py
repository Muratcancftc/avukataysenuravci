#!/usr/bin/env python3
"""Normalize favicon link tags across all HTML pages."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FAVICON_BLOCK = """    <link rel="icon" href="/favicon.ico" sizes="48x48">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="/favicon-180.png">
    <link rel="manifest" href="/site.webmanifest">"""

OLD_PATTERNS = [
    """    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="apple-touch-icon" sizes="180x180" href="/favicon-180.png">""",
    """    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">""",
]


def main() -> None:
    updated = 0
    for path in ROOT.rglob("*.html"):
        if "public" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        new_text = text
        for pattern in OLD_PATTERNS:
            if pattern in new_text:
                new_text = new_text.replace(pattern, FAVICON_BLOCK, 1)
                break
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(path.relative_to(ROOT))
    print(f"Updated {updated} HTML files.")


if __name__ == "__main__":
    main()
