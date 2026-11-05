#!/bin/sh
# Export one 2560x1440 PNG per slide (build/png/slide.001.png ...), to paste into any deck.

set -e

PNG_DIR="${PNG_DIR:-build/png}"

if command -v marp > /dev/null 2>&1; then
    MARP_CMD="marp"
elif [ -x ./node_modules/.bin/marp ]; then
    MARP_CMD="./node_modules/.bin/marp"
else
    MARP_CMD="npx --yes @marp-team/marp-cli@4.1.2"
fi

mkdir -p build
rm -rf "${PNG_DIR}"
mkdir -p "${PNG_DIR}"

${MARP_CMD} --images png --image-scale 2 --html --allow-local-files --no-stdin \
    slides.md -o "${PNG_DIR}/slide.png" --theme-set themes

echo "✅ PNGs: ${PNG_DIR}/ ($(ls "${PNG_DIR}" | wc -l) files)"
