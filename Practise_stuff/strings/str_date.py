

import time
import datetime
import numpy as np
from dateutil import parser

#http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

import sys

def test(SYM):
    o1="http://uk.advfn.com/p.php?pid=financials&symbol=NY_5E%s" % (SYM)
    o1=o1.replace('_', '%')
    return o1
o="SELECT * FROM idtoticker where ticker = '%s' ;" % ('pp')

print o
p=test('GS')
print p+'-p'


