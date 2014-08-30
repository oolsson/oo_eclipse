import time
import threading

'''
the way the treading objrct is written below it creates the object and takes the function ans arguments as inputs, 
arguments is given as a tuple
'''
class th(threading.Thread):
    def __init__(self, func,threadID, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.threadID = threadID
    def run(self):
        apply(self.func, self.args)
    def stop(self):
        self._stop.set()

def wh(*args):
    for arg in args:
        #print arg
        time.sleep(1)

    

thr1 =th(wh,'pp',(1,'we',1,1,1,1,1,1,1,1,1)) #initiates the object back and sets the xxx variable to 'ppp'       
thr2 =th(wh,'ll',(2,'oop',2,2,2,2,2,2,2,2))        
thr1.start()    # starts running the thread
thr2.start()
print 'd.isAlive()', thr1.isAlive()
for t in threading.enumerate():
    print t.getName()



print 'property -----------------------------------------' 

thr1.setName('fist t')


#for property, value in vars(thr1).iteritems():
#    print property, ": ", value
    
for t in threading.enumerate():
    print t.getName()
    
#thr2.threading.cancel()
thr1.join()
print 'first thread', thr1.isAlive()
print 'ccol'

