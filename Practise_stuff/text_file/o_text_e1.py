'''
Created on Dec 27, 2011

@author: oo
'''
f = open('data.txt', 'w')
f.write('Hello\n')
f.close()

f = open('data.txt')
text = f.read()
print(text)
