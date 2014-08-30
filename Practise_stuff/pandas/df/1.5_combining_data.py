import numpy as np
randn = np.random.randn
import pandas as pd

df1 = pd.DataFrame({'A' : [1., np.nan, 3., 5., np.nan],
				'B' : [np.nan, 2., 3., np.nan, 6.]})
df2 = pd.DataFrame({'A' : [5., 2., 4., np.nan, 3., 7.],
				'B' : [np.nan, np.nan, 3., 4., 6., 8.]})
df3 = pd.DataFrame({'A' : [5., 2., 4., np.nan, 3., 7.],
				'C' : [np.nan, np.nan, 3., 4., 6., 8.]})


#'----combining data'
# print df1
# print df2
#print df1+df2
#print df1.combine_first(df2)

#appending
print'----------'
df=df1.append(df3)
print df



#'------------simple stats along rows and columns'
#print df1
#print df1.mean(0) #average along columns
#print df1.mean(1) #average along rows
#print '---------'
#print df1.sum(0, skipna=False)
#print df1.sum(0, skipna=True)
#print df1.sum(1, skipna=True)

'''
#print 'summary stats for df'
a=df1.describe()
print a
print a.A
'''

'''
#print 'finding min and max column/row number'
print df1
print df1.idxmin(axis=0)
print '-----------------'
print df1.idxmin(axis=1)
'''

