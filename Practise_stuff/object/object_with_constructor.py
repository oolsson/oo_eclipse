'''
Created on Jan 29, 2012

@author: oo
'''
class swine:
    def method1(self):
        print "beef pie"
        
obj=swine()
obj.method1()


class new:
    def __init__(self):
        print 'this is a constructor'
        
obj=new()
print type(obj)
print type(new)