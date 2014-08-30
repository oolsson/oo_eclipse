    
import wx
import time 
import threading   
    
    
class th(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
    def run(self):
        apply(self.func, self.args)    
    
    
def ttest():
    while 1==1:
        print 'ok'
        time.sleep(2)
    
    
def getDataThread():
        thr4 =th(ttest())
        thr4.start()

getDataThread()