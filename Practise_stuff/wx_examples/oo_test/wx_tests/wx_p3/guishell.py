#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Trading Model - created by OO and SV

#----------------------Import Modules---------------------
import wx
import time
import pylab
import string
import numpy as np
import os
import sys
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
from matplotlib.ticker import Formatter
from matplotlib.finance import quotes_historical_yahoo, candlestick,plot_day_summary, candlestick2
from wx.lib.pubsub import Publisher
import wx.grid as gridlib


from wx.py import shell
from wx.py import editor
import wx.richtext as rt

from numpy import arange

from datetime import datetime
from pandas import *
import pandas as pd
from matplotlib.widgets import Cursor




#---- code run ------------------------------------------------------------
#This is where the code runs (and the GUI is created)
if __name__ == "__main__":
   

            
    class tab4(wx.Panel): 
        
        def __init__(self, parent):
            wx.Panel.__init__(self, parent, style=wx.BORDER_SUNKEN)
            panel = wx.Panel(self, -1)
            vbox = wx.BoxSizer(wx.VERTICAL)
            vbox.Add(panel, 1, wx.EXPAND | wx.ALL, 10)
            self.SetSizer(vbox)
            panel1 = wx.Panel(panel, -1,style=wx.BORDER_SUNKEN)
            #panel2 = wx.Panel(panel, -1,style=wx.BORDER_SUNKEN)
            vbox2 = wx.BoxSizer(wx.HORIZONTAL)
            ###STILL WORKING ON THIS SECTION - WILL BE MOVED OFF SCRIPT LATER ON
            list = wx.ListCtrl(panel,style=wx.LC_REPORT|wx.SUNKEN_BORDER)
            list.InsertColumn(0,"Model Name")
            list.InsertColumn(1,"Security")
            list.InsertColumn(2,"Current Drawdown")
            list.InsertColumn(3,"P&L")
            list.InsertColumn(4,"Model Status")
            list.SetColumnWidth(0, 175)
            list.SetColumnWidth(1, 175)
            list.SetColumnWidth(2, 175)
            list.SetColumnWidth(3, 175)
            list.SetColumnWidth(4, 175)
            self.index = 0     
            vbox2.Add(panel1, 2, wx.EXPAND | wx.ALL, 1)
            vbox2.Add(list, 8, wx.EXPAND | wx.ALL, 1)
            panel.SetSizer(vbox2)
            self.button = wx.Button(panel1, label="Model 1", pos=(20, 20),size=(180, 60), style=wx.STAY_ON_TOP)
            #self.Bind(wx.EVT_BUTTON, self.m1Thread, self.button)
     
  
                        
    class Choicebook(wx.Notebook):
        def __init__(self, parent):
            wx.Notebook.__init__(self, parent, wx.ID_ANY)
            #self.AddPage(tab1(self), "Model Directory/Editor")
            #self.AddPage(tab2(self), "Position/Risk Metrics")
            #self.AddPage(tab3(self), "Charting")
            self.AddPage(tab4(self), "Model Status")

    class tradingProgram(wx.Frame):
        def __init__(self, parent, id, title):
            wx.Frame.__init__(self, parent, id, title, size=(1380, 850))
            panel = wx.Panel(self)
            notebook = Choicebook(panel)
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
            panel.SetSizer(sizer)
            self.Layout()
            self.Show()

            
#This is standardised code required to run the panel      
    app = wx.App(redirect = False)
    frame=tradingProgram(None, -1, 'A line chart')
    frame.Show()
    app.MainLoop()