'''
Created on Feb 11, 2012

@author: oo
'''
import time
#good website   http://effbot.org/librarybook/time.htm


print time.clock()  #prints CPU Time

now = time.time()
print now
print now, "seconds since", time.gmtime(0)[:6]
print "- local time:", time.localtime(now)
print "- utc:", time.gmtime(now)

print "--------------------------------------------"

now = time.localtime(time.time())
print now
print time.asctime(now)
print time.strftime("%y/%m/%d %H:%M", now)
print time.strftime("%H:%M", now)
print time.strftime("%a %b %d", now)
print time.strftime("%c", now)
print time.strftime("%I %p", now)
print time.strftime("%Y-%m-%d %H:%M:%S %Z", now)
print time.strftime("%Y-%m-%d %H:%M:%S", now)

print '-------measuring time----------'
def procedure():
    time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print time.clock() - t0, "seconds process time"

# measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"

'''
class minuteFormatter(Formatter):
    def __init__(self, dates, fmt='%H:%M'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        'Return the label for time x at position pos'
        ind = int(round(x))
        if ind>=len(self.dates) or ind<0: return ''

        return time.strftime(self.fmt, time.localtime(int(self.dates[ind])))
    
def convertExecTime(eTime):
    stdTime=time.strptime(eTime,"%Y%m%d  %H:%M:%S")
    return time.mktime(stdTime)
'''