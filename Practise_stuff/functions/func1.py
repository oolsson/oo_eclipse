import args

def t1(x):
    print x
    
def t2():
    t1('oskar')
    print 'hello'
    
t2()
args.test_var_args(22)