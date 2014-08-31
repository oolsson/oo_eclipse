import pandas as pd
import numpy as np
from pandas.io.parsers import *
import matplotlib.pyplot as plt
import statsmodels.api as sm



# acf = sm.tsa.acf(eeg,50)
x=sm.datasets.macrodata.load_pandas().data
index = pd.Index(sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3'))
x.index = index
x=pd.DataFrame(x)
print x
x.plot()
plt.show()
