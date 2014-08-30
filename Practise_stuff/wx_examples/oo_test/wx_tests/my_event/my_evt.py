import wx
import time
import my_evt_extra

class TwoButtonEvent(wx.PyCommandEvent):
    def __init__(self, evtType, id):
        wx.PyCommandEvent.__init__(self, evtType, id)
        self.clickCount = 0
        print 'init'

    def GetClickCount(self):
        print 'p'
        return self.clickCount
    

    def SetClickCount(self, count):
        print 'pp'
#         time.sleep(11)
#         print 'rrr'
        
        self.clickCount = count

myEVT_TWO_BUTTON = wx.NewEventType()
EVT_TWO_BUTTON = wx.PyEventBinder(myEVT_TWO_BUTTON, 1)
evt = TwoButtonEvent(myEVT_TWO_BUTTON, -1)

class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',size=(290, 290)) 
        self.x=0


        p1=wx.Panel(self,-1,(40,40),(40,40))
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
        print my_evt_extra.testt()
        
    def b1(self, event):
        self.algo = wx.Timer(self)
        self.algo.Start(1000)
        self.Bind(wx.EVT_TIMER,self.a1,self.algo)
        print 1
        
    def a1(self,x):
        self.x +=1
        print self.x
        if self.x ==1:
            pass
#             self.evt = TwoButtonEvent(myEVT_TWO_BUTTON, self.GetId())
#             print self.GetId()
        elif self.x % 3 ==0:
            print self.x
#             self.evt.SetClickCount(self.x)
#             evt = TwoButtonEvent(myEVT_TWO_BUTTON, self.GetId())
#             self.GetEventHandler().ProcessEvent(self.evt)
            evt.SetClickCount(self.x)
            self.GetEventHandler().ProcessEvent(evt)
        

if __name__ == '__main__':
  
    app = wx.App(0)
    o_frame=ToolbarFrame(parent=None,id=-1)
    o_frame.Show()
    app.MainLoop()
