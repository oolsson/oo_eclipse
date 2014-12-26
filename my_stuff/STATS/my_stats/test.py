# some example data
import pandas
import statsmodels.api as sm
from statsmodels.api import *
import numpy as np
mdata = sm.datasets.macrodata.load_pandas().data

#---------------------------------------------------------------
#http://statsmodels.sourceforge.net/devel/vector_ar.html?highlight=panel
#----------------------------------------------------------------

# prepare the dates index
dates = mdata[['year', 'quarter']].astype(int).astype(str)
quarterly = dates["year"] + "Q" + dates["quarter"]
from statsmodels.tsa.base.datetools import dates_from_str
quarterly = dates_from_str(quarterly)

mdata = mdata[['realgdp','realcons','realinv']]
mdata.index = pandas.DatetimeIndex(quarterly)
data = np.log(mdata).diff().dropna()

# make a VAR model
model=sm.tsa.VAR(data)
results = model.fit(3)
print results.summary()
# model = VAR(data)