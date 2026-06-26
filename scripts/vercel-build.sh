#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

bash scripts/minify-css.sh

rm -rf public
mkdir -p public

copy_if_exists() {
  for path in "$@"; do
    if [ -e "$path" ]; then
      cp -R "$path" public/
    fi
  done
}

copy_if_exists \
  index.html \
  css \
  js \
  images \
  blog \
  faaliyet-alanlari \
  favicon.ico \
  favicon.svg \
  favicon-16.png \
  favicon-32.png \
  favicon-48.png \
  favicon-96.png \
  favicon-180.png \
  favicon-192.png \
  favicon-512.png \
  site.webmanifest \
  robots.txt \
  sitemap.xml \
  logo.png \
  .htaccess

for file in *.html; do
  [ -f "$file" ] || continue
  cp "$file" public/
done

echo "Vercel public/ klasörü hazır."
