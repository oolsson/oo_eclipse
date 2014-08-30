import numpy as np
randn = np.random.randn
import pandas as pd
from pandas import Series, DataFrame

#obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
#print obj
#print ' --------'
#obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'],fill_value=0)
#print obj2

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])

f = lambda x: x.max() - x.min()
print frame
print frame.apply(f)
print frame.apply(f, axis=1)

format = lambda x: '%.2f' % x
print frame.applymap(format)

print 'sorting-----------'
print frame.sort_index()
print frame.sort_index(by='e')

print frame.describe()


