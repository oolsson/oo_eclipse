'''
Created on Jan 22, 2012

@author: oo
'''
import numpy
np=numpy

A=[1,2,3]
B=[4,5,6]
A=np.array(A)
B=np.array(B)
c=np.concatenate((A,B))
print c
print '2------------'
c=np.column_stack((A,B))
print c
print '3------------'
c=np.hstack((A,B))
print c
c=np.vstack((A,B))
print c
print '4------------'
c=np.array_split(c,1)
print c
print '5-----------'
d=np.array([1])
d=np.tile(d,7)
print d
print '6-----------'
x = np.array([[1,2],[3,4]])
print np.repeat(x, 1)
print np.repeat(x, 3, axis=1)
print np.repeat(x, [1, 2], axis=0)
