'''
Created on Jun 7, 2012

@author: oo
'''
A={}
A['test']=[11,22,33,44]
print A['test'][2]

from collections import defaultdict

if 'test' in A:
    print "yes"
else:
    print 'pp'

print len(A['test'])