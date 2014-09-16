#http://nbviewer.ipython.org/github/dalejung/ts-charting/blob/master/notebooks/ohlc.ipynb

import ts_charting as charting
import pandas.io.data as pdd
import pandas as pd
import matplotlib.pyplot as plt
charting.figsize(13, 10)

df = pdd.get_data_yahoo('MSFT')
# spy = pdd.get_data_yahoo('SPY')
df = df.tail(100)
# spy = spy.tail(100)
returns = df.Close.pct_change()
# spy_returns = spy.Close.pct_change()

fig = charting.figure(1)
df.ohlc_plot()
# (df.Close.pct_change() > 0).fplot_markers('close up', yvalues=(df.Open + df.Close) / 2, color='green')
fig.line(40)
plt.show()