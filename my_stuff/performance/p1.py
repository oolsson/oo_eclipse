from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np
import Quandl
from datetime import datetime
import datetime as dt

end=dt.datetime.today()
start=datetime(2013,1,1)


# df= Quandl.get(["YAHOO/INDEX_GSPC.6"],trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
# df2=Quandl.get(["YAHOO/INDEX_RUT.6"],trim_start =start, trim_end=end, authtoken="XgkWhb4QXS6cgd4AxWSz")
# df['b']=df2
# df.to_excel("C:\Users\oskar\Documents\GitHub\oo_eclipse\my_stuff\Data\sp500.xls")



xl = pd.ExcelFile("C:\Users\oskar\Documents\GitHub\oo_eclipse\my_stuff\Data\sp500.xls")
df = xl.parse("sheet1",  index_col=0,  skiprows=0)

 
 
df.columns=['p','b']
df[['pr','br']]=df.pct_change(1)

df[['pi','bi']]=df[['pr','br']]+1

df['sig']=(df['pr']>0.005)*1
df['sig2']=(df['pr']>0.009)*1
portsig_str=df[['sig','sig2']].astype(str)
df['sig_c']=portsig_str['sig']+portsig_str['sig2']
print df.head(27)


df1=df.groupby(df.index.map(lambda x: x.year)).mean()
print df1

#annual return bu month
df2=df[['pi','bi']].groupby(df.index.map(lambda x: x.month)).prod()
df2c=252/df[['pi','bi']].groupby(df.index.map(lambda x: x.month)).count()
df2r=df2**df2c
df2p=df['pi'].groupby(df.index.map(lambda x: x.month))
print df2p.to_string()


# return by signal
df3=df[['pi','bi']].groupby(df['sig_c']).prod()
print df3.to_string()
 
 
# print df.describe()

# print (df2r-1).to_string()
# print df3.to_string()
# print df.to_string()