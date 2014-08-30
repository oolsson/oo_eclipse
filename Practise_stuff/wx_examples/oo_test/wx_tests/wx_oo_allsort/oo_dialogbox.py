
import wx
from wx.lib.pubsub import Publisher


class SecuritySelection(wx.Dialog):  
# used to return the contract in the correct formate to makestkcontract
    def GetContract(self):
        retval1 = str(self.text.GetValue()) 
        retval2  = str(self.text1.GetValue()) 
        retval3  = str(self.text2.GetValue())
        retval4  = str(self.text3.GetValue())
        retval = (retval1, retval2, retval3, retval4)
        return retval
#used to return the number of candles that the user would like to see on the chart
    def GetOtherData(self):
        retval5  = int(self.text4.GetValue())
        retval6  = str(self.text5.GetValue())
        retval7  = str(self.text6.GetValue())
        retval8  = int(self.text8.GetValue())
        retval9 = self.text7.GetValue()
        retval1 = (retval5, retval6, retval7, retval8, retval9)
        print retval1
        return retval1

#retrieve data from the dialog box and prepare for sending to another class to be used to change chart
    def ReturnValue(self, event):
        msg = self.GetContract()
        msg1 = self.GetOtherData()
#publisher must be named (anything) and then what you would like to send (ie msg, msg1)
        Publisher().sendMessage(("show.mainframe"), msg)
        Publisher().sendMessage(("show.candlesticks"), msg1)
        self.Close()
                        
    def __init__(self, parent, id): 
        wx.Dialog.__init__(self, parent, id, size=(400,400))             
# set the layout of the dialog box with inputs and various comboboxes.
        label = wx.StaticText(self, -1, "Currency",pos=(10,10))
        self.text = wx.TextCtrl(self, -1, "", size=wx.DefaultSize, pos=(170,10))
        self.text.SetValue("USD")
        label1 = wx.StaticText(self, -1, "Type",pos=(10,30))
        self.text1 = wx.TextCtrl(self, -1, "", size=wx.DefaultSize, pos=(170,30))
        self.text1.SetValue("CASH")
        label2 = wx.StaticText(self, -1, "Exchange",pos=(10,50))
        self.text2 = wx.TextCtrl(self, -1, "", size=wx.DefaultSize, pos=(170,50))
        self.text2.SetValue("IDEALPRO")
        label3 = wx.StaticText(self, -1, "Base Currency",pos=(10,70))
        self.text3 = wx.TextCtrl(self, -1, "", size=wx.DefaultSize, pos=(170,70))
        self.text3.SetValue("JPY")
        label4 = wx.StaticText(self, -1, "No. of Candlesticks",pos=(10,90))
        self.text4 = wx.TextCtrl(self, -1, "", size=wx.DefaultSize, pos=(170,90))
        self.text4.SetValue("160")
        duration = ['1 Y', '6 M', '3 M', '1 M', '1 W','2 D', '1 D']
        barsize = ['1 day','1 hour', '30 mins', '15 mins', '3 mins', '2 mins', '1 min','30 secs']
        label5 = wx.StaticText(self, -1, "Duration",pos=(10,110))
        self.text5 = wx.ComboBox(self,size=wx.DefaultSize,choices=duration,pos=(170,110))
        self.text5.SetValue('1 W')
        label6 = wx.StaticText(self, -1, "Bar Size",pos=(10,130))
        self.text6 = wx.ComboBox(self,size=wx.DefaultSize,choices=barsize,pos=(170,130))
        self.text6.SetValue('1 hour')            
        self.text7 = wx.CheckBox(self, label='Moving Average', pos=(10, 160))
        label8 = wx.StaticText(self, -1, "Moving Average Periods",pos=(10,180))
        self.text8 = wx.TextCtrl(self, -1, "", size=wx.DefaultSize, pos=(170,180))
        self.text8.SetValue("10")
        self.button = wx.Button(self, wx.ID_OK, label="Save", pos=(100, 210),size=(80, 50))
        self.button1 = wx.Button(self,wx.ID_CANCEL, label="Close", pos=(200, 210),size=(80, 50)) 
        self.Bind(wx.EVT_BUTTON, self.ReturnValue, self.button)