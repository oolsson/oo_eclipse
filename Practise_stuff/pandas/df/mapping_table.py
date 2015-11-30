import numpy as np
randn = np.random.randn
import pandas as pd



s = pd.Series(['six', 'seven', 'six', 'seven', 'six', 'eight'],
           index=['a', 'b', 'c', 'd', 'e', 'f'])

t = pd.Series({'six' : 6., 'seven' : 7.})


print s
print 'mats according to other serries-------------'
print s.map(t)


print '-reindexing---------'
p = pd.Series(randn(5), index=['a', 'b', 'c', 'd', 'e'])
print p.reindex(['e', 'b', 'f', 'd'])

