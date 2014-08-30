import numpy as np
randn = np.random.randn
from pandas import *

d = {'one' : [1., 2., 3., 4.],
     'two' : [4., 0., 2., 1.]}

df= DataFrame(d , index=['a','b','c','d'])
print df

df.two = df.two.shift(1)
print df
'''
def subtract_and_divide(x, sub, divide=1):
    return (x - sub) / divide

df.apply(subtract_and_divide, args=(5,), divide=3)
print df

print isnull(df['two'])
print iszero(df['two'])

'''
print df.diff(periods=1)

