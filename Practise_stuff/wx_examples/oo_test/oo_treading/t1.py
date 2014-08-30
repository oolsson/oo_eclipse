
import time

class className:
    def createName(self,name):
        self.name=name
    def displayName(self):
        return self.name
    def saying(self,sl):
        for i in range(1,5):
            time.sleep(sl)
            print 'tread %s' % self.name +  ' ' +str(i)


o1=className()
o1.createName('oskar')
o2=className()
o2.createName('hakan')

o1.saying(1)
o2.saying(2)


