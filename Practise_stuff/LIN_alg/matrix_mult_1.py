import numpy as np
import math

A=np.array([[1,2,4],[2,6,0]]) #matrix dim =2,3
B=np.array([[1],[-1],[7]])    #matrix dim =3,1
C=B.T                         #matrix dim =1,3
D=np.array([1,-1,7])


print'A======'
print A
print A.shape
print'B======'
print B
print B.shape
print'C======'
print C
print C.shape
print'D======'
print D
print D.shape #never use
print 'mult---------------------------'
print np.dot(A,B)
#print np.dot(B,A)   #dimension missmatch
# print np.dot(A,C)    ##dimension missmatch

