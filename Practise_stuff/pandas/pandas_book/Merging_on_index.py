import numpy as np
randn = np.random.randn
import pandas as pd
from pandas import Series, DataFrame

left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

print pd.merge(left1, right1, left_on='key', right_index=True)

print pd.merge(left1, right1, left_on='key', right_index=True, how='outer')

left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])

print '-----------------------'
print pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
#print left2.join(right2, how='outer')
another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]], index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])
print left2.join([right2, another], how='outer')
