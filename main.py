"""Write one funny tech-support line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads no environment variable except MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

LINE = (
    "Don't worry, this is a known issue \u2014 "
    "known to everyone except me, your support agent."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
