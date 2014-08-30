'''
Created on Jan 29, 2012

@author: oo
'''
#class is the blueprint for objects
class exampleClass():
    def __init__(self):
        eyes='blue'
        self.age=27
        print'p'
    def m1(self,x):
        return x+' is king'

#you need to create an object to acces values in a class
a=exampleClass()
print a.age
print a.m1('oskar')


A=2

# b=exampleClass()
# print b.testmethod()
