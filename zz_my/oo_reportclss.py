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
import Quandl
import ts_charting as charting
import time
import datetime as dt

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
        f = lambda x: round(x,2)
        df=df.applymap(f)
        
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


f = lambda x: float(x)
class fin:
    def __init__(self):
        self.rep=newreport()
        self.pic=pic_num()
        self.rep.addlogo()
        self.first=0
        print 'print reportclass'
    def add_chart(self,security,start,end,**kwargs):
        try:
    #         Libor2 = DataReader("USD3MTD156N",  "fred", start, end) #SPX
            try:
                print security
                df =Quandl.get(security[0], trim_start=start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
                df=df.iloc[:,0:4]
                df.columns=['Open','High','Low','Close']
                print df.head(8)
            except:
                try:
                    df =Quandl.get(security[0], trim_start=start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
                except:pass
            fig = charting.figure(1)
            df.ohlc_plot()
            plt.title(kwargs['title1'])
            self.pic.new()
            plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(self.pic.num)))
            self.rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(self.pic.num)),7,4,'LEFT')
            plt.close()
            self.first +=1
        except:
            try:
                data=Quandl.get(["YAHOO/INDEX_GSPC.6"],trim_start =start, trim_end=end,collapse="monthly")
            except:pass
            time.sleep(10)
            self.first=0
            print 'error'
    def add(self,security,start,end,**kwargs):
        try:
    #         Libor2 = DataReader("USD3MTD156N",  "fred", start, end) #SPX
            try:
                print security
                df =Quandl.get(security[0], trim_start=start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
            except:
                try:
                    df =Quandl.get(security[0], trim_start=start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
                except:pass
            plt.subplot(111)
            plt.title(kwargs['title1'])
            plt.plot(df.index,df)
            plt.xticks(rotation=45)
            plt.xticks(fontsize=8)
            plt.legend(df.columns,loc=0)
            self.pic.new()
            plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(self.pic.num)))
            self.rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(self.pic.num)),7,4,'LEFT')
    #         plt.show()
            plt.close()
            self.first +=1
        except:
            try:
                data=Quandl.get(["YAHOO/INDEX_GSPC.6"],trim_start =start, trim_end=end,collapse="monthly")
            except:pass
            time.sleep(10)
            self.first=0
            print 'error'
    def add_many(self,security,start,end,**kwargs):
#         try:
        df1=pd.DataFrame()
        for i in range(0,len(security)):
            df =Quandl.get(security[i], trim_start=start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
            y=pd.DataFrame(df.iloc[:,0].apply(f).values,columns=[i],index=df.index)
            df1=df1.combine_first(y)
        df=df1.ffill()
        plt.subplot(111)
        plt.title(kwargs['title1'])
        print df.tail(8)
        plt.plot(df.index,df)
        plt.xticks(rotation=45)
        plt.xticks(fontsize=8)
        plt.legend(kwargs['legend1'],loc=0)
#         plt.legend(df.columns,loc=0)
        self.pic.new()
        plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(self.pic.num)))
        self.rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(self.pic.num)),7,4,'LEFT')
#         plt.show()
        plt.close()
        self.first +=1
#         except:
#             print 'error'
#             self.first=0
    def add_many_2ax(self,security,start,end,**kwargs):
#         try:
        df1=pd.DataFrame()
        for i in range(0,len(security)):
            df =Quandl.get(security[i], trim_start=start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
            y=pd.DataFrame(df.iloc[:,0].apply(f).values,columns=[i],index=df.index)
            df1=df1.combine_first(y)
        df=df1.ffill()

        fig = charting.figure(1)
        df[1].fplot(kwargs['legend1'][0], secondary_y=True)
        df[0].fplot(kwargs['legend1'][1])
        plt.title(kwargs['title1'])
        plt.xticks(rotation=45)
        plt.xticks(fontsize=8)

        self.pic.new()
        plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(self.pic.num)))
        self.rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(self.pic.num)),7,4,'LEFT')
#         plt.show()
        plt.close()
        self.first +=1
    def add_relative_perf(self,security,start,end,**kwargs):
        df1=pd.DataFrame()
        for i in range(0,len(security)):
            df =Quandl.get(security[i], trim_start=start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
            y=pd.DataFrame(df.iloc[:,0].apply(f).values,columns=[i],index=df.index)
            df1=df1.combine_first(y)
        df=df1.ffill()
        df=df.pct_change(periods=1)+1
#         print df.head(10)
#         df22=oof.oo_outlier_filter(df, 3)
#         print df22.head(10)
        df=df.cumprod()
        df.columns=kwargs['columns']
        plt.subplot(111)
        plt.title(kwargs['title1'])
        plt.plot(df.index,df)
        plt.xticks(rotation=45)
        plt.xticks(fontsize=8)
        plt.legend(df.columns,loc=0,fontsize=8)
#         plt.legend(kwargs['legend'])
        self.pic.new()
        plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(self.pic.num)))
        self.rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(self.pic.num)),7,4,'LEFT')
#         plt.show()
        plt.close()
    def add_df(self,df,**kwargs):
        plt.subplot(111)
        plt.title(kwargs['title1'])
        plt.plot(df.index,df)
        plt.xticks(rotation=45)
        plt.xticks(fontsize=8)
        plt.legend(kwargs['legend1'],loc=0)
        self.pic.new()
        plt.savefig("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png" %(str(self.pic.num)))
        self.rep.addimage("C:/Users/oskar/Documents/doc_no_backup/python_crap/temp/%s.png"%(str(self.pic.num)),7,4,'LEFT')
        plt.close()
    def write_rep(self,name):
        self.rep.writereport(name) 
        
# start1=dt.date(2014,9,30)  
# start2=dt.date(2015,1,1)      
# end1=dt.date.today()
# fin=fin() 
# fin.add_chart(["OFDP/FUTURE_NG1"],start1,end1,title1='NAT GAS')
# fin.write_rep('oopooo')             


# rep=newreport()
# rep.addlogo()
# rep.addtext('dbcusdbppppppppp\noooooooooooooooooooooooousdb',0.8)
# 
# rep.add_data('return',[0.8],0)
# rep.addimage("C:\Users\oskar\Documents\doc_no_backup\python_crap\pics/pytrade_logo.png",4,2,'LEFT')
# rep.writereport('rc')