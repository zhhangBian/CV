#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "$0")"

if ! command -v latexmk >/dev/null 2>&1; then
  echo "Error: latexmk is not installed." >&2
  exit 1
fi

mkdir -p build

if [[ "$#" -eq 0 ]]; then
  TARGETS=(cv.tex cv_en.tex)
else
  TARGETS=("$@")
fi

for TARGET in "${TARGETS[@]}"; do
  if [[ ! -f "$TARGET" ]]; then
    echo "Error: TeX file not found: $TARGET" >&2
    exit 1
  fi

  latexmk -xelatex -outdir=build "$TARGET"
  PDF_PATH="build/${TARGET%.tex}.pdf"
  echo "Built: $PDF_PATH"
done
