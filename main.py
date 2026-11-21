"""Entry program for the make.fun news-image-20261121 bounty.

Copies the sibling entry.png into the output directory
($MAKEFUN_OUTPUT_DIR, or /output by default).

The image sums up Saturday, 21 November 2026 in six stories:
1. Russian missiles hit Poland
2. Trump speaks after the Xi-Putin talks
3. Cyclone Akvan strikes India
4. Cyberattack hits global banks
5. Myanmar rejects the genocide ruling
6. Berlin summit backs Ukraine
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
