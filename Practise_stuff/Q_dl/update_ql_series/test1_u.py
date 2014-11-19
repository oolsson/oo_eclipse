import pandas
import numpy
import Quandl

index = ['Dec 12 2100', 'Dec 12 2101', 'Dec 12 2102', 'Dec 12 2103',
         'Dec 12 2104', 'Dec 12 2105']
p = pandas.DataFrame(numpy.random.randn(6, 3), index=index,
                        columns=['D', 'B', 'C'])
# Quandl.push(data, code='T1', name='Test', desc='test',
#                   authtoken='XgkWhb4QXS6cgd4AxWSz')
# Quandl.push
# print p

print("code: T1")
print("name: Test")
print("----")
# print 'INDEX','D','B','C'

for i in range(0,len(p)):
    print p.index[i],',',p.iloc[i,0],',',p.iloc[i,1],',',p.iloc[i,2]
    

print p
print p.iloc[0:-2,[0,2]]