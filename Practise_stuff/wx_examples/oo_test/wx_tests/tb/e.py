import wx
import time
import generictable


class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',size=(900, 900)) 
        self.SetBackgroundColour('White')
        
        data=[[1, 2, 2],
              [3,4,5],
              [1,1,1]]
        grid = wx.grid.Grid(self)
        T=generictable.GenericTable(data)
        grid.SetTable(T, False)


if __name__ == '__main__':
  
    app = wx.App(0)
    o_frame=ToolbarFrame(parent=None,id=-1)
    o_frame.Show()
    app.MainLoop()