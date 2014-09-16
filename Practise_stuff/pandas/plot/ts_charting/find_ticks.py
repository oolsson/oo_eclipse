import ts_charting as charting
import pandas.io.data as pdd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
charting.figsize(13, 10)

df = pdd.get_data_yahoo('MSFT')
spy = pdd.get_data_yahoo('SPY')
df = df.tail(100)
spy = spy.tail(100)
returns = df.Close.pct_change()
spy_returns = spy.Close.pct_change()

overnight = np.log(df.Open / df.Close.shift(1))
intraday = np.log(df.Close / df.Open)
overnight_roll = pd.rolling_sum(overnight, 10)
intraday_roll = pd.rolling_sum(intraday, 10)
#------------------------------------------------------------------------------------------

fig = charting.figure(3)
fig.set_ax(1)
(returns + 1).cumprod().fplot('equity')
fig.set_xticks('MS') # pandas freq

fig.set_ax(2, sharex=1)
(returns + 1).cumprod().fplot('equity')
fig.set_xticks([pd.Timestamp("2014-07-01"), pd.Timestamp("2014-07-14")]) # explicit dates

fig.set_ax(3, sharex=1)
(returns + 1).cumprod().fplot('equity')
fig.set_xticks(returns > 0.02) # set tick whenver we are above .02

plt.show()