'''
Created on Feb 19, 2012

@author: oo
'''
'''
Created on Feb 18, 2012

@author: oo
'''
#!/usr/bin/env python
from pylab import *
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo, candlestick,\
     plot_day_summary, candlestick2

# (Year, month, day) tuples suffice as args for quotes_historical_yahoo
date1 = ( 2004, 2, 1)
date2 = ( 2004, 4, 12 )



quotes = quotes_historical_yahoo('INTC', date1, date2)
if len(quotes) == 0:
    raise SystemExit

high =[row[3] for row in quotes]
low =[row[4] for row in quotes]
print high



fig = figure(1)
ax = fig.add_subplot(111)


candlestick(ax, quotes, width=0.6) #width is size of candles
ax.plot(high)
ax.xaxis_date()
ax.autoscale_view()
# setp( gca().get_xticklabels(), rotation=20, horizontalalignment='right')

ax.plot(high)

show()