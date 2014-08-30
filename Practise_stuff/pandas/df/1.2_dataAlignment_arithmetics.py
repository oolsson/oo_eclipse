
import numpy as np
randn = np.random.randn
from pandas import *
import time
from datetime import datetime

df = DataFrame(randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = DataFrame(randn(7, 3), columns=['A', 'B', 'C'])

#print df + df2

index = date_range('1/1/2000', periods=8)
df = DataFrame(randn(8, 3), index=index,
               columns=['A', 'B', 'C'])
print df - df['A']
print df[:5].T
print df.dtypes
print 'row-----------------------------'

print df.xs('1/1/2000')['B']
print df.index[3]
if df.index[3]==datetime(2000,01,04):
    print 'true'
else:
    print 'np'