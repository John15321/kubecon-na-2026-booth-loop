#!/bin/sh
# Export the deck for PowerPoint users.
#   build/png/slide.001.png ...   one 2560x1440 PNG per slide (paste into any deck)
#   build/slides.pptx             PowerPoint file, one full-slide image per slide,
#                                 with the Marp notes as PowerPoint speaker notes

set -e

PNG_DIR="${PNG_DIR:-build/png}"
PPTX="${PPTX:-build/slides.pptx}"

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
${MARP_CMD} --pptx --html --allow-local-files --no-stdin \
    slides.md -o "${PPTX}" --theme-set themes

echo "✅ PNGs: ${PNG_DIR}/ ($(ls "${PNG_DIR}" | wc -l) files)"
echo "✅ PowerPoint: ${PPTX} ($(ls -lh "${PPTX}" | awk '{print $5}'))"
