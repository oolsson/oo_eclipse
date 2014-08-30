'''
Created on Dec 25, 2011

@author: oo
'''
#import logging
#logging.basicConfig(filename="mySnake.log", level=logging.INFO)
#logging.info("Program started")
#logging.info("Done!")
#
#
#for i in range(-3,3):
#    if i == -1:
#        i
#        i
#        #print(i, 'pythons')
#    elif i < 3:pass
#        #print(i, 'pyts')
import logging
#import otherMod
 
#----------------------------------------------------------------------


 
# add filemode="w" to overwrite
#logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename="C:/Users/oo/Documents/python_none_pythonfiles/log/sample.txt", level=logging.INFO, filemode='w')
 
log = logging.getLogger('ex')
 
try:
    raise RuntimeError
except Exception, err:
    log.exception("Error!")
#logging.debug("This is a debug message")
#logging.info("Informational message")
#logging.error("An error has happened!")
#print 'p'