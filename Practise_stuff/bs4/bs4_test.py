import numpy as np
randn = np.random.randn
import pandas as pd
from bs4 import BeautifulSoup
from urllib2 import urlopen
from pandas.io.parsers import TextParser
import urllib2
import string, datetime




def yf_get_key_stat(SYM):
    url = "http://finance.yahoo.com/q/ks?s=" + SYM + "+Key+Statistics"
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)
    res = [[x.text for x in y.parent.contents] for  y in soup.findAll('td', attrs={"class" : "yfnc_tablehead1"})]
    return res

def yf_get_inc_stat(SYM):

    url = "http://finance.yahoo.com/q/is?s=IBM+Income+Statement"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    res = [[x.text for x in y.parent.contents] for  y in soup.findAll('td', attrs={"colspan" : "2"})]
#     res = soup.findAll('td')
    print res


    res = [[y.replace(u"\n","") for y in x] for x in res]
    res = [[y.replace(u"\xa0","").strip() for y in x] for x in res]
    res = [x for x in res if len(x) > 1]
    
    res = [[y.replace(u"-","0") for y in x] for x in res]
    res = [[y.replace(u",","") for y in x] for x in res]
    
    for i in range(len(res)):
        if 'Period' in res[i][0]:
            for j in range(1,len(res[i])):
                res[i][j] = datetime.datetime.strptime(res[i][j], '%b %d %Y')
        else:
            for j in range(1,len(res[i])):
                res[i][j] = res[i][j]#int(res[i][j] )

    return     res


p=yf_get_inc_stat('IBM')
# print p
df=pd.DataFrame(p)
print df