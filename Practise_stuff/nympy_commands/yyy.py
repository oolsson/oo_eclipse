'''
Created on Dec 24, 2011

@author: oo
'''
import numpy

x=numpy.array([1,2,3])
z=numpy.array([3,4,5])
print x,z

#matrix mult
matrixproduct=numpy.prod([x,z])
print matrixproduct

#multilpy each vector
mm=numpy.prod([x,z], axis=1)
print mm


