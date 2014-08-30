import pandas as pd
import numpy as np
import statsmodels as sm
import statsmodels.api as smf
from pandas.stats.plm import PanelOLS
from pandas.io.data import DataReader
symbols = ['MSFT', 'GOOG', 'AAPL','AA']
data = dict((sym, DataReader(sym, "yahoo"))
            for sym in symbols)
panel = pd.Panel(data).swapaxes('items', 'minor')
close_px = panel['Close']
rets = close_px / close_px.shift(1) - 1


# model = pd.ols(y=rets['AAPL'], x=rets.ix[:, ['GOOG']])
# print model

volume = panel['Volume'] / 1e8
# model = pd.ols(y=volume, x={'return' : np.abs(rets)})
# print model

# fe_model = pd.ols(y=volume, x={'return' : np.abs(rets)},entity_effects=True,intercept=False)
fe_model = pd.ols(y=volume, x={'return' : rets},entity_effects=True,intercept=False)
print fe_model
print volume.head(8)
print rets.head(5)
print rets.columns