import pandas as pd
from pandas import *
import numpy as np

#create dataframes
dfj = DataFrame(np.random.randn(5, 2), columns=list('AB'))
# json1 = dfj.to_json()
# print json
# 
# dfd = DataFrame(np.random.randn(5, 2), columns=list('AB'))
# dfd['date'] = Timestamp('20130101')
# dfd = dfd.sort_index(1, ascending=False)
# json2 = dfd.to_json(date_format='iso')
# json3 = dfd.to_json(date_format='iso', date_unit='us')

#write to jason file------------------------------------
# dfj.to_json('test.json')
dfj.to_json('test2.json',orient="split")
dfj.to_json('test3.json',orient="values")
dfj.to_json('test4.json',orient="records")
dfj.to_json('test5.json',orient="index")
dfj.to_json('test6.json',orient="columns")

#read Jason-------------------
print open('test.json').read()
print open('test2.json').read()
print pd.read_json('test3.json')
print pd.read_json('test.json', dtype={'A' : 'float32', 'bools' : 'str'}).dtypes