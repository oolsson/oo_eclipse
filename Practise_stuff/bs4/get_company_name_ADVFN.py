import urllib
from bs4 import BeautifulSoup
import string, datetime
import pandas as pd
from pandas.io.data import DataReader


def get_name(SYM):
    if len(SYM)<4:
        url="http://uk.advfn.com/p.php?pid=financials&symbol=NY_5E%s" % (SYM)
    else:
        url="http://uk.advfn.com/p.php?pid=financials&symbol=N_5E%s" % (SYM)
#     url = "http://uk.advfn.com/p.php?pid=financials&symbol=NY%5EGS"
    url=url.replace('_', '%')
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)
    a=[]
    b=1
    for  y in soup.findAll('td', attrs={"colspan" : "2"}):
        a=[]
#         print y
        if b==1:
            res=y.text
        b=2
    print res
    res=res.replace(',', '')
    res=res.replace('.', '')
    res=res.replace(' ', '-')
    res=res+'-'+SYM
    return res

p=get_name('HLF')
print p
