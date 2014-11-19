
import Quandl
from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np
from datetime import datetime
import datetime as dt

index = ['Dec 12 2100', 'Dec 12 2101', 'Dec 12 2102', 'Dec 12 2103',
         'Dec 12 2104', 'Dec 12 2105']
p = pd.DataFrame(np.random.randn(6, 3), index=index,
                        columns=['D', 'B', 'C'])
# Quandl.push(data, code='T1', name='Test', desc='test',
#                   authtoken='XgkWhb4QXS6cgd4AxWSz')
# Quandl.push
# print p

print("code: T1")
print("name: Test")
print("----")
# print 'INDEX','D','B','C'

# for i in range(0,len(p)):
#     print p.index[i],',',p.iloc[i,0],',',p.iloc[i,1],',',p.iloc[i,2]


xl = pd.ExcelFile("C:\Users\oskar\Documents\GitHub\oo_eclipse\Practise_stuff\Q_dl\update_ql_series\Book1.xls")
df = xl.parse("Sheet1",  index_col=0,  skiprows=2)
df=df+50
# df.index=dt.date(df.index)
    

# print df.head(27)
for i in range(10000,len(df.head(27))+10000):
    print df.index[i],',',df.iloc[i,0],',',df.iloc[i,1],',',df.iloc[i,2]