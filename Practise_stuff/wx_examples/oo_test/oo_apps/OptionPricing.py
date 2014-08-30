import wx
from wx.lib.pubsub import Publisher
import wx
import time
import BS






class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        f1=wx.Frame.__init__(self, *args, **kwargs)
        p1 = wx.Panel(self)
        p1.SetBackgroundColour('White')
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(p1, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer)
        
        label6 = wx.StaticText(p1, -1, "call/put",pos=(10,10))
        self.type = wx.TextCtrl(p1, -1, "", size=wx.DefaultSize, pos=(170,10))
        self.type.SetValue("call")
        
        label = wx.StaticText(p1, -1, "Spot Price",pos=(10,40))
        self.spotprice = wx.TextCtrl(p1, -1, "", size=wx.DefaultSize, pos=(170,40))
        self.spotprice.SetValue('100')
        
        label1 = wx.StaticText(p1, -1, "Strike Price",pos=(10,70))
        self.strikeprice = wx.TextCtrl(p1, -1, "", size=wx.DefaultSize, pos=(170,70))
        self.strikeprice.SetValue('100')
        
        label2 = wx.StaticText(p1, -1, "Volatility",pos=(10,100))
        self.volatility = wx.TextCtrl(p1, -1, "", size=wx.DefaultSize, pos=(170,100))
        self.volatility.SetValue('0.2')
        
        label4 = wx.StaticText(p1, -1, "time 2 exp",pos=(10,130))
        self.time2exp = wx.TextCtrl(p1, -1, "", size=wx.DefaultSize, pos=(170,130))
        self.time2exp.SetValue('1')
        
        label3 = wx.StaticText(p1, -1, "int rate",pos=(10,160))
        self.intrate = wx.TextCtrl(p1, -1, "", size=wx.DefaultSize, pos=(170,160))
        self.intrate.SetValue('0.05')
    
        label5 = wx.StaticText(p1, -1, "dividend",pos=(10,190))
        self.dividend = wx.TextCtrl(p1, -1, "", size=wx.DefaultSize, pos=(170,190))
        self.dividend.SetValue('0')
        
        label7 = wx.StaticText(p1, -1, "price",pos=(10,280))
        self.price = wx.TextCtrl(p1, -1, "", size=wx.DefaultSize, pos=(170,280))
                
        bt1=wx.Button(p1,-1,'calculate',pos=(50,230))
        bt1.Bind(wx.EVT_BUTTON, self.bt_e1, bt1)

        
    def bt_e1(self,e):
        self.price.SetValue('')
        val = [self.type.GetValue(), self.spotprice.GetValue(), self.strikeprice.GetValue(), self.volatility.GetValue()
               , self.time2exp.GetValue(), self.intrate.GetValue(), self.dividend.GetValue()]
        obj=BS.BS(val[0],val[1],val[2],val[3],val[4],val[5],val[6])
        val2 = obj.Price()
        self.price.SetValue(str(val2))

        
 

if __name__ == '__main__':
  
    app = wx.App(0)
    o_frame=MainFrame(parent=None,id=-1,size=(900, 900))
    o_frame.Show()
    app.MainLoop()