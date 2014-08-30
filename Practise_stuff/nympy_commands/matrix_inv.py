'''
Created on Mar 15, 2013

@author: oo
'''
import numpy

x=numpy.array([[1,0,0,1],[0,1,1,1],[1,0,1,0],[1,0,0,2]])
y=numpy.linalg.inv(x)
print x
print y