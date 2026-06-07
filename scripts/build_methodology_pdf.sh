#!/usr/bin/env bash
# Build METHODOLOGY.pdf from METHODOLOGY.md via Pandoc + XeLaTeX.
#
# This is the "credibility artifact" build — produces a clean PDF suitable
# for sharing with peers / publishing alongside the framework. The PDF
# itself is gitignored (output artifact); regenerate on demand from the
# source markdown.
#
# DEPENDENCIES (NOT installed automatically — install once, then re-run):
#   macOS:   brew install pandoc basictex
#            sudo tlmgr update --self && sudo tlmgr install collection-fontsrecommended
#            # (basictex is the minimal TeX install; tlmgr fetches missing packages)
#   Linux:   sudo apt install pandoc texlive-xetex texlive-fonts-recommended
#   Verify:  pandoc --version    (≥ 2.x)
#            xelatex --version
#
# OUTPUT:    METHODOLOGY.pdf at project root
# RUN FROM:  any directory (script auto-locates project root via its own path)
#
# Design choices:
#   - XeLaTeX engine (handles Unicode glyphs in the document — bullets,
#     arrows, ⚑, ⟵, em-dashes — without escape gymnastics).
#   - Section numbering ON (--number-sections) so cross-references inside
#     the document survive the markdown → PDF transition.
#   - Table of contents (--toc) with depth 3 so §11.5 product-sector
#     subsections show up.
#   - Title page metadata via --metadata block (title / subtitle / date).
#   - Geometry: letter paper, 1in margins — standard for a research doc.

set -euo pipefail

# Locate project root (this script lives at <root>/scripts/)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "${SCRIPT_DIR}/.." && pwd )"
cd "${PROJECT_ROOT}"

# --- Dependency check -------------------------------------------------------
if ! command -v pandoc >/dev/null 2>&1; then
    cat <<'EOF' >&2
ERROR: pandoc is not installed.

Install instructions:
  macOS:   brew install pandoc basictex
  Linux:   sudo apt install pandoc texlive-xetex texlive-fonts-recommended

Then re-run this script.
EOF
    exit 1
fi

if ! command -v xelatex >/dev/null 2>&1; then
    cat <<'EOF' >&2
ERROR: xelatex is not installed (Pandoc needs a LaTeX engine for PDF output).

Install instructions:
  macOS:   brew install basictex
           sudo tlmgr update --self
           sudo tlmgr install collection-fontsrecommended
  Linux:   sudo apt install texlive-xetex texlive-fonts-recommended

Then re-run this script.
EOF
    exit 1
fi

# --- Build ------------------------------------------------------------------
SOURCE="METHODOLOGY.md"
OUTPUT="METHODOLOGY.pdf"
VERSION_DATE="$(date -u +%Y-%m-%d)"

if [[ ! -f "${SOURCE}" ]]; then
    echo "ERROR: ${SOURCE} not found in ${PROJECT_ROOT}" >&2
    exit 1
fi

echo "Building ${OUTPUT} from ${SOURCE}..."
echo "  project root: ${PROJECT_ROOT}"
echo "  version date: ${VERSION_DATE}"

# Pandoc invocation. Flags explained:
#   --from gfm+yaml_metadata_block  : parse as GitHub-flavored markdown
#   --pdf-engine=xelatex             : Unicode-friendly engine
#   --toc --toc-depth=3              : 3-level table of contents
#   --number-sections                : keep §1, §2.3, §11.5 numbering
#   --metadata title:...             : title page block
#   -V geometry:...                  : letter paper, 1in margins
#   -V colorlinks=true               : clickable cross-references
#   -V linkcolor:NavyBlue            : muted link colour (not bright blue)
pandoc "${SOURCE}" \
    --from gfm+yaml_metadata_block \
    --pdf-engine=xelatex \
    --toc --toc-depth=3 \
    --number-sections \
    --metadata title:"Tanker & Gas-Carrier Fair Value Tool" \
    --metadata subtitle:"Methodology" \
    --metadata author:"crude-tanker-fv" \
    --metadata date:"Compiled ${VERSION_DATE}" \
    -V geometry:"paperwidth=8.5in,paperheight=11in,margin=1in" \
    -V colorlinks=true \
    -V linkcolor:NavyBlue \
    -V urlcolor:NavyBlue \
    -V mainfont:"Helvetica Neue" \
    -V monofont:"Menlo" \
    -o "${OUTPUT}"

echo "✓ Generated ${PROJECT_ROOT}/${OUTPUT}"
ls -lh "${OUTPUT}"
