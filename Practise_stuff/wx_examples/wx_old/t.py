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
        return "(%s,%s)" % (self.rowLabels[row], self.colLabels[col])
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

class panel1(wx.Panel):     
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(750, 500),pos= (250,0),style=wx.BORDER_SUNKEN)
        self.SetBackgroundColour('red')
        '''
        self.figure = matplotlib.figure.Figure(figsize=(9.5, 6.25))
        self.figure.suptitle("Dynamic Price Chart Goes Here", fontsize=14)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_axis_bgcolor('black')
        t = np.arange(0, 10, 1)
        self.data = [0,2,3,4,5,6,3,3,3,2]
        line, = self.axes.plot(t, self.data,color=(1, 0, 1),linewidth=1)
        figure = FigureCanvas(self, -1, self.figure)
       '''
        
class panel2(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(750, 500),pos= (250,500),style=wx.BORDER_SUNKEN)
        self.SetBackgroundColour('green')
        '''
        self.figure = matplotlib.figure.Figure(figsize=(9.5, 3.25))
        self.figure.suptitle("Dynamic Price Chart Goes Here", fontsize=14)
        self.axes = self.figure.add_subplot(111)
        t = np.arange(0, 2*np.pi, 0.1)
        line, = self.axes.plot(t, np.sin(t))           
        figure = FigureCanvas(self, -1, self.figure)
        '''

class TradingProgram(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(1000, 800))
        
        
        Panel1 = panel1(self)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(Panel1, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(vbox1)
        
        Panel2 = panel2(self)
        vbox1.Add(Panel2, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(vbox1)
        
        
        
        
        table = CustTableGrid(Panel2)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(table, 1, wx.EXPAND | wx.ALL, 10)
        Panel2.SetSizer(vbox2)


    
        
app = wx.App(redirect = False)
frame=TradingProgram(None, -1, 'A line chart')
frame.Show()
app.MainLoop()