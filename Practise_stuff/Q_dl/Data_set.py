import Quandl
# data = Quandl.get("GOOG/NYSE_IBM",collapse="weekly")
# data= Quandl.get(['GOOG/NASDAQ_AAPL.4','GOOG/NASDAQ_MSFT.4'])
# data=Quandl.get("NSE/OIL", transformation = "cummul")
data=Quandl.get(["NSE/OIL.4"],trim_start ="March 2005", trim_end="December 2010")
print data.tail()