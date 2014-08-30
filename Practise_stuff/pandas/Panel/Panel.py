import pandas as pd
import numpy as np
import statsmodels as sm
import statsmodels.api as smf
from pandas.stats.plm import PanelOLS
from pandas.io.data import DataReader
import datetime as dt



start=dt.datetime(2013, 12, 20)
list=['MSFT','AA','AAPL']
d={}
for i in range(0,len(list)):
#     print list[i]
    df = DataReader(list[i], "yahoo", start)
    d[i]=df
p=pd.Panel.from_dict(d, orient='minor')
p.minor_axis=list
# print p
print p.items
print p.major_axis
print p.minor_axis
# print p['Close']
p['rets'] = p['Close'] / p['Close'].shift(1) - 1
print p['rets']

# model = pd.ols(y=p['Volume'] / 1e8, x={'return' : p['rets'],'h' : p['High']},entity_effects=True,intercept=False)
# print model