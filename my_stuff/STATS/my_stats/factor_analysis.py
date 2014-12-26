import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
randn = np.random.randn
from pandas import *
import datetime as dt
from pandas.io.data import DataReader
from scipy import stats
import time
import matplotlib.pyplot as plt
import string
import random; random.seed(0)

tickers=['a','s','p']
N=1000
def rands(n):
    choices = string.ascii_uppercase
    n=''.join([random.choice(choices) for _ in xrange(n)])
    return n

tickers = np.array([rands(5) for _ in xrange(N)])

fac1, fac2, fac3 = np.random.rand(3, 1000)
ticker_subset = tickers.take(np.random.permutation(N)[:1000])
port = Series(0.7 * fac1 - 1.2 * fac2 + 0.3 * fac3 + np.random.rand(1000),
              index=ticker_subset)
factors = DataFrame({'f1': fac1, 'f2': fac2, 'f3': fac3},
                    index=ticker_subset)

print factors.corrwith(port) #means nothing
print pd.ols(y=port, x=factors).beta
# print ticker_subset