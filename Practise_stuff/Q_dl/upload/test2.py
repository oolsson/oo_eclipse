import pandas as pd 
import datetime as dt
import numpy as np
randn = np.random.randn
import Quandl 

f = lambda x: round(abs(x),0)

d1=dt.date(2012, 03, 01)
num_q=3
dr1=pd.date_range(d1, periods=num_q, freq='D')
df = pd.DataFrame(randn(3, 4), index=dr1, columns=['A', 'B', 'C', 'D'])
df = df*1000
df=df.applymap(f)
df.index = df.index.date
df.index = df.index.map(lambda x: x.strftime('%Y-%m-%d'))

print 'id:','T2'
print df.index[0],', ',df.iat[0,0]
