import numpy as np
randn = np.random.randn
from pandas import *
'''
d = {'one' : Series([1., 2., 3.], index=['a', 'b', 'c']), 
     'two' : Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = DataFrame(d)
print df
print'1-------------------'
print DataFrame(d, index=['d', 'b', 'a'])
print'2-------------------'
print DataFrame(d, index=['b','c'], columns=['two','three'])

'''
print'dictionary-------------------'
d = {'one' : [1., 2., 3., 4.],
     'two' : [4., 3., 2., 1.]}

print DataFrame(d , index=['a','b','c','d'])

print 'list of dict---------------------'
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
print DataFrame(data2)
print DataFrame(data2, index=['first', 'second'])

print'dataframefrom item------------'
print DataFrame.from_items([('A', [1, 2, 3]), ('B', [4, 5, 6])])



