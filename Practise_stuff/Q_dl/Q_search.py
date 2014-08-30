import Quandl
# print help(Quandl.search)
# Quandl.search(query = 'G-20', page = +5, prints = True)
# Quandl.search(query = 'oil', source = "Source you wish to search", page = 1, prints = True)
datasets = Quandl.search('gdp',page = 1)

print datasets.Name