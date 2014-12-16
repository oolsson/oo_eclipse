#!/usr/bin/env python
import MySQLdb
import sys
import string
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
 
dbhost = 'localhost'
dbname = 'httplog'
dbuser = 'jonesy'
dbpasswd = 'mypassword'
 
PAGE_HEIGHT=defaultPageSize[1]
styles = getSampleStyleSheet()
Title = "Generating Reports with Python"
Author = "Brian K. Jones"
URL = "http://www.protocolostomy.com"
email = "bkjones@gmail.com"
Abstract = """This is a simple example document that illustrates how to put together a basic PDF with a chart.
I used the PLATYPUS library, which is part of ReportLab, and the charting capabilities built into ReportLab."""
Elements=[]
HeaderStyle = styles["Heading1"]
ParaStyle = styles["Normal"]
PreStyle = styles["Code"]
 
def header(txt, style=HeaderStyle, klass=Paragraph, sep=0.3):
    s = Spacer(0.2*inch, sep*inch)
    para = klass(txt, style)
    sect = [s, para]
    result = KeepTogether(sect)
    return result
 
def p(txt):
    return header(txt, style=ParaStyle, sep=0.1)
 
def pre(txt):
    s = Spacer(0.1*inch, 0.1*inch)
    p = Preformatted(txt, PreStyle)
    precomps = [s,p]
    result = KeepTogether(precomps)
    return result
 

 
def graphout(catnames, data):
    drawing = Drawing(400, 200)
    lc = HorizontalLineChart()
    lc.x = 30
    lc.y = 50
    lc.height = 125
    lc.width = 350
    lc.data = data
    catNames = catnames
    lc.categoryAxis.categoryNames = catNames
    lc.categoryAxis.labels.boxAnchor = 'n'
    lc.valueAxis.valueMin = 0
    lc.valueAxis.valueMax = 1500
    lc.valueAxis.valueStep = 300
    lc.lines[0].strokeWidth = 2
    lc.lines[0].symbol = makeMarker('FilledCircle') # added to make filled circles.
    lc.lines[1].strokeWidth = 1.5
    drawing.add(lc)
    return drawing
 
def go():
    doc = SimpleDocTemplate('gfe.pdf')
    doc.build(Elements)
 
mytitle = header(Title)
myname = header(Author, sep=0.1, style=ParaStyle)
mysite = header(URL, sep=0.1, style=ParaStyle)
mymail = header(email, sep=0.1, style=ParaStyle)
abstract_title = header("ABSTRACT")
myabstract = p(Abstract)
head_info = [mytitle, myname, mysite, mymail, abstract_title, myabstract]
Elements.extend(head_info)
 

 
go()