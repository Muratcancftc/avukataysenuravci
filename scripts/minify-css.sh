#!/bin/bash
# CSS minify - style.css güncellendiğinde çalıştırın
# Kullanım: ./scripts/minify-css.sh
cd "$(dirname "$0")/.."
npx --yes clean-css-cli -o css/style.min.css css/style.css
echo "style.min.css güncellendi."
