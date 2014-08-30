import numpy as np
randn = np.random.randn
import pandas as pd
import time as td



rng = pd.date_range('1/3/2000', periods=8)
ts = pd.Series(randn(8), index=rng)
ts2 = ts[[0, 3, 6]]
print ts+ts2
print '----------------'
print ts2
print '------'
print ts2.reindex(ts.index)
print '------'
print ts2.reindex(ts.index, method='ffill')
print '------'
print ts2.reindex(ts.index, method='bfill')
print '------'
print ts2.reindex(ts.index).fillna(method='ffill')



#index = range(8)
#df = pd.DataFrame(randn(8,3), index=index, columns=['one', 'two', 'thee'])

'''
print 'dropping stuff'
print df
df = df.drop([3,5], 0)
print df
df = df.drop('one', 1)
print df
'''

'''
print 'iterating over stuff'
print df.columns

for col in df:
    print col
print '---------------'    
for row_index, row in df.iterrows():
    print '%s\n%s' % (row_index, row)
'''