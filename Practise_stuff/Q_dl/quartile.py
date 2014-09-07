import Quandl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


px=Quandl.get(["NSE/OIL.4"],trim_start ="March 2005", trim_end="December 2010", authtoken="XgkWhb4QXS6cgd4AxWSz")
returns = px.pct_change()

def to_index(rets):
    index = (1+rets).cumprod()
#    first_loc = max(index.notnull().argmax() -1, 0)
    first_loc = max(55 -1, 0)
    index.values[first_loc] =1
    return index

def trend_signal(rets, lookback, lag):
    signal = pd.rolling_sum(rets, lookback, min_periods=lookback-5)
    return signal.shift(lag)

def sharpe(rets, ann=250):
    return rets.mean() / rets.std()*np.sqrt(ann)


signal= trend_signal(returns, 12, 10)
trade_friday = signal.resample('W-FRI').resample('B',fill_method='ffill')
trade_rets = trade_friday.shift(1)*returns

#plt.show(to_index(trade_rets).plot())

vol = pd.rolling_std(returns, 250, min_periods=200)*np.sqrt(250)

trade_rets.groupby(pd.qcut(vol,4)).agg(sharpe)
