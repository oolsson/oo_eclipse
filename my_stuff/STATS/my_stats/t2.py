import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.arima_process import arma_generate_sample
np.random.seed(12345)
arparams = np.array([.75, -.25])
maparams = np.array([.65, .35])
arparams = np.r_[1, -arparams]
maparam = np.r_[1, maparams]
nobs = 250
y = arma_generate_sample(arparams, maparams, nobs)
import pandas
dates = sm.tsa.datetools.dates_from_range('1980m1', length=nobs)
y = pandas.TimeSeries(y, index=dates)
arma_mod = sm.tsa.ARMA(y, freq='M')
arma_res = arma_mod.fit(order=(2,2), trend='nc', disp=-1)
def dump(arma_res):
    for attr in dir(arma_res):
        print "obj.%s = %s" % (attr, getattr(arma_res, attr))
dump(arma_res)