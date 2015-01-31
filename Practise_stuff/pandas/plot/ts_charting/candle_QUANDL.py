#http://nbviewer.ipython.org/github/dalejung/ts-charting/blob/master/notebooks/ohlc.ipynb

import ts_charting as charting
import pandas.io.data as pdd
import pandas as pd
import matplotlib.pyplot as plt
charting.figsize(13, 10)
import Quandl
import datetime as dt

start1=dt.date(2013,12,31)        
end1=dt.date.today()
df1 = pdd.get_data_yahoo('MSFT')
security=["OFDP/FUTURE_C1"]


df =Quandl.get(security[0], trim_start=start1, trim_end=end1, authtoken="XgkWhb4QXS6cgd4AxWSz")
df=df.iloc[:,0:4]
df.columns=['Open','High','Low','Close']
# spy = pdd.get_data_yahoo('SPY')
print df.head(4)
print df1.head(4)
print df.columns
print df1.columns
df = df.tail(100)
# spy = spy.tail(100)
# returns = df.Close.pct_change()
# spy_returns = spy.Close.pct_change()

fig = charting.figure(1)
print help(df.ohlc_plot)
df.ohlc_plot()
plt.title('ppppp')

# (df.Close.pct_change() > 0).fplot_markers('close up', yvalues=(df.Open + df.Close) / 2, color='green')
# fig.line(40)
plt.show()