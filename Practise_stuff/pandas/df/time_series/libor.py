import matplotlib.pyplot as plt
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
randn = np.random.randn
from pandas import *
import datetime as dt
from pandas.io.data import DataReader
from scipy import stats
import re
import urllib2
import time


f = lambda x: float(x)
# Parameters---------------------------------------------------------
start=dt.datetime(2007, 01, 01)
end=dt.date.today()
LI3=pd.date_range(start, end, freq='D')


curr=['USD','GBP','EUR']
libor_1m=[]
for i in curr:
    tick=i+'1MTD156N'
    libor_1m.append(tick)


df_libor_1m=pd.DataFrame(index=LI3)
for i in libor_1m:
    df2 = DataReader(i, "fred", start,end)
    df2=df2.applymap(f)
    df2=df2.ffill()
    df_libor_1m[i]=df2
df_libor_1m=df_libor_1m.ffill()
df_libor_1m.columns=curr
print df_libor_1m.head(8)


libor_1w=[]
for i in curr:
    tick=i+'1WKD156N'
    libor_1w.append(tick)

df_libor_1w=pd.DataFrame(index=LI3)
for i in libor_1w:
    df2 = DataReader(i, "fred", start,end)
    df2=df2.applymap(f)
    df2=df2.ffill()
    df_libor_1w[i]=df2
df_libor_1w=df_libor_1w.ffill()
df_libor_1w.columns=curr
print df_libor_1w.head(8)

df_diff=df_libor_1m-df_libor_1w
# print df_diff.to_string()
# plt.subplot(411)
plt.plot(df_diff.index,df_diff)
plt.show()


