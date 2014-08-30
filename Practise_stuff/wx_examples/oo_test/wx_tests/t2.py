import wx

class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',size=(900, 900)) 


        p1=wx.Panel(self,-1,(40,40),(140,60))
        p2=wx.Panel(self,-1)
        p1.SetBackgroundColour('Gray')
        p2.SetBackgroundColour('Red')
        
        mb2=wx.Button(p2,-1,'p2')
        mb=wx.Button(p1,-1,'p1')
        tt=wx.TextCtrl(p2, -1, "", style=wx.TE_READONLY)
        
        Hbox=wx.BoxSizer(wx.HORIZONTAL)
        Hbox.AddF(p1, wx.SizerFlags().Expand().Border(wx.ALL, 10).Proportion(2))
        Hbox.Add(p2, 2, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(Hbox)
        
        Vbox=wx.BoxSizer(wx.VERTICAL)
        Vbox.AddF(mb2, wx.SizerFlags().Expand().Border(wx.ALL, 10).Proportion(2))
        Vbox.AddF(tt, wx.SizerFlags().Expand().Border(wx.ALL, 10).Proportion(2))
        p2.SetSizer(Vbox)
        
        mb2.Bind(wx.EVT_BUTTON, self.b1, mb2)
        
    def b1(self, event):
        print 'ppppp'
        

if __name__ == '__main__':
  
    app = wx.App(0)
    o_frame=ToolbarFrame(parent=None,id=-1)
    o_frame.Show()
    app.MainLoop()