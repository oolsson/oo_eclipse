import wx

def one():
    print 1 
def two():
    print 2 

class zero():
    def __init__(self):
        print 3

class ListBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'List Box Example', 
                size=(350, 300))
        panel = wx.Panel(self, -1)

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                      'twelve', 'thirteen', 'fourteen']

        self.listBox = wx.ListBox(panel, -1, (20, 20), (80, 120), sampleList, 
                wx.LB_MULTIPLE)
        self.listBox.SetSelection(0)
        #self.Bind(wx.EVT_LISTBOX, self.OnSelection, self.myListBox)
        
        
        self.button = wx.Button(panel, -1, "Hello", pos=(200, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()
        print self.listBox

    def OnClick(self, event):
        self.button.SetLabel("Clicked")
        items= self.listBox.GetItems()
        sel =self.listBox.GetSelections()
        
        methods = {'one': one,
                   'two': two,
                   'zero':zero}
        
        for i in sel:
            #print i
            #print items[i]
            method_name = str(items[i])
            if method_name in methods:
                methods[method_name]() # + argument list of course
            else:
                raise Exception("Method %s not implemented" % method_name)
#        possibles = globals().copy()
#        possibles.update(locals())
#        method = possibles.get(method_name)()

                
if __name__ == '__main__':
    app = wx.PySimpleApp()
    ListBoxFrame().Show()
    app.MainLoop()                        
