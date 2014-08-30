import wx
'''
from ib.ext.Contract import Contract
from ib.ext.ExecutionFilter import ExecutionFilter
from ib.ext.Order import Order
from ib.opt import ibConnection, message
'''
from matplotlib.ticker import Formatter
import time
import datetime
import matplotlib
import numpy as n
import operator
import pylab
import scipy
import pickle
import math
import string

class LineChart(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(750, 500),pos= (250,0),style=wx.BORDER_SUNKEN)

class EquityChart(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(750, 500),pos= (250,500),style=wx.BORDER_SUNKEN)
        
class PositionPanel(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(250, 320),pos= (0,180),style=wx.BORDER_SUNKEN)
        
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
        wx.Frame.__init__(self, parent, id, title, size=(1000, 1000))

        panel = wx.Panel(self, -1)
        linechart = LineChart(panel)
        equitychart = EquityChart(panel)
        positionpanel = PositionPanel(panel)
        errorchecking = ErrorChecking(panel)
        buttons = Buttons(panel)
        self.Show(True)


app = wx.App()
TradingProgram(None, -1, 'A line chart')
app.MainLoop()