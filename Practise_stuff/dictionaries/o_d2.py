'''
Created on Feb 29, 2012

@author: oo
'''
pos={}
pos['EUR'] = [40,50]
pos['USD'] = 50
print pos['EUR']
print pos['USD']
 
if pos.has_key('dog'):
    print 'yes'
    #pos['EUR'] = pos['EUR']+20
   
print 'append------------------'
   
print pos['EUR']
pos['EUR'].append(55)
print pos['EUR']
 
'if there were stops associated with position'
 
 
print pos
 
 
pos={}
pos['EUR'] = {'position': 40, 'stop': 1.3}
 
print pos
print pos['EUR']
print pos['EUR']['position']
 
pos['EUR']['stop'] = 5
 
print pos