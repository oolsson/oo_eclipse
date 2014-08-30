import pandas.io.sql as sql
import MySQLdb as mdb
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
randn = np.random.randn
from pandas import *
import datetime as dt
from pandas.io.data import DataReader
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from matplotlib import finance
from matplotlib.collections import LineCollection
from sklearn import cluster, covariance, manifold

con = mdb.connect('localhost', "root","","daily_Data_Yahoo");
df=sql.read_frame("SELECT AA,AEP,AES FROM daily_Data_Yahoo.dja", con)
df=df.pct_change()
df=df.dropna()
df[df>1000000]=0

# print df.to_string()
# df=df.bfill()
# df=df.ffill()
# df = df[np.isfinite(df)]
# df = df[np.isnan(df)]
# print df.index[df.apply(np.isnan)]
# print df.index[df.apply(np.isinf)]

edge_model = covariance.GraphLassoCV()
print df.values
# X = df.values.copy().T
X = df.values.copy()
print X
X /= X.std(axis=0)
print X
edge_model.fit(X)


