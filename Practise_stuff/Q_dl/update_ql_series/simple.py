import Quandl
from datetime import datetime
import datetime as dt

end=dt.datetime.today()
start=datetime(1980,1,1)

data=Quandl.get(["OSKAR_OLSSON/T1"],trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
# data=Quandl.get(["YAHOO/INDEX_GSPC.6"],trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
print data
