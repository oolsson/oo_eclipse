import numpy
import talib
from pandas.io.data import DataReader
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import Quandl
from pandas import *
import datetime as dt
from scipy import stats
import re
import urllib2
import time


f = lambda x: float(x)


def getConstituentsOfAnIndexFromYahoo(symbol):
    url = 'http://finance.yahoo.com/q/cp?s=%s' % symbol
    p = re.compile('<td class=\"yfnc_tabledata1\"><b><a href=\"/q\?s=([A-Z0-9\.\-]*)\">')    
    components = []    
    pageIndex = 0
    finished = False
    while not finished:
        if pageIndex == 0: 
            actualUrl = url
        else:
            actualUrl = url + "&c=" + str(pageIndex)
        pageResults = p.findall(urllib2.urlopen(actualUrl).read())
        if len(pageResults) == 0:
            finished = True
        else:
            components.extend(pageResults)
            pageIndex+=1
    return components


# tickers=getConstituentsOfAnIndexFromYahoo('^OMXSPI')
# print len(tickers)
tickers=['ABB']


def get_data(start,end,sec):
    fl = lambda x: float(x)
    data = DataReader(sec, "yahoo", start,end)
    data=data.applymap(fl)
    data=data.ffill()
    return data
    
d=get_data(dt.datetime(2012, 12, 31),dt.datetime(2013, 6, 28),'ABB')
     

d= d.iloc[:,0:4]
plt.show(plt.plot(d))
