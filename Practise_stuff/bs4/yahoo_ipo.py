import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib2 import urlopen
from pandas.io.parsers import TextParser
import urllib2





def yf_get_key_stat(SYM):
#     url = "http://finance.yahoo.com/q/ks?s=" + SYM + "+Key+Statistics"
    url = "http://biz.yahoo.com/ipo/prc_mar14.html"
#     print url
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
#     res = [[x.text for x in y.parent.contents] for  y in soup.findAll('td')]
    a=[]
    b=1
    i=1
    for  y in soup.findAll('tr'):
        print '--------------------------------'
        for x in y:
            print x.text,'  '
    print res
    return res


p=yf_get_key_stat('EWW')
# df=pd.DataFrame(p)
# df=df.drop_duplicates(0)
# df.index=df[0]
# df= df.reindex(index=['Average Price/Earnings','Average Price/Book','Average Price/Sales','Average Price/Cashflow'])
# print df.hed(9)