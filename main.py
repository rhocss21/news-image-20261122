#!/usr/bin/env python3
"""news-image-20261122 entrypoint.

Checks the front-page image next to this file (entry.png) and copies
it unchanged into the judging output directory. Standard library only,
no network, no image libraries: the PNG/JPEG headers are parsed by hand.
"""

import hashlib
import os
import shutil
import struct
import sys

SOURCE = "entry.png"
MAX_BYTES = 1_048_576
WANT_W = 1024
WANT_H = 1024

PNG_SIG = b"\x89PNG\r\n\x1a\n"
JPG_SIG = b"\xff\xd8\xff"
JPG_END = b"\xff\xd9"


def die(msg):
    print("error:", msg, file=sys.stderr)
    raise SystemExit(1)


def png_size(blob):
    if len(blob) < 33 or blob[12:16] != b"IHDR":
        die("PNG entry.png has no IHDR chunk")
    w, h = struct.unpack(">II", blob[16:24])
    return w, h


def jpg_size(blob):
    # Walk JPEG segments until a Start-Of-Frame marker (SOF0/SOF2).
    i = 2
    while i + 9 < len(blob):
        if blob[i] != 0xFF:
            die("JPEG entry.png has a corrupt segment")
        marker = blob[i + 1]
        if marker in (0xC0, 0xC2):  # SOF0, SOF2
            h, w = struct.unpack(">HH", blob[i + 5:i + 9])
            return w, h
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        seg_len = struct.unpack(">H", blob[i + 2:i + 4])[0]
        i += 2 + seg_len
    die("JPEG entry.png has no Start-Of-Frame segment")


def inspect(path):
    if not os.path.isfile(path):
        die("missing source image: " + path)
    size = os.path.getsize(path)
    if size == 0:
        die("entry.png is empty")
    if size > MAX_BYTES:
        die("entry.png is %d bytes, over the %d byte cap" % (size, MAX_BYTES))
    with open(path, "rb") as fh:
        blob = fh.read()
    if blob[:8] == PNG_SIG:
        kind, (w, h) = "png", png_size(blob)
        if b"IEND" not in blob[-8:]:
            die("PNG entry.png has no IEND marker")
    elif blob[:3] == JPG_SIG:
        kind, (w, h) = "jpeg", jpg_size(blob)
        if not blob.endswith(JPG_END):
            die("JPEG entry.png does not end with FFD9")
    else:
        die("entry.png is neither PNG nor JPEG")
    if (w, h) != (WANT_W, WANT_H):
        die("entry.png is %dx%d, expected %dx%d" % (w, h, WANT_W, WANT_H))
    return kind, w, h, size, hashlib.sha256(blob).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SOURCE)
    kind, w, h, size, digest = inspect(src)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, SOURCE)
    try:
        os.makedirs(out_dir, exist_ok=True)
        shutil.copyfile(src, dst)
    except OSError as exc:
        die("could not write the output image: %s" % exc)
    with open(dst, "rb") as fh:
        got = hashlib.sha256(fh.read()).hexdigest()
    if got != digest:
        die("copied entry.png failed its sha256 check")
    print("wrote %s (%s %dx%d, %d bytes, sha256 %s)"
          % (dst, kind, w, h, size, got))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
