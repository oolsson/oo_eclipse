from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.lib import utils
from reportlab.lib.pagesizes import letter
import urllib2
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image
import os

def hello(c):
    c.drawString(100,100,"Hello World")
    
c = canvas.Canvas("hel.pdf")
hello(c)


#c.drawImage('pic1.png', 5*cm, 5*cm) 
#c.drawImage('pic1.png', inch, height - 2 * inch)
c.drawImage('pic1.png', 2*cm, 20*cm, width=7*cm, height=5*cm, mask=None, preserveAspectRatio=False, anchor='c')



c.showPage()
c.save()
