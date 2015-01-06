import Quandl
from datetime import datetime
import datetime as dt

end=dt.date.today()
start=dt.date(2014,12,20)
print end
print start

# # data=Quandl.get(["YAHOO/INDEX_GSPC.6"],trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz",collapse="monthly")
# data=Quandl.get(["YAHOO/INDEX_GSPC.6"],trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
data=Quandl.get("NSE/OIL", trim_start=start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
print data
# print len(data.index)
# print