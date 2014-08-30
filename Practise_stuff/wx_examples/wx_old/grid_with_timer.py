import wx
import wx.grid
import thread
import time
import random
 
 
class TestTable(wx.grid.PyGridTableBase):
    def __init__(self):
        wx.grid.PyGridTableBase.__init__(self)
        self.data ={}
        #self.SetValue(1, 1, 5)
 
    # these five are the required methods
    def GetNumberRows(self):
        return 50
 
    def GetNumberCols(self):
        return 50
 
    def IsEmptyCell(self, row, col):
        return self.data.get((row, col)) is None
 
    def GetValue(self, row, col):
        value = self.data.get((row, col))
        if value is not None:
            return value
        else:
            return ''
 
    def SetValue(self, row, col, value):
        self.data[(row,col)] = value
       

 
class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Grid Table",
                          size=(640,480))
        grid = wx.grid.Grid(self)
        table = TestTable()
        grid.SetTable(table, False)
        
        dict1={'a': 1, 'b': 2, 'c': 3}

        
        def ll():
            counter = 0
            for key in sorted(dict1):
                print(key, '=>', dict1[key])
                table.SetValue(counter, 2, dict1[key])
                table.SetValue(counter, 1, key)
                counter +=1
        ll()
           
       
        def newnumber(self):
            table.SetValue(3, 3, random.random())
            #grid.SetTable(table, True)
            grid.ForceRefresh()
            print random.random()
      
        self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER,newnumber,self.timer)


       
 
app = wx.PySimpleApp()
frame = TestFrame()
frame.Show()
app.MainLoop()