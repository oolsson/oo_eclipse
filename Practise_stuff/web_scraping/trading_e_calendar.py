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

buf = urlopen('http://www.tradingeconomics.com/calendar?g=world')
soup = BeautifulSoup(buf)
body = soup.body

tables = body.findAll('table')
# for i in tables:print 'i.attrs'
calls = tables[1]
# for property, value in vars(calls).iteritems():
#     print property, ": ", value
# print '----------'
# print calls.attrs

rows = calls.findAll('tr')

def _unpack(row, kind='td'):
    return [val.text for val in row.findAll(kind)]


def parse_options_data(table):
    rows = table.findAll('tr')
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]
    L1=[]
    for i in data:
        if len(i)>4:
            L1.append(i)
#             if len(i)==6:
#                 L1.append(i[1:])
#             else:
#                 L1.append(i)
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
    #------------------------------------
    return res

call_data = parse_options_data(calls)
print call_data.head(200).to_string()
call_data.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\deol.csv")