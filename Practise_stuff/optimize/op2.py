from sympy.abc import x
import sympy as sym
import scipy.optimize as opt
import numpy

f = sym.exp(x/(1+x))            # A symbolic function

fx = sym.diff(f,x)

Fx = sym.lambdify(x,fx)       # A function handle which can be evaluated numerically
print(Fx(0))                           # This returns 1.0

f2 =(x**2-4*x)
fx2= sym.diff(f2,x)
Fx2 = sym.lambdify(x,fx2)
print fx2
print opt.fmin(Fx2,2)
print '------------------------------------'
print Fx2(11)
print opt.newton(Fx2, 99)
# print opt.fsolve(Fx2, 55,full_output=1)
print [Fx2(x) for x in numpy.linspace(1, 2, 12)]