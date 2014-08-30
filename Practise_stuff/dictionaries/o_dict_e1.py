'''
Created on Dec 26, 2011

@author: oo
'''
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print D

print D['food']
D['quantity'] += 1
print D

D2 = {}
D2['name'] = 'Bob'
D2['job'] = 'dev'
D2['age'] = 40
print D2

#nested deictionary
D3 = {'name': {'first': 'Bob', 'last': 'Smith'},
      'job': ['dev', 'mgr'],
      'age': 40.5}
print D3
d3=D3['name']
print d3
d3=D3['name']['last']
print d3

D3['job'].append('janitor')
print D3


D4 = {'a': 1, 'b': 2, 'c': 3}
Ks = list(D4.keys())
print D4
print Ks

Ks.sort()
print Ks

Ks.reverse()
print Ks
print '-----------------------'
for key in Ks:
    print(key, '=', D4[key])
    
for key in sorted(D4):
    print(key, '=>', D4[key])
    
#D5={,{}}
#print D5