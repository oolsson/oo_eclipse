import Quandl
from datetime import datetime
import datetime as dt

end=dt.datetime.today()
start=datetime(1980,1,1)

# data=Quandl.get(["YAHOO/INDEX_GSPC.6"],trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz",collapse="monthly")
data=Quandl.get(["YAHOO/INDEX_GSPC.6"],trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
print data.tail(11)
print data.index[-1]-data.index[0]
