import Quandl
data=Quandl.get(["OSKAR_OLSSON/VAL_EWW"],trim_start ="July 2014", trim_end="December 2014", authtoken="XgkWhb4QXS6cgd4AxWSz",collapse="daily")


print data.tail(11)
print data.index[-1]-data.index[0]