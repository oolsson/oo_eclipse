# This is script that pulls the history of Facebook (FB) stock price from Google.
# It then prints the data to the screen in CSV format.
# It prepends the CSV with Quandl metadata (code, name, description)


import urllib2

ticker = 'FB'
url = "http://www.google.com/finance/historical?q=NASDAQ%3A{0}&output=csv".format(ticker)

data = urllib2.urlopen(url).readlines()

print("code: FB2")
print("name: Facebook Stock Price")
print("----")

for row in data:
    print(row.strip())
#     print row