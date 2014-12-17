#http://www-personal.umich.edu/~varel/sm/vector_ar.html#var

# some example data
import matplotlib.pyplot as plt
import pandas
import statsmodels as sm
import statsmodels.tsa.api
from statsmodels import datasets
import numpy as np
mdata = sm.datasets.macrodata.load_pandas().data

# prepare the dates index
dates = mdata[['year', 'quarter']].astype(int).astype(str)
quarterly = dates["year"] + "Q" + dates["quarter"]
from statsmodels.tsa.base.datetools import dates_from_str
quarterly = dates_from_str(quarterly)

mdata = mdata[['realgdp','realcons','realinv']]
mdata.index = pandas.DatetimeIndex(quarterly)
data = np.log(mdata).diff().dropna()

# make a VAR model
model = statsmodels.tsa.api.VAR(data)

results = model.fit()

print results.summary()
# plt.show(results.plot())
print help(model.fit)


