from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame, Spacer, Image, Table, TableStyle, SimpleDocTemplate
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing, string
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend

class pic_num:
    def __init__(self):
        self.num=1
    def new(self):
        self.num +=1

def dataToParagraph(name,data):
    p = name +':   ' + '  '
    for i in range(len(data)):
        p += str(data[i])
        if i != len(data) - 1:
            p += ', '
        else:
            p += ''    
    return p

class newreport:
    def __init__(self):
        self.story = []
        self.styles = getSampleStyleSheet()
        self.styleN = self.styles['Normal']
        
    def addlogo(self):
        #First add the Logo
        self.im = Image("C:\Users\oskar\Documents\doc_no_backup\python_crap\pics/pytrade_logo.png", width=1.6*inch, height=1*inch)
        self.im.hAlign = 'LEFT'
        self.story.append(self.im)
        self.story.append(Spacer(1,.25*inch))
        
    def addtext(self,text,space):
        self.story.append(Paragraph(text,self.styleN))
        self.story.append(Spacer(1,space*inch))
    def add_data(self,text,num,space):
        self.story.append(Paragraph(dataToParagraph(text, num),self.styleN))
        self.story.append(Spacer(1,space*inch))
    def addimage(self,img,_width,_hight,align):
        im = Image(img, width=_width*inch, height=_hight*inch)
        im.hAlign = align
        self.story.append(im)
        
        
    def writereport(self,filename):
#         pdfname = 'C:\Users\oskar\Documents\doc_no_backup\python_crap\reports/%s'%(filename+'.pdf')
        pdfname = 'C:/Users/oskar/Documents/doc_no_backup/python_crap/reports/%s'%(filename+'.pdf')
        doc = SimpleDocTemplate(pdfname,pagesize = letter, topMargin=0) 
        doc.build(self.story)
        
# rep=newreport()
# rep.addlogo()
# rep.addtext('dbcusdbppppppppp\noooooooooooooooooooooooousdb',0.8)
# 
# rep.add_data('return',[0.8],0)
# rep.addimage("C:\Users\oskar\Documents\doc_no_backup\python_crap\pics/pytrade_logo.png",4,2,'LEFT')
# rep.writereport('rc')