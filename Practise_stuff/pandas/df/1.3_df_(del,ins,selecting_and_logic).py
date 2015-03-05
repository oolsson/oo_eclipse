import numpy as np
randn = np.random.randn
from pandas import *

d = {'one' : Series([1., 2., 3.], index=['a', 'b', 'c']), 
     'two' : Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = DataFrame(d)
#print df['one'][:2]   #choosing 1 array and slicing it
#
#df['three'] = df['one'] * df['two']   #creates a 3rd column and sets it to th product
#df['flag'] = df['one'] > 2            #true if column 1 is greater than 2
#print df
#
#print 'deleting-----------------'
#three = df.pop('three')
#del df['two']
#print df
#
#print 'inserting-----------------'
#df['foo'] = 'bar'
#print df
#
#print 'inserting of differtnet length-----------------'
#df['one_trunc'] = df['one'][:2]
#print df
print 'inserting between columns-----------------'
df.insert(0, 'bar', df['one'])
print df
#print 'selecting rows----------------'
#print df.xs('b')
# print df.ix[1]
df=df.reindex(df.index[1:]) #'drop first row'
print df

# print 'multilogic----------------'
# print df
# print '--------------'
# print min(df['two'].ix[1:3])
# print df.ix[1]