import Quandl
from datetime import datetime
import datetime as dt
from pandas.io.data import DataReader

end=dt.datetime.today()
start=datetime(2013,06,30)
# , authtoken="XgkWhb4QXS6cgd4AxWSz"
# data=Quandl.get(["OSKAR_OLSSON/T1"],trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
data=Quandl.get(["CHRIS/ASX_AP1,CHRIS/ASX_YT1,CHRIS/CME_ES1.6,CHRIS/LIFFE_Z1.4,CHRIS/MX_SXF1.14,CHRIS/LIFFE_TPI1.4,CHRIS/EUREX_FSMI1.4,CHRIS/EUREX_FESX1.4"],trim_start =start, trim_end=end)
data=data.ffill()
print data.head(11)
data.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\data.csv")
