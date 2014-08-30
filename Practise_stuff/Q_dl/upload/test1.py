import pandas
import numpy
import Quandl

index = ['Dec 12 2196', 'Dec 21 1998', 'Oct 9 2000', 'Oct 19 2001',
         'Oct 30 2003', 'Nov 12 2003']
data = pandas.DataFrame(numpy.random.randn(6, 3), index=index,
                        columns=['D', 'B', 'C'])
# print Quandl.push(data, code='T1', name='Test', desc='test',
#                   authtoken='XgkWhb4QXS6cgd4AxWSz')
print data

