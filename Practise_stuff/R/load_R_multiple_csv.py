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
    if len(df.columns)==282:
        df=df.replace(np.nan,0)
        df=df.replace('0000/00/0','1900/01/01')
        df=df.replace('0000-00-00','1900/01/01')
        
        
        #df=df.translate(None, '!,@#$')
        fl = lambda x: float(x)
        f5 = lambda x: x.replace('/', '-')
        f = lambda x: x.translate(None, '!,@*#$')
        #ff= lambda x: parser.parse(x)
        ff= lambda x: dt.datetime.strptime(x, '%Y/%m')
        fff=lambda x: dt.datetime.strptime(x, '%Y/%m/%d')
        ffff=lambda x: x[:8]+str(max(int(x[8:9]),1))
        
        
        for i in df.ix[:,9:]:
            if type(df[i][0])==str:
                df[i]= df[i].apply(f)
                df[i]= df[i].apply(fl) 
                print df[i][0]
        
        for i in df.ix[:,0:2]:
            if type(df[i][0])==str:
                df[i]= df[i].apply(ff)
                
        print df.head(5).to_string()
#        df['date preliminary data loaded']= df['date preliminary data loaded'].apply(f5)
#        df['date preliminary data loaded']= df['date preliminary data loaded'].apply(ffff)
#        df['date preliminary data loaded']= df['date preliminary data loaded'].apply(fff)
                
        #deletes % sign in column lable SQL can handle it
        cc=list(df.columns.values)
        oo=0
        for i in cc:
            cc[oo]=cc[oo].replace('%','PCH')
            oo +=1
        df.columns=cc

        end=d[ii].find('.csv')
        start=d[ii].find('Documents\\')+len('Documents\\')
        ticker=d[ii][start:end]
        
        df.insert(0, 'ticker', ticker)
        
        #print df.head(5).to_string()
        #print df.ix[1:4,10:22].to_string()
        #print df.ix[:4,10:].to_string()
        
        con = mdb.connect('localhost', "root","MySQLoo","fundamentals");
        sql.write_frame(df, con=con, name='dd',
                        if_exists='append', flavor='mysql')
        
#        df2=df2.append(df)
    else:
        print len(df.columns)
#print '-------------------------------------------------'
print df2.head(5).to_string() 
print len(df2.columns)
   
#con = mdb.connect('localhost', "root","MySQLoo","fundamentals");
#sql.write_frame(df2, con=con, name='dd', 
#                if_exists='append', flavor='mysql')

