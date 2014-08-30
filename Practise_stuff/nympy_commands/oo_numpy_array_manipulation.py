'''
Created on Jan 22, 2012

@author: oo
'''
import numpy
np=numpy
A=[[1,2,3],[4,5,6],[7,8,9]]
B=A+A
print A
print B

print '2------------'
A=np.array(A)
B=A*A
print A
print B

print '3------------'
print A
z = np.transpose(A)
print z

print '4------------'
x = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
np.swapaxes(x,0,2)
print x

print '4------------'
print A
B=np.concatenate((A,A))
print "   "
print B