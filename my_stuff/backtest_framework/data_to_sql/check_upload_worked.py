import Quandl
import numpy as np
import pandas as pd
from pandas.io.parsers import TextParser
import urllib2
import datetime as dt
import MySQLdb as mdb
import pandas.io.sql as sql




f = lambda x: float(x)

list=['SPY','QQQ','IWM','EWC','EWW','EWG','EWQ','EWP','EWI','EWL'
,'GREK','RSX','TUR','EZA','EWJ','EWH','EWI','IDTW',
'EWY','EWA','EWT','EPI','IJH','PIN','EWS','EWM','VNM','EWU','EEM','ILF','FM','PKW']
# list=['EWW','IWM']

list2=[]
for i in list:
    list2.append("OSKAR_OLSSON/VAL_%s"%(i))
print list2

con = mdb.connect('localhost', "root","","test");
adv3='eq_fundamental'
start1=dt.date(1995,5,1)
for i in list:
    try:
        print i
        df=Quandl.get(["OSKAR_OLSSON/VAL_%s"%(i)],trim_start =start1, trim_end="December 2014", authtoken="XgkWhb4QXS6cgd4AxWSz",collapse="daily")
        df.columns=['pe','pb','ps','pc']
        df.insert(0, 'date', df.index)
        df.insert(0, 'ticker', i)
        for row in df.index:
            try:
                df2=pd.DataFrame(columns=df.columns,index=[0])
                df2.ix[0]=df.ix[row]
                sql.write_frame(df2, con=con, name=adv3, if_exists='append', flavor='mysql')
            except:pass
    except:print i,' not working'