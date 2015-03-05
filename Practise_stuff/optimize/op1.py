import scipy.optimize as opt

def my_f(x):
    return x**2+2
print opt.fmin(my_f,2)



