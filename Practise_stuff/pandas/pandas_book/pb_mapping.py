import numpy as np
randn = np.random.randn
import pandas as pd
from pandas import Series, DataFrame

frame = DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print frame

f = lambda x: x.max() - x.min()
print frame.apply(f)
print frame.apply(f, axis=1)

print 'fancy f(x)---------'

def f(x):
    return Series([x.min(), x.max()], index=['min', 'max'])

print frame.apply(f)
format = lambda x: '%.2f' % x
print frame.applymap(format)

print 'sorting-------------'
print frame.sort_index(by='b')
print frame.rank(method='max', axis=1)
