'''
Created on Jan 29, 2012

@author: oo
'''
class className:
    def createName(self,name):
        self.name=name
    def displayName(self):
        return self.name
    def saying(self):
        print 'hello %s' % self.name
        
#creates the object         
first=className()
#sets the name i to equal to oskar
first.createName('oskar')
#prints the value returned by desplay name which gets its name from the create name function
print first.displayName()
first.saying()


#This will copy the blueprint from the firs class and create a second object from it
class childclass(className):
    pass

second=childclass()
second.createName('hakan')
second.saying()

#you can also create multiple objects from same class FYI


