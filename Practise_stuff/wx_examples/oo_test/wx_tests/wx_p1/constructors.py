
import wx



#sizers--------------------------------------
  
#------------Boxsizer    
def oo_Hbox(self, *args, **kwargs):
        Hbox=wx.BoxSizer(wx.HORIZONTAL)
        for arg in args:
            Hbox.Add(arg, 1, wx.EXPAND | wx.ALL, 10)
        for key in kwargs:
            pass
        self.SetSizer(Hbox)
        
def oo_Vbox(self, *args, **kwargs):
        Vbox=wx.BoxSizer(wx.VERTICAL)
        for arg in args:
            Vbox.Add(arg, 1, wx.EXPAND | wx.ALL)
            #Vbox.Add(arg, 1, wx.EXPAND | wx.ALL, 10)
        for key in kwargs:
            pass
        self.SetSizer(Vbox)
        

        
