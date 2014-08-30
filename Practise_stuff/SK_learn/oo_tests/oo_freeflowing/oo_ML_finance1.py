import pandas.io.sql as sql
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
import datetime as dt
from pandas.io.data import DataReader
import pylab as pl
from sklearn.ensemble import GradientBoostingRegressor

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

xx = np.atleast_2d(np.linspace(0, 10, len(df))).T
xx = xx.astype(np.float32)


alpha = 0.99

clf = GradientBoostingRegressor(loss='quantile', alpha=alpha,
                                n_estimators=250, max_depth=31,
                                learning_rate=0.1, min_samples_leaf=20,
                                min_samples_split=20)

clf.fit(X, y)
y_upper = clf.predict(y)

clf.set_params(alpha=1.0 - alpha)
clf.fit(X, y)

# Make the prediction on the meshed x-axis
y_lower = clf.predict(y)


clf.set_params(loss='ls')
clf.fit(X, y)
y_pred = clf.predict(y)



fig = pl.figure()
#pl.plot(xx, f(xx), 'g:', label=u'$f(x) = x\,\sin(x)$')
#pl.plot(X, y, 'b.', markersize=10, label=u'Observations')
#pl.plot(xx, y_pred, 'r-', label=u'Prediction')
#pl.plot(xx, y_upper, 'k-')
#pl.plot(xx, y_lower, 'k-')
#pl.fill(np.concatenate([xx, xx[::-1]]),
#        np.concatenate([y_upper, y_lower[::-1]]),
#        alpha=.5, fc='b', ec='None', label='95% prediction interval')
#pl.xlabel('$x$')
#pl.ylabel('$f(x)$')
#pl.ylim(-10, 55)
#pl.legend(loc='upper left')
#pl.plot(y)
pl.plot(X,'g')
pl.plot(y_upper,'r')
pl.plot(y_lower,'r')
pl.plot(y_pred)
pl.show()