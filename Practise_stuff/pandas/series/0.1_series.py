import numpy as np
randn = np.random.randn
from pandas import *


# generating timeseries index
'''
rng = date_range('1/1/2011 00:01:00', periods=10, freq='D') #A,B,M,D,H,T,S
s = Series(randn(len(rng)), index=rng)
print s
'''

s = Series(randn(5), index=['a','b','c','d','e'])
o=Series(randn(5))
d = {'c' : 0., 'd' : 1., 'e' : 2., 'f' : 1., 'g' : 2.}
oo=Series(d)

#print oo
#print oo + s
print Series(d, index=['f','g','h'])
print '2------------------------'
print Series(3, index=['a','b'])
print '3------------------'
print oo[:2]
print 'larger than median------------------'
print s[s > s.median()]
print 'index values------------------'
print s[[4, 3, 1]]
print 'exponential------------------'
print np.exp(s)
print 'works like dictionary------------------'
s['e'] = 999.
print s

