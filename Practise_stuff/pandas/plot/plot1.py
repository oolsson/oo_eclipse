import pandas as pd
import numpy as np
from pandas.io.parsers import *
import matplotlib.pyplot as plt
# pd.options.display.mpl_style = 'default'


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()

ts.plot()
plt.show()