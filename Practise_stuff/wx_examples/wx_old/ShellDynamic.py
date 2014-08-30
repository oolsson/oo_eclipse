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

id = wx.NewId()


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
        
                
        def next():
            r = round(random.random()*10,0)
            return r
        
        def data():
            self.data.pop(0)
            self.data.append(next())
            return self.data
        
        def setaxes():
            self.axes.set_ybound(lower=min(data()), upper=max(data()))
    
        def update_line(self):
            line.set_ydata(data())
            setaxes()
            figure.draw()                 # redraw the canvas
        
        
        self.timer = wx.Timer(self)
        self.timer.Start(2000)
        self.Bind(wx.EVT_TIMER,update_line,self.timer)
        
        
        
class EquityChart(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(750, 500),pos= (250,500),style=wx.BORDER_SUNKEN)
        self.figure = matplotlib.figure.Figure(figsize=(9.5, 3.25))
        self.figure.suptitle("Dynamic Price Chart Goes Here", fontsize=14)
        self.axes = self.figure.add_subplot(111)
        t = np.arange(0, 2*np.pi, 0.1)
        line, = self.axes.plot(t, np.sin(t))
                
        figure = FigureCanvas(self, -1, self.figure)
        print self.figure      
        
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
        equitychart = EquityChart(panel)
        linechart = LineChart(panel)
        positionpanel = PositionPanel(panel)
        errorchecking = ErrorChecking(panel)
        buttons = Buttons(panel)
    
        
app = wx.App(redirect = False)
frame=TradingProgram(None, -1, 'A line chart')
frame.Show()
app.MainLoop()