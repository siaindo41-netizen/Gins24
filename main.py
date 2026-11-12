"""news-summary-01 entry: write the summary of 11 November 2026 world news
to /output/entry.txt. Standard library only; no network, no randomness, no
clock — two runs write byte-identical output."""

import os
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(HERE, "summary.txt"), "rb") as f:
    data = f.read()

if not 1000 <= len(data.decode("utf-8")) <= 2000:
    raise SystemExit("summary out of bounds (need 1000-2000 characters)")

os.makedirs(OUT_DIR, exist_ok=True)
out_path = os.path.join(OUT_DIR, "entry.txt")
# Write atomically: a crash mid-write must never leave a partial entry.txt.
fd, tmp_path = tempfile.mkstemp(dir=OUT_DIR, prefix=".entry.", suffix=".tmp")
try:
    with os.fdopen(fd, "wb") as f:
        f.write(data)
    with open(tmp_path, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("entry bytes do not match summary.txt")
    os.replace(tmp_path, out_path)
except BaseException:
    try:
        os.unlink(tmp_path)
    except OSError:
        pass
    raise
