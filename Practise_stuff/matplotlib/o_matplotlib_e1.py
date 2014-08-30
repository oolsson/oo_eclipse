#!/usr/bin/env python
from pylab import *

from matplotlib.finance import quotes_historical_yahoo, candlestick,\
     plot_day_summary, candlestick2

 #(Year, month, day) tuples suffice as args for quotes_historical_yahoo
date1 = ( 2004, 2, 1)
date2 = ( 2004, 4, 12 )

D=[731613,731614,731615,731616,731617,731618,731619,731620,731621]
O=[4,4,4,4,4,4,4,4,4]
H=[5,5,5,5,5,5,5,5,5]
L=[2,2,2,2,2,2,2,2,2]
C=[3,3,4,3,3,3,4,3,3]
   
quotes=zip(D,C,O,H,L)

print quotes


fig = figure()
fig.subplots_adjust(bottom=0.2)
ax = fig.add_subplot(111)

candlestick(ax, quotes, width=0.6)

#ax.xaxis_date()
ax.autoscale_view()
setp( gca().get_xticklabels(), rotation=45, horizontalalignment='right')

show()

