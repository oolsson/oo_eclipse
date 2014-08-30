import wx
import time


class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',size=(900, 900)) 
        self.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        toolbar.SetBackgroundColour('Blue')
        
        menuBar = wx.MenuBar(   )
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        
        self.SetMenuBar(menuBar)
        
        
        #mybut=wx.Button(self,-1,'ttt')
        #mybut.SetBackgroundColour('Orange')
        
        #print 'ppp'
        #o=oo(2)
        #print o
        #print o.det
        
#        p1=wx.Panel(self,-1,(40,40),(140,60))
#        p2=wx.Panel(self,-1)
#        p1.SetBackgroundColour('Gray')
#        p2.SetBackgroundColour('Red')
#        #mb2=mybut(self,-1)
#        mb2=wx.Button(p2,-1,'ttt')
#        mb=mybut(p1,-1)
#        tt=wx.TextCtrl(p2, -1, "", style=wx.TE_READONLY)
        ShowMessage(1)
#        
#        Hbox=wx.BoxSizer(wx.HORIZONTAL)
#        Hbox.AddF(p1, wx.SizerFlags().Expand().Border(wx.ALL, 10).Proportion(2))
#        Hbox.Add(p2, 2, wx.EXPAND | wx.ALL, 10)
#        self.SetSizer(Hbox)
#        
#        Vbox=wx.BoxSizer(wx.VERTICAL)
#        Vbox.AddF(mb2, wx.SizerFlags().Expand().Border(wx.ALL, 10).Proportion(2))
#        Vbox.AddF(tt, wx.SizerFlags().Expand().Border(wx.ALL, 10).Proportion(2))
#        Vbox.AddF(w, wx.SizerFlags().Expand().Border(wx.ALL, 10).Proportion(2))
#        p2.SetSizer(Vbox)
def ShowMessage(self):
    wx.MessageBox('Download completed', 'Info', 
        wx.OK | wx.ICON_INFORMATION)
        
        
class WatchlistSelection(wx.Dialog):        
    def __init__(self, parent, id): 
        wx.Dialog.__init__(self, parent, id)             
        label = wx.StaticText(self, -1, "Currency",pos=(10,10))
        self.text = wx.TextCtrl(self, -1, "", size=wx.DefaultSize, pos=(170,10))
        self.text.SetValue("USD")
        self.button = wx.Button(self, wx.ID_OK, label="Save", pos=(100, 210),size=(80, 50))
        self.button1 = wx.Button(self,wx.ID_CANCEL, label="Close", pos=(200, 210),size=(80, 50)) 
        #self.Bind(wx.EVT_BUTTON, self.ReturnValue, self.button)          
        
class oo():
    det='got'
    def __init__(self,ss):
        print 'ooo'
        print ss
        
class mybut(wx.Button):
    def __init__(self,parent,id=-1):
        wx.Button.__init__(self,parent,id)
         
              
  


if __name__ == '__main__':
  
    app = wx.App(0)
    o_frame=ToolbarFrame(parent=None,id=-1)
    o_frame.Show()
    app.MainLoop()