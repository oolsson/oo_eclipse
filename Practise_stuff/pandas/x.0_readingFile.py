import scipy
import numpy
import pandas
import datetime
from pandas import *
from pandas.core.datetools import *
import time
import datetime


file = open('C:/Users/oo/Downloads/data/AUDUSD.txt', 'r')

array1 = []

for line in file.readlines():
   line = line.split(',')
   array1.append(line)

file.close()

date = [row[0] for row in array1]
time = [row[1] for row in array1]
prices = [row[2:6] for row in array1]

    
dates = []
for i in range(len(date)):
    dates.append(date[i]+" "+time[i])
    
data = []
for i in range(len(dates)):
    data.append(dates[i][6:10]+"-"+dates[i][0:2]+"-"+dates[i][3:5]+dates[i][10:13]+":"+dates[i][13:15]+":00")

fmt = "%Y-%m-%d %H:%M:%S"

datetimes = []
for i in range(len(data)):
    datetimes.append(datetime.datetime.strptime(data[i], fmt))
    
dates = numpy.array(datetimes)

prices = [[float(j) for j in i] for i in prices]
prices = numpy.array(prices)

#data = np.column_stack((dates, prices)) 

rng = DateRange(start = '04/01/2012 17:01:00', end = '04/01/2012 17:30:00', offset=Minute())
df =  DataFrame(numpy.zeros((len(rng),4)), index=rng,columns=['Opens','Highs','Lows', 'Closes'])       
df1 =  DataFrame(prices, index=dates,columns=['Opens','Highs','Lows', 'Closes'])    

merger = df1+df
merger1=merger.fillna(method='pad')
m1= merger[:5]
for item, frame in m1.iteritems():
    print frame






    