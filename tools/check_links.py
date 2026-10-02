#!/usr/bin/env python3
"""Validate every internal link and anchor, for BOTH renderers.

GitHub and MkDocs slugify headings differently, so this checks each heading
produces the same anchor under both rules and that every link resolves.

    python tools/check_links.py

Exits non-zero if anything is broken, so it works as a CI gate.
"""

import glob
import os
import re
import sys
import unicodedata

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def norm(p):
    return p.replace("\\", "/")


def gh_slug(t):
    """github-slugger: strip non word/space/hyphen, spaces to hyphens, no collapsing."""
    t = t.strip().lower()
    t = re.sub(r"[^\w\- ]", "", t, flags=re.U)
    return t.replace(" ", "-")


def md_slug(t):
    """python-markdown toc: ascii-fold, strip punctuation, collapse runs."""
    v = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode("ascii")
    v = re.sub(r"[^\w\s-]", "", v).strip().lower()
    return re.sub(r"[-\s]+", "-", v)


def headings_and_anchors(path):
    out, fence = set(), False
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("```"):
                fence = not fence
                continue
            if fence:
                continue
            m = re.match(r"^#{1,6}\s+(.*?)\s*$", line)
            if m:
                out.add(gh_slug(m.group(1)))
                out.add(md_slug(m.group(1)))
            for am in re.finditer(r'<a id="([^"]+)"', line):
                out.add(am.group(1))
    return out


def main():
    os.chdir(ROOT)
    files = ["README.md"] + sorted(norm(p) for p in glob.glob("docs/*.md"))
    existing = set(files)
    anchors = {f: headings_and_anchors(f) for f in files}

    problems, total = [], 0

    # 1. headings must slug identically in both renderers
    for f in files:
        fence = False
        with open(f, encoding="utf-8") as fh:
            for line in fh:
                if line.strip().startswith("```"):
                    fence = not fence
                    continue
                if fence:
                    continue
                m = re.match(r"^#{1,6}\s+(.*?)\s*$", line)
                if m and gh_slug(m.group(1)) != md_slug(m.group(1)):
                    problems.append("SLUG SPLIT  %s: %r -> github=%s mkdocs=%s"
                                    % (f, m.group(1), gh_slug(m.group(1)), md_slug(m.group(1))))

    # 2. every link resolves
    for f in files:
        with open(f, encoding="utf-8") as fh:
            s = fh.read()
        d = os.path.dirname(f)
        for m in re.finditer(r"\]\(([^)\s]+)\)", s):
            link = m.group(1)
            total += 1
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, anc = link.partition("#")
            tgt = norm(os.path.normpath(os.path.join(d, path))) if path else f
            if path and not tgt.endswith(".md"):
                if not os.path.exists(tgt):
                    problems.append("MISSING ASSET %s -> %s" % (f, link))
                continue
            if tgt not in existing:
                problems.append("MISSING FILE  %s -> %s" % (f, link))
                continue
            if anc and anc not in anchors[tgt]:
                problems.append("BAD ANCHOR    %s -> %s" % (f, link))

    for p in problems:
        print(p)
    print("\n%d files, %d links checked, %d problem(s)" % (len(files), total, len(problems)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
