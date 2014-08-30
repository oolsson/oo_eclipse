import time
import threading

'''
the way the treading objrct is written below it creates the object and takes the function ans arguments as inputs, 
arguments is given as a tuple
'''
class th(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
    def run(self):
        apply(self.func, self.args)

def wh(x,e,t):
    print x
    time.sleep(1)
    print e
    time.sleep(1)
    print t
    

thr1 =th(wh,(1,'we',2)) #initiates the object back and sets the xxx variable to 'ppp'       
thr2 =th(wh,(4,'oop',99))        
thr1.start()    # starts running the thread
thr2.start()

thr1.join()

print 'ccol'

