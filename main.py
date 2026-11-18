#!/usr/bin/env python3
"""Render a labeled contact sheet of pages from a PDF."""
import argparse
import math
from pathlib import Path
import fitz
from PIL import Image, ImageDraw


def grid_size(count: int, columns: int) -> tuple[int, int]:
    if count < 1 or columns < 1:
        raise ValueError("count and columns must be positive")
    return columns, math.ceil(count / columns)


def render_sheet(source: Path, output: Path, columns: int = 4, max_pages: int | None = None, thumb_width: int = 220) -> int:
    document = fitz.open(source)
    try:
        total = len(document) if max_pages is None else min(len(document), max_pages)
        if total < 1:
            raise ValueError("PDF contains no pages")
        thumbnails = []
        for index in range(total):
            page = document.load_page(index)
            scale = thumb_width / max(page.rect.width, 1)
            pixmap = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
            image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
            thumbnails.append(image)
        cell_width = thumb_width + 24
        cell_height = max(image.height for image in thumbnails) + 54
        cols, rows = grid_size(len(thumbnails), columns)
        sheet = Image.new("RGB", (cols * cell_width, rows * cell_height), "#e8edf4")
        draw = ImageDraw.Draw(sheet)
        for index, image in enumerate(thumbnails):
            col, row = index % cols, index // cols
            x, y = col * cell_width, row * cell_height
            draw.rounded_rectangle((x + 6, y + 6, x + cell_width - 6, y + cell_height - 6), radius=8, fill="white")
            draw.text((x + 14, y + 12), f"Page {index + 1}", fill="#334155")
            sheet.paste(image, (x + 12, y + 34))
        output.parent.mkdir(parents=True, exist_ok=True)
        sheet.save(output, "PNG", optimize=True)
        return total
    finally:
        document.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--output", type=Path, default=Path("pdf-pages.png"))
    parser.add_argument("--columns", type=int, default=4)
    parser.add_argument("--max-pages", type=int)
    parser.add_argument("--thumb-width", type=int, default=220)
    args = parser.parse_args()
    if not args.pdf.is_file():
        parser.error(f"PDF not found: {args.pdf}")
    if args.columns < 1 or args.thumb_width < 40:
        parser.error("--columns must be positive and --thumb-width at least 40")
    try:
        count = render_sheet(args.pdf, args.output, args.columns, args.max_pages, args.thumb_width)
    except (OSError, ValueError, fitz.FileDataError) as exc:
        parser.error(str(exc))
    print(f"Rendered {count} pages -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
