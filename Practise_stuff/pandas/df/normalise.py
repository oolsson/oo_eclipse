
import numpy as np
randn = np.random.randn
from pandas import *
import time
import pandas as pd
from datetime import datetime

df = DataFrame(randn(10, 4), columns=['A', 'B', 'C', 'D'])
print df
dfs = (df - df.mean()) / df.std()
print dfs
print dfs.describe()

dfrm=rolling_mean(df, window=len(df), min_periods=1)
print dfrm
dfsd=pd.rolling_std(df, window=len(df), min_periods=1)
print dfsd
dfz=(df-rolling_mean(df, window=len(df), min_periods=1))/pd.rolling_std(df, window=len(df), min_periods=1)
print dfz
print dfs.ix[9]
print dfs.ix[9]==dfz.ix[9]

