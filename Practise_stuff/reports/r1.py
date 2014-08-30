#!/usr/bin/env python
 
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
 
PAGE_HEIGHT=defaultPageSize[1]
styles = getSampleStyleSheet()
Title = Paragraph("Generating Reports with Python", styles["Heading1"])
Author = Paragraph("Brian K. Jones", styles["Normal"])
URL = Paragraph("http://www.protocolostomy.com", styles["Normal"])
email = Paragraph("bkjones +_at_+ gmail.com", styles["Normal"])
Abstract = Paragraph("""This is a simple example document that illustrates how to put together a basic PDF with a chart.
I used the PLATYPUS library, which is part of ReportLab, and the charting capabilities built into ReportLab.""", styles["Normal"])
 
Elements = [Title, Author, URL, email, Abstract]
 
def go():
   doc = SimpleDocTemplate('gfe.pdf')
   doc.build(Elements)
 
go() 