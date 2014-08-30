'''
Created on Feb 19, 2012

@author: oo
'''
import numpy
np=numpy


M=[[1,2,3,4,5,6],
   [7,8,9,10,11,12],
   [13,14,15,16,17,18],
   [19,20,21,22,23,24],
   [25,26,27,28,29,30]]
print M
N = [[column[2]] for column in M]
E = [[column[1]] for column in M]
print N



