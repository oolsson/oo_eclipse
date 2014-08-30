#!/usr/bin/env python
import wx


class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars',
                          size=(400, 400))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        
        menuBar = wx.MenuBar()                                       #creates the menuebar
        self.SetMenuBar(menuBar)                                     #attaches the menuebar to the frame
        
        menu1 = wx.Menu()                                            #creates a submenue menue1
        menuBar.Append(menu1, "&File")                   #attaches the submenue1 to the menuebar under the name file 
        
        menu2 = wx.Menu()
        menuBar.Append(menu2, "&Edit")
                                                    #creates a submenue menue2
        menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")     #creates a menueitem to submenue2
        menu2.Append(wx.NewId(), "C&ut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display Options")    
        
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()