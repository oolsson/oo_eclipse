import pandas
import numpy
import Quandl

index = ['Dec 12 2100', 'Dec 12 2101', 'Dec 12 2102', 'Dec 12 2103',
         'Dec 12 2104', 'Dec 12 2105']
data = pandas.DataFrame(numpy.random.randn(6, 3), index=index,
                        columns=['D', 'B', 'C'])
Quandl.push(data, code='T1', name='Test', desc='test',
                  authtoken='XgkWhb4QXS6cgd4AxWSz')
Quandl.push
print data

