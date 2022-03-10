#!/usr/bin/env python3

import numpy as np
import sympy as sp

def secant(F,Fp,x0,M=1e5,delta=1e-10,eps=1e-10):
    x1 = x0 - F(x0)/Fp(x0)
    u = F(x0)
    v = F(x1)
    for i in range(int(M)):
        if abs(x1-x0) < delta:
            break
        if abs(u) < eps:
            x1 = x0
            break
        elif abs(v) < eps:
            break
        temp = x1
        x1 = x1 - v*(x1-x0)/(v-u)
        x0 = temp
        u = v
        v = F(x1)
    return x1

x  = sp.Symbol('x',real=True)
f  = sp.atan(x)
fp = sp.diff(f,x)

f_num  = sp.lambdify(x,f,'numpy')
fp_num = sp.lambdify(x,fp,'numpy')

x0 = np.array([-5.0,-1.0,-0.05,0.0,0.05,1.0,5.0])
print('The root of {} using the secant method was found using the following initial guesses:'.format(f))
for _ in x0:
    r = secant(f_num,fp_num,_)
    print('initial guess: {:.2f} --> approximate root: {:.3e}'.format(_,r))
