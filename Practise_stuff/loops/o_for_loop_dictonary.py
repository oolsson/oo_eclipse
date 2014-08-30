'''
Created on Dec 24, 2011

@author: oo
'''
D={'a':1, 'b':2, 'c':3}
for key in D:
    print(key, '<<', D[key])
   
   
for (key, value) in D.items():
    print(key, '-=-', value) 
    
print D.keys(1)