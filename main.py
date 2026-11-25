"""Write one funny tech-support line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line is a hopeless support agent's cheerfully useless reply to a
desperate customer; it is written exactly as stored in LINE, one line,
under 200 characters, so the sealed gate scorer accepts it.

Reads no environment variable except MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import sys

LINE = (
    "Don't worry, this is a known issue \u2014 "
    "known to everyone except me, your support agent."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Runtime guard: never ship an entry the gate would refuse. A line that is
# empty or 200+ characters fails the sealed scorer outright, so fail loudly
# here instead of writing an invalid artifact.
if not 1 <= len(LINE) <= 199 or not LINE.strip():
    print(f"entry invalid: {len(LINE)} chars", file=sys.stderr)
    sys.exit(1)

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
