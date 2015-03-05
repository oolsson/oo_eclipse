from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np
import Quandl
from datetime import datetime
import datetime as dt

end=dt.date.today()
start=dt.date(2003,12,20)

# data=Quandl.get("NSE/OIL", trim_start=start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
df= Quandl.get("YAHOO/INDEX_GSPC.6",trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
LI1=pd.date_range(start, end, freq='D')
df2=pd.DataFrame(index=LI1)
df2['pnl']=df
df2=df2.ffill()
print df2.head(22)


xl = pd.ExcelFile("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\sp500_btest.xlsx")
df3 = xl.parse("sheet1",  index_col=0,  skiprows=0)
df4=pd.DataFrame(df3['pnl2'].values, index=df3.index)
df4['strat']=df2
df4=df4.reindex(df4.index[1:])
df4.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\df4.csv")
print df4.head(20)