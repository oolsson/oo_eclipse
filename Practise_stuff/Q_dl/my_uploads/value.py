import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib2 import urlopen
from pandas.io.parsers import TextParser
import urllib2
import datetime as dt

# print dt.date.today()



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

list=['EWW','SPY']

for i in range(0,len(list)):
    p=yf_get_key_stat(list[i])
    print "code: VAL_%s" % (list[i])
    print "name: %s_Value" % (list[i])
    print("private: true")
    print("----")
    print 'Date,','pe,','pb,','ps,','pc'
    print dt.date.today(),',',p.iloc[0,1],',',p.iloc[1,1],',',p.iloc[2,1],',',p.iloc[3,1]
# p=yf_get_key_stat('EWW')
# print("code: VAL_EWW")
# print("name: EWW_Value")
# print("private: true")
# print("----")
# print 'Date,','pe,','pb,','ps,','pc'
# print dt.date.today(),',',p.iloc[0,1],',',p.iloc[1,1],',',p.iloc[2,1],',',p.iloc[3,1]