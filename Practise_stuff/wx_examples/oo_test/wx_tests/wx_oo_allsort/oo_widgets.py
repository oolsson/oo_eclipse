import wx
from wx.lib.pubsub import Publisher
import oo_dialogbox

class tab4(wx.Panel): 
    def __init__(self, parent):
        ww=wx.Panel.__init__(self, parent, style=wx.BORDER_SUNKEN)
        
        #static text widget----------------------------------------------------------
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, label='wx.StaticText', pos=(15, 15))
        heading.SetFont(font)
        
        wx.StaticLine(self, pos=(25, 50), size=(500,1))
        
        rtb = wx.ToggleButton(self, label='toggle', pos=(15, 65))
        rtb.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleRed)
        
        wx.StaticBox(self, -1, 'Personal Info', pos=(15, 110), size=(240, 30))
        cbox2=wx.CheckBox(self, -1 ,'Male', (15, 150))
        cbox=wx.CheckBox(self, -1 ,'Married', (15, 170))
        cbox.SetValue(True)
        cbox.Bind(wx.EVT_CHECKBOX, self.ShowOrHideTitle)
        
        
        wx.StaticText(self, -1, 'Age', (15, 220))
        wx.SpinCtrl(self, -1, '1', (15, 240), (60, -1), min=1, max=120)
        wx.Button(self, 1, 'Ok', (15, 275), (60, -1))
        
        distros = ['Ubuntu', 'Arch', 'Fedora', 'Debian', 'Mint']
        cb = wx.ComboBox(self, pos=(15, 320), choices=distros, 
            style=wx.CB_READONLY)
        
        slider = wx.Slider(self, 5, 6, 1, 10, (15, 360), (110, -1))
        
        
        slider.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
        cb.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
        cbox.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
        rtb.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
        heading.Bind(wx.EVT_ENTER_WINDOW, self.OnWidgetEnter)
        
        
        
    def OnWidgetEnter(self, e):
        name = e.GetEventObject().GetClassName()
        print (name + ' widget')
#        sb.SetStatusText(name + ' widget')
        e.Skip()    
        
    def ShowOrHideTitle(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue() 
        if isChecked:
            self.SetBackgroundColour('blue')            
        else: 
            self.SetBackgroundColour('green') 
        
    def ToggleRed(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        if isPressed:
            print 'pressed'
        else:
            print 'not pressed' 
            

        
class tab2(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.BORDER_SUNKEN)
        self.SetBackgroundColour('red')
        b1 = wx.Button(self, label="Change Security", pos=(1, 1),size=(180, 60), style=wx.STAY_ON_TOP)
        self.Bind(wx.EVT_BUTTON, self.OnButton, b1)
        
    def OnButton(self, evt):
        dlg = oo_dialogbox.SecuritySelection(None, -1) 
        dlg.Show()

class Choicebook(wx.Notebook):

    #----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, wx.ID_ANY)
        # Create the first tab and add it to the notebook
        self.AddPage(tab2(self), "Model Directory/Editor")
        # Create and add the second tab
        self.AddPage(tab4(self), "Position/Risk Metrics")



        self.Bind(wx.EVT_CHOICEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_CHOICEBOOK_PAGE_CHANGING, self.OnPageChanging)

    #----------------------------------------------------------------------
    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()

    #----------------------------------------------------------------------
    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        event.Skip()