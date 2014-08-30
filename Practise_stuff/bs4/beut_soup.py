import urllib
from bs4 import BeautifulSoup
import string, datetime
import pandas as pd


def yf_get_key_stat(SYM):
    url = "http://finance.yahoo.com/q/ks?s=" + SYM + "+Key+Statistics"
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)
    res = [[x.text for x in y.parent.contents] for  y in soup.findAll('td', attrs={"class" : "yfnc_tablehead1"})]
    return res

def yf_get_inc_stat(SYM):

#     url = "http://finance.yahoo.com/q/is?s=IBM+Income+Statement&annual"
    url = "http://finance.yahoo.com/q/bs?s=AA%2C+&ql=1"
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)
    print soup
    res = [[x.text for x in y.parent.contents] for  y in soup.findAll('td', attrs={"colspan" : "2"})]

    res = [[y.replace(u"\n","") for y in x] for x in res]
    res = [[y.replace(u"\xa0","").strip() for y in x] for x in res]
    res = [x for x in res if len(x) > 1]
    
    res = [[y.replace(u"-","0") for y in x] for x in res]
    res = [[y.replace(u",","") for y in x] for x in res]
    
    for i in range(len(res)):
#         print i
        if 'Period' in res[i][0]:
            for j in range(1,len(res[i])):
                res[i][j] = datetime.datetime.strptime(res[i][j], '%b %d %Y')
        else:
            for j in range(1,len(res[i])):
                res[i][j] = res[i][j]#int(res[i][j] )

    return     res

p=yf_get_inc_stat('AA')
print p
df=pd.DataFrame(p)
print df