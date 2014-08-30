import wx
import time
import datetime
import operator
import pylab
import scipy
import pickle
import math
import string
import numpy as np
import os
import pprint
import random
import sys
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
import threading
import wx.grid as gridlib

class TestTable(wx.grid.PyGridTableBase):
    def __init__(self):
        gridlib.PyGridTableBase.__init__(self)
        self.rowLabels = ["uno", "dos", "tres", "quatro", "cinco"]
        self.colLabels = ["homer", "marge", "bart", "lisa", "maggie"]
    def GetNumberRows(self):
        return 5
    def GetNumberCols(self):
        return 5
    def IsEmptyCell(self, row, col):
        return False
    def GetValue(self, row, col):
        #return "(%s,%s)" % (self.rowLabels[row], self.colLabels[col])
        return (1,2)
    def SetValue(self, row, col, value):
        pass
    def GetColLabelValue(self, col):
        return self.colLabels[col]
    def GetRowLabelValue(self, row):
        return self.rowLabels[row]



class CustTableGrid(gridlib.Grid):
    def __init__(self, parent):
        gridlib.Grid.__init__(self, parent, -1)
        table = TestTable()
        # The second parameter means that the grid is to takeownership of the
        # table and will destroy it when done.  Otherwise you wouldneed to keep
        # a reference to it and call it's Destroy method later.
        self.SetTable(table, True)
        self.SetRowLabelSize(0)
        self.SetMargins(0,0)
        self.AutoSizeColumns(False)
        
id = wx.NewId()

class th(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
    def run(self):
        apply(self.func, self.args)

class LineChart(wx.Panel):     
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(750, 500),pos= (250,0),style=wx.BORDER_SUNKEN)
        self.figure = matplotlib.figure.Figure(figsize=(9.5, 6.25))
        self.figure.suptitle("Dynamic Price Chart Goes Here", fontsize=14)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_axis_bgcolor('black')
        t = np.arange(0, 10, 1)
        self.data = [0,2,3,4,5,6,3,3,3,2]
        line, = self.axes.plot(t, self.data,color=(1, 0, 1),linewidth=1)
        figure = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(figure, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        
                
        def next():
            r = round(random.random()*10,0)
            return r
        
        def data():
            self.data.pop(0)
            self.data.append(next())
            return self.data
        
        def setaxes():
            self.axes.set_ybound(lower=min(data()), upper=max(data()))
    
        def update_line2():
            line.set_ydata(data())
            setaxes()
            time.sleep(2)
            figure.draw()                 # redraw the canvas
            
        def  update_line(self):
            thr1 =th(update_line2,())
            thr1.start()
            
            
        
        self.timer = wx.Timer(self)
        self.timer.Start(3000)
        self.Bind(wx.EVT_TIMER,update_line,self.timer)
        
        
        
class EquityChart(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(750, 500),pos= (250,500),style=wx.BORDER_SUNKEN)
        self.figure = matplotlib.figure.Figure()
        self.figure.suptitle("Dynamic Price Chart Goes Here", fontsize=14)
        self.axes = self.figure.add_subplot(111)
        

        
        t = np.arange(0, 2*np.pi, 0.1)
        line, = self.axes.plot(t, np.sin(t))    
        figure = FigureCanvas(self, -1, self.figure)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(figure, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        #self.Fit()
             
        
        def update_line(self):
            line.set_ydata(np.sin(t+update_line.i/10.))
            figure.draw()                 # redraw the canvas
            update_line.i += 1
        update_line.i = 0
        
        
        self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER,update_line,self.timer)
        
    
        
class PositionPanel(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(250, 320),pos= (0,180),style=wx.BORDER_SUNKEN)
        
        font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, -1, 'Positions')
        heading.SetFont(font)
        
        wx.StaticText(self, -1, 'AUD/USD', (5, 30))
        wx.StaticText(self, -1, '50,000', (150, 30))
        
        wx.StaticText(self, -1, 'AUD/EUR', (5, 60))
        wx.StaticText(self, -1, '70,000', (150, 60))
        
        wx.StaticText(self, -1, 'AUD/JPY', (5, 90))
        wx.StaticText(self, -1, '50,000', (150, 90))
        
        
class ErrorChecking(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(250, 500),pos= (0,500),style=wx.BORDER_SUNKEN)

class Buttons(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(250, 180),style=wx.BORDER_SUNKEN)
        self.panel = wx.Panel(self,size=(240, 150),pos=(10, 10))
        self.button = wx.Button(self.panel, label="Connect", pos=(25, 15),size=(180, 50))
        self.button1 = wx.Button(self.panel, label="Stop", pos=(25, 75),size=(180, 50))
        self.Bind(wx.EVT_BUTTON, self.OnConnect, self.button)
        self.Bind(wx.EVT_BUTTON, self.OnStop, self.button1)
    
    def OnConnect(self, event):
        self.Close(True)   
        
        
    def OnStop(self, event):
        self.Close(True)   

class TradingProgram(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(1000, 800))
        
        panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(panel, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(vbox)
        
        panel1 = wx.Panel(panel, -1)
        panel1.SetBackgroundColour('red') 
        panel2 = wx.Panel(panel, -1)
        vbox2 = wx.BoxSizer(wx.HORIZONTAL)
        vbox2.Add(panel1, 1, wx.EXPAND | wx.ALL, 1)
        vbox2.Add(panel2, 2, wx.EXPAND | wx.ALL, 1)
        panel.SetSizer(vbox2)
        
        equitychart = EquityChart(panel2)
        linechart = LineChart(panel2)
        vbox3 = wx.BoxSizer(wx.VERTICAL)
        vbox3.Add(linechart, 1, wx.EXPAND | wx.ALL, 1)
        vbox3.Add(equitychart, 1, wx.EXPAND | wx.ALL, 1)
        panel2.SetSizer(vbox3)
        
        buttons = Buttons(panel1)
        #positionpanel = PositionPanel(panel1)
        table = CustTableGrid(panel1)
        errorchecking = ErrorChecking(panel1)
        vbox4 = wx.BoxSizer(wx.VERTICAL)
        vbox4.Add(buttons, 1, wx.EXPAND | wx.ALL, 1)
        vbox4.Add(table, 1, wx.EXPAND | wx.ALL, 1)
        vbox4.Add(errorchecking, 1, wx.EXPAND | wx.ALL, 1)
        panel1.SetSizer(vbox4)
        
    
        
app = wx.App(redirect = False)
frame=TradingProgram(None, -1, 'A line chart')
frame.Show()
app.MainLoop()