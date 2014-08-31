import pandas as pd
import numpy as np
from pandas.io.parsers import *
import matplotlib.pyplot as plt
# pd.options.display.mpl_style = 'default'


# xl = pd.ExcelFile("C:\Users\oskar\Documents\GitHub\oo_eclipse\my_stuff\Data\Retail_turnover.xls")
# x = xl.parse("Sheet1")
# print x.head(10)
# fig=x.plot()

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

ts.plot()
plt.show()

