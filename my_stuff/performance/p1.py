from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np
import Quandl
from datetime import datetime
import datetime as dt

end=dt.datetime.today()
start=datetime(2013,1,1)


df= Quandl.get(["YAHOO/INDEX_GSPC.6"],trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
df.to_excel("C:\Users\oskar\Documents\GitHub\oo_eclipse\my_stuff\Data\simple_df.xls")
# df.to_csv("C:\Users\oskar\Documents\GitHub\oo_eclipse\my_stuff\Data\simple_df.xls")
df_r=df.pct_change(1)
print df_r.head(11)

df_r['r']=df.pct_change(1)
df=df.groupby(df.index.map(lambda x: x.year)).mean()


# print df.describe()
# print df.to_string