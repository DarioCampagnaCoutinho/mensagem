#!/usr/bin/env python3
"""Gera um PDF a partir do arquivo docs/infra_documentation.md usando ReportLab.

Uso:
    python scripts/generate_infra_pdf.py

Gera: docs/infra_documentation.pdf
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

SRC = os.path.join(os.path.dirname(__file__), '..', 'docs', 'infra_documentation.md')
DST = os.path.join(os.path.dirname(__file__), '..', 'docs', 'infra_documentation.pdf')


def main():
    with open(SRC, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    c = canvas.Canvas(DST, pagesize=A4)
    width, height = A4
    left_margin = 20 * mm
    top = height - 20 * mm
    y = top
    line_height = 6 * mm
    c.setFont("Helvetica", 10)

    for raw in lines:
        line = raw.rstrip('\n')
        # Simple wrapping
        while line:
            max_chars = 90
            chunk = line[:max_chars]
            line = line[max_chars:]
            c.drawString(left_margin, y, chunk)
            y -= line_height
            if y < 20 * mm:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = top

    c.save()
    print(f"PDF gerado: {DST}")


if __name__ == '__main__':
    main()

