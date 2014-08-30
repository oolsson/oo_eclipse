import wx
import sys
import time
import datetime
import pylab
import numpy as np
import os
import random
import sys
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib


#-- message handlers---------------------------------------------------------


#classes------------------------------------------------------------------
class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl
    def write(self,string):
        self.out.WriteText(string)

class o_Panel(wx.Panel): 
    def __init__(self, parent, size_x, pos_x):
        wx.Panel.__init__(self, parent,size=size_x,pos=pos_x,style=wx.BORDER_SUNKEN)
 #Functions-----------------------------------------------------------------------------


        
        
class ToolbarFrame(wx.Frame):
    #-------------Layout--------------------------------------------------------------------------------------
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars', size=(1000, 800))
        

        
        panel1 = o_Panel(self, (0, 0), (0,0))
        panel1.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        
        log = wx.TextCtrl(self, pos=(3, 600), size=(970, 100),
                          style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
        redir=RedirectText(log)
        sys.stdout=redir
        
        panel2 = o_Panel(self, (750, 250), (250,10))          #self can be switched for panel if you want the panel to be parent
        panel2.figure = matplotlib.figure.Figure(figsize=(9.3, 3.25))
        panel2.figure.suptitle("Dynamic Price Chart Goes Here", fontsize=14)
        panel2.axes = panel2.figure.add_subplot(111)
        t = np.arange(0, 2*np.pi, 0.1)
        line, = panel2.axes.plot(t, np.sin(t))
                
        figure = FigureCanvas(panel2, -1, panel2.figure)

        def update_line(self):
            line.set_ydata(np.sin(t+update_line.i/10.))
            figure.draw()
            print ['hello',t[-1]]                # redraw the canvas
            update_line.i += 1
        update_line.i = 0

        panel2.timer = wx.Timer(panel2)
        panel2.timer.Start(100)
        panel2.Bind(wx.EVT_TIMER,update_line,panel2.timer)
#-panel3---------------------------------------------------------------------------
        panel4 = o_Panel(self, (750, 250), (250,300))          #self can be switched for panel if you want the panel to be parent
        panel4.figure = matplotlib.figure.Figure(figsize=(9.3, 3.25))
        panel4.figure.suptitle("EQ Chart", fontsize=14)
        panel4.axes = panel4.figure.add_subplot(111)
        t = np.arange(0, 2*np.pi, 0.1)
        line2, = panel4.axes.plot(t, np.sin(t))                
        figure2 = FigureCanvas(panel4, -1, panel4.figure)
        

     
   
        
        panel3 = o_Panel(self, (200, 400), (10,150))          #self can be switched for panel if you want the panel to be parent
        heading = wx.StaticText(panel3, -1, 'Positions') 
        wx.StaticText(panel3, -1, 'AUD/USD', (5, 30))
        wx.StaticText(panel3, -1, '50,000', (150, 30))
        wx.StaticText(panel3, -1, 'AUD/EUR', (5, 60))
        wx.StaticText(panel3, -1, '70,000', (150, 60))  
        wx.StaticText(panel3, -1, 'AUD/JPY', (5, 90))
        wx.StaticText(panel3, -1, '50,000', (150, 90))       
        
        
        menuBar = wx.MenuBar()                                       #creates the menuebar
        self.SetMenuBar(menuBar)                                     #attaches the menuebar to the frame       
        menu1 = wx.Menu()                                            #creates a submenue menue1
        menuBar.Append(menu1, "&File")                   #attaches the submenue1 to the menuebar under the name file 
        
        button = wx.Button(panel1, -1, "Connect", pos=(10, 10), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.o_Connect, button)
        button = wx.Button(panel1, -1, "DisConnect", pos=(10, 60), size=(100, 40))
        self.Bind(wx.EVT_BUTTON, self.o_DisConnect, button)
        
    

        print 'rrr'
        self.Show(True)
        
    #-----Functionality-------------------------------------------------------------------------------    
    def o_Connect(self, event):
        self.Close(True)
    def o_DisConnect(self, event):
        self.Close(True)


    
if __name__ == '__main__':
    app = wx.PySimpleApp(redirect = True)
    frame = ToolbarFrame(parent=None, id=-1)
    app.MainLoop()