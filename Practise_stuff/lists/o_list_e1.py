'''
Created on Dec 26, 2011

@author: oo
'''
L1 = [123, 'spam', 1.23]
print L1

l1=len(L1)
print l1

l1=L1[1]
print l1

l1=L1[:-1]
print l1

L1=L1+[1, 3, 'oo']
print L1


L1 = ['a', 's', 'u', 'i', 'o', 'p', 'h', 'j', 'm']
print L1
print L1[-1]
L2=[[1,2,3],[4,5,6]]
print L2[1][-1]
n=zip(L2[0],L2[1])
print list(n[0])