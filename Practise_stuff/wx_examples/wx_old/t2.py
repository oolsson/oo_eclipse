
import wx
import wx.grid as gridlib

class TestTable(wx.grid.PyGridTableBase):
    def __init__(self):
        gridlib.PyGridTableBase.__init__(self)
        self.rowLabels = ["uno", "dos", "tres", "quatro", "cinco"]
        self.colLabels = ["homer", "marge", "bart", "lisa", "maggie"]


    def GetNumberRows(self):
        return 5

    def GetNumberCols(self):
        return 5

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        return "(%s,%s)" % (self.rowLabels[row], self.colLabels[col])

    def SetValue(self, row, col, value):
        pass

    def GetColLabelValue(self, col):
        return self.colLabels[col]

    def GetRowLabelValue(self, row):
        return self.rowLabels[row]

class CustTableGrid(gridlib.Grid):
    def __init__(self, parent):
        gridlib.Grid.__init__(self, parent, -1)

        table = TestTable()

        # The second parameter means that the grid is to takeownership of the
        # table and will destroy it when done.  Otherwise you wouldneed to keep
        # a reference to it and call it's Destroy method later.
        self.SetTable(table, True)

        self.SetRowLabelSize(0)
        self.SetMargins(0,0)
        self.AutoSizeColumns(False)

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Grid Table",
                          size=(500,200))
        panel1 = wx.Panel(self, -1)
        panel2 = wx.Panel(self, -1)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        hbox1.Add(panel1, 1, wx.EXPAND | wx.ALL, 3)
        hbox1.Add(panel2, 1, wx.EXPAND | wx.ALL, 3)


        table = CustTableGrid(panel2)
        tblSizer = wx.BoxSizer(wx.VERTICAL)
        tblSizer.Add(table, 1, wx.ALL|wx.EXPAND, 5)
        panel2.SetSizer(tblSizer)

        self.SetSizer(hbox1)

app = wx.PySimpleApp()
frame = TestFrame()
frame.Show()
app.MainLoop()