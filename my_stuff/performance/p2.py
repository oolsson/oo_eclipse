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
df=df['p']
df=pd.DataFrame(df)

df['pr']=df.pct_change(1)
df['pi']=df['pr']+1
df['sig']=df['pr']>0.01
df1=df.groupby(df.index.map(lambda x: x.year)).mean()
#sesonality
df2=df['pi'].groupby(df.index.map(lambda x: x.month)).prod()
df2c=252/df['pi'].groupby(df.index.map(lambda x: x.month)).count()
df2r=df2**df2c
print df2r.to_string()

#take a dataframe and group by some way then loop through the the groups
df2p=df['pi'].groupby(df.index.map(lambda x: x.month))
print df2p.to_string()
for i in df2p.groups:
    print i
    print '-----------------------------'
    ii=df2p.get_group(i).reset_index()
    print ii

#signal alaysis
# df3=df['pi'].groupby(df['sig']).prod()
# df3=df['pi'].groupby(df['sig'])
# print df3.to_string()
# # print df3.get_group(True)
# df4=pd.DataFrame()
# for i in df3.groups:
#     print i
#     print '-----------------------------'
#     ii=df3.get_group(i).reset_index()
#     print ii
# #     df4[i]=ii.values
 
 
# print df.describe()



