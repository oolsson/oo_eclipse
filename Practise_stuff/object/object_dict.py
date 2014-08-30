'''
Created on Jan 29, 2012

@author: oo
'''
#class is the blueprint for objects
class exampleClass:
    pos={}
    eyes='b'
    def testmethod(self):
        return 'oskar is king'

#you need to create an object to acces values in a class
exampleobject=exampleClass()
print exampleobject.eyes

exampleobject2=exampleClass()
print exampleobject.testmethod()


import os
def recursive_file_gen(mydir):
    for root, dirs, files in os.walk(mydir):
        for file in files:
            yield os.path.join(root, file)
            
print list(recursive_file_gen('C:\Users\oo\Documents\workspace-sts-2.8.1.RELEASE\prectice\object'))