#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
        
    def InitUI(self):   

        self.pnl = wx.Panel(self)
        Hbox=wx.BoxSizer(wx.HORIZONTAL)
        Hbox.Add(self.pnl, 2, wx.EXPAND | wx.ALL, 2)
        self.SetSizer(Hbox)

        
        wx.StaticText(self.pnl, label='Convert Fahrenheit temperature to Celsius', 
            pos=(20,20))
        wx.StaticText(self.pnl, label='Fahrenheit: ', pos=(20, 80))
        wx.StaticText(self.pnl, label='Celsius: ', pos=(20, 150))
        
        self.celsius = wx.StaticText(self.pnl, label='', pos=(150, 150))
        self.sc = wx.SpinCtrl(self.pnl, value='0', pos=(150, 75), size=(60, -1))
        self.sc.SetRange(-459, 1000)
        
        btn = wx.Button(self.pnl, label='Compute', pos=(70, 230))
        btn.SetFocus()
        cbtn = wx.Button(self.pnl, label='Close', pos=(185, 230))

        btn.Bind(wx.EVT_BUTTON, self.OnCompute)
        cbtn.Bind(wx.EVT_BUTTON, self.OnClose)
           
        self.SetSize((350, 310))
        self.SetTitle('wx.SpinCtrl')
        self.Centre()
        self.Show(True)          
        
    def OnClose(self, e):
        
        self.Close(True)    
        
    def OnCompute(self, e):
        
        fahr = self.sc.GetValue()
        cels = round((fahr - 32) * 5 / 9.0, 2)
        self.celsius.SetLabel(str(cels))        
                      
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == '__main__':
    main()