def argkwargfunc( **kwargs ):
    options = {
            'v1' : 1,
            'v2' : 2,
            'v3' : 3, }
    #options.update(kwargs)
    #options[kwargs]=7
    Ks = list(options.keys())
    print Ks
   
    
def test_var_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg:", arg
    print 'specific args-------------------'
    print args[0]
    print args
 
 
def test_var_kwargs(farg, **kwargs):
    print "formal arg:", farg
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])
    print 'this works'
    if 'myarg2' in kwargs: print kwargs['myarg2']  
#    if key=='myarg3':
#        print 'this works'
       

test_var_kwargs(farg=1, myarg2="two", myarg3=3)
#test_var_kwargs(farg=1, myarg2="two")
print '-----------'
test_var_args(1, "two", 3)
