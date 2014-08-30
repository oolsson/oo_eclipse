#!/usr/bin/env python
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

doc = SimpleDocTemplate("paragraphs.pdf", pagesize=letter)
parts = []

style = ParagraphStyle(
    name='Normal',
    fontName='Helvetica-Bold',
    fontSize=9,
)

parts.append(Paragraph("Paragraphs are a kind of Flowable.  " * 20, style))
parts.append(Spacer(1, 0.2 * inch))
parts.append(Paragraph("Paragraphs are natural in their behavior.  " * 20,
    style))
parts.append(Spacer(1, 0.2 * inch))
parts.append(Paragraph(
    "Paragraphs make sense for flexible and dynamic documents.  " * 20, style))
doc.build(parts)