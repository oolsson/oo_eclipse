import itertools as it

#for i in izip([1, 2, 3], ['a', 'b', 'c']):
#    print i
print list(it.izip([1, 2, 3], ['a', 'b', 'c']))
print list(it.izip_longest("ABCD", 'xy', fillvalue='-'))
print list(it.islice(it.count(), 5))
print list(it.islice(it.count(), 0,100,10))

r = it.islice(it.count(), 3)
i1, i2 = it.tee(r)
print list(i1),list(i2)
print list(it.dropwhile(lambda x: x<5, [1,4,6,9,12])) #returns list after first false

print list(it.ifilter(lambda x: x%2, range(10)))
print list(it.ifilterfalse(lambda x: x%2, range(10)))

print list(it.imap(pow, (2,2,2), (2,3,4,5)))



