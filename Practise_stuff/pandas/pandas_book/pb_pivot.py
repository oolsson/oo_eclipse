import numpy as np
randn = np.random.randn
import pandas as pd
from pandas import Series, DataFrame

#dd = pd.date_range('1/1/2000', periods=6)
dd = ('1/1/2000', '1/1/2000','1/1/2000','2/1/2000','2/1/2000','2/1/2000',)
ldata=DataFrame({'item': ['gdp', 'inf', 'emp', 'gdp', 'inf', 'emp'],'value': range(6), 'date':dd})
print ldata
print '--------------'
print ldata.pivot('date', 'item', 'value')
 
print'adding another sets of values to the data'
ldata['value2'] = np.random.randn(len(ldata))
print ldata
 
pivoted = ldata.pivot('date', 'item','value')
print pivoted
pivoted = ldata.pivot('date', 'item')
print pivoted
