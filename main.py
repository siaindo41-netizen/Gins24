"""news-summary-01 entry: write the summary of 11 November 2026 world news
to /output/entry.txt. Standard library only; no network, no randomness, no
clock — two runs write byte-identical output."""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(HERE, "summary.txt"), "r", encoding="utf-8") as f:
    text = f.read()

os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(text)
