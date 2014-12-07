import pandas.io.sql as sql
import MySQLdb as mdb
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
randn = np.random.randn
from pandas import *
import datetime as dt
from pandas.io.data import DataReader
from scipy import stats
from dateutil import parser
import time
import datetime
import matplotlib.pyplot as plt


f = lambda x: float(x)

# get universe
con = mdb.connect('localhost', "root","","test");
sqll="SELECT ticker FROM test.index_constit where indexx = 'SP500' and ticker like 'Y%';"
tick=sql.read_frame(sqll, con)
print tick

con = mdb.connect('localhost', "root","","test");
sqll2="SELECT freecashflow FROM test.adv3 where ticker = 'YHOO';"
roe=sql.read_frame(sqll2, con)
print roe




# e = myr(dtt)
# e=e.T.groupby(level=0).first().T
# print e.to_string()
# num_q=1
# LI2 = pd.date_range(dtt+dt.timedelta(days=80), periods=num_q, freq='Q')
# for i in LI2:
#     d=myr(i)
#     d=d.T.groupby(level=0).first().T
#     print'-----------------'
#     print d.to_string()
#     print'-----------------'
#     e=e.append(d)
#     print e.to_string()
# # e=pd.rolling_max(e, 4,True)
# print e.to_string()
# df=e.iloc[[-1]][e.iloc[[-1]]>0].dropna(1).transpose()
# print df
# 
# #
# dtt=date
# ebit_date2=dtt-dt.timedelta(days=405)
# oo="%Y/%m"
# LI= pd.date_range(dtt, periods=3, freq='M')
# dtstr=dtt.strftime(oo)
# con = mdb.connect('localhost', "root","","test");
# sqll="SELECT adv3.ticker,adv3.quarterenddate,adv3.workingcapital,adv3.netfixedassets,adv3.intangibles,adv3.shorttermdebt,adv3.longtermdebt,adv3.minorityinterestliability,adv3.preferredstockequity,adv3.totalcommonsharesout,adv3.depreciation,adv3.cashequivalents \
# FROM test.adv3 inner join test.index_constit on adv3.ticker=index_constit.ticker where quarterenddate ='%s' or quarterenddate ='%s' or quarterenddate = '%s' ;" % (LI[0].strftime(oo),LI[1].strftime(oo),LI[2].strftime(oo))
# df=sql.read_frame(sqll, con)
# df.index = df['ticker']
# num_values=df.columns[2:-1]
# df[num_values]=df[num_values].applymap(f)
# sqll2="select ticker,quarterenddate,sum(EBIT) 'EBIT4' FROM test.adv3 \
# where quarterenddate >'%s' and quarterenddate <'%s'  GROUP BY adv3.ticker ;" % (ebit_date2.strftime(oo),ebit_date.strftime(oo))
# df2=sql.read_frame(sqll2, con)
# df2.index = df2['ticker']
# df['EBIT']=df2['EBIT4']
# df_p=sql.read_frame('select Adj_Close,ticker from yahoo_p where date="%s"'%(run_date),con, index_col='ticker')
# print 'select Adj_Close,ticker from yahoo_p where date="%s"'%(run_date)
# df_p=df_p.reindex(index=df.index)
# df['price']=df_p['Adj_Close']
# #     df['price']=df['price'].apply(f) ############
# #     print df.to_string()
# df[['price','EBIT','cashequivalents']]=df[['price','EBIT','cashequivalents']].applymap(f)
# df['ROC']=df['EBIT']/(df['workingcapital']+df['netfixedassets']+df['depreciation']-df['intangibles'])
# df['EY']=df['EBIT']/(df['price']*df['totalcommonsharesout']+df['shorttermdebt']+df['longtermdebt']+df['totalcommonsharesout']+df['preferredstockequity']-df['cashequivalents'])
# df['ROC'][df['ROC']>55]=0 #sets column ROC to 0 when is inf
# df2=df.rank(axis=0)
# df['ROC_r']=df2['ROC']
# df['EY_r']=df2['EY']
# df['score']=df['ROC_r']+df['EY_r']
# df['score']=df['score'].rank()
# df['score']=df['score'].fillna(0)
# precentile=stats.scoreatpercentile(df['score'], pch_tile)
# df['include']=df['score']>precentile
# df['include']=df['include']*1
# df.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\%s.csv" %(str(randn(1))))
# #     print df.to_string()
# df2=df.transpose()
# df2= df2.ix['include':]
# df2.index=[df['quarterenddate'][0]]
# #     df2=df2*1
# #     df2=df2.fillna(0)
# return df2