'''
Created on Feb 25, 2012

@author: oo
'''
import time

now = time.localtime(time.time())
print time.strftime("%c", now)
print now
print now[5]
print type(now)
#A=now ++ 2
while now[5]>20 and now[5]<39:
    if 2<4:
        print now[5]
        time.sleep(2)
        now = time.localtime(time.time())
    

    

