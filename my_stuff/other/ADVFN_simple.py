import pandas.io.sql as sql
import MySQLdb as mdb
import pandas as pd
from pandas.tseries.offsets import Hour, Minute
import numpy as np
randn = np.random.randn
from pandas import *
import datetime as dt
import re
import urllib2
import time
import urllib
from bs4 import BeautifulSoup
import string, datetime
from pandas.io.data import DataReader
from dateutil import parser
from urllib import urlopen
import datetime as dt
import pandas as pd
from dateutil.parser import parse



def get_accg(url_list):
    start=1
    looping=0
    df2=pd.DataFrame()
    loop_num=0
    diff=99
    while diff>69:
        try:
            start1=str(start)
            if len(url_list)<4:
                url = "http://uk.advfn.com/p.php?pid=financials&btn=istart_date&mode=quarterly_reports&symbol=NYSE3A%s&istart_date=%s"% (url_list,start1)
                url=url.replace("NYSE3","NYSE%3") 
            else:
                url = "http://uk.advfn.com/p.php?pid=financials&btn=istart_date&mode=quarterly_reports&symbol=NASDAQ3A%s&istart_date=%s"% (url_list,start1)
                url=url.replace("NASDAQ3","NASDAQ%3")
            page = urllib.urlopen(url)  
            soup = BeautifulSoup(page)
            print diff
            a=[]
            b=[]
            for  y in soup.findAll('td'):
                a=[]
                for x in y.parent.contents:
                    try:
                        a.append(x.text)
                    except:pass
                if len(a)>4:b.append(a)
        #         if len(a)==6:b.append(a[1:])
            res=b
            res = [[y.replace(u"Bil","000000") for y in x] for x in res]
            res = [[y.replace(u"Mil","000").strip() for y in x] for x in res]
            res = [[y.replace(u".","").strip() for y in x] for x in res]
            res = [[y.replace(u",","").strip() for y in x] for x in res]
            res = [[y.replace(u"-","").strip() for y in x] for x in res]
            res = [[y.replace(u"&","").strip() for y in x] for x in res]
            res = [[y.replace(u";","").strip() for y in x] for x in res]
            res = [[y.replace(u" ","").strip() for y in x] for x in res]

            
            df=pd.DataFrame(res)
            df=df.drop_duplicates(0)
            df=df[[0,1,2,3,4,5]]
            list1=['ticker','q1','q2','q3','q4','q5']
            df=df.reindex(index=df.index[2:-1])
            df.index=df[0]
        #     df.index=df[0]
            last_q='2013/09'
            current_q=df[5]['quarterenddate']
            p1=dt.datetime.strptime(current_q, '%Y/%m')
            p2=dt.datetime.strptime(last_q, '%Y/%m')
            td=p2-p1
            diff=int((td.days)/1)/89
            if diff<5:
                start +=diff
            else:
                start +=5
            df.columns=df.ix['quarterenddate']
            if loop_num==0:
                df2=df
            else:
                df2= pd.merge(df2, df, how='inner')
            loop_num +=1
        except:diff=0
    df2.index=df2['quarterenddate']
    return     df2



#This gets the accounting data and wirtes it to SQL
con = mdb.connect('localhost', "root","","test_test");

# simple test-------------------------------------------------------------------------------------------------------------
SYM=['MSFT']
missing=[]
df=get_accg(SYM[0])
df = df.transpose()
df.insert(0, 'ticker', SYM[0])
print df.to_string()
# df.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\simple.csv")
# sql.write_frame(df, con=con, name='adv2', if_exists='append', flavor='mysql')
df=df.reindex(df.index[1:])
f = lambda x: parse(x).date()
g= lambda y: int(y)
df['quarterenddate']= df['quarterenddate'].map(f)
df.iloc[:,11:15]=df.iloc[:,11:15].applymap(g)

for row in df.index:
    df2=pd.DataFrame(columns=df.columns,index=[0])
    df2.ix[0]=df.ix[row]
    try:
        sql.write_frame(df2, con=con, name='adv', if_exists='append', flavor='mysql')
    except:print 'not working2'

# #end simple test--------------------------------------------------------------------------------------------------------
# a = []
# for i in range(0,len(SYM)):
#     try:
#         #-------------------------------------------------
#         print SYM[i]
#         accg=get_accg(SYM[i])
#         df=pd.DataFrame(accg)
#         # df.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\%s.csv" % (SYM[i]))
#         df = df.transpose()
#         df.insert(0, 'ticker', SYM[i])
#         df.rename(columns={'DepreciationandAmortization':'DepreciationandAmortization2'}, inplace=True)
#         #     adv='adv'+str(len(df.columns))
#         adv3='adv3'
#         with con:
#             cur = con.cursor(mdb.cursors.DictCursor)
#             cur.execute("SELECT COLUMN_NAME FROM information_schema.columns WHERE  table_name = '%s' ORDER  BY ordinal_position"  % (adv3))
#             rows = cur.fetchall()
#             list1=[]
#             for row in rows:
#                 list1.append(row["COLUMN_NAME"])
#         df=df.reindex(columns=list1)
#         for row in df.index:
#             df2=pd.DataFrame(columns=df.columns,index=[0])
#             df2.ix[0]=df.ix[row]
#             try:
#                 sql.write_frame(df2, con=con, name=adv3, if_exists='append', flavor='mysql')
#             except:pass
#     except:
#         a.append(1)
#         print a

# #--------------------------------------------------


