#!/usr/bin/env python

import numpy as np

def secant(f,x0,x1,M=1e5,delta=1e-10,eps=1e-10):
    u = f(x0)
    v = f(x1)
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
        v = f(x1)
    return x1

f = lambda x: x**2 - 3
x0 = 0.0
x1 = 1.0
print('x0 = {}, x1 = {}, root = {:.6f}'.format(x0,x1,secant(f,x0,x1,delta=1e-6)))
