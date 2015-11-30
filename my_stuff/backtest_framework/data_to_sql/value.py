import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib2 import urlopen
from pandas.io.parsers import TextParser
import urllib2
import datetime as dt
import MySQLdb as mdb
import pandas.io.sql as sql
import matplotlib.pyplot as plt

# print dt.date.today()

f = lambda x: float(x)

def yf_get_key_stat(SYM):
#     url = "http://finance.yahoo.com/q/ks?s=" + SYM + "+Key+Statistics"
    url = "http://finance.yahoo.com/q/hl?s=" + SYM
#     print url
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    res = [[x.text for x in y.parent.contents] for  y in soup.findAll('td', attrs={"class" : "yfnc_tabledata1"})]
    res=pd.DataFrame(res)
    res=res.drop_duplicates(0)
    res.index=res[0]
    res= res.reindex(index=['Average Price/Earnings','Average Price/Book','Average Price/Sales','Average Price/Cashflow'])
    return res

# list=['EWW','SPY']
list=['SPY','QQQ','IWM','EWC','EWW','EWG','EWQ','EWP','EWI','EWL'
,'GREK','RSX','TUR','EZA','EWJ','EWH','EWI','IDTW',
'EWY','EWA','EWT','EPI','IJH','PIN','EWS','EWM','VNM','EWU','EEM','ILF','FM','PKW']

# list=['SPY','QQQ','IWM','EWT','EPI']
list2=[]


for i in range(0,len(list)+1):
    try:
        p=yf_get_key_stat(list[i])
        print dt.date.today(),',',p.iloc[0,1],',',p.iloc[1,1],',',p.iloc[2,1],',',p.iloc[3,1]
        l=[list[i],dt.date.today(),float(p.iloc[0,1]),float(p.iloc[1,1]),float(p.iloc[2,1]),float(p.iloc[3,1])]
        list2.append(l)
    except:print i
df=pd.DataFrame(list2,columns=['ticker','Date','pe','pb','ps','pc'])
df.index=df['ticker']
# del df['ticker']
print df

# df[['pe','pb','ps','pc']]=df[['pe','pb','ps','pc']].applymap(f)



con = mdb.connect('localhost', "root","","test");
adv3='eq_fundamental'
for row in df.index:
    try:
        df2=pd.DataFrame(columns=df.columns,index=[0])
        df2.ix[0]=df.ix[row]
        sql.write_frame(df2, con=con, name=adv3, if_exists='append', flavor='mysql')
    except:pass