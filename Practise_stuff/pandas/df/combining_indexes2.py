'''
Created on Feb 5, 2013

@author: oo
'''
import pandas as pd
import numpy as np
print np.arange(6).reshape((3, 2))
df1 = pd.DataFrame(np.arange(6).reshape((3, 2)), columns=list('ab'),index=[1,3,5])

df2 = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=list('bcd'),index=[2,3,4,5])
print df1
print df2
df3=df1.combine_first(df2)
print df3
