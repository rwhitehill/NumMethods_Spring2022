#!/usr/bin/env python3

import numpy as np
import sympy as sp

x = sp.symbols(r'x',real=True)

def newton(f,fp,r,M=1e5,eps=1e-10):
    u = f(r)
    up = fp(r)
    for i in range(int(M)):
        if up == 0.0:
            r = 'Horizontal tangent reached: method fails'
            break
        if abs(u) < eps:
            break
        r = r - u/up
        u = f(r)
        up = fp(r)
    return r

f_sym  = x**2 - 3
fp_sym = sp.diff(f_sym,x)
f  = sp.lambdify((x),f_sym,'numpy')
fp = sp.lambdify((x),fp_sym,'numpy')

r = [-100.0,-5.0,-0.001,0.0,0.001,5,100]
root = []
for val in r:
    root.append(newton(f,fp,val))
print(root)
