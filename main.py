"""news-summary-01 entry: write the summary of 11 November 2026 world news
to /output/entry.txt. Standard library only; no network, no randomness, no
clock — two runs write byte-identical output.

The write must be a plain open(out_path, "wb"): the sandbox grader reads
entry.txt as a different user, so the file must be world-readable (mode 0644
via umask). An atomic temp-file write (tempfile.mkstemp) creates mode 0600,
which made v2 fail in the sandbox with "entry.txt is not readable"."""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(HERE, "summary.txt"), "rb") as f:
    data = f.read()

try:
    text = data.decode("utf-8")
except UnicodeDecodeError:
    raise SystemExit("summary.txt is not valid UTF-8")
if not 1000 <= len(text) <= 2000:
    raise SystemExit(f"summary out of bounds: {len(text)} characters (need 1000-2000)")

os.makedirs(OUT_DIR, exist_ok=True)
out_path = os.path.join(OUT_DIR, "entry.txt")
with open(out_path, "wb") as f:
    f.write(data)
# Guarantee world-readable output regardless of the runtime umask: the
# sandbox grader reads entry.txt as a different user. (This VM's umask is
# 0007, so a plain open() alone yields 0660 here.)
os.chmod(out_path, 0o644)
