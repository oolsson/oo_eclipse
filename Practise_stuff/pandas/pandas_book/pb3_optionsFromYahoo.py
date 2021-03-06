import numpy as np
randn = np.random.randn
import pandas as pd
from bs4 import BeautifulSoup
from urllib2 import urlopen
from pandas.io.parsers import TextParser

'''
buf = urlopen('http://www.telltaleinvestor.com')
#buf = urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options')
soup = BeautifulSoup(buf)
print soup.head.title

body = soup.body
links = body.findAll('a')
print links[:4]
'''

buf = urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options')
soup = BeautifulSoup(buf)
body = soup.body
links = body.findAll('a')
lnk = links[19]
#print lnk
lnk.get('href')
lnk.text
print '----------------------'
urls = [lnk.get('href') for lnk in body.findAll('a')]
#urls2 = [[column[0]] for column in urls]    #my try, quite useless
#print urls[-10:]


tables = body.findAll('table')

calls = tables[9]
rows = calls.findAll('tr')


def _unpack(row, kind='td'):
    return [val.text for val in row.findAll(kind)]

#basic
#rr=_unpack(rows[0], kind='th')
#print rr
#rr2=_unpack(rows[1], kind='td')
#print rr2

def parse_options_data(table):
    rows = table.findAll('tr')
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data, names=header).get_chunk()

call_data = parse_options_data(calls)
print call_data[:10]
# call_data=call_data.drop_duplicates(['strike'])

print call_data.to_string()
