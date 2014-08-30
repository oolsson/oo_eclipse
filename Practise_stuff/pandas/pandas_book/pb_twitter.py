import numpy as np
randn = np.random.randn
import pandas as pd
from StringIO import StringIO
from lxml import objectify
import geojson
import requests
import json


tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()
print root.get('href')
print root.text

url = 'http://search.twitter.com/search.json?q=python%20pandas'
resp = requests.get(url)
print resp

data = json.loads(resp.text)
print data.keys()

