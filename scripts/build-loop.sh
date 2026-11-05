#!/bin/sh
# Build a self-contained, auto-advancing HTML deck for the booth screen.
# Output: build/booth-loop/index.html (+ assets). Open it fullscreen or with
#   chromium --kiosk "file://$PWD/build/booth-loop/index.html?interval=10"

set -e

OUT_DIR="${OUT_DIR:-build/booth-loop}"
mkdir -p "${OUT_DIR}"

if command -v marp > /dev/null 2>&1; then
    MARP_CMD="marp"
elif [ -x ./node_modules/.bin/marp ]; then
    MARP_CMD="./node_modules/.bin/marp"
else
    MARP_CMD="npx --yes @marp-team/marp-cli@4.1.2"
fi

${MARP_CMD} --html --allow-local-files --no-stdin slides.md \
    -o "${OUT_DIR}/index.html" --theme-set themes \
    --bespoke.osc=false --bespoke.transition=false

# Ship the assets next to the HTML so the folder can be copied to the kiosk.
rm -rf "${OUT_DIR}/assets"
cp -r assets "${OUT_DIR}/assets"

# Inline the autoplay script just before </body>.
python3 - "${OUT_DIR}/index.html" scripts/autoplay.js <<'PY'
import sys
html_path, js_path = sys.argv[1:3]
html = open(html_path, encoding="utf-8").read()
js = open(js_path, encoding="utf-8").read()
html = html.replace("</body>", "<script>" + js + "</script></body>", 1)
open(html_path, "w", encoding="utf-8").write(html)
PY

echo "✅ Booth loop ready: ${OUT_DIR}/index.html"
