from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
randn = np.random.randn

f = lambda x: float(x)

SPX = DataReader("SP500",  "fred", datetime(2013,1,1), datetime(2013,05,05) ) #SPX
SPX=SPX['SP500'].replace('.',np.nan).fillna(method='ffill')
SPX=pd.DataFrame(SPX)
SPX=SPX.applymap(f)

#dr = pd.date_range('1/1/2013', periods=20, freq=3 * pd.datetools.bday)

start = datetime(2013, 1, 1)
end = datetime(2013, 5, 11)
#startrng = pd.bdate_range(start,end,freq='BQS-MAR')
#startrng = pd.bdate_range(start,end,freq='BMS')                                      #first business day of month
startrng = pd.bdate_range(start,end,freq='WOM-2TUE')                                  #second Tuesday of month

#startrng = startrng + pd.datetools.WeekOfMonth(week=1,weekday=4) - pd.datetools.BDay()
print startrng


SPX=SPX.reindex(startrng)
print SPX