#!/usr/bin/env python3
"""Run lightweight mechanical checks on Point social-template deliverables."""

from __future__ import annotations

import argparse
import struct
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path


PRESENTATION_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
DRAWING_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"


def png_info(path: Path) -> tuple[int, int, bool]:
    with path.open("rb") as file:
        signature = file.read(8)
        if signature != b"\x89PNG\r\n\x1a\n":
            raise ValueError("not a PNG file")
        length = struct.unpack(">I", file.read(4))[0]
        if file.read(4) != b"IHDR" or length != 13:
            raise ValueError("missing PNG IHDR")
        width, height, _, color_type, _, _, _ = struct.unpack(">IIBBBBB", file.read(13))
        file.read(4)  # IHDR CRC
        has_alpha = color_type in {4, 6}
        while True:
            raw_length = file.read(4)
            if not raw_length:
                break
            chunk_length = struct.unpack(">I", raw_length)[0]
            chunk_type = file.read(4)
            file.seek(chunk_length + 4, 1)
            if chunk_type == b"tRNS":
                has_alpha = True
            if chunk_type == b"IEND":
                break
        return width, height, has_alpha


def inspect_pptx(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        with zipfile.ZipFile(path) as deck:
            names = set(deck.namelist())
            presentation = ET.fromstring(deck.read("ppt/presentation.xml"))
            size = presentation.find(f"{{{PRESENTATION_NS}}}sldSz")
            if size is None:
                errors.append("PowerPoint slide size is missing")
            else:
                width = int(size.attrib["cx"])
                height = int(size.attrib["cy"])
                if height == 0 or abs((width / height) - 0.8) > 0.002:
                    errors.append(f"PowerPoint aspect ratio is not 4:5 ({width}:{height})")

            slide_names = sorted(
                name
                for name in names
                if name.startswith("ppt/slides/slide") and name.endswith(".xml")
            )
            if not slide_names:
                errors.append("PowerPoint contains no slides")

            for slide_name in slide_names:
                slide = ET.fromstring(deck.read(slide_name))
                text_nodes = slide.findall(f".//{{{DRAWING_NS}}}t")
                pictures = slide.findall(f".//{{{PRESENTATION_NS}}}pic")
                if not text_nodes:
                    warnings.append(f"{slide_name} contains no editable text nodes")
                if not pictures:
                    warnings.append(f"{slide_name} contains no separate picture objects")
    except (KeyError, ET.ParseError, zipfile.BadZipFile) as error:
        errors.append(f"PowerPoint could not be inspected: {error}")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check a 4:5 PowerPoint, 1080x1350 preview PNGs, and transparent illustration PNGs."
    )
    parser.add_argument("--deck", type=Path, help="Editable .pptx source deck")
    parser.add_argument("--preview", action="append", default=[], type=Path)
    parser.add_argument("--illustration", action="append", default=[], type=Path)
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    if not args.deck and not args.preview and not args.illustration:
        parser.error("provide at least one --deck, --preview, or --illustration")

    if args.deck:
        if not args.deck.is_file():
            errors.append(f"missing deck: {args.deck}")
        else:
            deck_errors, deck_warnings = inspect_pptx(args.deck)
            errors.extend(deck_errors)
            warnings.extend(deck_warnings)

    for preview in args.preview:
        if not preview.is_file():
            errors.append(f"missing preview: {preview}")
            continue
        try:
            width, height, _ = png_info(preview)
            if (width, height) != (1080, 1350):
                errors.append(f"preview has wrong size: {preview} ({width}x{height})")
        except ValueError as error:
            errors.append(f"invalid preview {preview}: {error}")

    for illustration in args.illustration:
        if not illustration.is_file():
            errors.append(f"missing illustration: {illustration}")
            continue
        try:
            _, _, has_alpha = png_info(illustration)
            if not has_alpha:
                errors.append(f"illustration has no alpha channel: {illustration}")
        except ValueError as error:
            errors.append(f"invalid illustration {illustration}: {error}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"Preflight failed with {len(errors)} error(s) and {len(warnings)} warning(s).")
        return 1
    print(f"Preflight passed with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
