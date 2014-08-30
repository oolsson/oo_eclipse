import wx
from wx.lib.pubsub import Publisher
import wx
import time
import constructors
import newframe



class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs) 
        self.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        toolbar.SetBackgroundColour('Blue')
        
        menuBar = wx.MenuBar(   )
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        
        self.SetMenuBar(menuBar)
        

        p1=wx.Panel(self,-1,(40,40),(140,60))
        p2=wx.Panel(self,-1)
        p1.SetBackgroundColour('Gray')
        p2.SetBackgroundColour('Red')
        p3=wx.Panel(self,-1)
        
        mybut=wx.Button(p1,-1,'newframe')


    
        tt=wx.TextCtrl(p1, -1, "", style=wx.TE_READONLY)
        constructors.oo_Vbox(self,p1,p2,p3,k='pp',k2='wx.EXPAND')


#        Hbox=wx.BoxSizer(wx.HORIZONTAL)
#        Hbox.AddF(p1, wx.SizerFlags().Expand().Border(wx.ALL, 10).Proportion(2))
#        Hbox.Add(p2, 2, wx.EXPAND | wx.ALL, 10)
#        self.SetSizer(Hbox)
#        

        constructors.oo_Vbox(p1,mybut,tt)
        newframe.Example(self, title="Create newframe") 

#        vbox=wx.BoxSizer(wx.VERTICAL)
#        
#        vbox.Add(gs, proportion=1, flag=wx.EXPAND)


if __name__ == '__main__':
  
    app = wx.App(0)
    o_frame=MainFrame(parent=None,id=-1,size=(900, 900))
    o_frame.Show()
    app.MainLoop()