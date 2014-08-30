import numpy as np
randn = np.random.randn
import pandas as pd
from bs4 import BeautifulSoup
from urllib2 import urlopen
from pandas.io.parsers import TextParser

buf = urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options')
soup = BeautifulSoup(buf)
body = soup.body
links = body.findAll('a')
lnk = links[19]
lnk.get('href')
lnk.text
urls = [lnk.get('href') for lnk in body.findAll('a')]


tables = body.findAll('table')
# for i in tables: print i
calls = tables[9]
print calls
rows = calls.findAll('tr')


def _unpack(row, kind='td'):
    return [val.text for val in row.findAll(kind)]


def parse_options_data(table):
    print table
    rows = table.findAll('tr')
    header = _unpack(rows[0], kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data, names=header).get_chunk()

call_data = parse_options_data(calls)
print call_data[:10]
