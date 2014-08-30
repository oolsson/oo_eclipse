import urllib
from bs4 import BeautifulSoup
import string, datetime
import pandas as pd
from pandas.io.data import DataReader




def yf_get_inc_stat(SYM):

    url = "http://uk.advfn.com/common/financial/NYSE/alcoa-AA/full-financials?pm=Q&isfull=1"
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)
#     print soup
#     res = [[x.text for x in y.parent.contents] for  y in soup.findAll('td', attrs={"colspan" : "2"})]
    a=[]
    b=[]
    for  y in soup.findAll('td'):
        a=[]
        for x in y.parent.contents:
            try:
                a.append(x.text)
            except:pass
#         print a
#         print len(a)
        if len(a)>20:b.append(a)
        if len(a)==6:b.append(a[1:])
    res=b
         
#     print res
# 
    res = [[y.replace(u"Bil","000000") for y in x] for x in res]
    res = [[y.replace(u"Mil","000").strip() for y in x] for x in res]
    res = [[y.replace(u".","").strip() for y in x] for x in res]
    res = [[y.replace(u" ","").strip() for y in x] for x in res]
    res = [[y.replace(u" ","").strip() for y in x] for x in res]
#     res = [x for x in res if len(x) > 1]
#     
#     res = [[y.replace(u"-","0") for y in x] for x in res]
#     res = [[y.replace(u",","") for y in x] for x in res]
#     
#     for i in range(len(res)):
#         if 'Period' in res[i][0]:
#             for j in range(1,len(res[i])):
#                 res[i][j] = datetime.datetime.strptime(res[i][j], '%b %d %Y')
#         else:
#             for j in range(1,len(res[i])):
#                 res[i][j] = res[i][j]#int(res[i][j] )

    return     res



p=yf_get_inc_stat('IBM')
# print p
df=pd.DataFrame(p)
df=df.drop_duplicates(0)
df.index=df[0]
# df.columns=df.index['PeriodEnding']
del df[0]
df = df.drop(df.index[0])
df.replace("Bil", '000', inplace=True)
print df.head(6).to_string()
df.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\excel\oa.csv")
# print df.tail(4).to_string()
# df.to_csv("C:\Users\oskar\Documents\doc_no_backup\python_crap\exel\ff.csv")