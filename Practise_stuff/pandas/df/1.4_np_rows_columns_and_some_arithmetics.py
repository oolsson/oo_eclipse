import numpy as np
randn = np.random.randn
#from pandas import *
import pandas as pd

index = pd.date_range('1/1/2000', periods=12)
df = pd.DataFrame(randn(12, 3), index=index,columns=['A', 'B', 'C'])

'''
print '------------print and print transpose'
print df
print df.T
print df.T.to_string()
'''

'''
print '---------make numpy array of df'
print np.asarray(df)
print np.asarray(index)
'''

'''
'------print selected column, head and tail '
print df.A
print df.head(2)
print df.tail(2)
'''

'''
----modifying col names'
df.columns = [x.lower() for x in df.columns] #makes col names lower case
print df
'''

'''
'----accessing column values'
print df
print df.A[1:4].values
print df.A.tail(5).values
'''

'''
'---accessing and manipolating using rows and columns
row = df.ix[1] #chooses row 1, !NOT 0
column = df['A']  #same as df.A
print df
print row
print column
print df.sub(row, axis='columns') #subtracts rows choosen from all other rows
print df.sub(column, axis='index') #subtracts column choosen from all other columns
''' 
