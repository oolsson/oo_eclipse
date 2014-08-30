import wx
from wx.lib.pubsub import Publisher
import wx
import time
import oo_widgets




class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        panel = wx.Panel(self) 
        panel.SetBackgroundColour('White')
        notebook = oo_widgets.Choicebook(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        panel.SetSizer(sizer)
        sb = self.CreateStatusBar()

#


if __name__ == '__main__':
  
    app = wx.App(0)
    o_frame=MainFrame(parent=None,id=-1,size=(900, 900))
    o_frame.Show()
    app.MainLoop()