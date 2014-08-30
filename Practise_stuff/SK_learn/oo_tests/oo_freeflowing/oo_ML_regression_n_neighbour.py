import pandas.io.sql as sql
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
import datetime as dt
from pandas.io.data import DataReader
import pylab as pl
from sklearn import neighbors

l1=['MSFT']
rng=pd.date_range('2012-08-23', '2013-04-25' )
df=pd.DataFrame(index=rng)

for ii in l1:
    data = DataReader(ii, "yahoo", dt.datetime(2012, 8, 23),dt.datetime(2013, 4, 25))
    df[ii]=data['Close']

df=df.fillna(method='ffill')
#df=df.pct_change(1).fillna(method='bfill')
df2= df.shift(1)
df2=df2.fillna(method='bfill')
y=df2.values
X=df.values


T=y
y=y.flatten()
n_neighbors = 33
oo=[]
for i, weights in enumerate(['uniform', 'distance']):
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    y_ = knn.fit(X, y).predict(T)
    oo.append(y_)
print oo[0]
fig = pl.figure()
pl.plot(X,'g')
pl.plot(oo[0],'r')

pl.show()
