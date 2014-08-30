
import itertools as it

#python equvalent---------------------------------------    
def chain(*iterables):
    for it in iterables:
        for element in it:
            yield element
            
a= chain('abc', 'def')
for e in a:
    print e
    
#itertools--------------------------
for i in it.count(2,4): #cycle falls in this never ending iterators
    if i > 20:
        break
    print i,
print 'next'

print list(it.chain('abc', 'def'))
print list(it.chain(['abc', 'def']))
print list(it.combinations('ABC', 2))
print list(it.permutations('ABC', 2))
print list(it.combinations_with_replacement('ABC', 2))
print list(it.compress('ABCder', [1,0,1]))
print list(it.repeat('ABC', 2))
print list(it.product(('a',1), (0,1), (0,1)))
print list(it.product('af',repeat=2))

