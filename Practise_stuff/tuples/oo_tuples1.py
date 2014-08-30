'''
Created on Jan 21, 2012

@author: oo
'''
T = ('cc', 'aa', 'dd', 'bb')
TT = (('a','p'),('s','o'))
tmp = list(T)
tmp.sort()
print tmp
print T
print TT[1]
print TT
print '--------------------'
TTT=[[]]
TTT[0]='pp'
TTT[[0][1]]='ww'
print TTT


B=['1', '2', '3', '3']
c=B[1]+B[2]
print B
print c

print '---------------------------'
D=[[2,1,3,4,5]]
O=[4,4,4,4,4]
H=[5,5,5,5,5]
L=[2,2,2,2,2]
C=[3,3,4,3,3]
def combine(D,O,H,L,C):
    F=[]
    for x in D:
            F.append(tuple([x]+[O[x-1]]+[H[x-1]]+[L[x-1]]+[C[x-1]]))
    return F



    

