
A=[1,1]
B=2
try:
    x=A[0]/B
except ZeroDivisionError:
    print A
    #raise 
except IndexError:
    print 'arit'
    #raise
except:
    print 'other'
    raise
else:
    print B
finally:
    print 'ok'

print x