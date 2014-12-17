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
from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    def add_plot(self,df,**kwargs):
        plt.subplot(111)
        plt.title(kwargs['title1'])
        plt.plot(df.index,df)
        plt.xticks(rotation=45)
        plt.xticks(fontsize=8)
        plt.legend(df.columns,loc=0)
        self.pic.new()
        plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(self.pic.num)))
        self.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(self.pic.num)),7,4,'LEFT')
#         plt.show()
        plt.close()
        self.story.append(Spacer(1,0.1*inch))
    def add_df(self,df,h,w):
        def dfTable(df):
            df2 = df.reset_index() # reset the index so row labels show up in the reportlab table
            n = df2.columns.nlevels # number of table header rows to repeat
            if n > 1:
                labels = map(list, zip(*df2.columns.values))
            else:
                labels = [df2.columns[:,].values.astype(str).tolist()]
            values = df2.values.tolist()
            datalist = labels + values
            return datalist
        
        data=dfTable(df)
        table_with_style = Table(data, [w * inch, h * inch, inch])
        
        s2 = TableStyle(
        [('LINEABOVE', (1,0), (-1,1), 2, colors.green),                 #first 0=starting from column, sec0nd=?, -1= goes to last column
        # ('LINEABOVE', (0,-1), (-1,-1), 0.25, colors.black),
        ('INNERGRID', (0, 1), (-1, -1), 0.25, colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 1, colors.blue),
        ('BOX', (0, 1), (-1, -1), 0.25, colors.black),
        ('ALIGN', (0,0), (0,-1), 'LEFT'),
        ('ALIGN', (1,0), (-1,-1), 'CENTRE'),
        ('BACKGROUND', (1,0), (-1,0), colors.Color(0,0,0)),
        ('TEXTCOLOR',(0,0),(0,0),colors.white),
        ('TEXTCOLOR',(1,0),(-1,0),colors.yellow)])
        
        table_with_style.setStyle(s2)
        self.story.append(table_with_style)
        self.story.append(Spacer(1,0.1*inch))
        
        
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