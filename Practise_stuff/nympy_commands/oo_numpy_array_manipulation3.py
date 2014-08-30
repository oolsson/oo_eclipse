'''
Created on Jan 22, 2012

@author: oo
'''
import numpy
np=numpy

arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print arr
print '2------'
print np.delete(arr, 1, 0)
print '3------'
print np.delete(arr,1, 1)
print '4------'
print arr.flatten()
print '5------'
print np.insert(arr, 1, 5)
print np.insert(arr, 0, 5)
print '6-----------------------------'
print arr
print np.insert(arr, 4, 5, axis=1)
print '7-----------------------------'
print np.append(arr, [[7], [8], [9]], axis=1)
print np.append(arr, [[7, 8, 9, 12]], axis=0)
print '8-----------------------------'
print np.resize(arr,(3,3))
print '9-----------------------------'
A = np.diag([1.,2.,3.])
print A
print np.fliplr(A)

