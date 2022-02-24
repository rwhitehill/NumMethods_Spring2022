#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def bisection(f,a,b,M=1e5,delta=1e-10,eps=1e-10):
    u = f(a)
    v = f(b)
    C = []

    if u*v > 0:
        c = 'Error: f(a) and f(b) have same sign'
    elif u == 0.0:
        c = a
    elif v == 0.0:
        c = b
    else:
        c = (a+b)/2
        m = f(c)    
        for i in range(int(M)):
            C.append(c)
            if abs(a-b) < delta or abs(m) < eps:
                break
            if f(a)*f(c) < 0:
                b = c
                v = m
            else:
                a = c
                u = m
            c = (a+b)/2
            m = f(c)
    C.append(c)
    return c,C

m = [7,13,17]
s = 2.0
for i in range(len(m)):
    f = lambda x: x**2-m[i]
    a = s
    b = s+1
    root,iterations = bisection(f,a,b,M=7)
    print('sqrt(%d) = %f'%(m[i],root))
    print('iterations:',iterations)
    print()
    s += 1

