import pandas as pd
import numpy as np
from pandas.io.parsers import *
import matplotlib.pyplot as plt
# pd.options.display.mpl_style = 'default'


xl = pd.ExcelFile("C:\Users\oskar\Documents\GitHub\oo_eclipse\my_stuff\Data\Retail_turnover.xls")
x = xl.parse("Sheet1")
print x.head(10)




x.plot()
plt.show()

