#!/usr/bin/env python3
"""news-image-20261121: sum up Saturday 21 November 2026 in one image.

A dense newspaper front page: a Russian missile hits Kryvyi Rih,
the ICJ finds Myanmar guilty of genocide against the Rohingya,
Mexico captures FBI most-wanted cartel boss "El Chapo Isidro",
plus the AI sell-off, COP31 overtime, the Shenzhen summit, and
more, all dated Saturday 21 November 2026, with a drawn
illustration in every story panel. The picture lives in
entry.png next to this file; this program only copies it to the
output path, so both runs write exactly the same bytes.
Standard library only, no network.
"""
import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(outdir, "entry.png")
    with open(src, "rb") as f:
        head = f.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    width, height = struct.unpack(">II", head[16:24])
    shutil.copyfile(src, dst)
    print(f"wrote {dst} {width}x{height} {os.path.getsize(dst)} bytes")


if __name__ == "__main__":
    main()
