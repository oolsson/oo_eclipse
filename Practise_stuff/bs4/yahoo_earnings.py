import numpy as np
randn = np.random.randn
import pandas as pd
from bs4 import BeautifulSoup
from urllib2 import urlopen
from pandas.io.parsers import TextParser
import pandas.io.parsers as pdp
from pandas.io.data import DataReader

f = lambda x: str(x)
remove_w = lambda x: x.strip()

buf = urlopen('http://biz.yahoo.com/z/20140328.html')
soup = BeautifulSoup(buf)
body = soup.body

tables = body.findAll('table')
# for i in tables:print i.attrs
calls = tables
# print tables
# for property, value in vars(calls).iteritems():
#     print property, ": ", value
# print '----------'


rows = body.findAll('tr')

def _unpack(row, kind='td'):
    return [val.text for val in row.findAll(kind)]
 
 
def parse_options_data(table):
    rows = body.findAll('tr')
    header = _unpack(rows[0], kind='th')
    print header
    data = [_unpack(r) for r in rows[:]]
    L1=[]
    for i in data:
        if len(i)>4:
            if len(i)==6:
                L1.append(i[0:-2])
            else:
                L1.append(i[0:-2])
    for i in range(0,len(L1)):
        for ii in range(0,len(L1[i])):
            oo=L1[i][ii].strip()
            L1[i][ii]=oo
    res=TextParser(L1, names=header).get_chunk()
    res=res.applymap(f)
    #not if downloading is
#     res.index=res[0]
#     res= res.reindex(columns=res.columns[1:])
#     res=res.T
    res.columns=['name','ticker','supprice','reported_eps','estimat']
    #------------------------------------
    return res
 
call_data = parse_options_data(calls)
print call_data.head(10).to_string()