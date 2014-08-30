

import time
from dateutil import parser
import pandas as pd
import MySQLdb as mdb
import pandas.io.sql as sql
import datetime as dt

begin = dt.datetime(2013,05,11,23,04) #time the main loop starts from
firstbar=begin-dt.timedelta(minutes=4)
stop=begin+dt.timedelta(hours=1) 
closetime = begin+dt.timedelta(hours=5)




print begin
print firstbar
print stop
print closetime
print begin.strftime("%Y%m%d %H:%M:%S")
#GAT='20130507 20:25:00')


ticker='AUD.USD'
con_SQL = mdb.connect('localhost', "root","MySQLoo","random");
df=sql.read_frame("select * from prices where ticker = '%s' AND dt >'%s';" % (ticker,begin), con_SQL)
#print df.to_string()