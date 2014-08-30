
import wx
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import numpy as np
import wx.grid as gridlib


class o_Panel(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('White')  

        
        
class panel1(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(700, 300),pos= (100,20),style=wx.BORDER_SUNKEN)
        self.SetBackgroundColour('red') 
        

        
class panel2(wx.Panel):        
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(700, 300),pos= (100,400),style=wx.BORDER_SUNKEN)
        self.SetBackgroundColour('green') 


        

class TradingProgram(wx.Frame):
    def __init__(self, parent, title):
        super(TradingProgram, self).__init__(parent, title=title, 
            size=(260, 180))    
        self.InitUI()
        self.Centre()
        self.Show()
        
    def InitUI(self):
        
        panelo = o_Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(panelo, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(vbox)
          
        Panel1 = panel1(panelo)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(Panel1, 1, wx.EXPAND | wx.ALL, 10)
        panelo.SetSizer(vbox2)
        
        Panel2 = panel2(Panel1)
        vbox3 = wx.BoxSizer(wx.VERTICAL)
        vbox3.Add(Panel2, 1, wx.EXPAND | wx.ALL, 10)
        Panel1.SetSizer(vbox3)
        


            
app = wx.App(redirect = False)
frame=TradingProgram(None, title='fremesetup')
frame.Show()
app.MainLoop()