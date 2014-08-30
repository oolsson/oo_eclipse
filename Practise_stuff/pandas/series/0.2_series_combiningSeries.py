import numpy as np
randn = np.random.randn
from pandas import *


s = Series(randn(5), index=['a','b','c','d','e'])
o=Series(randn(5))
d = {'c' : 0., 'd' : 1., 'e' : 2., 'f' : 1., 'g' : 2.}
oo=Series(d)

print oo + s
print '-------------------'
print s[1:] + s[:-1]
print '--set name attribute'
s = Series(np.random.randn(2), name='something')
print s
print s.name
