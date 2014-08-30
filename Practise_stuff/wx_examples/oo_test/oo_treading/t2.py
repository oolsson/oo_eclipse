
import time
import threading


class th(threading.Thread):
    def __init__(self,xxx):
        threading.Thread.__init__(self)
        self.xxx=xxx
    def run(self):
        for i in range(1,5):
            time.sleep(1)
            print self.xxx

thr1 =th('ppp') #initiates the object back and sets the xxx variable to 'ppp'
thr1.start()    # starts running the thread
thr2 =th('oskar')
thr2.start()


print 'tt'
time.sleep(2)   #  
thr1.join()     #make sure that wait for thead to finish before ceep prosessing
print 'yy'
