import numpy as np
randn = np.random.randn
import pandas as pd
import matplotlib.pyplot as plt


ts = pd.Series(randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()

