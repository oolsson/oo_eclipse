import os
import pandas as pd
import MySQLdb as mdb
import pandas.io.sql as sql
import numpy as np
import datetime as dt
from dateutil import parser



#finction to loop through all csv files in a directory
def dir_list(dir_name, sub_dir, *args):
    file_list = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if len(args) == 0:
                file_list.append(dirfile)
            else:
                if os.path.splitext(dirfile)[1][1:] in args:
                    file_list.append(dirfile)
        elif os.path.isdir(dirfile) and sub_dir:
            file_list += dir_list(dirfile, sub_dir, *args)
    return file_list

d=dir_list('C:\Users\oo\Documents',False,'csv')
#d=d[1:3]

df2=pd.DataFrame()

for ii in range(0,len(d)):
    print d[ii]
    df = pd.read_csv(d[ii])
    print len(df.columns)
    

