
import datetime as dt
from dateutil import parser

#d=['C:\\Users\\oo\\Documents\\AXP.csv', 'C:\\Users\\oo\\Documents\\BA.csv']
#end=d[0].find('.csv')
#start=d[0].find('Documents\\')+len('Documents\\')
#ticker=d[0][start:end]
#print start
#print end
#print ticker

num='22,222.00'
f=num.translate(None, '!,@#$')
print float(f)

d='1900/01/01'
print help(parser.parse(d))
d=parser.parse(d)
print d
print type(d)

print '------------'
p='2012/10/02'
dd=dt.datetime.strptime(p, '%Y/%m/%d')
print dd
print type(dd)

print 'new test------------'
p1='2013/08'
p2='2013/11'
p1=dt.datetime.strptime(p1, '%Y/%m')
p2=dt.datetime.strptime(p2, '%Y/%m')
print p1
td=p2-p1
days=int((td.days)/1)/28
# days, remainder = divmod(td.days, 22)
print days
print dt.datetime.now()  
