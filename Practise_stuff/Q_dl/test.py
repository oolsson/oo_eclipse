import Quandl
data=Quandl.get(["NSE/OIL.4"],trim_start ="March 2005", trim_end="December 2010", authtoken="XgkWhb4QXS6cgd4AxWSz",collapse="monthly")
print data.tail(11)
print data.index[-1]-data.index[0]

a=data.index[-1]-data.index[0]
b=len(data)


print a.days
print b
print b/float(a.days)


if b/float(a.days)>0.9:
    pa=365
elif b/float(a.days)>0.5:
    pa=252
elif b/float(a.days)>0.1:
    pa=52
elif b/float(a.days)>0.02:
    pa=12
else:
    pa=1
    
print pa