import wx
from wx.lib.pubsub import Publisher
import wx
import time
import oo_widgets




class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        f1=wx.Frame.__init__(self, *args, **kwargs)
        p1 = wx.Panel(self)
        p2 = wx.Panel(self) 
        p1.SetBackgroundColour('White')
        p1.SetBackgroundColour('red')
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(p1, 1, wx.ALL|wx.EXPAND, 5)
        sizer.Add(p2, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer)
        
        label = wx.StaticText(p1, -1, "Currency",pos=(10,10))
        self.text = wx.TextCtrl(p1, -1, "", size=wx.DefaultSize, pos=(170,10))
        self.text.SetValue("USD")
        
        label1 = wx.StaticText(p2, -1, "Type",pos=(10,30))
        self.text1 = wx.TextCtrl(p2, -1, "", size=wx.DefaultSize, pos=(170,30))
        
        label3 = wx.StaticText(p2, -1, "value from publisher",pos=(10,100))
        self.text3 = wx.TextCtrl(p2, -1, "", size=wx.DefaultSize, pos=(170,100))
        
        
        bt1=wx.Button(p2,-1,'import',pos=(300,30))
        bt1.Bind(wx.EVT_BUTTON, self.bt_e1, bt1)
        
        bt2=wx.Button(p1,-1,'f2',pos=(310,10))
        bt2.Bind(wx.EVT_BUTTON, self.bt_e2, bt2)
        
        Publisher().subscribe(self.pub, ("show.oo"))
        #Publisher().subscribe(self.pub, ("show.mainframe")) 
        
    def bt_e1(self,e):
        print 'b1'
        val = self.text.GetValue()
        self.text1.SetValue(val)
        
    def bt_e2(self,e):
        f2=wx.Frame(parent=None,id=-1,size=(900, 900))
        self.label2 = wx.StaticText(f2, -1, "Currency",pos=(10,10))
        self.text2 = wx.TextCtrl(f2, -1, "", size=wx.DefaultSize, pos=(10,10))
        self.text2.SetValue("ffff")
        
        self.label4 = wx.StaticText(f2, -1, "pub",pos=(10,100))
        self.text4 = wx.TextCtrl(f2, -1, "", size=wx.DefaultSize, pos=(150,100))
        
        bt3=wx.Button(f2,-1,'export',pos=(300,10))
        bt3.Bind(wx.EVT_BUTTON, self.bt_e3, bt3)
        
        bt4=wx.Button(f2,-1,'ex_pub',pos=(300,100))
        bt4.Bind(wx.EVT_BUTTON, self.bt_e4, bt4)
        f2.Show()
        
    def bt_e3(self,e):
        val = self.text2.GetValue()
        print val
        self.text1.SetValue(val)
        
    def bt_e4(self,e):
        msg = self.text4.GetValue()
        Publisher().sendMessage(("show.oo"), msg)
        
    def pub(self, msg):
        print msg
        self.text3.SetValue(msg.data)
        
    





if __name__ == '__main__':
  
    app = wx.App(0)
    o_frame=MainFrame(parent=None,id=-1,size=(900, 900))
    o_frame.Show()
    app.MainLoop()
    
    
#Publisher().subscribe(self.showFrame, ("show.mainframe"))  
#
#def onSendAndClose(self, event):
#    """
#    Send a message and close frame
#    """
#    msg = self.msgTxt.GetValue()
#    Publisher().sendMessage(("show.mainframe"), msg)
#    self.Close()
#    
#def showFrame(self, msg):
#    """
#    Shows the frame and shows the message sent in the
#    text control
#    """
#    self.pubsubText.SetValue(msg.data)
#    frame = self.GetParent()
#    frame.Show()
