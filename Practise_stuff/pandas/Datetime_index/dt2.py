from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
randn = np.random.randn

rng = pd.date_range('2012-06-01 07:30', '2012-06-01 11:30', freq='H')
rng = rng.append([rng + pd.offsets.BDay(i) for i in range(1, 12)])
#rng = rng.append([rng + pd.offsets.WeekOfMonth(i) for i in range(1, 5)])
#rng = rng.append([rng + pd.offsets.WeekOfMonth(week=1,weekday=1) for i in range(1, 3)])
ts = pd.Series(np.arange(len(rng), dtype=float), index=rng)
print ts
