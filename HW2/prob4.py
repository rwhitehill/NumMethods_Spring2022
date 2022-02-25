#!/usr/bin/env python3

import numpy as np
import sympy as sp

def newton(f,fp,r,M=1e5,delta=1e-10,eps=1e-10):
    u = f(r)
    up = fp(r)
    for i in range(int(M)):
        if abs(u) < eps:
            break
        if up == 0.0:
            r = 'Error: horizontal tangent reached'
            break
        r1 = r - u/up
        if abs(r1-r) < delta:
            r = r1
            break
        r = r1
        u = f(r)
        up = fp(r)
    return r

x = sp.symbols(r'x',real=True)
f_sym  = x**2 - 3
fp_sym = sp.diff(f_sym,x)
f  = sp.lambdify((x),f_sym,'numpy')
fp = sp.lambdify((x),fp_sym,'numpy')

r = [-100.0,-5.0,-0.001,0.0,0.001,5,100]
for val in r:
    print('start = {} --> root = {}'.format(val,newton(f,fp,val)))
    print()
