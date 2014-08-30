import rpy2.robjects as robjects

r = robjects.r 

#print r('R.Version()$version.string')

r('require(xts)')
r('require(quantmod)')
#aux = r('aux = getSymbols("GOOG", auto.assign=FALSE, from="2009-01-01")')
#type(aux)                    # <class 'rpy2.robjects.RArray'>
#
## or 
#aux = r.assign('aux', 'getSymbols("GOOG", auto.assign=FALSE, from="2009-01-01")')
#print aux


w=r.getFinancials("IBM")  # automatically assigns data to "IBM.f" object
print w
for property, value in vars(w.rx0).iteritems():
    print property, ": ", value
#r.viewFinancials(,"BS","Q")  # quarterly balance sheet

#print a
#classAux = r('class(aux)')   # this is an RVector
#classaux[0] == "xts"         # True 
#type(classAux[0])            # it's a python str 
#
## require(SecDb)
## ld = tsdb.readCurve('nepool_load_hist', as.POSIXct("2009-01-01"), Sys.time())
## ld = xts(ld$value, ld$time)
## merge(ld, aux)  # should replicate the daily value for all hours
#
#
#iaux = r('index(aux)')
#iaux = r.index(aux)      # is this slower than above ?!  What's recommended?
#iaux = np.array(iaux)
#
#[datetime.fromtimestamp(x) for x in indR]
#
#
#
## What is an RArray and how to operate on it?
#
#
## What is an RVector 
#v = r.seq(1,10)     #<RVector - Python:0x0146A0F8 / R:0x022BBA90>
#
#res = robjects.FloatVector([1.0, 2.0, 3.0])
#
#
#
## example of data.frame ...
#d = {'value': robjects.IntVector((1,2,3)),
#     'letter': robjects.StrVector(('x', 'y', 'z'))}
#dataf = robjects.r['data.frame'](**d)
#print(dataf.colnames())
#
###################################################################
## Conversion to numpy
#import numpy as np
#
#
#ltr = robjects.r.letters
#ltr_np = np.array(ltr)     # an array of strings
## can be done with asarray() too
#
## convert an RArray to an numpy array
#qq = np.array(aux)                     # works GREAT!
#np.size(qq)
#
#
#v = r.seq(1,10)            # an RVector
#v_np = np.array(v)         # an array of doubles
#
## from numpy to rpy2
#import rpy2.robjects.numpy2ri