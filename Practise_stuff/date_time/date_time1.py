import datetime as dt
import pandas as pd

d1=dt.date(2012, 03, 01)
d2=d1+dt.timedelta(days=3)
num_q=3

print d1,d2
# print help(dt.timedelta)
dr1=pd.date_range(d1, periods=num_q+1, freq='Q')
dr2=dr1+dt.timedelta(days=5)
print dr1
print dr2
print list(dr2)
# d3=dt.datetime(2012, 03, 01)