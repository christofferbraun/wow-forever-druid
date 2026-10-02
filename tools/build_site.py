#!/usr/bin/env python3
"""Generate docs/index.md (the site homepage) from README.md.

README.md is the GitHub landing page. The site homepage needs the same content but
with links rewritten, because README sits at the repo root while index.md sits in
docs/. Generating one from the other keeps them from drifting.

    python tools/build_site.py
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "README.md")
DST = os.path.join(ROOT, "docs", "index.md")



def main():
    with open(SRC, encoding="utf-8") as f:
        text = f.read()

    # Drop any YAML front matter from the README.
    text = re.sub(r"\A---\n.*?\n---\n+", "", text, flags=re.S)

    # docs/foo.md -> foo.md   (links are relative to docs/ once inside index.md)
    text = re.sub(r"\]\(docs/([^)]+)\)", r"](\1)", text)

    front = "---\ntitle: Overview\n---\n\n"
    with open(DST, "w", encoding="utf-8", newline="\n") as f:
        f.write(front + text)

    print("wrote %s" % os.path.relpath(DST, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
