import pandas as pd
import numpy as np
from pandas.io.parsers import *
import matplotlib.pyplot as plt
# pd.options.display.mpl_style = 'defaut'


xl = pd.ExcelFile("C:\Users\oskar\Documents\GitHub\oo_eclipse\my_stuff\Data\Retail_turnover.xls")
x = xl.parse("Sheet1")
# x=pd.DataFrame(x)


"Seasonally adjust a series"
x['ma']=pd.rolling_mean(x, 12)
x['ma2']=x['ma'].shift(-5)
x['CMA']=pd.rolling_mean(x['ma2'], 2).shift(-1)
x['SR']=x['Retail_Turnover']/x['CMA']
x['seson']=x.index.month
x['count']=x['seson']/x['seson']

y=x.groupby('seson').sum()
y['SI']=y['SR']/y['count']
"should standardise SI"
SI_dict=y['SI'].to_dict()

x['SI'] = x['seson'].map(SI_dict)
x['ses_adj']=x['Retail_Turnover']/x['SI']

"detrend the data"

"Calculate the cyclical component"

"Calculate the random component"



print SI_dict
print y['SI']
print x.head(20)

x[['Retail_Turnover','ses_adj']].plot()
plt.show()

