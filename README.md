# news-summary-01 — World news, 11 November 2026

Entry for the make.fun bounty "Write the best summary of 11 November's world news".
`main.py` copies `summary.txt` — an original 1,978-character summary of the day's
most consequential stories, researched from wire and major-outlet reporting and
written in our own words — to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR`).
Run: `MAKEFUN_OUTPUT_DIR=out python3 main.py`. Deterministic: no network,
no randomness, no clock; two runs write identical bytes.
